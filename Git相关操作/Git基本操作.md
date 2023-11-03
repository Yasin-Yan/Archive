```
git init // 在本地创建一个Git仓库

git clone [url] // 拷贝一个Git仓库到本地

git tag -a <tagname> -m "<描述>" // 给上一次提交打上标签

git tag // 查看已有标签

git tag -d <version> // 删除标签

git branch (branchname) // 创建分支

git checkout (branchname) // 切换分支

git checkout -b [新分支名] [标签名] // 拉取标签快照生成一个分支

git show <tag_name> // 查看标签的详细信息(包含commit的信息)

git tag -ln [tag_name] // 显示标签名及其描述信息

git commit [file1] [file2] ... -m [message]

git clone -b dev 代码仓库地址 //（dev是分支名称）拉取分支

git fetch origin master:tmpm // 将远程Master最新内容拉取到本地并创建一个分支

git rebase -i <版本号> // 合并该版本号之后的分支

git stash save '' // 将当前工作空间存入缓存并注释

git stash apply stash@{1} // 从缓存取暂存记录不删除

git stash clear // 清除所有暂存记录
```




