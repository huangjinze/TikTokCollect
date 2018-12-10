from DataBaseOper.InitModel import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from time import sleep
import datetime, os

from IPTest import getheaders

download_headers = {
    'Connection':                "keep-alive",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent':                getheaders()['User-Agent'],
    'Accept':                    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding':           "gzip, deflate, br",
    'Accept-Language':           "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
    'Cache-Control':             "no-cache"
}



driver = webdriver.Chrome(executable_path='tools\chromedriver.exe')
# 从这个网址解析视频： http://douyin.iiilab.com/
def get_real_url(video_url):
    print("\r正在解析地址")
    try:
        driver.get("http://douyin.iiilab.com")

        inputElem = driver.find_element_by_tag_name("input")
        inputElem.clear()
        inputElem.send_keys(video_url)
        inputElem.send_keys(Keys.RETURN)

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-success')))
        url = element.get_attribute("href")

        return {
            'state': 'success',
            'data': url,
            'reason': ''
        }
    except Exception as e:
        print('get real failed,', id, e)
        saveFile = open('FailFile.txt', 'a')
        saveFile.write(video_url)
        saveFile.write('\n')
        saveFile.close()
        return {
            'state': 'fail',
            'data': '',
            'reason': 'get real failed' + video_url
        }


def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        print(path+' 创建成功')
        os.makedirs(path)
        return True
    else:
        print(path+' 目录已存在')
        return False


def download_video(id, city, url, retry=3):
    '''
     下载视频,显示进度
     '''
    print("\r正在下载%s第%s个视频" % (city, id))
    try:
        response = requests.get(url, stream=True, headers=download_headers, timeout=15, allow_redirects=False)

        video_url = response.headers['Location']

        video_response = requests.get(video_url, headers=download_headers, timeout=15)

        mkpath = "video\\"+str(datetime.date.today())+"\\"+city
        mkdir(mkpath)

        # 保存视频，显示下载进度
        if video_response.status_code == 200:
            with open(mkpath + "\\%d.mp4" % id, 'wb') as f:
                data_length = 0
                for data in video_response.iter_content(chunk_size=1024):
                    data_length += len(data)
                    f.write(data)
            print('download success!')
            return {
                'state': 'success',
                'data': '',
                'reason': ''
            }
        # 失败重试3次
        elif video_response.status_code != 200 and retry:
            print('retrying...')
            retry -= 1
            download_video(id, url, retry)
        else:
            print('link is unavailable...')
            return{
                'state': 'fail',
                'data': '',
                'reason': 'time out'
            }
    except Exception as e:
        print('download failed,', id, e)
        saveFile = open('FailFile.txt', 'a')
        saveFile.write(url)
        saveFile.write('\n')
        saveFile.close()
        return {
            'state': 'fail',
            'data': '',
            'reason': e
        }


# 获取指定的视频存放在文件夹中
def runDownLoad():
    url = session.query(TikTokVideo).filter(
        TikTokVideo.finished == 'N'
    ).first()
    if url:
        video_url = url.video_share_address
        id = url.id
        city = url.city

        data = get_real_url(video_url)


        if data['state'] == 'success':
            real_url = data['data']
            down_data = download_video(id, city, real_url)

            try:
                if down_data['state'] == 'success':
                    session.query(TikTokVideo).filter(TikTokVideo.id == id).update({'finished': 'Y'})
                else:
                    session.query(TikTokVideo).filter(TikTokVideo.id == id).update({'finished': 'F'})
            except Exception as e:
                print(e)
                session.rollback()

            return {
                'state': 'success',
                'data': '',
                'reason': '',
            }
        else:
            print('链接无效')
            session.query(TikTokVideo).filter(TikTokVideo.id == id).update({'finished': 'F'})
            return {
                'state': 'fail',
                'data': '',
                'reason': '链接无效',
            }

    else:
        print('下载完成')
        driver.quit()
        return {
            'state': 'fail',
            'data': '',
            'reason': '下载完成',
        }


if __name__ == '__main__':
    session = DBSession()
    while True:

        data = runDownLoad()
        if data['state'] == 'fail':
            sleep(10)
        else:
            print('success!')
