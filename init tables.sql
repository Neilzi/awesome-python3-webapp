-- init table sql
DROP DATABASE IF EXISTS awesome;
CREATE DATABASE awesome;
USE awesome;

-- mysql8.0 创建用户的唯一方式：
CREATE USER 'awesome_mst'@'%' IDENTIFIED BY 'password'

CREATE TABLE IF NOT EXISTS users(
id INT NOT NULL AUTO_INCREMENT COMMENT '主键id',
NAME VARCHAR(50) COMMENT '用户名',
PASSWORD VARCHAR(255) COMMENT '用户密码',
isadmin BOOLEAN COMMENT '是否为管理员，1:是，0:否',
avator VARCHAR(500) COMMENT '头像',
email VARCHAR(50) COMMENT '邮箱',
create_time DATETIME DEFAULT NOW() COMMENT '注册日期',
UNIQUE KEY `idx_email` (`email`),
PRIMARY KEY ( `id` )
)ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS blogs(
id INT NOT NULL AUTO_INCREMENT COMMENT '主键id',
user_id INT NOT NULL COMMENT '用户id',
title VARCHAR(100) COMMENT '博客标题',
summary VARCHAR(200) COMMENT '简介',
context TEXT COMMENT '正文',
create_time DATETIME DEFAULT NOW() COMMENT '创建时间',
PRIMARY KEY ( `id` )
)ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Comments(
id INT NOT NULL AUTO_INCREMENT COMMENT '主键id',
blog_id INT NOT NULL COMMENT '博客id',
user_id VARCHAR(100) COMMENT '用户id',
COMMENT TEXT COMMENT '评论',
create_time DATETIME DEFAULT NOW() COMMENT '评论时间',
PRIMARY KEY ( `id` )
)ENGINE=INNODB DEFAULT CHARSET=utf8;