[TOC]

#### Docker简介

+ 什么是容器

  一种虚拟化的方案

  操作系统级别的虚拟化

  只能运行相同或相似内核的操作系统

+ 什么是Docker

  将应用程序自动部署到容器

+ Docker的目标

  提供简单轻量的建模方式

  职责的逻辑分离

  快速高效的开发生命周期

  鼓励面向服务的架构

+ Docker的使用场景

  使用Docker容器开发、测试、部署服务

  创建隔离的运行环境

  搭建测试环境

  PaaS

  SaaS

  高性能、超大规模的宿主机部署



#### Docker的基本组成

+ Docker客户端/守护进程

+ Docker Image镜像

  容器的基石

  层叠的只读文件系统

  联合加载

+ Docker Container容器

  通过镜像启动

  启动和执行阶段

  写时复制

+ Docker Registry仓库

  公有

  私有

  Docker Hub



#### Docker安装与配置

+ 安装Docker维护的版本

  ```sh
  sudo apt-get install -y curl
  curl -sSL https://get.docker.com/ubuntu/ | sudo sh
  ```

+ 使用非root用户

  ```sh
  sudo groupadd docker
  sudo gpasswd -a 用户名 docker
  sudo service docker restart
  ```

+ 在Windows中安装Docker

  **Boot2Docker for Windows**

  - Boot2Docker Linux ISO
  - Virtualbox
  - MSYS-git
  - 管理工具



#### 容器的基本操作

+ 启动容器

  ```sh
  docker run IMAGE [COMMAND][ARG...] run 在新容器中执行命令
  ```

+ 启动交互式容器

  ```sh
  docker run -i -t IMAGE /bin/bash
  ```

+ 查看容器

  ```sh
  docker ps -a 显示所有容器
  docker ps -l 显示最近创建的容器
  docker inspect [ID/Name] 显示容器详细信息
  ```

+ 自定义容器名

  ```sh
  docker run --name=自定义名 -i -t IMAGE /bin/bash
  ```

+ 重新启动停止的容器

  ```sh
  docker start [-i] 容器名
  ```

+ 删除停止的容器

  ```sh
  docker rm 容器名
  ```



#### 守护式容器

+ 什么是守护式容器

  能够长期运行

  没有交互式会话

  适合运行应用程序和服务

+ 以守护形式运行容器

  ```sh
  docker run -i -t IMAGE /bin/bash
  Ctrl+P Ctrl+Q
  ```

+ 附加到运行中的容器

  ```sh
  docker attach 容器名
  ```

+ 启动守护式容器

  ```sh
  docker run -d 镜像名 [COMMAND][ARG...]
  ```

+ 查看容器日志

  ```sh
  docker logs [-f] [-t] [--tail]
  ```

+ 查看容器内进程

  ```sh
  docker top 容器名
  ```

+ 在运行的容器内启动新进程

  ```sh
  docker exec [-d][-i][-t] 容器名 [COMMAND][ARG...]
  ```

+ 停止守护式容器

  ```sh
  docker stop 容器名 等待停止
  docker kill 容器名 立刻停止
  ```



#### 在容器中部署静态网站

+ 设置容器端口映射

  run [-P] [-p]

+ Nginx部署流程

  1. 创建映射80端口的交互式容器
  2. 安装Nginx
  3. 安装文本编辑器Vim
  4. 创建静态页面
  5. 修改Nginx配置文件
  6. 运行Nginx
  7. 验证网站访问

  ```sh
  docker run -p 80 --name web -i -t ubuntu /bin/bash
  apt-get update
  apt-get install -y nginx
  apt-get install -y vim
  mkdir -p /var/www/html
  cd /var/www/html
  vim index.html
  whereis nginx
  vim /etc/nginx/sites-available/default
  nginx
  ps -ef
  docker ps
  curl http://127.0.0.1:32769
  ```



#### 查看和删除镜像

+ 镜像的存储地址

  ```sh
  /var/lib/docker
  ```

+ 列出镜像

  ```sh
  docker images [OPTSIONS] [REPOSITORY]
  ```

+ 查看镜像

  ```sh
  docker inspect [OPTIONS] CONTAINER|IMAGE [CONTAINER|IMAGE...]
  ```

+ 删除镜像

  ```sh
  docker rmi [OPTIONS] IMAGE [IMAGE...]
  ```




#### 获取和推送镜像

