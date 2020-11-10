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

  