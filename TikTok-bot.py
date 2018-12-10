# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep
from DataBaseOper.InitModel import *
from DataBaseOper.DBOperation import *
import pyperclip
import base64
import threading, asyncio
from multiprocessing import Process, Pool
from ReadConf import read_conf
# os.system("G:\\NOX\\Nox\\bin\\nox_adb.exe connect 127.0.0.1:62002")
# os.system("G:\\NOX\\Nox\\bin\\nox_adb.exe connect 127.0.0.1:62025")

conf = read_conf('config.json')
threshold = conf['star_num']

def get_share_url(driver):


    data_dict = {}



    star_num = driver.find_element_by_id('bbx').text
    if star_num.find('k') != -1:
        star_num = float(star_num.replace('k', '')) * 1000
    elif star_num.find('w') != -1:
        star_num = float(star_num.replace('w', '')) * 10000
    elif star_num.find('m') != -1:
        star_num = float(star_num.replace('m', '')) * 1000000
    else:
        star_num = float(star_num)


    if star_num <= threshold:
        sleep(10)
        return {
            'state': 'fail',
            'data': data_dict,
            'reason': 'not good'
        }
    else:
        sleep(1)
        print(star_num)
        username = driver.find_element_by_id('title').text
        print(username)
        send_button = driver.find_element_by_id('aq2').click()
        link_img_id = driver.find_elements_by_id("yz")
        link_text_id = driver.find_elements_by_id("z0")
        for i in range(len(link_text_id)):
            print(link_text_id[i].text)
            baseText = base64.b64encode(link_text_id[i].text.encode("utf-8"))
            print(baseText)
            # 韩国
            if baseText == b'66eB4oGg7YGs4oGgIOuzteKBoOyCrOKBoA==':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '韩国'
                data_dict['name'] = username[1: ]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:'+data_dict['city'])
                break
            # 欧美
            elif link_text_id[i].text == 'C⁠o⁠p⁠y⁠ L⁠i⁠n⁠k⁠':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '欧美'
                data_dict['name'] = username[1: ]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:'+data_dict['city'])
                break
            # 越南
            elif baseText == b'U+KBoGHigaBv4oGgIGPigaBo4oGgw6nigaBw4oGgIEzigaBp4oGgw6rigaBu4oGgIGvigaDhur/igaB04oGg':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '越南'
                data_dict['name'] = username[1: ]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:'+data_dict['city'])

                break
            # 日本
            elif baseText == b'44Kz4oGg44OU4oGg44O84oGg':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '日本'
                data_dict['name'] = username[1: ]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:'+data_dict['city'])
                break
            # 俄国
            elif baseText == b'0KHigaDRgeKBoNGL4oGg0LvigaDQuuKBoNCw4oGg':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '俄国'
                data_dict['name'] = username[1:]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:' + data_dict['city'])
                break
            # 德国
            elif baseText == b'TOKBoGnigaBu4oGga+KBoCAKa+KBoG/igaBw4oGgaeKBoGXigaBy4oGgZeKBoG7igaA=':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '德国'
                data_dict['name'] = username[1:]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:' + data_dict['city'])
                break
            # 法国
            elif baseText == b'Q+KBoG/igaBw4oGgaeKBoGXigaBy4oGgIGzigaBl4oGgIGzigaBp4oGgZeKBoG7igaA=':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '法国'
                data_dict['name'] = username[1:]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:' + data_dict['city'])
                break
            # 泰国
            elif baseText == b'4LiE4oGg4Lix4oGg4LiU4oGg4Lil4oGg4Lit4oGg4LiB4oGg4Lil4oGg4Li04oGg4LiH4oGg4LiB4oGg4LmM4oGg':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '泰国'
                data_dict['name'] = username[1:]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:' + data_dict['city'])
                break
            # 菲律宾
            elif baseText == b'4LiE4oGg4Lix4oGg4LiU4oGg4Lil4oGg4Lit4oGg4LiB4oGg4Lil4oGg4Li04oGg4LiH4oGg4LiB4oGg4LmM4oGg':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '菲律宾'
                data_dict['name'] = username[1:]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:' + data_dict['city'])
                break
            # 葡萄牙
            elif baseText == b'Q+KBoG/igaBw4oGgaeKBoGHigaBy4oGgIEzigaBp4oGgbuKBoGvigaA=':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '葡萄牙'
                data_dict['name'] = username[1:]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:' + data_dict['city'])
                break
            # 印度尼西亚
            elif baseText == b'U+KBoGHigaBs4oGgaeKBoG7igaAgVOKBoGHigaB14oGgdOKBoGHigaBu4oGg':
                link_button = link_img_id[i].click()
                link = pyperclip.paste()
                link = link.split()[-1]
                print(link)
                data_dict['city'] = '印度尼西亚'
                data_dict['name'] = username[1:]
                data_dict['star_num'] = star_num
                data_dict['video_share_address'] = link
                print('get info:' + data_dict['city'])
                break
        return {
            'state': 'success',
            'data': data_dict,
            'reason': ''
        }