+ 查找镜像

  [Docker Hub](https://registry.hub.docker.com)

  ```sh
  docker search [OPTIONS] TERM 
  最多显示25结果
  ```

+ 拉取镜像

  docker pull [OPTIONS] NAME [:TAG]

+ 使用--registry-mirror选项

  1. 修改：/etc/default/docker

  2. 添加：DOCKER_OPTS = "--registry-mirror=镜像地址"

     https://daocloud.io



#### 构建镜像

> + 保存对容器的修改，并再次使用
> + 自定义镜像的功能
> + 以软件的形式打包并分发服务及其运行环境

+ 使用commit构建镜像

  ```sh
  docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
  ```

+ 使用Dockerfile构建镜像

  1. 创建Dockerfile
  2. 使用docker build命令

  ```sh
  docker build [OPTIONS] PATH | URL
  ```

  ```sh
  # 过程
  mkdir -p dockerfile/df_test1
  cd dockerfile/df_test1
  vim Dockerfile
  docker build -t='yanwu/df_test1' .
  ```



#### Docker的C/S模式

+ Remote API
+ 连接方式



#### Docker守护进程的配置和操作

+ 查看守护进程

  ```sh
  ps -ef | grep docker
  systemctl status docker
  ```

+ 使用service命令管理

  ```sh
  sudo service docker start
  sudo service docker stop
  sudo service docker restart
  ```

+ Docker的启动选项

  docker -d [OPTIONS]

+ 启动配置文件

  /etc/default/docker



#### Docker的远程访问

+ 环境准备
  1. 第二台安装Docker的服务器
  2. 修改Docker守护进程启动选项，区别服务器
  3. 保证Client API与Server API版本一致



#### Dockerfile指令

+ FROM

  ```dockerfile
  FROM <image> #image已存在的镜像
  FROM <image>:<tag>
  ```

+ MAINTAINER <name>

  指定镜像的作者信息，包含镜像的所有者和联系信息

  [Dockerfile指令详解](https://www.runoob.com/docker/docker-dockerfile.html)



#### Dockerfile构建过程



#### Docker容器的网络连接

##### Docker容器的网络基础

```sh
ifconfig
```

+ docker0 linux虚拟网桥

  linux虚拟网桥的特点：

  - 可以设置IP地址
  - 相当于拥有一个隐藏的虚拟网卡

  ```sh
  sudo apt-get install bridage-utils
  sudo brctl show
  ```

+ 自定义docker0

  ```sh
  sudo ifconfig docker0 192.168.200.1 netmask 255.255.255.0
  ```

+ 自定义虚拟网桥

  ```sh
  sudo brctl addbr br0
  sudo ifconfig br0 192.168.100.1 netmask 255.255.255.0
  ```

  更改docker守护进程的启动配置

##### Docker容器的互联

> + 允许所有容器互联
> + 拒绝容器间互联
> + 允许特定容器间的连接

+ 环境准备

  ```dockerfile
  FROM ubuntu:14.04
  RUN apt-get update
  RUN apt-get install -y inetutils-ping
  RUN apt-get install -y nginx
  RUN apt-get install -y curl
  EXPOSE 80
  CMD /bin/bash
  ```

+ 允许所有容器间连接

  ```sh
  docker run --link [容器名]:[别名] IMAGE [COMMAND]
  docker run -it --name cct3 --link=cct1:webtest yanwu/cct
  ```

+ 拒绝所有容器间连接

  修改daemon.js 
  
+ 允许特定容器间的连接

  修改daemon.js

##### Docker容器与外部网络的连接

> + ip_forward
> + iptables
> + 允许端口映射访问
> + 限制IP访问容器

+ 守护进程配置--ip-forward

  --ip-forward=true 数据转发开启

  查看数据转发情况

  ```sh
  sysctl net.ipv4.conf.all.forwarding
  ```
  
+ iptables包过滤防火墙

  主要使用到filter表，包含：

  - INPUT
  - FORWARD
  - OUTPUT

  ```sh
  sudo iptables -L -n # 查看filter表
  
  Chain DOCKER (1 references)
  target     prot opt source               destination
  # 允许外部访问
  ACCEPT     tcp  --  0.0.0.0/0            172.17.0.5           tcp dpt:80
  
  # 禁止某IP访问目标IP
  sudo iptables -I DOCKER -s 10.211.55.3 -d 172.17.0.5 -p TCP --dport 80 -j DROP
  
  target     prot opt source               destination 
  # 被禁止IP
  DROP       tcp  --  10.211.55.3          172.17.0.5           tcp dpt:80
  ACCEPT     tcp  --  0.0.0.0/0            172.17.0.5           tcp dpt:80
  ```

  