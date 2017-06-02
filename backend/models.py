
from db_wrapper.api import *
from db_wrapper.model import TimeStampMixin, SoftDeleteMixin
from db_wrapper.api import Column, String, Integer, DateTime, Text, engine
from sqlalchemy import ForeignKey, SmallInteger, BigInteger


Base = declarative_base()

class User(Base, TimeStampMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    passwd = Column(String(255), nullable=False)

    balance = Column(Integer, nullable=False)
    userLevel = Column(Integer, nullable=False)
    #base_image_id = Column(Integer, ForeignKey('image.id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True)





class Cart(Base, TimeStampMixin):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True)

    book_id = Column(Integer, ForeignKey('book.id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True)
    quantity = Column(Integer, nullable=False)
    

class Comment(Base, TimeStampMixin):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('book.id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True)
    rate = Column(String(255), nullable=False)
    comment = Column(String(255), nullable=False)
    

class Order(Base, TimeStampMixin):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_number = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True)

    book_list = Column(String(255), nullable=False)
    pay_amount = Column(String(255), nullable=False)
    status = Column(Integer, nullable=False)


class Book(Base, TimeStampMixin):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    cover = Column(String(255), nullable=False)
    details = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)
    briefInfo = Column(String(255), nullable=False)
    rate = Column(String(255), nullable=False)
    rateNumber = Column(Integer, nullable=False)
    publisher = Column(String(255), nullable=False)
    publishDate = Column(String(255), nullable=False)
    ISBN = Column(String(255), nullable=False)
    packaging = Column(String(255), nullable=False)
    pagesNumber = Column(Integer, nullable=False)
 
    salesVolume = Column(Integer, nullable=False)
    bookType = Column(String(255), nullable=False) 






metadata = Base.metadata
metadata.create_all(engine)

