from bs4 import BeautifulSoup as but
from requests import get
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
import pymysql

pymysql.install_as_MySQLdb()

ngin = create_engine("mysql://roto:3Zpas5w0rd*@localhost/flask_api")

Session = sessionmaker(bind=ngin)
ssion = Session()

Base = declarative_base()


class Tutoes(Base):
    __tablename__ = "tutoes"

    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(255), nullable=False)
    img = Column("img", Text)
    date = Column("date", DateTime)
    content = Column("content", Text, nullable=False)
    dscp = Column("dscp", String(511))
    type = Column("type", Integer, nullable=False)
    origin = Column("origin", Text)

    def __repr__(self):
        return "<Tutoes(id='%d',title='%s', date='%s', dscp='%s')>" % (
            self.id,
            self.title,
            self.date,
            self.dscp,
        )
res = get("http://www.yxdown.com/zt/ACGreece/gl/")
soup = but(res.content, 'html.parser')
div = soup.find(class_='glbox').find_all("li")
for i in range(2,10):
    for new in div:
        link = new.a['href']
        title=new.a.text
        time=new.em.text
        #print（img）
        #print(link)
        #print(title)
        #print(time)
        details = get(link)
        soup = but(details.content, 'html.parser')
        content = soup.find(class_='news')
        content.h1.extract()
        content.find(class_='intro').extract()
        print(content)
    res = get("http://www.yxdown.com/zt/ACGreece/gl/"+i+"/")
    soup = but(res.content, 'html.parser')
    div = soup.find(class_='glbox').find_all("li")    