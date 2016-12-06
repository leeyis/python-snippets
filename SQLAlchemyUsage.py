# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import sessionmaker

# mysql-python
engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/scrapy?charset=utf8')

# 创建对象的基类:
Base = declarative_base()
# 创建DBSession类型
Session = sessionmaker(bind=engine)
session=Session()
class ProxyIP(Base):

    __tablename__="ProxyIPs"
    # 表的结构:
    IpPort=Column(String(20),primary_key=True)
    Country=Column(String(20))
    Speed=Column(Integer)
    Type=Column(String(10))
    Level=Column(String(20))
    LastCheck=Column(DateTime)
    GoogleProxy=Column(String(1))


# 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
Base.metadata.create_all(engine)

ip=ProxyIP(IpPort='127.0.0.1:8080',Country='CN',Speed=500,Type='HTTP',Level='Anonymous',LastCheck='2016-11-20',GoogleProxy='Y')
session.add(ip)
session.commit()