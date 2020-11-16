passwd

apt-get update

apt-get install -y vim

apt-get install sudo

apt-get install openssh-client

apt-get install openssh-server

sudo vim /etc/ssh/sshd_config

service ssh start

docker run -it -p 55555:22 yanwu/ubuntu-ssh /bin/bash