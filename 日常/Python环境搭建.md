#### 安装pipenv虚拟环境

1. ```sh
   pip install --upgrade setuptools // 更新setuptools
   ```

2. ```sh
   python -m pip install --upgrade pip // 更新pip windows
   pip install --upgrade pip // linux
   ```

3. 以管理员身份运行cmd

   ```sh
   pip install pipenv
   ```

4. 在创建的项目文件夹下执行命令搭建Django项目

   ```sh
   pipenv install django==2.2.3
   ```

5.  查看到项目对应的虚拟环境的具体位置 

   ```sh
   pipenv --venv
   ```


#### pipenv更换国内镜像源

+ 将项目目录下Pipfile文件url改为清华大学镜像源https://pypi.tuna.tsinghua.edu.cn/simple/ 

