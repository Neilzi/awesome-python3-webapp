#! /usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, create_engine, ForeignKey, String, Integer, Boolean, DateTime, Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    isadmin = Column(Boolean, nullable=False)
    avator = Column(String(500))
    email = Column(String(50))
    create_time = Column(DateTime, default=datetime.now())

    blogs = relationship('Blog')
    comments = relationship('Comment')


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True,autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(100))
    summary = Column(String(200))
    context = Column(Text)
    create_time = Column(DateTime, default=datetime.now())


class Comment(Base):
    __tablename__ = 'Comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    blog_id = Column(Integer, ForeignKey('blogs.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    comment = Column(Text)
    create_time = Column(DateTime, default=datetime.now())


engine = create_engine('mysql+mysqlconnector://awesome_mst:Tuniu520@localhost:3306/awesome')
DBSession = sessionmaker(bind=engine)

if __name__ == '__main__':
    user = User(name="小南", password="abcde", isadmin=1)
    blog = Blog(user_id=1, title="杂谈", summary='balabla', context='经济杂谈，you are the champions!')
    comment = Comment(blog_id=1, user_id=1, comment="it's a greate article!")
    session = DBSession()
    session.add(user)
    session.add(blog)
    session.add(comment)
    session.commit()