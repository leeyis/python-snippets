# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()

global engine

#建立数据库表
def create_all_tables(DB_type,DB_host,DB_port,DB_name,username,password,charset="utf8"):
    global engine
    if DB_type.upper() == "MYSQL":
        DB_URI = "mysql+mysqldb://%s:%s@%s:%s/%s?charset=%s" % (username,password,DB_host,DB_port,DB_name,charset)
        engine = create_engine(DB_URI,echo=True)
        # 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
        Base.metadata.create_all(engine)

#返回数据库会话
def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class User(Base):

    __tablename__="User"
    # 表的结构:
    id = Column(Integer,primary_key=True)
    userName = Column(String(50),nullable=False,default="Noob")
    password = Column(String(50),nullable=False,default="123456")
    gender = Column(String(1),nullable=True,default=None)

    def __init__(self,id,userName,password,gender = None):
        self.id = id
        self.userName = userName
        self.password = password
        self.gender = gender


if __name__=="__main__":
    #建表
    create_all_tables("mysql","localhost",3306,"test","root","123456")

    #获取数据库会话
    session = loadSession()

    #增加
    u1 = User(id=1,userName="Rose",password="aaaa",gender="F")
    u2 = User(id=2, userName="Joe", password="bbbb",gender="M")
    u3 = User(id=3, userName="jack", password="bbbb", gender="M")
    u4 = User(id=4, userName="Billy", password="cccc")
    session.add(u1)
    session.add(u2)
    session.add(u3)
    session.add(u4)
    session.commit()

    #删除
    session.query(User).filter(User.id > 2, User.gender == None).delete()
    session.commit()

    #修改
    session.query(User).filter(User.userName == "jack").update({User.password:"xxxx"})
    session.commit()

    #查询
        #查第一行
    session.query(User.id,User.userName,User.password).first()
        #查所有行
    session.query(User.id, User.userName, User.password).all()
        #根据id倒序并取前两行
    session.query(User).order_by(User.id.desc()).limit(2)