# 向上滑动
def swipeUp(driver, t):

    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']

    x1 = int(x * 0.5)
    y1 = int(y * 0.75)
    y2 = int(y * 0.25)
    driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver, t):

    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']

    x1 = int(x * 0.5)
    y1 = int(y * 0.75)
    y2 = int(y * 0.5)
    driver.swipe(x1, y2, x1, y1, t)

def collect_vedio(driver):
    # flag 作为标志，每个隔20次刷新一下
    flag = 0
    session = DBSession()
    while True:

        # 获取视频具体信息
        try:
            print(flag)
            if flag % 30 == 0:
                refreshBar = driver.find_element_by_id('p9')
                refreshButton = refreshBar.find_elements_by_class_name('android.widget.ImageView')[0].click()

                sleep(20)
                print("refreshing...")

            data = get_share_url(driver)
        except Exception as e:
            print(e)
            sleep(5)
            print('reconnect...')
            refreshBar = driver.find_element_by_id('p9')
            refreshButton = refreshBar.find_elements_by_class_name('android.widget.ImageView')[0].click()
            continue

        if data['state'] == 'fail':
            print(data['reason'])

        else:
            data = data['data']
            try:
                # 存储于数据库中
                if QueryUrlExist(data['video_share_address'], session, TikTokVideo):
                    print("this video has been collected.")
                else:
                    new_video = TikTokVideo(
                        name=data['name'],
                        city=data['city'],
                        star_num=data['star_num'],
                        video_share_address=data['video_share_address'],
                        finished='N',
                    )
                    session.add(new_video)
                    session.commit()
            except Exception as e:
                print(e)
                session.rollback()
                sleep(1)


        # 下一个视频
        try:
            flag += 1
            swipeUp(driver, 200)
        except Exception as e:
            print(e)
            sleep(1)
            continue

if __name__ == '__main__':
    desired_caps1 = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'udid': '127.0.0.1:62001',
        'platformVersion': '4.4.2',
        'appPackage': 'com.ss.android.ugc.trill',
        'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity'
    }

    desired_caps2 = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62025',
        'udid': '127.0.0.1:62025',
        'platformVersion': '4.4.2',
        'appPackage': 'com.ss.android.ugc.trill',
        'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity'
    }

    desired_caps3 = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62026',
        'udid': '127.0.0.1:62026',
        'platformVersion': '4.4.2',
        'appPackage': 'com.ss.android.ugc.trill',
        'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity'
    }

    driver = []

    driver0 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
    # driver1 = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
    # driver2 = webdriver.Remote('http://127.0.0.1:4726/wd/hub', desired_caps3)

    driver.append(driver0)

    collect_vedio(driver[0])
    # driver.append(driver1)
    # driver.append(driver2)

    # processNum = len(driver)
    #
    # print('Parent process %s. ' % os.getpid())
    # p = Pool(processNum)
    # for i in range(processNum):
    #     print(i)
    #     p.apply_async(collect_vedio, args=(driver[i], ))
    # print('Waiting for all subprocess done...')
    # p.close()
    # p.join()
    # print('All Process done.')



