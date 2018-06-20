#! /usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, create_engine, ForeignKey, String, Integer, Boolean, DateTime, Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tabel__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    admin = Column(Boolean, nullable=False)
    avator = Column(String(500))
    email = Column(String(50))
    create_time = Column(DateTime, default=datetime.now())

    blogs = relationship('Blog', back_populates="users")
    comments = relationship('commtents', back_populates="users")

class Blog(Base):
    __table__ = 'blogs'

    id = Column(Integer, primary_key=True,autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(100))
    summary = Column(String(200))
    context = Column(Text)
    create_time = Column(DateTime, default=datetime.now())

class Comment(Base):
    __table__ = 'Comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    blog_id = Column(Integer, ForeignKey('blogs.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    comment = Column(Text)
    create_time = Column(DateTime, default=datetime.now())

