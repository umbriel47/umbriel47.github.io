---
layout: post
title: "MongoDB安装简要"
date: 2016-11-17 22:23:47
lang: zh
ref: installing-mongodb
tags: [tech]
redirect_from:
  - "/科学技术/2016/11/17/MongoDB安装简要.html"
---

前段时间尝试使用MongoDB，在安装过程中也是稍微遇到了些许的周折，先将简要的安装步骤记录如下。

- 系统：ubuntu 14.04, 64bit
- MongoDB: 3.4


# 按照官网步骤安装 #
没有太复杂的步骤，按照[这里](https://docs.mongodb.com/master/tutorial/install-mongodb-on-ubuntu/)官网的解释进行一步步的安装即可。

# 配置文件 #
安装好以后可以配置 /etc/mongodb.conf 文件进行一些基本的设置。在初期可能和我自己相关的是：

- 注释掉 `bind = 127.0.0.1` 以允许远程客户端的访问（同时因为我自己使用的阿里云，需要在云服务器配置上打开相应端口）
- 打开 `auth = true`
- MongoDB默认数据文件夹在`/data/db`, 开启数据库服务前若没有相应文件夹将报错

# 启动服务 #
最简单的 `mongod` 就可以。如需使用配置文件，可以加上 `--config`参数，其它的如 `--port`(指定端口)等可以参考帮助。重启或者关闭使用 `service mongodb restart(stop)` 就好了

# 创建用户 #
因为指定了要求验证，数据库的操作需要验证登陆用户，验证的具体语法是
	
	use <db_name>
	db.auth("<username>", "<password>")
	
当然，验证前需要创建相应的用户

	use <db_name>
	db.createUser(
		{ user: "username",
		  pwd: "password",
		  roles: [{role: "<role_group>", db: "db_name}, 
		  			{...}, 
		  			"<role_group>"]
		}
	)
	
最后一个 `role_group` 将应用于当前的collection。相应的用户权限有一部分是已经定义好的，可以在[这里](https://docs.mongodb.com/manual/reference/built-in-roles/#superuser-roles)查看。

# 远程登录 #
如果使用GUI（这里我用的是robomongo），那没什么说的。在客户端shell条件下，直接输入 mongo IP:port 就可以登录了。进入相应collection，然后验证用户之后就可以进行相应的操作。
