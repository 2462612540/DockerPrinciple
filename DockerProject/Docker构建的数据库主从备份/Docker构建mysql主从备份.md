# docker 构建mysql的主从备份

## 镜像的下载

```shell
#查询mysql镜像
docker search mysql:5.7
#拉取mysql5.7镜像
docker pull mysql:5.7
```

## 挂载卷文件创建

```shell
#创建主数据库
mkdir /mysqldata/mysql-master/conf
mkdir /mysqldata/mysql-master/data
mkdir /mysqldata/mysql-master/log

#创建备数据库
mkdir /mysqldata/mysql-slave/conf
mkdir /mysqldata/mysql-slave/data
mkdir /mysqldata/mysql-slave/log
```

### mysql master conf文件配置
```shell
# 创建mysql master的conf文件 
/mysqldata/mysql-master/conf
## 配置文件
[mysqld]## 设置server_id，同一局域网中需要唯一
server_id=101
## 指定不需要同步的数据库名称
binlog-ignore-db=mysql
## 开启二进制日志功能
log-bin=mall-mysql-bin
# 设置二进制日志使用内存大小（事务）
binlog_cache_size=1M
# 设置使用的二进制日志格式（mixed,statement,row）
binlog_format=mixed
# 二进制日志过期清理时间。默认值为0，表示不自动清理。
expire_logs_days=7
# 跳过主从复制中遇到的所有错误或指定类型的错误，避免slave端复制中断。
# 如：1062错误是指一些主键重复，1032错误是因为主从数据库数据不一致
slave_skip_errors=1062
```

### mysql slave conf文件配置
```shell
# 创建mysql master的conf文件 
/mysqldata/mysql-slave/conf
## 配置文件
[mysqld]## 设置server_id，同一局域网中需要唯一
server_id=102
## 指定不需要同步的数据库名称
binlog-ignore-db=mysql
## 开启二进制日志功能，以备Slave作为其它数据库实例的Master时使用
log-bin=mall-mysql-slave1-bin
# 设置二进制日志使用内存大小（事务）
binlog_cache_size=1M
#设置使用的二进制日志格式（mixed,statement,row）
binlog_format=mixed
## 二进制日志过期清理时间。默认值为0，表示不自动清理。
expire_logs_days=7
# 跳过主从复制中遇到的所有错误或指定类型的错误，避免slave端复制中断。
# 如：1062错误是指一些主键重复，1032错误是因为主从数据库数据不一致
slave_skip_errors=1062
# relay_log配置中继日志
relay_log=mall-mysql-relay-bin
# log_slave_updates表示slave将复制事件写进自己的二进制日志
log_slave_updates=1
## slave设置为只读（具有super权限的用户除外）
read_only=1
```

## mysql master 主容器的启动

```shell
# 删除指定容器
docker run -p 3306:3306 --name mysql-master -v /mysqldata/mysql-master/log:/var/log/mysql -v /mysqldata/mysql-master/data:/var/lib/mysql -v /mysqldata/mysql-master/conf:/etc/mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
```

## mysql slave 从容器的启动

```shell
# 删除指定容器
docker run -p 3307:3306 --name mysql-slave -v /mysqldata/mysql-slave/log:/var/log/mysql -v /mysqldata/mysql-slave/data:/var/lib/mysql -v /mysqldata/mysql-slave/conf:/etc/mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
```

## mysql master 配置

```shell
# 进入mysql-master容器
docker exec -it mysql-master /bin/bash
mysql -uroot -proot
# master容器实例内创建数据同步用户
CREATE USER 'slave'@'%' IDENTIFIED BY '123456';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'slave'@'%';
#在主数据库中查看主从同步状态
show master status;
```

## mysql slave 配置

```shell
# 进入mysql-slave容器
docker exec -it mysql-slave /bin/bash
mysql -uroot -proot
#在从数据库中配置主从复制
change master to master_host='宿主机ip', master_user='slave', master_password='123456', master_port=3307, master_log_file='mall-mysql-bin.000001', master_log_pos=617, master_connect_retry=30;
# 主从复制命令参数说明
master_host:主数据库的IP地址
master_port:主数据库的运行端口
master_user:在主数据库创建的用于同步数据的用户账号
master_password:在主数据库创建的用于同步数据的用户密码
master_log_file:指定从数据库要复制数据的日志文件,通过查看主数据的状态,获取File参数
master_log_pos:指定从数据库从哪个位置开始复制数据,通过查看主数据的状态,获取Position参数
master_connect_retry:连接失败重试的时间间隔,单位为秒

# 在从数据库中查看主从同步状态
show slave status \G;
```

# mysql主从复制测试
主机新建库-使用库-新建表-插入数据，ok
从机使用库-查看记录，ok
