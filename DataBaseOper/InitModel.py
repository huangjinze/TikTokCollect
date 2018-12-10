# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Float, Sequence, Integer, create_engine
from sqlalchemy import and_, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from ReadConf import read_conf

conf = read_conf('config.json')

db_user = conf['db_user']
db_pass = conf['db_pass']
db_ip = conf['db_ip']
db_port = conf['db_port']
db_name = conf['db_name']

Base = declarative_base()

class TikTokVideo(Base):
    __tablename__ = "TikTokVideo"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(200))
    city = Column(String(20))
    star_num = Column(Float)
    video_share_address = Column(String(300))
    video_real_address = Column(String(300))
    finished = Column(String(5))


# 初始化数据库连接:
# 连接数据库
engine = create_engine(
    "mysql+pymysql://"+conf["db_user"]+":"+conf["db_pass"]+"@"+conf["db_ip"]+":"+conf["db_port"]+"/"+conf["db_name"]+"?charset=utf8",
    encoding="utf-8",
    echo=False
)# 创建DBSession类型:
session_factory = sessionmaker(bind=engine)
DBSession = scoped_session(session_factory)

metadata = MetaData()





