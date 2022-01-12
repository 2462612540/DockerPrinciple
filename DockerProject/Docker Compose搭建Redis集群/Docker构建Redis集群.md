# docker 构建 redis集群

## redis的镜像的拉取

```shell
#查询redis镜像
docker search redis
#拉取redis镜像
docker pull redis
```

## redis挂载卷配置

```shell
#创建redis数据文件夹
mkdir /redisdata/redis-node-1
mkdir /redisdata/redis-node-2
mkdir /redisdata/redis-node-3
mkdir /redisdata/redis-node-4
mkdir /redisdata/redis-node-5
mkdir /redisdata/redis-node-6
mkdir /redisdata/redis-node-7
mkdir /redisdata/redis-node-8
```

## redis node 6个容器运行
```shell
#运行redis-node1
docker run -d --name redis-node-1 --net host --privileged=true -v /redisdata/redis-node-1:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6381 
docker run -d --name redis-node-2 --net host --privileged=true -v /redisdata/redis-node-2:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6382
docker run -d --name redis-node-3 --net host --privileged=true -v /redisdata/redis-node-3:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6383
docker run -d --name redis-node-4 --net host --privileged=true -v /redisdata/redis-node-4:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6384
docker run -d --name redis-node-5 --net host --privileged=true -v /redisdata/redis-node-5:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6385
docker run -d --name redis-node-6 --net host --privileged=true -v /redisdata/redis-node-6:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6386
```

## redis 构建集群关系
```shell
#进入容器
docker exec -it redis-node-1 /bin/bash
# 注意，进入docker容器后才能执行一下命令，且注意自己的真实IP地址  --cluster-replicas 1表示为每个master创建一个slave节点   
redis-cli --cluster create 192.168.111.147:6381 192.168.111.147:6382 192.168.111.147:6383 192.168.111.147:6384 192.168.111.147:6385 192.168.111.147:6386 --cluster-replicas 1
#链接进入6381作为切入点，查看集群状态
cluster info
cluster nodes
```

# docker 主从容错切换迁移
```shell
# 数据读写存储
启动6机构成的集群并通过exec进入
对6381新增两个key
防止路由失效加参数-c并新增两个key
加入参数-c,优化路由
# 查看集群信息
redis-cli --cluster check 192.168.111.147:6381
```

## 容错切换迁移
```shell
# 主6381和从机切换，先停止主机6381
6381主机停了,对应的真实从机上位
6381作为1号主机分配的从机以实际情况为准,具体是几号机器就是几号

# 先启6381
docker start redis-node-1

# 再停6385
docker stop redis-node-5

# 再启6385
docker start redis-node-5

# 查看集群状态
redis-cli --cluster check 自己IP:6381
```

## 主从扩容案例
```shell
# 新建6387、6388两个节点+新建后启动+查看是否8节点
docker run -d --name redis-node-7 --net host --privileged=true -v /redisdata/redis-node-7:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6387
docker run -d --name redis-node-8 --net host --privileged=true -v /redisdata/redis-node-8:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6388
# 进入6387容器实例内部
docker exec -it redis-node-7 /bin/bash
# 将新增的6387节点(空槽号)作为master节点加入原集群
将新增的6387作为master节点加入集群 redis-cli --cluster add-node 自己实际IP地址:6387 自己实际IP地址:6381 6387 就是将要作为master新增节点6381 就是原来集群节点里面的领路人.相当于6387拜拜6381的码头从而找到组织加入集群
# 检查集群情况第1次
redis-cli --cluster check 真实ip地址:6381
# 重新分派槽号
重新分派槽号命令:redis-cli --cluster reshard IP地址:端口号redis-cli --cluster reshard 192.168.111.147:6381
# 检查集群情况第2次
redis-cli --cluster check 真实ip地址:6381
# 槽号分派说明
为什么6387是3个新的区间,以前的还是连续?重新分配成本太高,所以前3家各自匀出来一部分,从6381/6382/6383三个旧节点分别匀出1364个坑位给新节点6387
# 为主节点6387分配从节点6388

命令:redis-cli --cluster add-node ip:新slave端口 ip:新master端口 --cluster-slave --cluster-master-id 新主机节点ID 
redis-cli --cluster add-node 192.168.111.147:6388 192.168.111.147:6387 --cluster-slave --cluster-master-id e4781f644d4a4e4d4b4d107157b9ba8144631451-------这个是6387的编号,按照自己实际情况
# 检查集群情况第3次
redis-cli --cluster check 192.168.111.147:6382
```

## 主从缩容案例

```shell
# 目的：6387和6388下线 检查集群情况1获得6388的节点ID
redis-cli --cluster check 192.168.111.147:6382
# 将6388删除 从集群中将4号从节点6388删除
redis-cli --clusterdel-nodeip:从机端口 从机6388节点ID redis-cli --clusterdel-node192.168.111.147:6388 5d149074b7e57b802287d1797a874ed7a1a284a8 redis-cli 
--cluster check 192.168.111.147:6382检查一下发现,6388被删除了,只剩下7台机器了.
# 将6387的槽号清空，重新分配，本例将清出来的槽号都给6381
redis-cli --cluster reshard 192.168.111.147:6381
# 将6387删除
命令:redis-cli --cluster del-node ip:端口 6387节点ID redis-cli --cluster del-node 192.168.111.147:6387 e4781f644d4a4e4d4b4d107157b9ba8144631451
# 检查集群情况第三次
redis-cli --cluster check 192.168.111.147:6381
```

	