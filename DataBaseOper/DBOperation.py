def QueryUrlExist(url, session, UrlModel):
    url = session.query(UrlModel).filter(UrlModel.video_share_address == url).first()
    return url

def QueryUserExist(appID, session, UserModel):
    app_ID = session.query(UserModel).filter(UserModel.appID == appID).first()
    return app_ID

# if __name__ == '__main__':
#     from DataBaseOper.InitModel import *
#     from sqlalchemy import and_
#     session = DBSession()
#     iurl = session.query(ListUrl).filter(
#         and_(ListUrl.finish == 'N', ListUrl.id % 10 == 1)
#     ).limit(1)
#     user_url = iurl[0].url.decode()
#     print(user_url)





