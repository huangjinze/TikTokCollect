from DataBaseOper.InitModel import *

metadata = MetaData()

TikTokTable = Table(
    "TikTokVideo", metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(200)),
    Column('city', String(20)),
    Column('star_num', Float),
    Column('video_share_address', String(300)),
    Column('video_real_address', String(300), unique=True),
    Column('finished', String(5))
)

metadata.create_all(engine)
conn = engine