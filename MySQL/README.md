### 用户创建&授权
``` sql

-- 创建新用户
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password'; 

-- 授予完全权限
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost'; 

-- 刷新所有权限，使修改生效
FLUSH PRIVILEGES; 


-- type_of_permission
/*
CREATE-允许他们创建新的表或数据库
DROP-允许他们删除表或数据库
DELETE-允许他们从表中删除行
INSERT-允许它们将行插入表中
SELECT-允许他们使用该SELECT命令读取数据库
UPDATE - 允许他们更新表行
GRANT OPTION-允许他们授予或删除其他用户的权限
*/

-- 授予权限
GRANT type_of_permission ON database_name.table_name TO 'username'@'localhost'; 

-- 撤销权限
REVOKE type_of_permission ON database_name.table_name FROM 'username'@'localhost'; 

-- 查看用户的当前权限
SHOW GRANTS FOR username

-- 删除用户
DROP USER 'username'@'localhost'; 
```

