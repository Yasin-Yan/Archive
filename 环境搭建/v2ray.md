#### ununtu1604

1. 修改系统时间
```shell
# 删除本地的时间文件，加入上海时区
rm -rf /etc/localtime
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

2. 安装v2ray
```shell
bash <(curl -L -s https://install.direct/go.sh)

# 用于程序开机启动并且崩溃时自动重启程序
sudo systemctl enable v2ray
```

3. 启动
```shell
systemctl start v2ray
```

4. 锐速安装
```shell
# Debian/Ubuntun: LotServer+内核更换一键脚本
wget --no-check-certificate https://www.vrrmr.net/55R/rs_nh.sh && bash rs_nh.sh
```

5. 多用户配置
```shell
# 再创建一个用户 id
cat /proc/sys/kernel/random/uuid

# 输入 i 进入编辑模式，复制inbounds[ ]中的内容，再粘贴一个出来
vi /etc/v2ray/config.json
```

