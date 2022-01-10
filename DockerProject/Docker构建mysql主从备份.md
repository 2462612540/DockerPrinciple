## 基础篇(零基小白)

### Docker简介

- 前提知识+课程定位+开场闲聊
- 是什么

	- 问题：为什么会有docker出现

	  假定您在开发一个尚硅谷的谷粒商城，您使用的是一台笔记本电脑而且您的开发环境具有特定的配置。其他开发人员身处的环境配置也各有不同。您正在开发的应用依赖于您当前的配置且还要依赖于某些配置文件。此外，您的企业还拥有标准化的测试和生产环境，且具有自身的配置和一系列支持文件。您希望尽可能多在本地模拟这些环境而不产生重新创建服务器环境的开销。请问？您要如何确保应用能够在这些环境中运行和通过质量检测？并且在部署过程中不出现令人头疼的版本、配置问题，也无需重新编写代码和进行故障修复？ 答案就是使用容器。Docker之所以发展如此迅速，也是因为它对此给出了一个标准化的解决方案-----系统平滑移植，容器虚拟化技术。 环境配置相当麻烦，换一台机器，就要重来一次，费力费时。很多人想到，能不能从根本上解决问题，软件可以带环境安装？也就是说，安装的时候，把原始环境一模一样地复制过来。开发人员利用 Docker 可以消除协作编码时“在我的机器上可正常工作”的问题。  之前在服务器配置一个应用的运行环境，要安装各种软件，就拿尚硅谷电商项目的环境来说，Java/RabbitMQ/MySQL/JDBC驱动包等。安装和配置这些东西有多麻烦就不说了，它还不能跨平台。假如我们是在 Windows 上安装的这些环境，到了 Linux 又得重新装。况且就算不跨操作系统，换另一台同样操作系统的服务器，要移植应用也是非常麻烦的。传统上认为，软件编码开发/测试结束后，所产出的成果即是程序或是能够编译执行的二进制字节码等(java为例)。而为了让这些程序可以顺利执行，开发团队也得准备完整的部署文件，让维运团队得以部署应用程式，开发需要清楚的告诉运维部署团队，用的全部配置文件+所有软件环境。不过，即便如此，仍然常常发生部署失败的状况。Docker的出现使得Docker得以打破过去「程序即应用」的观念。透过镜像(images)将作业系统核心除外，运作应用程式所需要的系统环境，由下而上打包，达到应用程式跨平台间的无缝接轨运作。

	- docker理念

	  Docker是基于Go语言实现的云开源项目。Docker的主要目标是“Build，Ship and Run Any App,Anywhere”，也就是通过对应用组件的封装、分发、部署、运行等生命周期的管理，使用户的APP（可以是一个WEB应用或数据库应用等等）及其运行环境能够做到“一次镜像，处处运行”。Linux容器技术的出现就解决了这样一个问题，而 Docker 就是在它的基础上发展过来的。将应用打成镜像，通过镜像成为运行在Docker容器上面的实例，而 Docker容器在任何操作系统上都是一致的，这就实现了跨平台、跨服务器。只需要一次配置好环境，换到别的机子上就可以一键部署好，大大简化了操作。

	- 一句话

		- 解决了运行环境和配置问题的软件容器，
方便做持续集成并有助于整体发布的容器虚拟化技术。

- 容器与虚拟机比较

	- 容器发展简史 

	   

	- 传统虚拟机技术

	  虚拟机（virtual machine）就是带环境安装的一种解决方案。它可以在一种操作系统里面运行另一种操作系统，比如在Windows10系统里面运行Linux系统CentOS7。应用程序对此毫无感知，因为虚拟机看上去跟真实系统一模一样，而对于底层系统来说，虚拟机就是一个普通文件，不需要了就删掉，对其他部分毫无影响。这类虚拟机完美的运行了另一套系统，能够使应用程序，操作系统和硬件三者之间的逻辑不变。  Win10VMWareCentos7各种cpu、内存网络额配置+各种软件虚拟机实例 虚拟机的缺点：1    资源占用多               2    冗余步骤多                 3    启动慢

	- 容器虚拟化技术

	  由于前面虚拟机存在某些缺点，Linux发展出了另一种虚拟化技术：Linux容器(Linux Containers，缩写为 LXC)Linux容器是与系统其他部分隔离开的一系列进程，从另一个镜像运行，并由该镜像提供支持进程所需的全部文件。容器提供的镜像包含了应用的所有依赖项，因而在从开发到测试再到生产的整个过程中，它都具有可移植性和一致性。 Linux 容器不是模拟一个完整的操作系统而是对进程进行隔离。有了容器，就可以将软件运行所需的所有资源打包到一个隔离的容器中。容器与虚拟机不同，不需要捆绑一整套操作系统，只需要软件工作所需的库资源和设置。系统因此而变得高效轻量并保证部署在任何环境中的软件都能始终如一地运行。  

	- 对比

	   比较了 Docker 和传统虚拟化方式的不同之处：*传统虚拟机技术是虚拟出一套硬件后，在其上运行一个完整操作系统，在该系统上再运行所需应用进程；*容器内的应用进程直接运行于宿主的内核，容器内没有自己的内核且也没有进行硬件虚拟。因此容器要比传统虚拟机更为轻便。* 每个容器之间互相隔离，每个容器有自己的文件系统 ，容器之间进程不会相互影响，能区分计算资源。

- 能干嘛

	- 技术职级变化

		- coder

			- programmer

				- software engineer

					- DevOps engineer

	- 开发/运维（DevOps）新一代开发工程师

		- 一次构建、随处运行

			- 更快速的应用交付和部署

			  传统的应用开发完成后，需要提供一堆安装程序和配置说明文档，安装部署后需根据配置文档进行繁杂的配置才能正常运行。Docker化之后只需要交付少量容器镜像文件，在正式生产环境加载镜像并运行即可，应用安装配置在镜像里已经内置好，大大节省部署配置和测试验证时间。

			- 更便捷的升级和扩缩容

			  随着微服务架构和Docker的发展，大量的应用会通过微服务方式架构，应用的开发构建将变成搭乐高积木一样，每个Docker容器将变成一块“积木”，应用的升级将变得非常容易。当现有的容器不足以支撑业务处理时，可通过镜像运行新的容器进行快速扩容，使应用系统的扩容从原先的天级变成分钟级甚至秒级。

			- 更简单的系统运维

			  应用容器化运行后，生产环境运行的应用可与开发、测试环境的应用高度一致，容器会将应用程序相关的环境和状态完全封装起来，不会因为底层基础架构和操作系统的不一致性给应用带来影响，产生新的BUG。当出现程序异常时，也可以通过测试环境的相同容器进行快速定位和修复。

			- 更高效的计算资源利用

			   　Docker是内核级虚拟化，其不像传统的虚拟化技术一样需要额外的Hypervisor支持，所以在一台物理机上可以运行很多个容器实例，可大大提升物理服务器的CPU和内存的利用率。

		- · Docker应用场景

		   

	- 哪些企业在使用

		- 新浪

		   

		- 美团

		   

		- 蘑菇街
		- ......

- 去哪下

	- 官网

		- docker官网：http://www.docker.com

	- 仓库

		- Docker Hub官网: https://hub.docker.com/

### Docker安装

- 前提说明

  CentOS Docker 安装前提条件目前，CentOS 仅发行版本中的内核支持 Docker。Docker 运行在CentOS 7 (64-bit)上，要求系统为64位、Linux系统内核版本为 3.8以上，这里选用Centos7.x 查看自己的内核uname命令用于打印当前系统相关信息（内核版本号、硬件架构、主机名称和操作系统类型等）。

- Docker的基本组成

	- 镜像(image)

	  Docker 镜像（Image）就是一个只读的模板。镜像可以用来创建 Docker 容器，一个镜像可以创建很多容器。它也相当于是一个root文件系统。比如官方镜像 centos:7 就包含了完整的一套 centos:7 最小系统的 root 文件系统。相当于容器的“源代码”，docker镜像文件类似于Java的类模板，而docker容器实例类似于java中new出来的实例对象。    

	- 容器(container)

	   1 从面向对象角度Docker 利用容器（Container）独立运行的一个或一组应用，应用程序或服务运行在容器里面，容器就类似于一个虚拟化的运行环境，容器是用镜像创建的运行实例。就像是Java中的类和实例对象一样，镜像是静态的定义，容器是镜像运行时的实体。容器为镜像提供了一个标准的和隔离的运行环境，它可以被启动、开始、停止、删除。每个容器都是相互隔离的、保证安全的平台 2 从镜像容器角度可以把容器看做是一个简易版的 Linux 环境（包括root用户权限、进程空间、用户空间和网络空间等）和运行在其中的应用程序。

	- 仓库(repository)

	   仓库（Repository）是集中存放镜像文件的场所。 类似于Maven仓库，存放各种jar包的地方；github仓库，存放各种git项目的地方；Docker公司提供的官方registry被称为Docker Hub，存放各种镜像模板的地方。 仓库分为公开仓库（Public）和私有仓库（Private）两种形式。最大的公开仓库是 Docker Hub(https://hub.docker.com/)，存放了数量庞大的镜像供用户下载。国内的公开仓库包括阿里云 、网易云等

	- 小总结

	  需要正确的理解仓库/镜像/容器这几个概念:Docker 本身是一个容器运行载体或称之为管理引擎。我们把应用程序和配置依赖打包好形成一个可交付的运行环境，这个打包好的运行环境就是image镜像文件。只有通过这个镜像文件才能生成Docker容器实例(类似Java中new出来一个对象)。 image文件可以看作是容器的模板。Docker 根据 image 文件生成容器的实例。同一个 image 文件，可以生成多个同时运行的容器实例。 镜像文件*  image 文件生成的容器实例，本身也是一个文件，称为镜像文件。容器实例*  一个容器运行一种服务，当我们需要的时候，就可以通过docker客户端创建一个对应的运行实例，也就是我们的容器仓库* 就是放一堆镜像的地方，我们可以把镜像发布到仓库中，需要的时候再从仓库中拉下来就可以了。 

- Docker平台架构图解(架构版)

	- 首次懵逼正常，后续深入，先有大概轮廓，混个眼熟
	- 整体架构及底层通信原理简述

	  Docker 是一个 C/S 模式的架构，后端是一个松耦合架构，众多模块各司其职。 

- 安装步骤

	- CentOS7安装Docker

		- https://docs.docker.com/engine/install/centos/
		- 安装步骤

			- 确定你是CentOS7及以上版本

				- cat /etc/redhat-release

			- 卸载旧版本

			   https://docs.docker.com/engine/install/centos/  

			- yum安装gcc相关

				- CentOS7能上外网

					- Subtopic

				- yum -y install gcc
				- yum -y install gcc-c++

			- 安装需要的软件包

				- 官网要求
				- 执行命令

					- yum install -y yum-utils

			- 设置stable镜像仓库

				- 大坑

					- yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

					   报错：1   [Errno 14] curl#35 - TCP connection reset by peer  2   [Errno 12] curl#35 - Timeout

					- 官网要求

					   报错：1   [Errno 14] curl#35 - TCP connection reset by peer  2   [Errno 12] curl#35 - Timeout

				- 推荐

					- yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
					- 我们自己

					   

			- 更新yum软件包索引

				- yum makecache fast

			- 安装DOCKER CE

				- yum -y install docker-ce docker-ce-cli containerd.io

					- 官网要求
					- 执行结果

			- 启动docker

				- systemctl start docker

			- 测试

				- docker version

					- 本次安装时间2021.11

					   本次安装时间2021.11  

				- docker run hello-world

			- 卸载

				- systemctl stop docker 
				- yum remove docker-ce docker-ce-cli containerd.io
				- rm -rf /var/lib/docker
				- rm -rf /var/lib/containerd

- 阿里云镜像加速

	- 是什么

		- https://promotion.aliyun.com/ntms/act/kubernetes.html

	- 注册一个属于自己的阿里云账户(可复用淘宝账号)
	- 获得加速器地址连接

		- 登陆阿里云开发者平台
		- 点击控制台
		- 选择容器镜像服务
		- 获取加速器地址

		   

	- 粘贴脚本直接执行

		- 直接粘

		   mkdir -p /etc/dockertee /etc/docker/daemon.json <<-'EOF'{  "registry-mirrors": ["https://aa25jngu.mirror.aliyuncs.com"]}EOF 

		- 或者分步骤都行

			- mkdir -p /etc/docker
			- vim  /etc/docker/daemon.json

			     #阿里云{  "registry-mirrors": ["https://｛自已的编码｝.mirror.aliyuncs.com"]}

	- 重启服务器

		- systemctl daemon-reload
		- systemctl restart docker

- 永远的HelloWorld

	- 启动Docker后台容器(测试运行 hello-world)

		- docker run hello-world

		  输出这段提示以后，hello world就会停止运行，容器自动终止。

		- run干了什么

- 底层原理

	- 为什么Docker会比VM虚拟机快

	  (1)docker有着比虚拟机更少的抽象层   由于docker不需要Hypervisor(虚拟机)实现硬件资源虚拟化,运行在docker容器上的程序直接使用的都是实际物理机的硬件资源。因此在CPU、内存利用率上docker将会在效率上有明显优势。(2)docker利用的是宿主机的内核,而不需要加载操作系统OS内核   当新建一个容器时,docker不需要和虚拟机一样重新加载一个操作系统内核。进而避免引寻、加载操作系统内核返回等比较费时费资源的过程,当新建一个虚拟机时,虚拟机软件需要加载OS,返回新建过程是分钟级别的。而docker由于直接利用宿主机的操作系统,则省略了返回过程,因此新建一个docker容器只需要几秒钟。    

### Docker常用命令

- 帮助启动类命令

	- 启动docker： systemctl start docker
	- 停止docker： systemctl stop docker
	- 重启docker： systemctl restart docker
	- 查看docker状态： systemctl status docker
	- 开机启动： systemctl enable docker
	- 查看docker概要信息： docker info
	- 查看docker总体帮助文档： docker --help
	- 查看docker命令帮助文档： docker 具体命令 --help

- 镜像命令

	- docker images

		- 列出本地主机上的镜像

		   各个选项说明:REPOSITORY：表示镜像的仓库源TAG：镜像的标签版本号IMAGE ID：镜像IDCREATED：镜像创建时间SIZE：镜像大小 同一仓库源可以有多个 TAG版本，代表这个仓库源的不同个版本，我们使用 REPOSITORY:TAG 来定义不同的镜像。如果你不指定一个镜像的版本标签，例如你只使用 ubuntu，docker 将默认使用 ubuntu:latest 镜像  

		- OPTIONS说明：

			- -a :列出本地所有的镜像（含历史映像层）
			- -q :只显示镜像ID。

	- docker search 某个XXX镜像名字

		- 网站

			- https://hub.docker.com

		- 命令

			- docker search [OPTIONS] 镜像名字
			- 案例

			    

			- OPTIONS说明：

				- --limit : 只列出N个镜像，默认25个
				- docker search --limit 5 redis

	- docker pull 某个XXX镜像名字

		- 下载镜像
		- docker pull 镜像名字[:TAG]
		- docker pull 镜像名字

			- 没有TAG就是最新版
			- 等价于
			- docker pull 镜像名字:latest
			- docker pull ubuntu

	- docker system df 查看镜像/容器/数据卷所占的空间
	- docker rmi 某个XXX镜像名字ID

		- 删除镜像
		- 删除单个

			- docker rmi  -f 镜像ID

		- 删除多个

			- docker rmi -f 镜像名1:TAG 镜像名2:TAG 

		- 删除全部

			- docker rmi -f $(docker images -qa)

	- 面试题：谈谈docker虚悬镜像是什么？

		- 是什么

			- 仓库名、标签都是<none>的镜像，俗称虚悬镜像dangling image
			- 长什么样

		- 后续Dockerfile章节再介绍

	- 思考

		- 结合我们Git的学习心得，大家猜猜是否会有
docker commit /docker push？？

- 容器命令

	- 有镜像才能创建容器，
这是根本前提(下载一个CentOS或者ubuntu镜像演示)

		- 说明

		   

		- docker pull centos
		- docker pull ubuntu
		- 本次演示用ubuntu演示

	- 新建+启动容器

		- docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

			-  OPTIONS说明

			   OPTIONS说明（常用）：有些是一个减号，有些是两个减号 --name="容器新名字"       为容器指定一个名称；-d: 后台运行容器并返回容器ID，也即启动守护式容器(后台运行)； -i：以交互模式运行容器，通常与 -t 同时使用；-t：为容器重新分配一个伪输入终端，通常与 -i 同时使用；也即启动交互式容器(前台有伪终端，等待交互)； -P: 随机端口映射，大写P-p: 指定端口映射，小写p

			- 启动交互式容器(前台命令行)

			  #使用镜像centos:latest以交互模式启动一个容器,在容器内执行/bin/bash命令。docker run -it centos /bin/bash  参数说明：-i: 交互式操作。-t: 终端。centos : centos 镜像。/bin/bash：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。要退出终端，直接输入 exit: 

	- 列出当前所有正在运行的容器

		- docker ps [OPTIONS]

			-  OPTIONS说明

			  OPTIONS说明（常用）： -a :列出当前所有正在运行的容器+历史上运行过的-l :显示最近创建的容器。-n：显示最近n个创建的容器。-q :静默模式，只显示容器编号。

	- 退出容器

		- 两种退出方式

			- exit

				- run进去容器，exit退出，容器停止

			- ctrl+p+q

				- run进去容器，ctrl+p+q退出，容器不停止

	- 启动已停止运行的容器

		- docker start 容器ID或者容器名

	- 重启容器

		- docker restart 容器ID或者容器名

	- 停止容器

		- docker stop 容器ID或者容器名

	- 强制停止容器

		- docker kill 容器ID或容器名

	- 删除已停止的容器

		- docker rm 容器ID

			- 一次性删除多个容器实例

				- docker rm -f $(docker ps -a -q)
				- docker ps -a -q | xargs docker rm

	- 重要

		- 有镜像才能创建容器，这是根本前提(下载一个Redis6.0.8镜像演示)
		- 启动守护式容器(后台服务器)

			- 在大部分的场景下，我们希望 docker 的服务是在后台运行的，
我们可以过 -d 指定容器的后台运行模式。
			- docker run -d 容器名

			   #使用镜像centos:latest以后台模式启动一个容器docker run -d centos 问题：然后docker ps -a 进行查看, 会发现容器已经退出很重要的要说明的一点: Docker容器后台运行,就必须有一个前台进程.容器运行的命令如果不是那些一直挂起的命令（比如运行top，tail），就是会自动退出的。 这个是docker的机制问题,比如你的web容器,我们以nginx为例，正常情况下,我们配置启动服务只需要启动响应的service即可。例如service nginx start但是,这样做,nginx为后台进程模式运行,就导致docker前台没有运行的应用,这样的容器后台启动后,会立即自杀因为他觉得他没事可做了.所以，最佳的解决方案是,将你要运行的程序以前台进程的形式运行，常见就是命令行模式，表示我还有交互操作，别中断，O(∩_∩)O哈哈~

			- redis 前后台启动演示case

				- 前台交互式启动

					-  docker run -it redis:6.0.8

				- 后台守护式启动

					- docker run -d redis:6.0.8

		- 查看容器日志

			- docker logs 容器ID

		- 查看容器内运行的进程

			- docker top 容器ID

		- 查看容器内部细节

			- docker inspect 容器ID

		- 进入正在运行的容器并以命令行交互

			- docker exec -it 容器ID bashShell
			- 重新进入docker attach 容器ID
			- 案例演示，用centos或者unbuntu都可以
			- 上述两个区别

				- attach 直接进入容器启动命令的终端，不会启动新的进程
用exit退出，会导致容器的停止。

				   

				- exec 是在容器中打开新的终端，并且可以启动新的进程
用exit退出，不会导致容器的停止。

			- 推荐大家使用 docker exec 命令，因为退出容器终端，不会导致容器的停止。
			- 用之前的redis容器实例进入试试

				- 进入redis服务

					- docker exec -it 容器ID /bin/bash
					- docker exec -it 容器ID redis-cli
					- 一般用-d后台启动的程序，再用exec进入对应容器实例

		- 从容器内拷贝文件到主机上

			- 容器→主机
			- docker cp  容器ID:容器内路径 目的主机路径

			   公式：docker cp  容器ID:容器内路径 目的主机路径 

		- 导入和导出容器

			- export 导出容器的内容留作为一个tar归档文件[对应import命令]
			- import 从tar包中的内容创建一个新的文件系统再导入为镜像[对应export]
			- 案例

				- docker export 容器ID > 文件名.tar
				- cat 文件名.tar | docker import - 镜像用户/镜像名:镜像版本号

- 小总结

	- 常用命令

	  图片正下方还有命令 attach    Attach to a running container                 # 当前 shell 下 attach 连接指定运行镜像build     Build an image from a Dockerfile              # 通过 Dockerfile 定制镜像commit    Create a new image from a container changes   # 提交当前容器为新的镜像cp        Copy files/folders from the containers filesystem to the host path   #从容器中拷贝指定文件或者目录到宿主机中create    Create a new container                        # 创建一个新的容器，同 run，但不启动容器diff      Inspect changes on a container's filesystem   # 查看 docker 容器变化events    Get real time events from the server          # 从 docker 服务获取容器实时事件exec      Run a command in an existing container        # 在已存在的容器上运行命令export    Stream the contents of a container as a tar archive   # 导出容器的内容流作为一个 tar 归档文件[对应 import ]history   Show the history of an image                  # 展示一个镜像形成历史images    List images                                   # 列出系统当前镜像import    Create a new filesystem image from the contents of a tarball # 从tar包中的内容创建一个新的文件系统映像[对应export]info      Display system-wide information               # 显示系统相关信息inspect   Return low-level information on a container   # 查看容器详细信息kill      Kill a running container                      # kill 指定 docker 容器load      Load an image from a tar archive              # 从一个 tar 包中加载一个镜像[对应 save]login     Register or Login to the docker registry server    # 注册或者登陆一个 docker 源服务器logout    Log out from a Docker registry server          # 从当前 Docker registry 退出logs      Fetch the logs of a container                 # 输出当前容器日志信息port      Lookup the public-facing port which is NAT-ed to PRIVATE_PORT    # 查看映射端口对应的容器内部源端口pause     Pause all processes within a container        # 暂停容器ps        List containers                               # 列出容器列表pull      Pull an image or a repository from the docker registry server   # 从docker镜像源服务器拉取指定镜像或者库镜像push      Push an image or a repository to the docker registry server    # 推送指定镜像或者库镜像至docker源服务器restart   Restart a running container                   # 重启运行的容器rm        Remove one or more containers                 # 移除一个或者多个容器rmi       Remove one or more images       # 移除一个或多个镜像[无容器使用该镜像才可删除，否则需删除相关容器才可继续或 -f 强制删除]run       Run a command in a new container              # 创建一个新的容器并运行一个命令save      Save an image to a tar archive                # 保存一个镜像为一个 tar 包[对应 load]search    Search for an image on the Docker Hub         # 在 docker hub 中搜索镜像start     Start a stopped containers                    # 启动容器stop      Stop a running containers                     # 停止容器tag       Tag an image into a repository                # 给源中镜像打标签top       Lookup the running processes of a container   # 查看容器中运行的进程信息unpause   Unpause a paused container                    # 取消暂停容器version   Show the docker version information           # 查看 docker 版本号wait      Block until a container stops, then print its exit code   # 截取容器停止时的退出状态值 

### Docker镜像

- 是什么

	- 是什么

	  镜像是一种轻量级、可执行的独立软件包，它包含运行某个软件所需的所有内容，我们把应用程序和配置依赖打包好形成一个可交付的运行环境(包括代码、运行时需要的库、环境变量和配置文件等)，这个打包好的运行环境就是image镜像文件。 只有通过这个镜像文件才能生成Docker容器实例(类似Java中new出来一个对象)。  

	- 分层的镜像

	   以我们的pull为例，在下载的过程中我们可以看到docker的镜像好像是在一层一层的在下载  

	- UnionFS（联合文件系统）

	  UnionFS（联合文件系统）：Union文件系统（UnionFS）是一种分层、轻量级并且高性能的文件系统，它支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下(unite several directories into a single virtual filesystem)。Union 文件系统是 Docker 镜像的基础。镜像可以通过分层来进行继承，基于基础镜像（没有父镜像），可以制作各种具体的应用镜像。 特性：一次同时加载多个文件系统，但从外面看起来，只能看到一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有底层的文件和目录

	-  Docker镜像加载原理

	    Docker镜像加载原理：   docker的镜像实际上由一层一层的文件系统组成，这种层级的文件系统UnionFS。bootfs(boot file system)主要包含bootloader和kernel, bootloader主要是引导加载kernel, Linux刚启动时会加载bootfs文件系统，在Docker镜像的最底层是引导文件系统bootfs。这一层与我们典型的Linux/Unix系统是一样的，包含boot加载器和内核。当boot加载完成之后整个内核就都在内存中了，此时内存的使用权已由bootfs转交给内核，此时系统也会卸载bootfs。 rootfs (root file system) ，在bootfs之上。包含的就是典型 Linux 系统中的 /dev, /proc, /bin, /etc 等标准目录和文件。rootfs就是各种不同的操作系统发行版，比如Ubuntu，Centos等等。 。  平时我们安装进虚拟机的CentOS都是好几个G，为什么docker这里才200M？？对于一个精简的OS，rootfs可以很小，只需要包括最基本的命令、工具和程序库就可以了，因为底层直接用Host的kernel，自己只需要提供 rootfs 就行了。由此可见对于不同的linux发行版, bootfs基本是一致的, rootfs会有差别, 因此不同的发行版可以公用bootfs。 

	- 为什么 Docker 镜像要采用这种分层结构呢

	    镜像分层最大的一个好处就是共享资源，方便复制迁移，就是为了复用。 比如说有多个镜像都从相同的 base 镜像构建而来，那么 Docker Host 只需在磁盘上保存一份 base 镜像；同时内存中也只需加载一份 base 镜像，就可以为所有容器服务了。而且镜像的每一层都可以被共享。 

- 重点理解

	- Docker镜像层都是只读的，容器层是可写的
当容器启动时，一个新的可写层被加载到镜像的顶部。
这一层通常被称作“容器层”，“容器层”之下的都叫“镜像层”。

	  当容器启动时，一个新的可写层被加载到镜像的顶部。这一层通常被称作“容器层”，“容器层”之下的都叫“镜像层”。所有对容器的改动 - 无论添加、删除、还是修改文件都只会发生在容器层中。只有容器层是可写的，容器层下面的所有镜像层都是只读的。

- Docker镜像commit操作案例

	- docker commit提交容器副本使之成为一个新的镜像
	- docker commit -m="提交的描述信息" -a="作者" 容器ID 要创建的目标镜像名:[标签名]
	- 案例演示ubuntu安装vim

		- 从Hub上下载ubuntu镜像到本地并成功运行
		- 原始的默认Ubuntu镜像是不带着vim命令的
		- 外网连通的情况下，安装vim

		   docker容器内执行上述两条命令：apt-get updateapt-get -y install vim   

		- 安装完成后，commit我们自己的新镜像

		    

		- 启动我们的新镜像并和原来的对比

		   1 官网是默认下载的Ubuntu没有vim命令2我们自己commit构建的镜像，新增加了vim功能，可以成功使用。 

	- 小总结

	   Docker中的镜像分层，支持通过扩展现有镜像，创建新的镜像。类似Java继承于一个Base基础类，自己再按需扩展。新镜像是从 base 镜像一层一层叠加生成的。每安装一个软件，就在现有镜像的基础上增加一层

### 本地镜像发布到阿里云

- 本地镜像发布到阿里云流程

    

- 镜像的生成方法

	- 上一讲已经介绍过

		- 基于当前容器创建一个新的镜像，新功能增强
docker commit [OPTIONS] 容器ID [REPOSITORY[:TAG]]

		  OPTIONS说明：-a :提交的镜像作者；-m :提交时的说明文字；本次案例centos+ubuntu两个，当堂讲解一个，家庭作业一个，请大家务必动手，亲自实操。 

	- 后面的DockerFile章节，第2种方法

- 将本地镜像推送到阿里云

	- 本地镜像素材原型

	     

	- 阿里云开发者平台

		- https://promotion.aliyun.com/ntms/act/kubernetes.html

		   

	- 创建仓库镜像

		- 选择控制台，进入容器镜像服务
		- 选择个人实例
		- 命名空间

		   

			- 继续

		- 仓库名称

		    

			- 继续

		- 进入管理界面获得脚本

		   

	- 将镜像推送到阿里云

		- 将镜像推送到阿里云registry

			- 管理界面脚本
			- 脚本实例

			   docker login --username=zzyybuy registry.cn-hangzhou.aliyuncs.comdocker tag cea1bb40441c registry.cn-hangzhou.aliyuncs.com/atguiguwh/myubuntu:1.1docker push registry.cn-hangzhou.aliyuncs.com/atguiguwh/myubuntu:1.1上面命令是阳哥自己本地的，你自己酌情处理，不要粘贴我的。 

- 将阿里云上的镜像下载到本地

	- 下载到本地

	   docker pull registry.cn-hangzhou.aliyuncs.com/atguiguwh/myubuntu:1.1

### 本地镜像发布到私有库

- 本地镜像发布到私有库流程

    

- 是什么

  1 官方Docker Hub地址：https://hub.docker.com/，中国大陆访问太慢了且准备被阿里云取代的趋势，不太主流。2 Dockerhub、阿里云这样的公共镜像仓库可能不太方便，涉及机密的公司不可能提供镜像给公网，所以需要创建一个本地私人仓库供给团队使用，基于公司内部项目构建镜像。    Docker Registry是官方提供的工具，可以用于构建私有镜像仓库

	- Docker Registry

- 将本地镜像推送到私有库

	- 下载镜像Docker Registry

	  docker pull registry    

	- 运行私有库Registry，相当于本地有个私有Docker hub

	   docker run -d -p 5000:5000  -v /zzyyuse/myregistry/:/tmp/registry --privileged=true registry默认情况，仓库被创建在容器的/var/lib/registry目录下，建议自行用容器卷映射，方便于宿主机联调   

	- 案例演示创建一个新镜像，ubuntu安装ifconfig命令

		- 从Hub上下载ubuntu镜像到本地并成功运行
		- 原始的Ubuntu镜像是不带着ifconfig命令的

		   

		- 外网连通的情况下，安装ifconfig命令并测试通过

		  docker容器内执行上述两条命令：apt-get updateapt-get install net-tools

		- 安装完成后，commit我们自己的新镜像

		  公式：docker commit -m="提交的描述信息" -a="作者" 容器ID 要创建的目标镜像名:[标签名]命令：在容器外执行，记得docker commit -m="ifconfig cmd add" -a="zzyy" a69d7c825c4f zzyyubuntu:1.2  

		- 启动我们的新镜像并和原来的对比

		  1 官网是默认下载的Ubuntu没有ifconfig命令2我们自己commit构建的新镜像，新增加了ifconfig功能，可以成功使用。 

	- curl验证私服库上有什么镜像

	   curl -XGET http://192.168.111.162:5000/v2/_catalog 可以看到，目前私服库没有任何镜像上传过。。。。。。 

	- 将新镜像zzyyubuntu:1.2修改符合私服规范的Tag

	   按照公式： docker   tag   镜像:Tag   Host:Port/Repository:Tag自己host主机IP地址，填写同学你们自己的，不要粘贴错误，O(∩_∩)O使用命令 docker tag 将zzyyubuntu:1.2 这个镜像修改为192.168.111.162:5000/zzyyubuntu:1.2 docker tag  zzyyubuntu:1.2  192.168.111.162:5000/zzyyubuntu:1.2 

	- 修改配置文件使之支持http

	    别无脑照着复制，registry-mirrors 配置的是国内阿里提供的镜像加速地址，不用加速的话访问官网的会很慢。2个配置中间有个逗号 ','别漏了，这个配置是json格式的。2个配置中间有个逗号 ','别漏了，这个配置是json格式的。2个配置中间有个逗号 ','别漏了，这个配置是json格式的。 vim命令新增如下红色内容：vim /etc/docker/daemon.json{  "registry-mirrors": ["https://aa25jngu.mirror.aliyuncs.com"],  "insecure-registries": ["192.168.111.162:5000"]} 上述理由：docker默认不允许http方式推送镜像，通过配置选项来取消这个限制。====> 修改完后如果不生效，建议重启docker 

	- push推送到私服库

	  docker push 192.168.111.162:5000/zzyyubuntu:1.2  

	- curl验证私服库上有什么镜像2

	   curl -XGET http://192.168.111.162:5000/v2/_catalog 

	- pull到本地并运行

	  docker pull 192.168.111.162:5000/zzyyubuntu:1.2docker run -it 镜像ID /bin/bash

### Docker容器数据卷

- 坑：容器卷记得加入

	- --privileged=true
	- why

	    Docker挂载主机目录访问如果出现cannot open directory .: Permission denied解决办法：在挂载目录后多加一个--privileged=true参数即可  如果是CentOS7安全模块会比之前系统版本加强，不安全的会先禁止，所以目录挂载的情况被默认为不安全的行为，在SELinux里面挂载目录被禁止掉了额，如果要开启，我们一般使用--privileged=true命令，扩大容器的权限解决挂载目录没有权限的问题，也即使用该参数，container内的root拥有真正的root权限，否则，container内的root只是外部的一个普通用户权限。

- 回顾下上一讲的知识点，参数V

   还记得蓝色框框中的内容吗？ 

- 是什么

  卷就是目录或文件，存在于一个或多个容器中，由docker挂载到容器，但不属于联合文件系统，因此能够绕过Union File System提供一些用于持续存储或共享数据的特性：卷的设计目的就是数据的持久化，完全独立于容器的生存周期，因此Docker不会在容器删除时删除其挂载的数据卷  

	- 一句话：有点类似我们Redis里面的rdb和aof文件
	- 将docker容器内的数据保存进宿主机的磁盘中
	- 运行一个带有容器卷存储功能的容器实例

		-  docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录      镜像名

- 能干嘛

  *  将运用与运行的环境打包镜像，run后形成容器实例运行 ，但是我们对数据的要求希望是持久化的 Docker容器产生的数据，如果不备份，那么当容器实例删除后，容器内的数据自然也就没有了。为了能保存数据在docker中我们使用卷。 特点：1：数据卷可在容器之间共享或重用数据2：卷中的更改可以直接实时生效，爽3：数据卷中的更改不会包含在镜像的更新中4：数据卷的生命周期一直持续到没有容器使用它为止 

- 数据卷案例

	- 宿主vs容器之间映射添加容器卷

		- 直接命令添加

			- 命令

			   公式：docker run -it -v /宿主机目录:/容器内目录 ubuntu /bin/bashdocker run -it --name myu3 --privileged=true -v /tmp/myHostData:/tmp/myDockerData ubuntu /bin/bash 

				-  docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录      镜像名

			- 查看数据卷是否挂载成功

			   docker inspect 容器ID  

			- 容器和宿主机之间数据共享

			  1  docker修改，主机同步获得 2 主机修改，docker同步获得3 docker容器stop，主机修改，docker容器重启看数据是否同步。

	- 读写规则映射添加说明

		- 读写(默认)

		    rw = read + write   

			-  docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录:rw      镜像名
			- 默认同上案例，默认就是rw

		- 只读

			- 容器实例内部被限制，只能读取不能写

			    /容器目录:ro 镜像名               就能完成功能，此时容器自己只能读取不能写   ro = read only 此时如果宿主机写入内容，可以同步给容器内，容器可以读取到。

			-  docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录:ro      镜像名

	- 卷的继承和共享

		- 容器1完成和宿主机的映射

		   docker run -it  --privileged=true -v /mydocker/u:/tmp --name u1 ubuntu 

		- 容器2继承容器1的卷规则

			- docker run -it  --privileged=true --volumes-from 父类  --name u2 ubuntu

### Docker常规安装简介

- 总体步骤

	- 搜索镜像
	- 拉取镜像
	- 查看镜像
	- 启动镜像

		- 服务端口映射

	- 停止容器
	- 移除容器

- 安装tomcat

	- docker hub上面查找tomcat镜像

		- docker search tomcat

	- 从docker hub上拉取tomcat镜像到本地

		- docker pull tomcat

	- docker images查看是否有拉取到的tomcat
	- 使用tomcat镜像创建容器实例(也叫运行镜像)

		- docker run -it -p 8080:8080 tomcat

			- -p 小写，主机端口:docker容器端口
			- -P 大写，随机分配端口
			- i:交互
			- t:终端
			- d:后台

	- 访问猫首页

		- 问题
		- 解决

			- 可能没有映射端口或者没有关闭防火墙
			- 把webapps.dist目录换成webapps

				- 先成功启动tomcat
				- 查看webapps 文件夹查看为空

	- 免修改版说明

		- docker pull billygoo/tomcat8-jdk8
		- docker run -d -p 8080:8080 --name mytomcat8 billygoo/tomcat8-jdk8

- 安装mysql

	- docker hub上面查找mysql镜像
	- 从docker hub上(阿里云加速器)拉取mysql镜像到本地标签为5.7

	   

	- 使用mysql5.7镜像创建容器(也叫运行镜像)

		- 命令出处，哪里来的？
		- 简单版

			- 使用mysql镜像

			  docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7docker psdocker exec -it 容器ID /bin/bashmysql -uroot -p  

			- 建库建表插入数据
			- 外部Win10也来连接运行在dokcer上的mysql容器实例服务

			   

			- 问题

				- 插入中文数据试试

				   

					- 为什么报错?

						- docker上默认字符集编码隐患

						    docker里面的mysql容器实例查看，内容如下： SHOW VARIABLES LIKE 'character%'

				- 删除容器后，里面的mysql数据如何办

					- 容器实例一删除，你还有什么？
删容器到跑路。。。。。？

		- 实战版

			- 新建mysql容器实例

			  docker run -d -p 3306:3306 --privileged=true -v /zzyyuse/mysql/log:/var/log/mysql -v /zzyyuse/mysql/data:/var/lib/mysql -v /zzyyuse/mysql/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=123456  --name mysql mysql:5.7

			- 新建my.cnf

				- 通过容器卷同步给mysql容器实例

				  [client]default_character_set=utf8[mysqld]collation_server = utf8_general_cicharacter_set_server = utf8 

			- 重新启动mysql容器实例再重新进入并查看字符编码

			   

			- 再新建库新建表再插入中文测试
			- 结论

			   之前的DB  无效 修改字符集操作+重启mysql容器实例 之后的DB  有效，需要新建 结论：docker安装完MySQL并run出容器后，建议请先修改完字符集编码后再新建mysql库-表-插数据 

			- 假如将当前容器实例删除，再重新来一次，之前建的db01实例还有吗？trytry

- 安装redis

	- 从docker hub上(阿里云加速器)拉取redis镜像到本地标签为6.0.8

	   

	- 入门命令
	- 命令提醒：容器卷记得加入--privileged=true

	  Docker挂载主机目录Docker访问出现cannot open directory .: Permission denied解决办法：在挂载目录后多加一个--privileged=true参数即可

	- 在CentOS宿主机下新建目录/app/redis

	    1 建目录  mkdir -p /app/redis

		- mkdir -p /app/redis

	- 将一个redis.conf文件模板拷贝进/app/redis目录下

	   2 拷贝配置文件  将准备好的redis.conf文件放进/app/redis目录下

	- /app/redis目录下修改redis.conf文件

	   3 /app/redis目录下修改redis.conf文件  3.1 开启redis验证    可选    requirepass 123   3.2 允许redis外地连接  必须     注释掉 # bind 127.0.0.1   3.3   daemonize no     将daemonize yes注释起来或者 daemonize no设置，因为该配置和docker run中-d参数冲突，会导致容器一直启动失败   3.4 开启redis数据持久化  appendonly yes  可选 

		- 默认出厂的原始redis.conf

		  # Redis configuration file example.## Note that in order to read the configuration file, Redis must be# started with the file path as first argument:## ./redis-server /path/to/redis.conf # Note on units: when memory size is needed, it is possible to specify# it in the usual form of 1k 5GB 4M and so forth:## 1k => 1000 bytes# 1kb => 1024 bytes# 1m => 1000000 bytes# 1mb => 1024*1024 bytes# 1g => 1000000000 bytes# 1gb => 1024*1024*1024 bytes## units are case insensitive so 1GB 1Gb 1gB are all the same. ################################## INCLUDES ################################### # Include one or more other config files here.  This is useful if you# have a standard template that goes to all Redis servers but also need# to customize a few per-server settings.  Include files can include# other files, so use this wisely.## Notice option "include" won't be rewritten by command "CONFIG REWRITE"# from admin or Redis Sentinel. Since Redis always uses the last processed# line as value of a configuration directive, you'd better put includes# at the beginning of this file to avoid overwriting config change at runtime.## If instead you are interested in using includes to override configuration# options, it is better to use include as the last line.## include /path/to/local.conf# include /path/to/other.conf ################################## MODULES ##################################### # Load modules at startup. If the server is not able to load modules# it will abort. It is possible to use multiple loadmodule directives.## loadmodule /path/to/my_module.so# loadmodule /path/to/other_module.so ################################## NETWORK ##################################### # By default, if no "bind" configuration directive is specified, Redis listens# for connections from all the network interfaces available on the server.# It is possible to listen to just one or multiple selected interfaces using# the "bind" configuration directive, followed by one or more IP addresses.## Examples:## bind 192.168.1.100 10.0.0.1# bind 127.0.0.1 ::1## ~~~ WARNING ~~~ If the computer running Redis is directly exposed to the# internet, binding to all the interfaces is dangerous and will expose the# instance to everybody on the internet. So by default we uncomment the# following bind directive, that will force Redis to listen only into# the IPv4 loopback interface address (this means Redis will be able to# accept connections only from clients running into the same computer it# is running).## IF YOU ARE SURE YOU WANT YOUR INSTANCE TO LISTEN TO ALL THE INTERFACES# JUST COMMENT THE FOLLOWING LINE.# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#bind 127.0.0.1 # Protected mode is a layer of security protection, in order to avoid that# Redis instances left open on the internet are accessed and exploited.## When protected mode is on and if:## 1) The server is not binding explicitly to a set of addresses using the#    "bind" directive.# 2) No password is configured.## The server only accepts connections from clients connecting from the# IPv4 and IPv6 loopback addresses 127.0.0.1 and ::1, and from Unix domain# sockets.## By default protected mode is enabled. You should disable it only if# you are sure you want clients from other hosts to connect to Redis# even if no authentication is configured, nor a specific set of interfaces# are explicitly listed using the "bind" directive.protected-mode no # Accept connections on the specified port, default is 6379 (IANA #815344).# If port 0 is specified Redis will not listen on a TCP socket.port 6379 # TCP listen() backlog.## In high requests-per-second environments you need an high backlog in order# to avoid slow clients connections issues. Note that the Linux kernel# will silently truncate it to the value of /proc/sys/net/core/somaxconn so# make sure to raise both the value of somaxconn and tcp_max_syn_backlog# in order to get the desired effect.tcp-backlog 511 # Unix socket.## Specify the path for the Unix socket that will be used to listen for# incoming connections. There is no default, so Redis will not listen# on a unix socket when not specified.## unixsocket /tmp/redis.sock# unixsocketperm 700 # Close the connection after a client is idle for N seconds (0 to disable)timeout 0 # TCP keepalive.## If non-zero, use SO_KEEPALIVE to send TCP ACKs to clients in absence# of communication. This is useful for two reasons:## 1) Detect dead peers.# 2) Take the connection alive from the point of view of network#    equipment in the middle.## On Linux, the specified value (in seconds) is the period used to send ACKs.# Note that to close the connection the double of the time is needed.# On other kernels the period depends on the kernel configuration.## A reasonable value for this option is 300 seconds, which is the new# Redis default starting with Redis 3.2.1.tcp-keepalive 300 ################################# GENERAL ##################################### # By default Redis does not run as a daemon. Use 'yes' if you need it.# Note that Redis will write a pid file in /var/run/redis.pid when daemonized.daemonize no # If you run Redis from upstart or systemd, Redis can interact with your# supervision tree. Options:#   supervised no      - no supervision interaction#   supervised upstart - signal upstart by putting Redis into SIGSTOP mode#   supervised systemd - signal systemd by writing READY=1 to $NOTIFY_SOCKET#   supervised auto    - detect upstart or systemd method based on#                        UPSTART_JOB or NOTIFY_SOCKET environment variables# Note: these supervision methods only signal "process is ready."#       They do not enable continuous liveness pings back to your supervisor.supervised no # If a pid file is specified, Redis writes it where specified at startup# and removes it at exit.## When the server runs non daemonized, no pid file is created if none is# specified in the configuration. When the server is daemonized, the pid file# is used even if not specified, defaulting to "/var/run/redis.pid".## Creating a pid file is best effort: if Redis is not able to create it# nothing bad happens, the server will start and run normally.pidfile /var/run/redis_6379.pid # Specify the server verbosity level.# This can be one of:# debug (a lot of information, useful for development/testing)# verbose (many rarely useful info, but not a mess like the debug level)# notice (moderately verbose, what you want in production probably)# warning (only very important / critical messages are logged)loglevel notice # Specify the log file name. Also the empty string can be used to force# Redis to log on the standard output. Note that if you use standard# output for logging but daemonize, logs will be sent to /dev/nulllogfile "" # To enable logging to the system logger, just set 'syslog-enabled' to yes,# and optionally update the other syslog parameters to suit your needs.# syslog-enabled no # Specify the syslog identity.# syslog-ident redis # Specify the syslog facility. Must be USER or between LOCAL0-LOCAL7.# syslog-facility local0 # Set the number of databases. The default database is DB 0, you can select# a different one on a per-connection basis using SELECT <dbid> where# dbid is a number between 0 and 'databases'-1databases 16 # By default Redis shows an ASCII art logo only when started to log to the# standard output and if the standard output is a TTY. Basically this means# that normally a logo is displayed only in interactive sessions.## However it is possible to force the pre-4.0 behavior and always show a# ASCII art logo in startup logs by setting the following option to yes.always-show-logo yes ################################ SNAPSHOTTING  ################################## Save the DB on disk:##   save <seconds> <changes>##   Will save the DB if both the given number of seconds and the given#   number of write operations against the DB occurred.##   In the example below the behaviour will be to save:#   after 900 sec (15 min) if at least 1 key changed#   after 300 sec (5 min) if at least 10 keys changed#   after 60 sec if at least 10000 keys changed##   Note: you can disable saving completely by commenting out all "save" lines.##   It is also possible to remove all the previously configured save#   points by adding a save directive with a single empty string argument#   like in the following example:##   save "" save 900 1save 300 10save 60 10000 # By default Redis will stop accepting writes if RDB snapshots are enabled# (at least one save point) and the latest background save failed.# This will make the user aware (in a hard way) that data is not persisting# on disk properly, otherwise chances are that no one will notice and some# disaster will happen.## If the background saving process will start working again Redis will# automatically allow writes again.## However if you have setup your proper monitoring of the Redis server# and persistence, you may want to disable this feature so that Redis will# continue to work as usual even if there are problems with disk,# permissions, and so forth.stop-writes-on-bgsave-error yes # Compress string objects using LZF when dump .rdb databases?# For default that's set to 'yes' as it's almost always a win.# If you want to save some CPU in the saving child set it to 'no' but# the dataset will likely be bigger if you have compressible values or keys.rdbcompression yes # Since version 5 of RDB a CRC64 checksum is placed at the end of the file.# This makes the format more resistant to corruption but there is a performance# hit to pay (around 10%) when saving and loading RDB files, so you can disable it# for maximum performances.## RDB files created with checksum disabled have a checksum of zero that will# tell the loading code to skip the check.rdbchecksum yes # The filename where to dump the DBdbfilename dump.rdb # The working directory.## The DB will be written inside this directory, with the filename specified# above using the 'dbfilename' configuration directive.## The Append Only File will also be created inside this directory.## Note that you must specify a directory here, not a file name.dir ./ ################################# REPLICATION ################################# # Master-Replica replication. Use replicaof to make a Redis instance a copy of# another Redis server. A few things to understand ASAP about Redis replication.##   +------------------+      +---------------+#   |      Master      | ---> |    Replica    |#   | (receive writes) |      |  (exact copy) |#   +------------------+      +---------------+## 1) Redis replication is asynchronous, but you can configure a master to#    stop accepting writes if it appears to be not connected with at least#    a given number of replicas.# 2) Redis replicas are able to perform a partial resynchronization with the#    master if the replication link is lost for a relatively small amount of#    time. You may want to configure the replication backlog size (see the next#    sections of this file) with a sensible value depending on your needs.# 3) Replication is automatic and does not need user intervention. After a#    network partition replicas automatically try to reconnect to masters#    and resynchronize with them.## replicaof <masterip> <masterport> # If the master is password protected (using the "requirepass" configuration# directive below) it is possible to tell the replica to authenticate before# starting the replication synchronization process, otherwise the master will# refuse the replica request.## masterauth <master-password> # When a replica loses its connection with the master, or when the replication# is still in progress, the replica can act in two different ways:## 1) if replica-serve-stale-data is set to 'yes' (the default) the replica will#    still reply to client requests, possibly with out of date data, or the#    data set may just be empty if this is the first synchronization.## 2) if replica-serve-stale-data is set to 'no' the replica will reply with#    an error "SYNC with master in progress" to all the kind of commands#    but to INFO, replicaOF, AUTH, PING, SHUTDOWN, REPLCONF, ROLE, CONFIG,#    SUBSCRIBE, UNSUBSCRIBE, PSUBSCRIBE, PUNSUBSCRIBE, PUBLISH, PUBSUB,#    COMMAND, POST, HOST: and LATENCY.#replica-serve-stale-data yes # You can configure a replica instance to accept writes or not. Writing against# a replica instance may be useful to store some ephemeral data (because data# written on a replica will be easily deleted after resync with the master) but# may also cause problems if clients are writing to it because of a# misconfiguration.## Since Redis 2.6 by default replicas are read-only.## Note: read only replicas are not designed to be exposed to untrusted clients# on the internet. It's just a protection layer against misuse of the instance.# Still a read only replica exports by default all the administrative commands# such as CONFIG, DEBUG, and so forth. To a limited extent you can improve# security of read only replicas using 'rename-command' to shadow all the# administrative / dangerous commands.replica-read-only yes # Replication SYNC strategy: disk or socket.## -------------------------------------------------------# WARNING: DISKLESS REPLICATION IS EXPERIMENTAL CURRENTLY# -------------------------------------------------------## New replicas and reconnecting replicas that are not able to continue the replication# process just receiving differences, need to do what is called a "full# synchronization". An RDB file is transmitted from the master to the replicas.# The transmission can happen in two different ways:## 1) Disk-backed: The Redis master creates a new process that writes the RDB#                 file on disk. Later the file is transferred by the parent#                 process to the replicas incrementally.# 2) Diskless: The Redis master creates a new process that directly writes the#              RDB file to replica sockets, without touching the disk at all.## With disk-backed replication, while the RDB file is generated, more replicas# can be queued and served with the RDB file as soon as the current child producing# the RDB file finishes its work. With diskless replication instead once# the transfer starts, new replicas arriving will be queued and a new transfer# will start when the current one terminates.## When diskless replication is used, the master waits a configurable amount of# time (in seconds) before starting the transfer in the hope that multiple replicas# will arrive and the transfer can be parallelized.## With slow disks and fast (large bandwidth) networks, diskless replication# works better.repl-diskless-sync no # When diskless replication is enabled, it is possible to configure the delay# the server waits in order to spawn the child that transfers the RDB via socket# to the replicas.## This is important since once the transfer starts, it is not possible to serve# new replicas arriving, that will be queued for the next RDB transfer, so the server# waits a delay in order to let more replicas arrive.## The delay is specified in seconds, and by default is 5 seconds. To disable# it entirely just set it to 0 seconds and the transfer will start ASAP.repl-diskless-sync-delay 5 # Replicas send PINGs to server in a predefined interval. It's possible to change# this interval with the repl_ping_replica_period option. The default value is 10# seconds.## repl-ping-replica-period 10 # The following option sets the replication timeout for:## 1) Bulk transfer I/O during SYNC, from the point of view of replica.# 2) Master timeout from the point of view of replicas (data, pings).# 3) Replica timeout from the point of view of masters (REPLCONF ACK pings).## It is important to make sure that this value is greater than the value# specified for repl-ping-replica-period otherwise a timeout will be detected# every time there is low traffic between the master and the replica.## repl-timeout 60 # Disable TCP_NODELAY on the replica socket after SYNC?## If you select "yes" Redis will use a smaller number of TCP packets and# less bandwidth to send data to replicas. But this can add a delay for# the data to appear on the replica side, up to 40 milliseconds with# Linux kernels using a default configuration.## If you select "no" the delay for data to appear on the replica side will# be reduced but more bandwidth will be used for replication.## By default we optimize for low latency, but in very high traffic conditions# or when the master and replicas are many hops away, turning this to "yes" may# be a good idea.repl-disable-tcp-nodelay no # Set the replication backlog size. The backlog is a buffer that accumulates# replica data when replicas are disconnected for some time, so that when a replica# wants to reconnect again, often a full resync is not needed, but a partial# resync is enough, just passing the portion of data the replica missed while# disconnected.## The bigger the replication backlog, the longer the time the replica can be# disconnected and later be able to perform a partial resynchronization.## The backlog is only allocated once there is at least a replica connected.## repl-backlog-size 1mb # After a master has no longer connected replicas for some time, the backlog# will be freed. The following option configures the amount of seconds that# need to elapse, starting from the time the last replica disconnected, for# the backlog buffer to be freed.## Note that replicas never free the backlog for timeout, since they may be# promoted to masters later, and should be able to correctly "partially# resynchronize" with the replicas: hence they should always accumulate backlog.## A value of 0 means to never release the backlog.## repl-backlog-ttl 3600 # The replica priority is an integer number published by Redis in the INFO output.# It is used by Redis Sentinel in order to select a replica to promote into a# master if the master is no longer working correctly.## A replica with a low priority number is considered better for promotion, so# for instance if there are three replicas with priority 10, 100, 25 Sentinel will# pick the one with priority 10, that is the lowest.## However a special priority of 0 marks the replica as not able to perform the# role of master, so a replica with priority of 0 will never be selected by# Redis Sentinel for promotion.## By default the priority is 100.replica-priority 100 # It is possible for a master to stop accepting writes if there are less than# N replicas connected, having a lag less or equal than M seconds.## The N replicas need to be in "online" state.## The lag in seconds, that must be <= the specified value, is calculated from# the last ping received from the replica, that is usually sent every second.## This option does not GUARANTEE that N replicas will accept the write, but# will limit the window of exposure for lost writes in case not enough replicas# are available, to the specified number of seconds.## For example to require at least 3 replicas with a lag <= 10 seconds use:## min-replicas-to-write 3# min-replicas-max-lag 10## Setting one or the other to 0 disables the feature.## By default min-replicas-to-write is set to 0 (feature disabled) and# min-replicas-max-lag is set to 10. # A Redis master is able to list the address and port of the attached# replicas in different ways. For example the "INFO replication" section# offers this information, which is used, among other tools, by# Redis Sentinel in order to discover replica instances.# Another place where this info is available is in the output of the# "ROLE" command of a master.## The listed IP and address normally reported by a replica is obtained# in the following way:##   IP: The address is auto detected by checking the peer address#   of the socket used by the replica to connect with the master.##   Port: The port is communicated by the replica during the replication#   handshake, and is normally the port that the replica is using to#   listen for connections.## However when port forwarding or Network Address Translation (NAT) is# used, the replica may be actually reachable via different IP and port# pairs. The following two options can be used by a replica in order to# report to its master a specific set of IP and port, so that both INFO# and ROLE will report those values.## There is no need to use both the options if you need to override just# the port or the IP address.## replica-announce-ip 5.5.5.5# replica-announce-port 1234 ################################## SECURITY ################################### # Require clients to issue AUTH <PASSWORD> before processing any other# commands.  This might be useful in environments in which you do not trust# others with access to the host running redis-server.## This should stay commented out for backward compatibility and because most# people do not need auth (e.g. they run their own servers).## Warning: since Redis is pretty fast an outside user can try up to# 150k passwords per second against a good box. This means that you should# use a very strong password otherwise it will be very easy to break.## requirepass foobared # Command renaming.## It is possible to change the name of dangerous commands in a shared# environment. For instance the CONFIG command may be renamed into something# hard to guess so that it will still be available for internal-use tools# but not available for general clients.## Example:## rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52## It is also possible to completely kill a command by renaming it into# an empty string:## rename-command CONFIG ""## Please note that changing the name of commands that are logged into the# AOF file or transmitted to replicas may cause problems. ################################### CLIENTS #################################### # Set the max number of connected clients at the same time. By default# this limit is set to 10000 clients, however if the Redis server is not# able to configure the process file limit to allow for the specified limit# the max number of allowed clients is set to the current file limit# minus 32 (as Redis reserves a few file descriptors for internal uses).## Once the limit is reached Redis will close all the new connections sending# an error 'max number of clients reached'.## maxclients 10000 ############################## MEMORY MANAGEMENT ################################ # Set a memory usage limit to the specified amount of bytes.# When the memory limit is reached Redis will try to remove keys# according to the eviction policy selected (see maxmemory-policy).## If Redis can't remove keys according to the policy, or if the policy is# set to 'noeviction', Redis will start to reply with errors to commands# that would use more memory, like SET, LPUSH, and so on, and will continue# to reply to read-only commands like GET.## This option is usually useful when using Redis as an LRU or LFU cache, or to# set a hard memory limit for an instance (using the 'noeviction' policy).## WARNING: If you have replicas attached to an instance with maxmemory on,# the size of the output buffers needed to feed the replicas are subtracted# from the used memory count, so that network problems / resyncs will# not trigger a loop where keys are evicted, and in turn the output# buffer of replicas is full with DELs of keys evicted triggering the deletion# of more keys, and so forth until the database is completely emptied.## In short... if you have replicas attached it is suggested that you set a lower# limit for maxmemory so that there is some free RAM on the system for replica# output buffers (but this is not needed if the policy is 'noeviction').## maxmemory <bytes> # MAXMEMORY POLICY: how Redis will select what to remove when maxmemory# is reached. You can select among five behaviors:## volatile-lru -> Evict using approximated LRU among the keys with an expire set.# allkeys-lru -> Evict any key using approximated LRU.# volatile-lfu -> Evict using approximated LFU among the keys with an expire set.# allkeys-lfu -> Evict any key using approximated LFU.# volatile-random -> Remove a random key among the ones with an expire set.# allkeys-random -> Remove a random key, any key.# volatile-ttl -> Remove the key with the nearest expire time (minor TTL)# noeviction -> Don't evict anything, just return an error on write operations.## LRU means Least Recently Used# LFU means Least Frequently Used## Both LRU, LFU and volatile-ttl are implemented using approximated# randomized algorithms.## Note: with any of the above policies, Redis will return an error on write#       operations, when there are no suitable keys for eviction.##       At the date of writing these commands are: set setnx setex append#       incr decr rpush lpush rpushx lpushx linsert lset rpoplpush sadd#       sinter sinterstore sunion sunionstore sdiff sdiffstore zadd zincrby#       zunionstore zinterstore hset hsetnx hmset hincrby incrby decrby#       getset mset msetnx exec sort## The default is:## maxmemory-policy noeviction # LRU, LFU and minimal TTL algorithms are not precise algorithms but approximated# algorithms (in order to save memory), so you can tune it for speed or# accuracy. For default Redis will check five keys and pick the one that was# used less recently, you can change the sample size using the following# configuration directive.## The default of 5 produces good enough results. 10 Approximates very closely# true LRU but costs more CPU. 3 is faster but not very accurate.## maxmemory-samples 5 # Starting from Redis 5, by default a replica will ignore its maxmemory setting# (unless it is promoted to master after a failover or manually). It means# that the eviction of keys will be just handled by the master, sending the# DEL commands to the replica as keys evict in the master side.## This behavior ensures that masters and replicas stay consistent, and is usually# what you want, however if your replica is writable, or you want the replica to have# a different memory setting, and you are sure all the writes performed to the# replica are idempotent, then you may change this default (but be sure to understand# what you are doing).## Note that since the replica by default does not evict, it may end using more# memory than the one set via maxmemory (there are certain buffers that may# be larger on the replica, or data structures may sometimes take more memory and so# forth). So make sure you monitor your replicas and make sure they have enough# memory to never hit a real out-of-memory condition before the master hits# the configured maxmemory setting.## replica-ignore-maxmemory yes ############################# LAZY FREEING #################################### # Redis has two primitives to delete keys. One is called DEL and is a blocking# deletion of the object. It means that the server stops processing new commands# in order to reclaim all the memory associated with an object in a synchronous# way. If the key deleted is associated with a small object, the time needed# in order to execute the DEL command is very small and comparable to most other# O(1) or O(log_N) commands in Redis. However if the key is associated with an# aggregated value containing millions of elements, the server can block for# a long time (even seconds) in order to complete the operation.## For the above reasons Redis also offers non blocking deletion primitives# such as UNLINK (non blocking DEL) and the ASYNC option of FLUSHALL and# FLUSHDB commands, in order to reclaim memory in background. Those commands# are executed in constant time. Another thread will incrementally free the# object in the background as fast as possible.## DEL, UNLINK and ASYNC option of FLUSHALL and FLUSHDB are user-controlled.# It's up to the design of the application to understand when it is a good# idea to use one or the other. However the Redis server sometimes has to# delete keys or flush the whole database as a side effect of other operations.# Specifically Redis deletes objects independently of a user call in the# following scenarios:## 1) On eviction, because of the maxmemory and maxmemory policy configurations,#    in order to make room for new data, without going over the specified#    memory limit.# 2) Because of expire: when a key with an associated time to live (see the#    EXPIRE command) must be deleted from memory.# 3) Because of a side effect of a command that stores data on a key that may#    already exist. For example the RENAME command may delete the old key#    content when it is replaced with another one. Similarly SUNIONSTORE#    or SORT with STORE option may delete existing keys. The SET command#    itself removes any old content of the specified key in order to replace#    it with the specified string.# 4) During replication, when a replica performs a full resynchronization with#    its master, the content of the whole database is removed in order to#    load the RDB file just transferred.## In all the above cases the default is to delete objects in a blocking way,# like if DEL was called. However you can configure each case specifically# in order to instead release memory in a non-blocking way like if UNLINK# was called, using the following configuration directives: lazyfree-lazy-eviction nolazyfree-lazy-expire nolazyfree-lazy-server-del noreplica-lazy-flush no ############################## APPEND ONLY MODE ############################### # By default Redis asynchronously dumps the dataset on disk. This mode is# good enough in many applications, but an issue with the Redis process or# a power outage may result into a few minutes of writes lost (depending on# the configured save points).## The Append Only File is an alternative persistence mode that provides# much better durability. For instance using the default data fsync policy# (see later in the config file) Redis can lose just one second of writes in a# dramatic event like a server power outage, or a single write if something# wrong with the Redis process itself happens, but the operating system is# still running correctly.## AOF and RDB persistence can be enabled at the same time without problems.# If the AOF is enabled on startup Redis will load the AOF, that is the file# with the better durability guarantees.## Please check http://redis.io/topics/persistence for more information. appendonly no # The name of the append only file (default: "appendonly.aof") appendfilename "appendonly.aof" # The fsync() call tells the Operating System to actually write data on disk# instead of waiting for more data in the output buffer. Some OS will really flush# data on disk, some other OS will just try to do it ASAP.## Redis supports three different modes:## no: don't fsync, just let the OS flush the data when it wants. Faster.# always: fsync after every write to the append only log. Slow, Safest.# everysec: fsync only one time every second. Compromise.## The default is "everysec", as that's usually the right compromise between# speed and data safety. It's up to you to understand if you can relax this to# "no" that will let the operating system flush the output buffer when# it wants, for better performances (but if you can live with the idea of# some data loss consider the default persistence mode that's snapshotting),# or on the contrary, use "always" that's very slow but a bit safer than# everysec.## More details please check the following article:# http://antirez.com/post/redis-persistence-demystified.html## If unsure, use "everysec". # appendfsync alwaysappendfsync everysec# appendfsync no # When the AOF fsync policy is set to always or everysec, and a background# saving process (a background save or AOF log background rewriting) is# performing a lot of I/O against the disk, in some Linux configurations# Redis may block too long on the fsync() call. Note that there is no fix for# this currently, as even performing fsync in a different thread will block# our synchronous write(2) call.## In order to mitigate this problem it's possible to use the following option# that will prevent fsync() from being called in the main process while a# BGSAVE or BGREWRITEAOF is in progress.## This means that while another child is saving, the durability of Redis is# the same as "appendfsync none". In practical terms, this means that it is# possible to lose up to 30 seconds of log in the worst scenario (with the# default Linux settings).## If you have latency problems turn this to "yes". Otherwise leave it as# "no" that is the safest pick from the point of view of durability. no-appendfsync-on-rewrite no # Automatic rewrite of the append only file.# Redis is able to automatically rewrite the log file implicitly calling# BGREWRITEAOF when the AOF log size grows by the specified percentage.## This is how it works: Redis remembers the size of the AOF file after the# latest rewrite (if no rewrite has happened since the restart, the size of# the AOF at startup is used).## This base size is compared to the current size. If the current size is# bigger than the specified percentage, the rewrite is triggered. Also# you need to specify a minimal size for the AOF file to be rewritten, this# is useful to avoid rewriting the AOF file even if the percentage increase# is reached but it is still pretty small.## Specify a percentage of zero in order to disable the automatic AOF# rewrite feature. auto-aof-rewrite-percentage 100auto-aof-rewrite-min-size 64mb # An AOF file may be found to be truncated at the end during the Redis# startup process, when the AOF data gets loaded back into memory.# This may happen when the system where Redis is running# crashes, especially when an ext4 filesystem is mounted without the# data=ordered option (however this can't happen when Redis itself# crashes or aborts but the operating system still works correctly).## Redis can either exit with an error when this happens, or load as much# data as possible (the default now) and start if the AOF file is found# to be truncated at the end. The following option controls this behavior.## If aof-load-truncated is set to yes, a truncated AOF file is loaded and# the Redis server starts emitting a log to inform the user of the event.# Otherwise if the option is set to no, the server aborts with an error# and refuses to start. When the option is set to no, the user requires# to fix the AOF file using the "redis-check-aof" utility before to restart# the server.## Note that if the AOF file will be found to be corrupted in the middle# the server will still exit with an error. This option only applies when# Redis will try to read more data from the AOF file but not enough bytes# will be found.aof-load-truncated yes # When rewriting the AOF file, Redis is able to use an RDB preamble in the# AOF file for faster rewrites and recoveries. When this option is turned# on the rewritten AOF file is composed of two different stanzas:##   [RDB file][AOF tail]## When loading Redis recognizes that the AOF file starts with the "REDIS"# string and loads the prefixed RDB file, and continues loading the AOF# tail.aof-use-rdb-preamble yes ################################ LUA SCRIPTING  ############################### # Max execution time of a Lua script in milliseconds.## If the maximum execution time is reached Redis will log that a script is# still in execution after the maximum allowed time and will start to# reply to queries with an error.## When a long running script exceeds the maximum execution time only the# SCRIPT KILL and SHUTDOWN NOSAVE commands are available. The first can be# used to stop a script that did not yet called write commands. The second# is the only way to shut down the server in the case a write command was# already issued by the script but the user doesn't want to wait for the natural# termination of the script.## Set it to 0 or a negative value for unlimited execution without warnings.lua-time-limit 5000 ################################ REDIS CLUSTER  ############################### # Normal Redis instances can't be part of a Redis Cluster; only nodes that are# started as cluster nodes can. In order to start a Redis instance as a# cluster node enable the cluster support uncommenting the following:## cluster-enabled yes # Every cluster node has a cluster configuration file. This file is not# intended to be edited by hand. It is created and updated by Redis nodes.# Every Redis Cluster node requires a different cluster configuration file.# Make sure that instances running in the same system do not have# overlapping cluster configuration file names.## cluster-config-file nodes-6379.conf # Cluster node timeout is the amount of milliseconds a node must be unreachable# for it to be considered in failure state.# Most other internal time limits are multiple of the node timeout.## cluster-node-timeout 15000 # A replica of a failing master will avoid to start a failover if its data# looks too old.## There is no simple way for a replica to actually have an exact measure of# its "data age", so the following two checks are performed:## 1) If there are multiple replicas able to failover, they exchange messages#    in order to try to give an advantage to the replica with the best#    replication offset (more data from the master processed).#    Replicas will try to get their rank by offset, and apply to the start#    of the failover a delay proportional to their rank.## 2) Every single replica computes the time of the last interaction with#    its master. This can be the last ping or command received (if the master#    is still in the "connected" state), or the time that elapsed since the#    disconnection with the master (if the replication link is currently down).#    If the last interaction is too old, the replica will not try to failover#    at all.## The point "2" can be tuned by user. Specifically a replica will not perform# the failover if, since the last interaction with the master, the time# elapsed is greater than:##   (node-timeout * replica-validity-factor) + repl-ping-replica-period## So for example if node-timeout is 30 seconds, and the replica-validity-factor# is 10, and assuming a default repl-ping-replica-period of 10 seconds, the# replica will not try to failover if it was not able to talk with the master# for longer than 310 seconds.## A large replica-validity-factor may allow replicas with too old data to failover# a master, while a too small value may prevent the cluster from being able to# elect a replica at all.## For maximum availability, it is possible to set the replica-validity-factor# to a value of 0, which means, that replicas will always try to failover the# master regardless of the last time they interacted with the master.# (However they'll always try to apply a delay proportional to their# offset rank).## Zero is the only value able to guarantee that when all the partitions heal# the cluster will always be able to continue.## cluster-replica-validity-factor 10 # Cluster replicas are able to migrate to orphaned masters, that are masters# that are left without working replicas. This improves the cluster ability# to resist to failures as otherwise an orphaned master can't be failed over# in case of failure if it has no working replicas.## Replicas migrate to orphaned masters only if there are still at least a# given number of other working replicas for their old master. This number# is the "migration barrier". A migration barrier of 1 means that a replica# will migrate only if there is at least 1 other working replica for its master# and so forth. It usually reflects the number of replicas you want for every# master in your cluster.## Default is 1 (replicas migrate only if their masters remain with at least# one replica). To disable migration just set it to a very large value.# A value of 0 can be set but is useful only for debugging and dangerous# in production.## cluster-migration-barrier 1 # By default Redis Cluster nodes stop accepting queries if they detect there# is at least an hash slot uncovered (no available node is serving it).# This way if the cluster is partially down (for example a range of hash slots# are no longer covered) all the cluster becomes, eventually, unavailable.# It automatically returns available as soon as all the slots are covered again.## However sometimes you want the subset of the cluster which is working,# to continue to accept queries for the part of the key space that is still# covered. In order to do so, just set the cluster-require-full-coverage# option to no.## cluster-require-full-coverage yes # This option, when set to yes, prevents replicas from trying to failover its# master during master failures. However the master can still perform a# manual failover, if forced to do so.## This is useful in different scenarios, especially in the case of multiple# data center operations, where we want one side to never be promoted if not# in the case of a total DC failure.## cluster-replica-no-failover no # In order to setup your cluster make sure to read the documentation# available at http://redis.io web site. ########################## CLUSTER DOCKER/NAT support  ######################## # In certain deployments, Redis Cluster nodes address discovery fails, because# addresses are NAT-ted or because ports are forwarded (the typical case is# Docker and other containers).## In order to make Redis Cluster working in such environments, a static# configuration where each node knows its public address is needed. The# following two options are used for this scope, and are:## * cluster-announce-ip# * cluster-announce-port# * cluster-announce-bus-port## Each instruct the node about its address, client port, and cluster message# bus port. The information is then published in the header of the bus packets# so that other nodes will be able to correctly map the address of the node# publishing the information.## If the above options are not used, the normal Redis Cluster auto-detection# will be used instead.## Note that when remapped, the bus port may not be at the fixed offset of# clients port + 10000, so you can specify any port and bus-port depending# on how they get remapped. If the bus-port is not set, a fixed offset of# 10000 will be used as usually.## Example:## cluster-announce-ip 10.1.1.5# cluster-announce-port 6379# cluster-announce-bus-port 6380 ################################## SLOW LOG ################################### # The Redis Slow Log is a system to log queries that exceeded a specified# execution time. The execution time does not include the I/O operations# like talking with the client, sending the reply and so forth,# but just the time needed to actually execute the command (this is the only# stage of command execution where the thread is blocked and can not serve# other requests in the meantime).## You can configure the slow log with two parameters: one tells Redis# what is the execution time, in microseconds, to exceed in order for the# command to get logged, and the other parameter is the length of the# slow log. When a new command is logged the oldest one is removed from the# queue of logged commands. # The following time is expressed in microseconds, so 1000000 is equivalent# to one second. Note that a negative number disables the slow log, while# a value of zero forces the logging of every command.slowlog-log-slower-than 10000 # There is no limit to this length. Just be aware that it will consume memory.# You can reclaim memory used by the slow log with SLOWLOG RESET.slowlog-max-len 128 ################################ LATENCY MONITOR ############################## # The Redis latency monitoring subsystem samples different operations# at runtime in order to collect data related to possible sources of# latency of a Redis instance.## Via the LATENCY command this information is available to the user that can# print graphs and obtain reports.## The system only logs operations that were performed in a time equal or# greater than the amount of milliseconds specified via the# latency-monitor-threshold configuration directive. When its value is set# to zero, the latency monitor is turned off.## By default latency monitoring is disabled since it is mostly not needed# if you don't have latency issues, and collecting data has a performance# impact, that while very small, can be measured under big load. Latency# monitoring can easily be enabled at runtime using the command# "CONFIG SET latency-monitor-threshold <milliseconds>" if needed.latency-monitor-threshold 0 ############################# EVENT NOTIFICATION ############################## # Redis can notify Pub/Sub clients about events happening in the key space.# This feature is documented at http://redis.io/topics/notifications## For instance if keyspace events notification is enabled, and a client# performs a DEL operation on key "foo" stored in the Database 0, two# messages will be published via Pub/Sub:## PUBLISH __keyspace@0__:foo del# PUBLISH __keyevent@0__:del foo## It is possible to select the events that Redis will notify among a set# of classes. Every class is identified by a single character:##  K     Keyspace events, published with __keyspace@<db>__ prefix.#  E     Keyevent events, published with __keyevent@<db>__ prefix.#  g     Generic commands (non-type specific) like DEL, EXPIRE, RENAME, ...#  $     String commands#  l     List commands#  s     Set commands#  h     Hash commands#  z     Sorted set commands#  x     Expired events (events generated every time a key expires)#  e     Evicted events (events generated when a key is evicted for maxmemory)#  A     Alias for g$lshzxe, so that the "AKE" string means all the events.##  The "notify-keyspace-events" takes as argument a string that is composed#  of zero or multiple characters. The empty string means that notifications#  are disabled.##  Example: to enable list and generic events, from the point of view of the#           event name, use:##  notify-keyspace-events Elg##  Example 2: to get the stream of the expired keys subscribing to channel#             name __keyevent@0__:expired use:#  notify-keyspace-events Ex##  By default all notifications are disabled because most users don't need#  this feature and the feature has some overhead. Note that if you don't#  specify at least one of K or E, no events will be delivered.#notify-keyspace-events "" ############################### ADVANCED CONFIG ############################### # Hashes are encoded using a memory efficient data structure when they have a# small number of entries, and the biggest entry does not exceed a given# threshold. These thresholds can be configured using the following directives.hash-max-ziplist-entries 512hash-max-ziplist-value 64 # Lists are also encoded in a special way to save a lot of space.# The number of entries allowed per internal list node can be specified# as a fixed maximum size or a maximum number of elements.# For a fixed maximum size, use -5 through -1, meaning:# -5: max size: 64 Kb  <-- not recommended for normal workloads# -4: max size: 32 Kb  <-- not recommended# -3: max size: 16 Kb  <-- probably not recommended# -2: max size: 8 Kb   <-- good# -1: max size: 4 Kb   <-- good# Positive numbers mean store up to _exactly_ that number of elements# per list node.# The highest performing option is usually -2 (8 Kb size) or -1 (4 Kb size),# but if your use case is unique, adjust the settings as necessary.list-max-ziplist-size -2 # Lists may also be compressed.# Compress depth is the number of quicklist ziplist nodes from *each* side of# the list to *exclude* from compression.  The head and tail of the list# are always uncompressed for fast push/pop operations.  Settings are:# 0: disable all list compression# 1: depth 1 means "don't start compressing until after 1 node into the list,#    going from either the head or tail"#    So: [head]->node->node->...->node->[tail]#    [head], [tail] will always be uncompressed; inner nodes will compress.# 2: [head]->[next]->node->node->...->node->[prev]->[tail]#    2 here means: don't compress head or head->next or tail->prev or tail,#    but compress all nodes between them.# 3: [head]->[next]->[next]->node->node->...->node->[prev]->[prev]->[tail]# etc.list-compress-depth 0 # Sets have a special encoding in just one case: when a set is composed# of just strings that happen to be integers in radix 10 in the range# of 64 bit signed integers.# The following configuration setting sets the limit in the size of the# set in order to use this special memory saving encoding.set-max-intset-entries 512 # Similarly to hashes and lists, sorted sets are also specially encoded in# order to save a lot of space. This encoding is only used when the length and# elements of a sorted set are below the following limits:zset-max-ziplist-entries 128zset-max-ziplist-value 64 # HyperLogLog sparse representation bytes limit. The limit includes the# 16 bytes header. When an HyperLogLog using the sparse representation crosses# this limit, it is converted into the dense representation.## A value greater than 16000 is totally useless, since at that point the# dense representation is more memory efficient.## The suggested value is ~ 3000 in order to have the benefits of# the space efficient encoding without slowing down too much PFADD,# which is O(N) with the sparse encoding. The value can be raised to# ~ 10000 when CPU is not a concern, but space is, and the data set is# composed of many HyperLogLogs with cardinality in the 0 - 15000 range.hll-sparse-max-bytes 3000 # Streams macro node max size / items. The stream data structure is a radix# tree of big nodes that encode multiple items inside. Using this configuration# it is possible to configure how big a single node can be in bytes, and the# maximum number of items it may contain before switching to a new node when# appending new stream entries. If any of the following settings are set to# zero, the limit is ignored, so for instance it is possible to set just a# max entires limit by setting max-bytes to 0 and max-entries to the desired# value.stream-node-max-bytes 4096stream-node-max-entries 100 # Active rehashing uses 1 millisecond every 100 milliseconds of CPU time in# order to help rehashing the main Redis hash table (the one mapping top-level# keys to values). The hash table implementation Redis uses (see dict.c)# performs a lazy rehashing: the more operation you run into a hash table# that is rehashing, the more rehashing "steps" are performed, so if the# server is idle the rehashing is never complete and some more memory is used# by the hash table.## The default is to use this millisecond 10 times every second in order to# actively rehash the main dictionaries, freeing memory when possible.## If unsure:# use "activerehashing no" if you have hard latency requirements and it is# not a good thing in your environment that Redis can reply from time to time# to queries with 2 milliseconds delay.## use "activerehashing yes" if you don't have such hard requirements but# want to free memory asap when possible.activerehashing yes # The client output buffer limits can be used to force disconnection of clients# that are not reading data from the server fast enough for some reason (a# common reason is that a Pub/Sub client can't consume messages as fast as the# publisher can produce them).## The limit can be set differently for the three different classes of clients:## normal -> normal clients including MONITOR clients# replica  -> replica clients# pubsub -> clients subscribed to at least one pubsub channel or pattern## The syntax of every client-output-buffer-limit directive is the following:## client-output-buffer-limit <class> <hard limit> <soft limit> <soft seconds>## A client is immediately disconnected once the hard limit is reached, or if# the soft limit is reached and remains reached for the specified number of# seconds (continuously).# So for instance if the hard limit is 32 megabytes and the soft limit is# 16 megabytes / 10 seconds, the client will get disconnected immediately# if the size of the output buffers reach 32 megabytes, but will also get# disconnected if the client reaches 16 megabytes and continuously overcomes# the limit for 10 seconds.## By default normal clients are not limited because they don't receive data# without asking (in a push way), but just after a request, so only# asynchronous clients may create a scenario where data is requested faster# than it can read.## Instead there is a default limit for pubsub and replica clients, since# subscribers and replicas receive data in a push fashion.## Both the hard or the soft limit can be disabled by setting them to zero.client-output-buffer-limit normal 0 0 0client-output-buffer-limit replica 256mb 64mb 60client-output-buffer-limit pubsub 32mb 8mb 60 # Client query buffers accumulate new commands. They are limited to a fixed# amount by default in order to avoid that a protocol desynchronization (for# instance due to a bug in the client) will lead to unbound memory usage in# the query buffer. However you can configure it here if you have very special# needs, such us huge multi/exec requests or alike.## client-query-buffer-limit 1gb # In the Redis protocol, bulk requests, that are, elements representing single# strings, are normally limited ot 512 mb. However you can change this limit# here.## proto-max-bulk-len 512mb # Redis calls an internal function to perform many background tasks, like# closing connections of clients in timeout, purging expired keys that are# never requested, and so forth.## Not all tasks are performed with the same frequency, but Redis checks for# tasks to perform according to the specified "hz" value.## By default "hz" is set to 10. Raising the value will use more CPU when# Redis is idle, but at the same time will make Redis more responsive when# there are many keys expiring at the same time, and timeouts may be# handled with more precision.## The range is between 1 and 500, however a value over 100 is usually not# a good idea. Most users should use the default of 10 and raise this up to# 100 only in environments where very low latency is required.hz 10 # Normally it is useful to have an HZ value which is proportional to the# number of clients connected. This is useful in order, for instance, to# avoid too many clients are processed for each background task invocation# in order to avoid latency spikes.## Since the default HZ value by default is conservatively set to 10, Redis# offers, and enables by default, the ability to use an adaptive HZ value# which will temporary raise when there are many connected clients.## When dynamic HZ is enabled, the actual configured HZ will be used as# as a baseline, but multiples of the configured HZ value will be actually# used as needed once more clients are connected. In this way an idle# instance will use very little CPU time while a busy instance will be# more responsive.dynamic-hz yes # When a child rewrites the AOF file, if the following option is enabled# the file will be fsync-ed every 32 MB of data generated. This is useful# in order to commit the file to the disk more incrementally and avoid# big latency spikes.aof-rewrite-incremental-fsync yes # When redis saves RDB file, if the following option is enabled# the file will be fsync-ed every 32 MB of data generated. This is useful# in order to commit the file to the disk more incrementally and avoid# big latency spikes.rdb-save-incremental-fsync yes # Redis LFU eviction (see maxmemory setting) can be tuned. However it is a good# idea to start with the default settings and only change them after investigating# how to improve the performances and how the keys LFU change over time, which# is possible to inspect via the OBJECT FREQ command.## There are two tunable parameters in the Redis LFU implementation: the# counter logarithm factor and the counter decay time. It is important to# understand what the two parameters mean before changing them.## The LFU counter is just 8 bits per key, it's maximum value is 255, so Redis# uses a probabilistic increment with logarithmic behavior. Given the value# of the old counter, when a key is accessed, the counter is incremented in# this way:## 1. A random number R between 0 and 1 is extracted.# 2. A probability P is calculated as 1/(old_value*lfu_log_factor+1).# 3. The counter is incremented only if R < P.## The default lfu-log-factor is 10. This is a table of how the frequency# counter changes with a different number of accesses with different# logarithmic factors:## +--------+------------+------------+------------+------------+------------+# | factor | 100 hits   | 1000 hits  | 100K hits  | 1M hits    | 10M hits   |# +--------+------------+------------+------------+------------+------------+# | 0      | 104        | 255        | 255        | 255        | 255        |# +--------+------------+------------+------------+------------+------------+# | 1      | 18         | 49         | 255        | 255        | 255        |# +--------+------------+------------+------------+------------+------------+# | 10     | 10         | 18         | 142        | 255        | 255        |# +--------+------------+------------+------------+------------+------------+# | 100    | 8          | 11         | 49         | 143        | 255        |# +--------+------------+------------+------------+------------+------------+## NOTE: The above table was obtained by running the following commands:##   redis-benchmark -n 1000000 incr foo#   redis-cli object freq foo## NOTE 2: The counter initial value is 5 in order to give new objects a chance# to accumulate hits.## The counter decay time is the time, in minutes, that must elapse in order# for the key counter to be divided by two (or decremented if it has a value# less <= 10).## The default value for the lfu-decay-time is 1. A Special value of 0 means to# decay the counter every time it happens to be scanned.## lfu-log-factor 10# lfu-decay-time 1 ########################### ACTIVE DEFRAGMENTATION ######################### WARNING THIS FEATURE IS EXPERIMENTAL. However it was stress tested# even in production and manually tested by multiple engineers for some# time.## What is active defragmentation?# -------------------------------## Active (online) defragmentation allows a Redis server to compact the# spaces left between small allocations and deallocations of data in memory,# thus allowing to reclaim back memory.## Fragmentation is a natural process that happens with every allocator (but# less so with Jemalloc, fortunately) and certain workloads. Normally a server# restart is needed in order to lower the fragmentation, or at least to flush# away all the data and create it again. However thanks to this feature# implemented by Oran Agra for Redis 4.0 this process can happen at runtime# in an "hot" way, while the server is running.## Basically when the fragmentation is over a certain level (see the# configuration options below) Redis will start to create new copies of the# values in contiguous memory regions by exploiting certain specific Jemalloc# features (in order to understand if an allocation is causing fragmentation# and to allocate it in a better place), and at the same time, will release the# old copies of the data. This process, repeated incrementally for all the keys# will cause the fragmentation to drop back to normal values.## Important things to understand:## 1. This feature is disabled by default, and only works if you compiled Redis#    to use the copy of Jemalloc we ship with the source code of Redis.#    This is the default with Linux builds.## 2. You never need to enable this feature if you don't have fragmentation#    issues.## 3. Once you experience fragmentation, you can enable this feature when#    needed with the command "CONFIG SET activedefrag yes".## The configuration parameters are able to fine tune the behavior of the# defragmentation process. If you are not sure about what they mean it is# a good idea to leave the defaults untouched. # Enabled active defragmentation# activedefrag yes # Minimum amount of fragmentation waste to start active defrag# active-defrag-ignore-bytes 100mb # Minimum percentage of fragmentation to start active defrag# active-defrag-threshold-lower 10 # Maximum percentage of fragmentation at which we use maximum effort# active-defrag-threshold-upper 100 # Minimal effort for defrag in CPU percentage# active-defrag-cycle-min 5 # Maximal effort for defrag in CPU percentage# active-defrag-cycle-max 75 # Maximum number of set/hash/zset/list fields that will be processed from# the main dictionary scan# active-defrag-max-scan-fields 1000  

	- 使用redis6.0.8镜像创建容器(也叫运行镜像)

	   docker run  -p 6379:6379 --name myr3 --privileged=true -v /app/redis/redis.conf:/etc/redis/redis.conf -v /app/redis/data:/data -d redis:6.0.8 redis-server /etc/redis/redis.conf   

	- 测试redis-cli连接上来

	    docker exec -it 运行着Rediis服务的容器ID redis-cli

	- 请证明docker启动使用了我们自己指定的配置文件

		- 修改前

		    我们用的配置文件，数据库默认是16个

		- 修改后

		  宿主机的修改会同步给docker容器里面的配置。

			- 记得重启服务

	- 测试redis-cli连接上来第2次

- 安装Nginx

	- 见高级篇Portainer

## 高级篇(大厂进阶)

### Docker复杂安装详说

- 安装mysql主从复制

	- 主从复制原理

		- 默认你懂

	- 主从搭建步骤

		- 新建主服务器容器实例3307

		  docker run -p 3307:3306 --name mysql-master \-v /mydata/mysql-master/log:/var/log/mysql \-v /mydata/mysql-master/data:/var/lib/mysql \-v /mydata/mysql-master/conf:/etc/mysql \-e MYSQL_ROOT_PASSWORD=root  \-d mysql:5.7

		- 进入/mydata/mysql-master/conf目录下新建my.cnf

			- vim my.cnf

			  [mysqld]## 设置server_id，同一局域网中需要唯一server_id=101 ## 指定不需要同步的数据库名称binlog-ignore-db=mysql  ## 开启二进制日志功能log-bin=mall-mysql-bin  ## 设置二进制日志使用内存大小（事务）binlog_cache_size=1M  ## 设置使用的二进制日志格式（mixed,statement,row）binlog_format=mixed  ## 二进制日志过期清理时间。默认值为0，表示不自动清理。expire_logs_days=7  ## 跳过主从复制中遇到的所有错误或指定类型的错误，避免slave端复制中断。## 如：1062错误是指一些主键重复，1032错误是因为主从数据库数据不一致slave_skip_errors=1062

		- 修改完配置后重启master实例

			- docker restart mysql-master

		- 进入mysql-master容器

			- docker exec -it mysql-master /bin/bash
			- mysql -uroot -proot

		- master容器实例内创建数据同步用户

			- CREATE USER 'slave'@'%' IDENTIFIED BY '123456';
			- GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'slave'@'%';

		- 新建从服务器容器实例3308

		  docker run -p 3308:3306 --name mysql-slave \-v /mydata/mysql-slave/log:/var/log/mysql \-v /mydata/mysql-slave/data:/var/lib/mysql \-v /mydata/mysql-slave/conf:/etc/mysql \-e MYSQL_ROOT_PASSWORD=root  \-d mysql:5.7

		- 进入/mydata/mysql-slave/conf目录下新建my.cnf

			- vim my.cnf

			  [mysqld]## 设置server_id，同一局域网中需要唯一server_id=102## 指定不需要同步的数据库名称binlog-ignore-db=mysql  ## 开启二进制日志功能，以备Slave作为其它数据库实例的Master时使用log-bin=mall-mysql-slave1-bin  ## 设置二进制日志使用内存大小（事务）binlog_cache_size=1M  ## 设置使用的二进制日志格式（mixed,statement,row）binlog_format=mixed  ## 二进制日志过期清理时间。默认值为0，表示不自动清理。expire_logs_days=7  ## 跳过主从复制中遇到的所有错误或指定类型的错误，避免slave端复制中断。## 如：1062错误是指一些主键重复，1032错误是因为主从数据库数据不一致slave_skip_errors=1062  ## relay_log配置中继日志relay_log=mall-mysql-relay-bin  ## log_slave_updates表示slave将复制事件写进自己的二进制日志log_slave_updates=1  ## slave设置为只读（具有super权限的用户除外）read_only=1

		- 修改完配置后重启slave实例

			- docker restart mysql-slave

		- 在主数据库中查看主从同步状态

			- show master status;

		- 进入mysql-slave容器

			- docker exec -it mysql-slave /bin/bash
			- mysql -uroot -proot

		- 在从数据库中配置主从复制

		  change master to master_host='宿主机ip', master_user='slave', master_password='123456', master_port=3307, master_log_file='mall-mysql-bin.000001', master_log_pos=617, master_connect_retry=30;  

			- 主从复制命令参数说明

			  master_host：主数据库的IP地址；master_port：主数据库的运行端口；master_user：在主数据库创建的用于同步数据的用户账号；master_password：在主数据库创建的用于同步数据的用户密码；master_log_file：指定从数据库要复制数据的日志文件，通过查看主数据的状态，获取File参数；master_log_pos：指定从数据库从哪个位置开始复制数据，通过查看主数据的状态，获取Position参数；master_connect_retry：连接失败重试的时间间隔，单位为秒。 

		- 在从数据库中查看主从同步状态

			- show slave status \G;

			   

		- 在从数据库中开启主从同步

			- Subtopic

		- 查看从数据库状态发现已经同步
		- 主从复制测试

			- 主机新建库-使用库-新建表-插入数据，ok
			- 从机使用库-查看记录，ok

- 安装redis集群(大厂面试题第4季-分布式存储案例真题)

	- cluster(集群)模式-docker版
哈希槽分区进行亿级数据存储

		- 面试题

			- 1~2亿条数据需要缓存，请问如何设计这个存储案例
			- 回答

				- 单机单台100%不可能，肯定是分布式存储，用redis如何落地？

			- 上述问题阿里P6~P7工程案例和场景设计类必考题目，
一般业界有3种解决方案

				- 哈希取余分区

				  2亿条记录就是2亿个k,v，我们单机不行必须要分布式多机，假设有3台机器构成一个集群，用户每次读写操作都是根据公式：hash(key) % N个机器台数，计算出哈希值，用来决定数据映射到哪一个节点上。优点：  简单粗暴，直接有效，只需要预估好数据规划好节点，例如3台、8台、10台，就能保证一段时间的数据支撑。使用Hash算法让固定的一部分请求落到同一台服务器上，这样每台服务器固定处理一部分请求（并维护这些请求的信息），起到负载均衡+分而治之的作用。缺点：   原来规划好的节点，进行扩容或者缩容就比较麻烦了额，不管扩缩，每次数据变动导致节点有变动，映射关系需要重新进行计算，在服务器个数固定不变时没有问题，如果需要弹性扩容或故障停机的情况下，原来的取模公式就会发生变化：Hash(key)/3会变成Hash(key) /?。此时地址经过取余运算的结果将发生很大变化，根据公式获取的服务器也会变得不可控。某个redis机器宕机了，由于台数数量变化，会导致hash取余全部数据重新洗牌。 

					- 缺点那？？？

					  缺点：   原来规划好的节点，进行扩容或者缩容就比较麻烦了额，不管扩缩，每次数据变动导致节点有变动，映射关系需要重新进行计算，在服务器个数固定不变时没有问题，如果需要弹性扩容或故障停机的情况下，原来的取模公式就会发生变化：Hash(key)/3会变成Hash(key) /?。此时地址经过取余运算的结果将发生很大变化，根据公式获取的服务器也会变得不可控。某个redis机器宕机了，由于台数数量变化，会导致hash取余全部数据重新洗牌。 

				- 一致性哈希算法分区

					- 是什么

					  一致性Hash算法背景　　一致性哈希算法在1997年由麻省理工学院中提出的，设计目标是为了解决分布式缓存数据变动和映射问题，某个机器宕机了，分母数量改变了，自然取余数不OK了。   

					- 能干嘛

						- 提出一致性Hash解决方案。
目的是当服务器个数发生变动时，
尽量减少影响客户端到服务器的映射关系

					- 3大步骤

						- 算法构建一致性哈希环

						  一致性哈希环    一致性哈希算法必然有个hash函数并按照算法产生hash值，这个算法的所有可能哈希值会构成一个全量集，这个集合可以成为一个hash空间[0,2^32-1]，这个是一个线性空间，但是在算法中，我们通过适当的逻辑控制将它首尾相连(0 = 2^32),这样让它逻辑上形成了一个环形空间。    它也是按照使用取模的方法，前面笔记介绍的节点取模法是对节点（服务器）的数量进行取模。而一致性Hash算法是对2^32取模，简单来说，一致性Hash算法将整个哈希值空间组织成一个虚拟的圆环，如假设某哈希函数H的值空间为0-2^32-1（即哈希值是一个32位无符号整形），整个哈希环如下图：整个空间按顺时针方向组织，圆环的正上方的点代表0，0点右侧的第一个点代表1，以此类推，2、3、4、……直到2^32-1，也就是说0点左侧的第一个点代表2^32-1， 0和2^32-1在零点中方向重合，我们把这个由2^32个点组成的圆环称为Hash环。

						- 服务器IP节点映射

						  节点映射   将集群中各个IP节点映射到环上的某一个位置。   将各个服务器使用Hash进行一个哈希，具体可以选择服务器的IP或主机名作为关键字进行哈希，这样每台机器就能确定其在哈希环上的位置。假如4个节点NodeA、B、C、D，经过IP地址的哈希函数计算(hash(ip))，使用IP地址哈希后在环空间的位置如下：  

						- key落到服务器的落键规则

						  当我们需要存储一个kv键值对时，首先计算key的hash值，hash(key)，将这个key使用相同的函数Hash计算出哈希值并确定此数据在环上的位置，从此位置沿环顺时针“行走”，第一台遇到的服务器就是其应该定位到的服务器，并将该键值对存储在该节点上。如我们有Object A、Object B、Object C、Object D四个数据对象，经过哈希计算后，在环空间上的位置如下：根据一致性Hash算法，数据A会被定为到Node A上，B被定为到Node B上，C被定为到Node C上，D被定为到Node D上。

					- 优点

						- 一致性哈希算法的容错性

						  容错性假设Node C宕机，可以看到此时对象A、B、D不会受到影响，只有C对象被重定位到Node D。一般的，在一致性Hash算法中，如果一台服务器不可用，则受影响的数据仅仅是此服务器到其环空间中前一台服务器（即沿着逆时针方向行走遇到的第一台服务器）之间数据，其它不会受到影响。简单说，就是C挂了，受到影响的只是B、C之间的数据，并且这些数据会转移到D进行存储。 

						- 一致性哈希算法的扩展性

						   扩展性数据量增加了，需要增加一台节点NodeX，X的位置在A和B之间，那收到影响的也就是A到X之间的数据，重新把A到X的数据录入到X上即可，不会导致hash取余全部数据重新洗牌。 

					- 缺点

						- 一致性哈希算法的数据倾斜问题

						   Hash环的数据倾斜问题一致性Hash算法在服务节点太少时，容易因为节点分布不均匀而造成数据倾斜（被缓存的对象大部分集中缓存在某一台服务器上）问题，例如系统中只有两台服务器： 

					- 小总结

					  为了在节点数目发生改变时尽可能少的迁移数据 将所有的存储节点排列在收尾相接的Hash环上，每个key在计算Hash后会顺时针找到临近的存储节点存放。而当有节点加入或退出时仅影响该节点在Hash环上顺时针相邻的后续节点。   优点加入和删除节点只影响哈希环中顺时针方向的相邻的节点，对其他节点无影响。 缺点 数据的分布和节点的位置有关，因为这些节点不是均匀的分布在哈希环上的，所以数据在进行存储时达不到均匀分布的效果。

				- 哈希槽分区

					- 是什么

					   1 为什么出现哈希槽实质就是一个数组，数组[0,2^14 -1]形成hash slot空间。 2 能干什么解决均匀分配的问题，在数据和节点之间又加入了一层，把这层称为哈希槽（slot），用于管理数据和节点之间的关系，现在就相当于节点上放的是槽，槽里放的是数据。槽解决的是粒度问题，相当于把粒度变大了，这样便于数据移动。哈希解决的是映射问题，使用key的哈希值来计算所在的槽，便于数据分配。 3 多少个hash槽一个集群只能有16384个槽，编号0-16383（0-2^14-1）。这些槽会分配给集群中的所有主节点，分配策略没有要求。可以指定哪些编号的槽分配给哪个主节点。集群会记录节点和槽的对应关系。解决了节点和槽的关系后，接下来就需要对key求哈希值，然后对16384取余，余数是几key就落入对应的槽里。slot = CRC16(key) % 16384。以槽为单位移动数据，因为槽的数目是固定的，处理起来比较容易，这样数据移动问题就解决了。 

					- 哈希槽计算

					   Redis 集群中内置了 16384 个哈希槽，redis 会根据节点数量大致均等的将哈希槽映射到不同的节点。当需要在 Redis 集群中放置一个 key-value时，redis 先对 key 使用 crc16 算法算出一个结果，然后把结果对 16384 求余数，这样每个 key 都会对应一个编号在 0-16383 之间的哈希槽，也就是映射到某个节点上。如下代码，key之A 、B在Node2， key之C落在Node3上 

		- 3主3从redis集群扩缩容配置案例架构说明

			- 见自己的processon笔记

		- 开打步骤

			- 3主3从redis集群配置

				- 关闭防火墙+启动docker后台服务

					- systemctl start docker

				- 新建6个docker容器redis实例

				  docker run -d --name redis-node-1 --net host --privileged=true -v /data/redis/share/redis-node-1:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6381 docker run -d --name redis-node-2 --net host --privileged=true -v /data/redis/share/redis-node-2:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6382 docker run -d --name redis-node-3 --net host --privileged=true -v /data/redis/share/redis-node-3:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6383 docker run -d --name redis-node-4 --net host --privileged=true -v /data/redis/share/redis-node-4:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6384 docker run -d --name redis-node-5 --net host --privileged=true -v /data/redis/share/redis-node-5:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6385 docker run -d --name redis-node-6 --net host --privileged=true -v /data/redis/share/redis-node-6:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6386如果运行成功，效果如下：

					- 命令分步解释

						- docker run

							- 创建并运行docker容器实例

						- --name redis-node-6

							- 容器名字

						- --net host

							- 使用宿主机的IP和端口，默认

						- --privileged=true

							- 获取宿主机root用户权限

						- -v /data/redis/share/redis-node-6:/data

							- 容器卷，宿主机地址:docker内部地址

						- redis:6.0.8

							- redis镜像和版本号

						- --cluster-enabled yes

							- 开启redis集群

						- --appendonly yes

							- 开启持久化

						- --port 6386

							- redis端口号

				- 进入容器redis-node-1并为6台机器构建集群关系

					- 进入容器

						- docker exec -it redis-node-1 /bin/bash

					- 构建主从关系

					  //注意，进入docker容器后才能执行一下命令，且注意自己的真实IP地址redis-cli --cluster create 192.168.111.147:6381 192.168.111.147:6382 192.168.111.147:6383 192.168.111.147:6384 192.168.111.147:6385 192.168.111.147:6386 --cluster-replicas 1 --cluster-replicas 1 表示为每个master创建一个slave节点   

					- 一切OK的话，3主3从搞定

				- 链接进入6381作为切入点，查看集群状态

					- 链接进入6381作为切入点，查看节点状态

					   

					- cluster info
					- cluster nodes

			- 主从容错切换迁移案例

				- 数据读写存储

					- 启动6机构成的集群并通过exec进入
					- 对6381新增两个key
					- 防止路由失效加参数-c并新增两个key

					   加入参数-c，优化路由

					- 查看集群信息

					   redis-cli --cluster check 192.168.111.147:6381 

				- 容错切换迁移

					- 主6381和从机切换，先停止主机6381

						- 6381主机停了，对应的真实从机上位
						- 6381作为1号主机分配的从机以实际情况为准，具体是几号机器就是几号

					- 再次查看集群信息

					     6381宕机了，6385上位成为了新的master。备注：本次脑图笔记6381为主下面挂从6385。每次案例下面挂的从机以实际情况为准，具体是几号机器就是几号

					- 先还原之前的3主3从

					    中间需要等待一会儿，docker集群重新响应。

						- 先启6381

							- docker start redis-node-1

						- 再停6385

							- docker stop redis-node-5

						- 再启6385

							- docker start redis-node-5

						- 主从机器分配情况以实际情况为准

					- 查看集群状态

						- redis-cli --cluster check 自己IP:6381

			- 主从扩容案例

				- 新建6387、6388两个节点+新建后启动+查看是否8节点

				  docker run -d --name redis-node-7 --net host --privileged=true -v /data/redis/share/redis-node-7:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6387docker run -d --name redis-node-8 --net host --privileged=true -v /data/redis/share/redis-node-8:/data redis:6.0.8 --cluster-enabled yes --appendonly yes --port 6388docker ps 

				- 进入6387容器实例内部

					- docker exec -it redis-node-7 /bin/bash

				- 将新增的6387节点(空槽号)作为master节点加入原集群

				   将新增的6387作为master节点加入集群redis-cli --cluster add-node 自己实际IP地址:6387 自己实际IP地址:63816387 就是将要作为master新增节点6381 就是原来集群节点里面的领路人，相当于6387拜拜6381的码头从而找到组织加入集群 

				- 检查集群情况第1次

				   redis-cli --cluster check 真实ip地址:6381  

				- 重新分派槽号

				  重新分派槽号命令:redis-cli --cluster reshard IP地址:端口号redis-cli --cluster reshard 192.168.111.147:6381

				- 检查集群情况第2次

				   redis-cli --cluster check 真实ip地址:6381 

					- 槽号分派说明

					   为什么6387是3个新的区间，以前的还是连续？重新分配成本太高，所以前3家各自匀出来一部分，从6381/6382/6383三个旧节点分别匀出1364个坑位给新节点6387 

				- 为主节点6387分配从节点6388

				   命令：redis-cli --cluster add-node ip:新slave端口 ip:新master端口 --cluster-slave --cluster-master-id 新主机节点ID redis-cli --cluster add-node 192.168.111.147:6388 192.168.111.147:6387 --cluster-slave --cluster-master-id e4781f644d4a4e4d4b4d107157b9ba8144631451-------这个是6387的编号，按照自己实际情况 

				- 检查集群情况第3次

				   redis-cli --cluster check 192.168.111.147:6382 

			- 主从缩容案例

				- 目的：6387和6388下线
				- 检查集群情况1获得6388的节点ID

				   redis-cli --cluster check 192.168.111.147:6382   

				- 将6388删除
从集群中将4号从节点6388删除

				   命令：redis-cli --cluster del-node ip:从机端口 从机6388节点ID redis-cli --cluster del-node 192.168.111.147:6388 5d149074b7e57b802287d1797a874ed7a1a284a8 redis-cli --cluster check 192.168.111.147:6382  检查一下发现，6388被删除了，只剩下7台机器了。  

				- 将6387的槽号清空，重新分配，本例将清出来的槽号都给6381

				  redis-cli --cluster reshard 192.168.111.147:6381  

				- 检查集群情况第二次

				   redis-cli --cluster check 192.168.111.147:6381 4096个槽位都指给6381，它变成了8192个槽位，相当于全部都给6381了，不然要输入3次，一锅端 

				- 将6387删除

				   命令：redis-cli --cluster del-node ip:端口 6387节点ID redis-cli --cluster del-node 192.168.111.147:6387 e4781f644d4a4e4d4b4d107157b9ba8144631451 

				- 检查集群情况第三次

				   redis-cli --cluster check 192.168.111.147:6381  

### DockerFile解析

- 是什么

	- Dockerfile是用来构建Docker镜像的文本文件，是由一条条构建镜像所需的指令和参数构成的脚本。
	- 概述

	   

	- 官网

		- https://docs.docker.com/engine/reference/builder/

	- 构建三步骤

		- 编写Dockerfile文件

			- docker build命令构建镜像

				- docker run依镜像运行容器实例

- DockerFile构建过程解析

	- Dockerfile内容基础知识

		- 1：每条保留字指令都必须为大写字母且后面要跟随至少一个参数
		- 2：指令按照从上到下，顺序执行
		- 3：#表示注释
		- 4：每条指令都会创建一个新的镜像层并对镜像进行提交

	- Docker执行Dockerfile的大致流程

		- （1）docker从基础镜像运行一个容器
		- （2）执行一条指令并对容器作出修改
		- （3）执行类似docker commit的操作提交一个新的镜像层
		- （4）docker再基于刚提交的镜像运行一个新容器
		- （5）执行dockerfile中的下一条指令直到所有指令都执行完成

	- 小总结

	   从应用软件的角度来看，Dockerfile、Docker镜像与Docker容器分别代表软件的三个不同阶段，*  Dockerfile是软件的原材料*  Docker镜像是软件的交付品*  Docker容器则可以认为是软件镜像的运行态，也即依照镜像运行的容器实例Dockerfile面向开发，Docker镜像成为交付标准，Docker容器则涉及部署与运维，三者缺一不可，合力充当Docker体系的基石。1 Dockerfile，需要定义一个Dockerfile，Dockerfile定义了进程需要的一切东西。Dockerfile涉及的内容包括执行代码或者是文件、环境变量、依赖包、运行时环境、动态链接库、操作系统的发行版、服务进程和内核进程(当应用进程需要和系统服务和内核进程打交道，这时需要考虑如何设计namespace的权限控制)等等; 2 Docker镜像，在用Dockerfile定义一个文件之后，docker build时会产生一个Docker镜像，当运行 Docker镜像时会真正开始提供服务; 3 Docker容器，容器是直接提供服务的。  

- DockerFile常用保留字指令

	- 参考tomcat8的dockerfile入门

		- https://github.com/docker-library/tomcat

	- FROM

		- 基础镜像，当前新镜像是基于哪个镜像的，指定一个已经存在的镜像作为模板，第一条必须是from

	- MAINTAINER

		- 镜像维护者的姓名和邮箱地址

	- RUN

		- 容器构建时需要运行的命令
		- 两种格式

			- shell格式

			   RUN yum -y install vim

			- exec格式

		- RUN是在 docker build时运行

	- EXPOSE

		- 当前容器对外暴露出的端口

	- WORKDIR

		- 指定在创建容器后，终端默认登陆的进来工作目录，一个落脚点

	- USER

		- 指定该镜像以什么样的用户去执行，如果都不指定，默认是root

	- ENV

		- 用来在构建镜像过程中设置环境变量

		   ENV MY_PATH /usr/mytest这个环境变量可以在后续的任何RUN指令中使用，这就如同在命令前面指定了环境变量前缀一样；也可以在其它指令中直接使用这些环境变量， 比如：WORKDIR $MY_PATH

	- ADD

		- 将宿主机目录下的文件拷贝进镜像且会自动处理URL和解压tar压缩包

	- COPY

		- 类似ADD，拷贝文件和目录到镜像中。
将从构建上下文目录中 <源路径> 的文件/目录复制到新的一层的镜像内的 <目标路径> 位置

			- COPY src dest
			- COPY ["src", "dest"]
			- <src源路径>：源文件或者源目录
			- <dest目标路径>：容器内的指定路径，该路径不用事先建好，路径不存在的话，会自动创建。

	- VOLUME

		- 容器数据卷，用于数据保存和持久化工作

	- CMD

		- 指定容器启动后的要干的事情
		- 注意

			- Dockerfile 中可以有多个 CMD 指令，但只有最后一个生效，CMD 会被 docker run 之后的参数替换
			- 参考官网Tomcat的dockerfile演示讲解

				- 官网最后一行命令

					- Subtopic

				- 我们演示自己的覆盖操作

					- Subtopic

		- 它和前面RUN命令的区别

			- CMD是在docker run 时运行。
			- RUN是在 docker build时运行。

	- ENTRYPOINT

		- 也是用来指定一个容器启动时要运行的命令
		- 类似于 CMD 指令，但是ENTRYPOINT不会被docker run后面的命令覆盖，
而且这些命令行参数会被当作参数送给 ENTRYPOINT 指令指定的程序
		- 命令格式和案例说明

		   命令格式：ENTRYPOINT可以和CMD一起用，一般是变参才会使用 CMD ，这里的 CMD 等于是在给 ENTRYPOINT 传参。当指定了ENTRYPOINT后，CMD的含义就发生了变化，不再是直接运行其命令而是将CMD的内容作为参数传递给ENTRYPOINT指令，他两个组合会变成 案例如下：假设已通过 Dockerfile 构建了 nginx:test 镜像：是否传参按照dockerfile编写执行传参运行Docker命令docker run  nginx:testdocker run  nginx:test -c /etc/nginx/new.conf衍生出的实际命令nginx -c /etc/nginx/nginx.confnginx -c /etc/nginx/new.conf 

		- 优点

			- 在执行docker run的时候可以指定 ENTRYPOINT 运行所需的参数。

		- 注意

			- 如果 Dockerfile 中如果存在多个 ENTRYPOINT 指令，仅最后一个生效。

	- 小总结

- 案例

	- 自定义镜像mycentosjava8

		- 要求

			- Centos7镜像具备vim+ifconfig+jdk8
			- JDK的下载镜像地址

				- 官网

				    下载地址：https://www.oracle.com/java/technologies/downloads/#java8

				- https://mirrors.yangxingzhen.com/jdk/

		- 编写

			- 准备编写Dockerfile文件

			   FROM centosMAINTAINER zzyy<zzyybs@126.com> ENV MYPATH /usr/localWORKDIR $MYPATH #安装vim编辑器RUN yum -y install vim#安装ifconfig命令查看网络IPRUN yum -y install net-tools#安装java8及lib库RUN yum -y install glibc.i686RUN mkdir /usr/local/java#ADD 是相对路径jar,把jdk-8u171-linux-x64.tar.gz添加到容器中,安装包必须要和Dockerfile文件在同一位置ADD jdk-8u171-linux-x64.tar.gz /usr/local/java/#配置java环境变量ENV JAVA_HOME /usr/local/java/jdk1.8.0_171ENV JRE_HOME $JAVA_HOME/jreENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATHENV PATH $JAVA_HOME/bin:$PATH EXPOSE 80 CMD echo $MYPATHCMD echo "success--------------ok"CMD /bin/bash 

				- 大写字母D

		- 构建

			- docker build -t 新镜像名字:TAG .

			  docker build -t centosjava8:1.5 .  

			- 注意，上面TAG后面有个空格，有个点

		- 运行

			- docker run -it 新镜像名字:TAG 

			   docker run -it centosjava8:1.5 /bin/bash

		- 再体会下UnionFS（联合文件系统）

		  UnionFS（联合文件系统）：Union文件系统（UnionFS）是一种分层、轻量级并且高性能的文件系统，它支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下(unite several directories into a single virtual filesystem)。Union 文件系统是 Docker 镜像的基础。镜像可以通过分层来进行继承，基于基础镜像（没有父镜像），可以制作各种具体的应用镜像。 特性：一次同时加载多个文件系统，但从外面看起来，只能看到一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有底层的文件和目录

	- 虚悬镜像

		- 是什么

			- 仓库名、标签都是<none>的镜像，俗称dangling image
			- Dockerfile写一个

			   1 vim Dockerfilefrom ubuntuCMD echo 'action is success'2 docker build .

		- 查看

			- docker image ls -f dangling=true
			- 命令结果

		- 删除

		   docker image prune 虚悬镜像已经失去存在价值，可以删除 

	- 家庭作业-自定义镜像myubuntu

		- 编写

			- 准备编写DockerFile文件

			   FROM ubuntuMAINTAINER zzyy<zzyybs@126.com> ENV MYPATH /usr/localWORKDIR $MYPATH RUN apt-get updateRUN apt-get install net-tools#RUN apt-get install -y iproute2#RUN apt-get install -y inetutils-ping EXPOSE 80 CMD echo $MYPATHCMD echo "install inconfig cmd into ubuntu success--------------ok"CMD /bin/bash 

		- 构建

			- docker build -t 新镜像名字:TAG .

		- 运行

			- docker run -it 新镜像名字:TAG 

- 小总结

   

### Docker微服务实战

- 通过IDEA新建一个普通微服务模块

	- 建Module

		- docker_boot

	- 改POM

	  <?xml version="1.0" encoding="UTF-8"?><project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">    <modelVersion>4.0.0</modelVersion>    <parent>        <groupId>org.springframework.boot</groupId>        <artifactId>spring-boot-starter-parent</artifactId>        <version>2.5.6</version>        <relativePath/>    </parent>    <groupId>com.atguigu.docker</groupId>    <artifactId>docker_boot</artifactId>    <version>0.0.1-SNAPSHOT</version>    <properties>        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>        <maven.compiler.source>1.8</maven.compiler.source>        <maven.compiler.target>1.8</maven.compiler.target>        <junit.version>4.12</junit.version>        <log4j.version>1.2.17</log4j.version>        <lombok.version>1.16.18</lombok.version>        <mysql.version>5.1.47</mysql.version>        <druid.version>1.1.16</druid.version>        <mapper.version>4.1.5</mapper.version>        <mybatis.spring.boot.version>1.3.0</mybatis.spring.boot.version>    </properties>    <dependencies>        <!--SpringBoot通用依赖模块-->        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-web</artifactId>        </dependency>        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-actuator</artifactId>        </dependency>        <!--test-->        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-test</artifactId>            <scope>test</scope>        </dependency>    </dependencies>    <build>        <plugins>            <plugin>                <groupId>org.springframework.boot</groupId>                <artifactId>spring-boot-maven-plugin</artifactId>            </plugin>            <plugin>                <groupId>org.apache.maven.plugins</groupId>                <artifactId>maven-resources-plugin</artifactId>                <version>3.1.0</version>            </plugin>        </plugins>    </build></project> 

	- 写YML

	   server.port=6001 

	- 主启动

	  package com.atguigu.docker;import org.springframework.boot.SpringApplication;import org.springframework.boot.autoconfigure.SpringBootApplication;@SpringBootApplicationpublic class DockerBootApplication{    public static void main(String[] args)    {        SpringApplication.run(DockerBootApplication.class, args);    }} 

	- 业务类

	  package com.atguigu.docker.controller;import org.springframework.beans.factory.annotation.Value;import org.springframework.web.bind.annotation.RequestMapping;import org.springframework.web.bind.annotation.RequestMethod;import org.springframework.web.bind.annotation.RestController;import java.util.UUID;/** * @auther zzyy * @create 2021-10-25 17:43 */@RestControllerpublic class OrderController{    @Value("${server.port}")    private String port;    @RequestMapping("/order/docker")    public String helloDocker()    {        return "hello docker"+"\t"+port+"\t"+ UUID.randomUUID().toString();    }    @RequestMapping(value ="/order/index",method = RequestMethod.GET)    public String index()    {        return "服务端口号: "+"\t"+port+"\t"+UUID.randomUUID().toString();    }}

- 通过dockerfile发布微服务部署到docker容器

	- IDEA工具里面搞定微服务jar包

	   docker_boot-0.0.1-SNAPSHOT.jar 

	- 编写Dockerfile

		- Dockerfile内容

		  # 基础镜像使用javaFROM java:8# 作者MAINTAINER zzyy# VOLUME 指定临时文件目录为/tmp，在主机/var/lib/docker目录下创建了一个临时文件并链接到容器的/tmpVOLUME /tmp# 将jar包添加到容器中并更名为zzyy_docker.jarADD docker_boot-0.0.1-SNAPSHOT.jar zzyy_docker.jar# 运行jar包RUN bash -c 'touch /zzyy_docker.jar'ENTRYPOINT ["java","-jar","/zzyy_docker.jar"]#暴露6001端口作为微服务EXPOSE 6001 

		- 将微服务jar包和Dockerfile文件上传到同一个目录下/mydocker

		   docker build -t zzyy_docker:1.6 .

	- 构建镜像

		- docker build -t zzyy_docker:1.6 .
		- 打包成镜像文件

	- 运行容器

	   docker run -d -p 6001:6001 zzyy_docker:1.6

	- 访问测试

### Docker网络

- 是什么

	- docker不启动，默认网络情况

		- ens33
		- lo
		- virbr0

		   在CentOS7的安装过程中如果有选择相关虚拟化的的服务安装系统后，启动网卡时会发现有一个以网桥连接的私网地址的virbr0网卡(virbr0网卡：它还有一个固定的默认IP地址192.168.122.1)，是做虚拟机网桥的使用的，其作用是为连接其上的虚机网卡提供 NAT访问外网的功能。 我们之前学习Linux安装，勾选安装系统的时候附带了libvirt服务才会生成的一个东西，如果不需要可以直接将libvirtd服务卸载，yum remove libvirt-libs.x86_64

	- docker启动后，网络情况

	  会产生一个名为docker0的虚拟网桥

		- 查看docker网络模式命令

		   默认创建3大网络模式

- 常用基本命令

	- All命令
	- 查看网络

		- docker network ls

	- 查看网络源数据

		- docker network inspect  XXX网络名字

	- 删除网络

		- docker network rm XXX网络名字

	- 案例

- 能干嘛

	- 容器间的互联和通信以及端口映射
	- 容器IP变动时候可以通过服务名直接网络通信而不受到影响

- 网络模式

	- 总体介绍

		- bridge模式：使用--network  bridge指定，默认使用docker0
		- host模式：使用--network host指定
		- none模式：使用--network none指定
		- container模式：使用--network container:NAME或者容器ID指定

	- 容器实例内默认网络IP生产规则

		- 说明

		  1 先启动两个ubuntu容器实例2 docker inspect 容器ID or 容器名字 3  关闭u2实例，新建u3，查看ip变化

		- 结论

			- docker容器内部的ip是有可能会发生改变的

	- 案例说明

		- bridge

			- 是什么

			   Docker 服务默认会创建一个 docker0 网桥（其上有一个 docker0 内部接口），该桥接网络的名称为docker0，它在内核层连通了其他的物理或虚拟网卡，这就将所有容器和本地主机都放到同一个物理网络。Docker 默认指定了 docker0 接口 的 IP 地址和子网掩码，让主机和容器之间可以通过网桥相互通信。 # 查看 bridge 网络的详细信息，并通过 grep 获取名称项docker network inspect bridge | grep name ifconfig

			- 案例

				- 说明

				  1 Docker使用Linux桥接，在宿主机虚拟一个Docker容器网桥(docker0)，Docker启动一个容器时会根据Docker网桥的网段分配给容器一个IP地址，称为Container-IP，同时Docker网桥是每个容器的默认网关。因为在同一宿主机内的容器都接入同一个网桥，这样容器之间就能够通过容器的Container-IP直接通信。 2 docker run 的时候，没有指定network的话默认使用的网桥模式就是bridge，使用的就是docker0。在宿主机ifconfig,就可以看到docker0和自己create的network(后面讲)eth0，eth1，eth2……代表网卡一，网卡二，网卡三……，lo代表127.0.0.1，即localhost，inet addr用来表示网卡的IP地址 3 网桥docker0创建一对对等虚拟设备接口一个叫veth，另一个叫eth0，成对匹配。   3.1 整个宿主机的网桥模式都是docker0，类似一个交换机有一堆接口，每个接口叫veth，在本地主机和容器内分别创建一个虚拟接口，并让他们彼此联通（这样一对接口叫veth pair）；   3.2 每个容器实例内部也有一块网卡，每个接口叫eth0；   3.3 docker0上面的每个veth匹配某个容器实例内部的eth0，两两配对，一一匹配。 通过上述，将宿主机上的所有容器都连接到这个内部网络上，两个容器在同一个网络下,会从这个网关下各自拿到分配的ip，此时两个容器的网络是互通的。

				- 代码

					- docker run -d -p 8081:8080   --name tomcat81 billygoo/tomcat8-jdk8
					- docker run -d -p 8082:8080   --name tomcat82 billygoo/tomcat8-jdk8

				- 两两匹配验证

		- host

			- 是什么

			   直接使用宿主机的 IP 地址与外界进行通信，不再需要额外进行NAT 转换。

			- 案例

				- 说明

				   容器将不会获得一个独立的Network Namespace， 而是和宿主机共用一个Network Namespace。容器将不会虚拟出自己的网卡而是使用宿主机的IP和端口。

				- 代码

					- 警告

						- docker run -d -p 8083:8080 --network host --name tomcat83 billygoo/tomcat8-jdk8

						    问题：     docke启动时总是遇见标题中的警告原因：    docker启动时指定--network=host或-net=host，如果还指定了-p映射端口，那这个时候就会有此警告，并且通过-p设置的参数将不会起到任何作用，端口号会以主机端口号为主，重复时则递增。解决:    解决的办法就是使用docker的其他网络模式，例如--network=bridge，这样就可以解决问题，或者直接无视。。。。O(∩_∩)O哈哈~

					- 正确

						- docker run -d                          --network host --name tomcat83 billygoo/tomcat8-jdk8

				- 无之前的配对显示了，看容器实例内部
				- 没有设置-p的端口映射了，如何访问启动的tomcat83？？

				   http://宿主机IP:8080/ 在CentOS里面用默认的火狐浏览器访问容器内的tomcat83看到访问成功，因为此时容器的IP借用主机的，所以容器共享宿主机网络IP，这样的好处是外部主机与容器可以直接通信。

		- none

			- 是什么

			    在none模式下，并不为Docker容器进行任何网络配置。 也就是说，这个Docker容器没有网卡、IP、路由等信息，只有一个lo需要我们自己为Docker容器添加网卡、配置IP等。

				- 禁用网络功能，只有lo标识(就是127.0.0.1表示本地回环)

			- 案例

			   docker run -d -p 8084:8080 --network none --name tomcat84 billygoo/tomcat8-jdk8 进入容器内部查看在容器外部查看

				- docker run -d -p 8084:8080 --network none --name tomcat84 billygoo/tomcat8-jdk8

		- container

			- 是什么

			  container⽹络模式 新建的容器和已经存在的一个容器共享一个网络ip配置而不是和宿主机共享。新创建的容器不会创建自己的网卡，配置自己的IP，而是和一个指定的容器共享IP、端口范围等。同样，两个容器除了网络方面，其他的如文件系统、进程列表等还是隔离的。

			- 案例

				- docker run -d -p 8085:8080                                     --name tomcat85 billygoo/tomcat8-jdk8
				- docker run -d -p 8086:8080 --network container:tomcat85 --name tomcat86 billygoo/tomcat8-jdk8
				- 运行结果

				      # 相当于tomcat86和tomcat85公用同一个ip同一个端口，导致端口冲突本案例用tomcat演示不合适。。。演示坑。。。。。。o(╥﹏╥)o 换一个镜像给大家演示，

			- 案例2

				- Alpine操作系统是一个面向安全的轻型 Linux发行版

				    Alpine Linux 是一款独立的、非商业的通用 Linux 发行版，专为追求安全性、简单性和资源效率的用户而设计。 可能很多人没听说过这个 Linux 发行版本，但是经常用 Docker 的朋友可能都用过，因为他小，简单，安全而著称，所以作为基础镜像是非常好的一个选择，可谓是麻雀虽小但五脏俱全，镜像非常小巧，不到 6M的大小，所以特别适合容器打包。

				- docker run -it                                                    --name alpine1  alpine /bin/sh
				- docker run -it --network container:alpine1 --name alpine2  alpine /bin/sh
				- 运行结果，验证共用搭桥
				- 假如此时关闭alpine1，再看看alpine2

				  15: eth0@if16: 消失了。。。。。。关闭alpine1，再看看alpine2

		- 自定义网络

			- 过时的link
			- 是什么
			- 案例

				- before

					- 案例

						- docker run -d -p 8081:8080   --name tomcat81 billygoo/tomcat8-jdk8
						- docker run -d -p 8082:8080   --name tomcat82 billygoo/tomcat8-jdk8
						- 上述成功启动并用docker exec进入各自容器实例内部

					- 问题

						- 按照IP地址ping是OK的
						- 按照服务名ping结果???

				- after

					- 案例

						- 自定义桥接网络,自定义网络默认使用的是桥接网络bridge
						- 新建自定义网络
						- 新建容器加入上一步新建的自定义网络

							- docker run -d -p 8081:8080 --network zzyy_network  --name tomcat81 billygoo/tomcat8-jdk8
							- docker run -d -p 8082:8080 --network zzyy_network  --name tomcat82 billygoo/tomcat8-jdk8

						- 互相ping测试

					- 问题结论

						- 自定义网络本身就维护好了主机名和ip的对应关系（ip和域名都能通）
						- 自定义网络本身就维护好了主机名和ip的对应关系（ip和域名都能通）
						- 自定义网络本身就维护好了主机名和ip的对应关系（ip和域名都能通）

- Docker平台架构图解

	- 整体说明

	  从其架构和运行流程来看，Docker 是一个 C/S 模式的架构，后端是一个松耦合架构，众多模块各司其职。  Docker 运行的基本流程为： 1 用户是使用 Docker Client 与 Docker Daemon 建立通信，并发送请求给后者。2 Docker Daemon 作为 Docker 架构中的主体部分，首先提供 Docker Server 的功能使其可以接受 Docker Client 的请求。3 Docker Engine 执行 Docker 内部的一系列工作，每一项工作都是以一个 Job 的形式的存在。4 Job 的运行过程中，当需要容器镜像时，则从 Docker Registry 中下载镜像，并通过镜像管理驱动 Graph driver将下载镜像以Graph的形式存储。5 当需要为 Docker 创建网络环境时，通过网络管理驱动 Network driver 创建并配置 Docker 容器网络环境。6 当需要限制 Docker 容器运行资源或执行用户指令等操作时，则通过 Execdriver 来完成。7 Libcontainer是一项独立的容器管理包，Network driver以及Exec driver都是通过Libcontainer来实现具体对容器进行的操作。

	- 整体架构

### Docker-compose容器编排

- 是什么

   Compose 是 Docker 公司推出的一个工具软件，可以管理多个 Docker 容器组成一个应用。你需要定义一个 YAML 格式的配置文件docker-compose.yml，写好多个容器之间的调用关系。然后，只要一个命令，就能同时启动/关闭这些容器

	- Docker-Compose是Docker官方的开源项目，
负责实现对Docker容器集群的快速编排。

- 能干嘛

    docker建议我们每一个容器中只运行一个服务,因为docker容器本身占用资源极少,所以最好是将每个服务单独的分割开来但是这样我们又面临了一个问题？ 如果我需要同时部署好多个服务,难道要每个服务单独写Dockerfile然后在构建镜像,构建容器,这样累都累死了,所以docker官方给我们提供了docker-compose多服务部署的工具 例如要实现一个Web微服务项目，除了Web服务容器本身，往往还需要再加上后端的数据库mysql服务容器，redis服务器，注册中心eureka，甚至还包括负载均衡容器等等。。。。。。 Compose允许用户通过一个单独的docker-compose.yml模板文件（YAML 格式）来定义一组相关联的应用容器为一个项目（project）。 可以很容易地用一个配置文件定义一个多容器的应用，然后使用一条指令安装这个应用的所有依赖，完成构建。Docker-Compose 解决了容器与容器之间如何管理编排的问题。

- 去哪下

	- 官网

		- https://docs.docker.com/compose/compose-file/compose-file-v3/

	- 官网下载

		- https://docs.docker.com/compose/install/

	- 安装步骤

	  curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-composechmod +x /usr/local/bin/docker-composedocker-compose --version 

	- 卸载步骤

- Compose核心概念

	- 一文件

		- docker-compose.yml

	- 两要素

		- 服务（service）

			- 一个个应用容器实例，比如订单微服务、库存微服务、mysql容器、nginx容器或者redis容器

		- 工程（project）

			- 由一组关联的应用容器组成的一个完整业务单元，在 docker-compose.yml 文件中定义。

- Compose使用的三个步骤

	- 编写Dockerfile定义各个微服务应用并构建出对应的镜像文件
	- 使用 docker-compose.yml 定义一个完整业务单元，安排好整体应用中的各个容器服务。
	- 最后，执行docker-compose up命令 来启动并运行整个应用程序，完成一键部署上线

- Compose常用命令

  Compose常用命令docker-compose -h                           # 查看帮助docker-compose up                           # 启动所有docker-compose服务docker-compose up -d                        # 启动所有docker-compose服务并后台运行docker-compose down                         # 停止并删除容器、网络、卷、镜像。docker-compose exec  yml里面的服务id                 # 进入容器实例内部  docker-compose exec docker-compose.yml文件中写的服务id /bin/bashdocker-compose ps                      # 展示当前docker-compose编排过的运行的所有容器docker-compose top                     # 展示当前docker-compose编排过的容器进程 docker-compose logs  yml里面的服务id     # 查看容器输出日志docker-compose config     # 检查配置docker-compose config -q  # 检查配置，有问题才有输出docker-compose restart   # 重启服务docker-compose start     # 启动服务docker-compose stop      # 停止服务 

- Compose编排微服务

	- 改造升级微服务工程docker_boot

		- 以前的基础版
		- SQL建表建库

		   CREATE TABLE `t_user` (  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,  `username` varchar(50) NOT NULL DEFAULT '' COMMENT '用户名',  `password` varchar(50) NOT NULL DEFAULT '' COMMENT '密码',  `sex` tinyint(4) NOT NULL DEFAULT '0' COMMENT '性别 0=女 1=男 ',  `deleted` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '删除标志，默认0不删除，1删除',  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',  PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='用户表'

		- 一键生成说明
		- 改POM

		  <?xml version="1.0" encoding="UTF-8"?><project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">    <modelVersion>4.0.0</modelVersion>    <parent>        <groupId>org.springframework.boot</groupId>        <artifactId>spring-boot-starter-parent</artifactId>        <version>2.5.6</version>        <!--<version>2.3.10.RELEASE</version>-->        <relativePath/> <!-- lookup parent from repository -->    </parent>    <groupId>com.atguigu.docker</groupId>    <artifactId>docker_boot</artifactId>    <version>0.0.1-SNAPSHOT</version>    <properties>        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>        <maven.compiler.source>1.8</maven.compiler.source>        <maven.compiler.target>1.8</maven.compiler.target>        <junit.version>4.12</junit.version>        <log4j.version>1.2.17</log4j.version>        <lombok.version>1.16.18</lombok.version>        <mysql.version>5.1.47</mysql.version>        <druid.version>1.1.16</druid.version>        <mapper.version>4.1.5</mapper.version>        <mybatis.spring.boot.version>1.3.0</mybatis.spring.boot.version>    </properties>    <dependencies>        <!--guava Google 开源的 Guava 中自带的布隆过滤器-->        <dependency>            <groupId>com.google.guava</groupId>            <artifactId>guava</artifactId>            <version>23.0</version>        </dependency>        <!-- redisson -->        <dependency>            <groupId>org.redisson</groupId>            <artifactId>redisson</artifactId>            <version>3.13.4</version>        </dependency>        <!--SpringBoot通用依赖模块-->        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-web</artifactId>        </dependency>        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-actuator</artifactId>        </dependency>        <!--swagger2-->        <dependency>            <groupId>io.springfox</groupId>            <artifactId>springfox-swagger2</artifactId>            <version>2.9.2</version>        </dependency>        <dependency>            <groupId>io.springfox</groupId>            <artifactId>springfox-swagger-ui</artifactId>            <version>2.9.2</version>        </dependency>        <!--SpringBoot与Redis整合依赖-->        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-data-redis</artifactId>        </dependency>        <!--springCache-->        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-cache</artifactId>        </dependency>        <!--springCache连接池依赖包-->        <dependency>            <groupId>org.apache.commons</groupId>            <artifactId>commons-pool2</artifactId>        </dependency>        <!-- jedis -->        <dependency>            <groupId>redis.clients</groupId>            <artifactId>jedis</artifactId>            <version>3.1.0</version>        </dependency>        <!--Mysql数据库驱动-->        <dependency>            <groupId>mysql</groupId>            <artifactId>mysql-connector-java</artifactId>            <version>5.1.47</version>        </dependency>        <!--SpringBoot集成druid连接池-->        <dependency>            <groupId>com.alibaba</groupId>            <artifactId>druid-spring-boot-starter</artifactId>            <version>1.1.10</version>        </dependency>        <dependency>            <groupId>com.alibaba</groupId>            <artifactId>druid</artifactId>            <version>${druid.version}</version>        </dependency>        <!--mybatis和springboot整合-->        <dependency>            <groupId>org.mybatis.spring.boot</groupId>            <artifactId>mybatis-spring-boot-starter</artifactId>            <version>${mybatis.spring.boot.version}</version>        </dependency>        <!-- 添加springboot对amqp的支持 -->        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-amqp</artifactId>        </dependency>        <dependency>            <groupId>commons-codec</groupId>            <artifactId>commons-codec</artifactId>            <version>1.10</version>        </dependency>        <!--通用基础配置junit/devtools/test/log4j/lombok/hutool-->        <!--hutool-->        <dependency>            <groupId>cn.hutool</groupId>            <artifactId>hutool-all</artifactId>            <version>5.2.3</version>        </dependency>        <dependency>            <groupId>junit</groupId>            <artifactId>junit</artifactId>            <version>${junit.version}</version>        </dependency>        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-devtools</artifactId>            <scope>runtime</scope>            <optional>true</optional>        </dependency>        <dependency>            <groupId>org.springframework.boot</groupId>            <artifactId>spring-boot-starter-test</artifactId>            <scope>test</scope>        </dependency>        <dependency>            <groupId>log4j</groupId>            <artifactId>log4j</artifactId>            <version>${log4j.version}</version>        </dependency>        <dependency>            <groupId>org.projectlombok</groupId>            <artifactId>lombok</artifactId>            <version>${lombok.version}</version>            <optional>true</optional>        </dependency>        <!--persistence-->        <dependency>            <groupId>javax.persistence</groupId>            <artifactId>persistence-api</artifactId>            <version>1.0.2</version>        </dependency>        <!--通用Mapper-->        <dependency>            <groupId>tk.mybatis</groupId>            <artifactId>mapper</artifactId>            <version>${mapper.version}</version>        </dependency>    </dependencies>    <build>        <plugins>            <plugin>                <groupId>org.springframework.boot</groupId>                <artifactId>spring-boot-maven-plugin</artifactId>            </plugin>            <plugin>                <groupId>org.apache.maven.plugins</groupId>                <artifactId>maven-resources-plugin</artifactId>                <version>3.1.0</version>            </plugin>        </plugins>    </build></project> 

		- 写YML

		  server.port=6001# ========================alibaba.druid相关配置=====================spring.datasource.type=com.alibaba.druid.pool.DruidDataSourcespring.datasource.driver-class-name=com.mysql.jdbc.Driverspring.datasource.url=jdbc:mysql://192.168.111.169:3306/db2021?useUnicode=true&characterEncoding=utf-8&useSSL=falsespring.datasource.username=rootspring.datasource.password=123456spring.datasource.druid.test-while-idle=false# ========================redis相关配置=====================spring.redis.database=0spring.redis.host=192.168.111.169spring.redis.port=6379spring.redis.password=spring.redis.lettuce.pool.max-active=8spring.redis.lettuce.pool.max-wait=-1msspring.redis.lettuce.pool.max-idle=8spring.redis.lettuce.pool.min-idle=0# ========================mybatis相关配置===================mybatis.mapper-locations=classpath:mapper/*.xmlmybatis.type-aliases-package=com.atguigu.docker.entities# ========================swagger=====================spring.swagger2.enabled=true 

		- 主启动

		  package com.atguigu.docker;import org.springframework.boot.SpringApplication;import org.springframework.boot.autoconfigure.SpringBootApplication;import tk.mybatis.spring.annotation.MapperScan;@SpringBootApplication@MapperScan("com.atguigu.docker.mapper") //import tk.mybatis.spring.annotation.MapperScan;public class DockerBootApplication{    public static void main(String[] args)    {        SpringApplication.run(DockerBootApplication.class, args);    }} 

		- 业务类

			- config配置类

				- RedisConfig

				  package com.atguigu.docker.config;import lombok.extern.slf4j.Slf4j;import org.springframework.context.annotation.Bean;import org.springframework.context.annotation.Configuration;import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;import org.springframework.data.redis.core.RedisTemplate;import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;import org.springframework.data.redis.serializer.StringRedisSerializer;import java.io.Serializable;/** * @auther zzyy * @create 2021-10-27 17:19 */@Configuration@Slf4jpublic class RedisConfig{    /**     * @param lettuceConnectionFactory     * @return     *     * redis序列化的工具配置类，下面这个请一定开启配置     * 127.0.0.1:6379> keys *     * 1) "ord:102"  序列化过     * 2) "\xac\xed\x00\x05t\x00\aord:102"   野生，没有序列化过     */    @Bean    public RedisTemplate<String,Serializable> redisTemplate(LettuceConnectionFactory lettuceConnectionFactory)    {        RedisTemplate<String,Serializable> redisTemplate = new RedisTemplate<>();        redisTemplate.setConnectionFactory(lettuceConnectionFactory);        //设置key序列化方式string        redisTemplate.setKeySerializer(new StringRedisSerializer());        //设置value的序列化方式json        redisTemplate.setValueSerializer(new GenericJackson2JsonRedisSerializer());        redisTemplate.setHashKeySerializer(new StringRedisSerializer());        redisTemplate.setHashValueSerializer(new GenericJackson2JsonRedisSerializer());        redisTemplate.afterPropertiesSet();        return redisTemplate;    }} 

				- SwaggerConfig

				  package com.atguigu.docker.config;import org.springframework.beans.factory.annotation.Value;import org.springframework.context.annotation.Bean;import org.springframework.context.annotation.Configuration;import springfox.documentation.builders.ApiInfoBuilder;import springfox.documentation.builders.PathSelectors;import springfox.documentation.builders.RequestHandlerSelectors;import springfox.documentation.service.ApiInfo;import springfox.documentation.spi.DocumentationType;import springfox.documentation.spring.web.plugins.Docket;import springfox.documentation.swagger2.annotations.EnableSwagger2;import java.text.SimpleDateFormat;import java.util.Date;/** * @auther zzyy * @create 2021-05-01 16:18 */@Configuration@EnableSwagger2public class SwaggerConfig{    @Value("${spring.swagger2.enabled}")    private Boolean enabled;    @Bean    public Docket createRestApi() {        return new Docket(DocumentationType.SWAGGER_2)                .apiInfo(apiInfo())                .enable(enabled)                .select()                .apis(RequestHandlerSelectors.basePackage("com.atguigu.docker")) //你自己的package                .paths(PathSelectors.any())                .build();    }    public ApiInfo apiInfo() {        return new ApiInfoBuilder()                .title("尚硅谷Java大厂技术"+"\t"+new SimpleDateFormat("yyyy-MM-dd").format(new Date()))                .description("docker-compose")                .version("1.0")                .termsOfServiceUrl("https://www.atguigu.com/")                .build();    }} 

			- 新建entity

				- User

				  package com.atguigu.docker.entities;import javax.persistence.Column;import javax.persistence.GeneratedValue;import javax.persistence.Id;import javax.persistence.Table;import java.util.Date;@Table(name = "t_user")public class User{    @Id    @GeneratedValue(generator = "JDBC")    private Integer id;    /**     * 用户名     */    private String username;    /**     * 密码     */    private String password;    /**     * 性别 0=女 1=男      */    private Byte sex;    /**     * 删除标志，默认0不删除，1删除     */    private Byte deleted;    /**     * 更新时间     */    @Column(name = "update_time")    private Date updateTime;    /**     * 创建时间     */    @Column(name = "create_time")    private Date createTime;    /**     * @return id     */    public Integer getId() {        return id;    }    /**     * @param id     */    public void setId(Integer id) {        this.id = id;    }    /**     * 获取用户名     *     * @return username - 用户名     */    public String getUsername() {        return username;    }    /**     * 设置用户名     *     * @param username 用户名     */    public void setUsername(String username) {        this.username = username;    }    /**     * 获取密码     *     * @return password - 密码     */    public String getPassword() {        return password;    }    /**     * 设置密码     *     * @param password 密码     */    public void setPassword(String password) {        this.password = password;    }    /**     * 获取性别 0=女 1=男      *     * @return sex - 性别 0=女 1=男      */    public Byte getSex() {        return sex;    }    /**     * 设置性别 0=女 1=男      *     * @param sex 性别 0=女 1=男      */    public void setSex(Byte sex) {        this.sex = sex;    }    /**     * 获取删除标志，默认0不删除，1删除     *     * @return deleted - 删除标志，默认0不删除，1删除     */    public Byte getDeleted() {        return deleted;    }    /**     * 设置删除标志，默认0不删除，1删除     *     * @param deleted 删除标志，默认0不删除，1删除     */    public void setDeleted(Byte deleted) {        this.deleted = deleted;    }    /**     * 获取更新时间     *     * @return update_time - 更新时间     */    public Date getUpdateTime() {        return updateTime;    }    /**     * 设置更新时间     *     * @param updateTime 更新时间     */    public void setUpdateTime(Date updateTime) {        this.updateTime = updateTime;    }    /**     * 获取创建时间     *     * @return create_time - 创建时间     */    public Date getCreateTime() {        return createTime;    }    /**     * 设置创建时间     *     * @param createTime 创建时间     */    public void setCreateTime(Date createTime) {        this.createTime = createTime;    }} 

				- UserDTO

				  package com.atguigu.docker.entities;import io.swagger.annotations.ApiModel;import io.swagger.annotations.ApiModelProperty;import lombok.AllArgsConstructor;import lombok.Data;import lombok.NoArgsConstructor;import java.io.Serializable;import java.util.Date;@NoArgsConstructor@AllArgsConstructor@Data@ApiModel(value = "用户信息")public class UserDTO implements Serializable{    @ApiModelProperty(value = "用户ID")    private Integer id;    @ApiModelProperty(value = "用户名")    private String username;    @ApiModelProperty(value = "密码")    private String password;    @ApiModelProperty(value = "性别 0=女 1=男 ")    private Byte sex;    @ApiModelProperty(value = "删除标志，默认0不删除，1删除")    private Byte deleted;    @ApiModelProperty(value = "更新时间")    private Date updateTime;    @ApiModelProperty(value = "创建时间")    private Date createTime;    /**     * @return id     */    public Integer getId() {        return id;    }    /**     * @param id     */    public void setId(Integer id) {        this.id = id;    }    /**     * 获取用户名     *     * @return username - 用户名     */    public String getUsername() {        return username;    }    /**     * 设置用户名     *     * @param username 用户名     */    public void setUsername(String username) {        this.username = username;    }    /**     * 获取密码     *     * @return password - 密码     */    public String getPassword() {        return password;    }    /**     * 设置密码     *     * @param password 密码     */    public void setPassword(String password) {        this.password = password;    }    /**     * 获取性别 0=女 1=男      *     * @return sex - 性别 0=女 1=男      */    public Byte getSex() {        return sex;    }    /**     * 设置性别 0=女 1=男      *     * @param sex 性别 0=女 1=男      */    public void setSex(Byte sex) {        this.sex = sex;    }    /**     * 获取删除标志，默认0不删除，1删除     *     * @return deleted - 删除标志，默认0不删除，1删除     */    public Byte getDeleted() {        return deleted;    }    /**     * 设置删除标志，默认0不删除，1删除     *     * @param deleted 删除标志，默认0不删除，1删除     */    public void setDeleted(Byte deleted) {        this.deleted = deleted;    }    /**     * 获取更新时间     *     * @return update_time - 更新时间     */    public Date getUpdateTime() {        return updateTime;    }    /**     * 设置更新时间     *     * @param updateTime 更新时间     */    public void setUpdateTime(Date updateTime) {        this.updateTime = updateTime;    }    /**     * 获取创建时间     *     * @return create_time - 创建时间     */    public Date getCreateTime() {        return createTime;    }    /**     * 设置创建时间     *     * @param createTime 创建时间     */    public void setCreateTime(Date createTime) {        this.createTime = createTime;    }    @Override    public String toString() {        return "User{" +                "id=" + id +                ", username='" + username + '\'' +                ", password='" + password + '\'' +                ", sex=" + sex +                '}';    }} 

			- 新建mapper

				- 新建接口UserMapper 

				  package com.atguigu.docker.mapper;import com.atguigu.docker.entities.User;import tk.mybatis.mapper.common.Mapper;public interface UserMapper extends Mapper<User> {} 

				- src\main\resources路径下新建mapper文件夹并新增UserMapper.xml

				  <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd"><mapper namespace="com.atguigu.docker.mapper.UserMapper">  <resultMap id="BaseResultMap" type="com.atguigu.docker.entities.User">    <!--      WARNING - @mbg.generated    -->    <id column="id" jdbcType="INTEGER" property="id" />    <result column="username" jdbcType="VARCHAR" property="username" />    <result column="password" jdbcType="VARCHAR" property="password" />    <result column="sex" jdbcType="TINYINT" property="sex" />    <result column="deleted" jdbcType="TINYINT" property="deleted" />    <result column="update_time" jdbcType="TIMESTAMP" property="updateTime" />    <result column="create_time" jdbcType="TIMESTAMP" property="createTime" />  </resultMap></mapper> 

			- 新建service

			  package com.atguigu.docker.service;import com.atguigu.docker.entities.User;import com.atguigu.docker.mapper.UserMapper;import lombok.extern.slf4j.Slf4j;import org.slf4j.Logger;import org.slf4j.LoggerFactory;import org.springframework.beans.factory.annotation.Autowired;import org.springframework.data.redis.core.RedisTemplate;import org.springframework.data.redis.core.ValueOperations;import org.springframework.stereotype.Service;import org.springframework.web.bind.annotation.PathVariable;import javax.annotation.Resource;import java.util.concurrent.TimeUnit;/** * @auther zzyy * @create 2021-05-01 14:58 */@Service@Slf4jpublic class UserService {    public static final String CACHE_KEY_USER = "user:";    @Resource    private UserMapper userMapper;    @Resource    private RedisTemplate redisTemplate;    /**     * addUser     * @param user     */    public void addUser(User user)    {        //1 先插入mysql并成功        int i = userMapper.insertSelective(user);        if(i > 0)        {            //2 需要再次查询一下mysql将数据捞回来并ok            user = userMapper.selectByPrimaryKey(user.getId());            //3 将捞出来的user存进redis，完成新增功能的数据一致性。            String key = CACHE_KEY_USER+user.getId();            redisTemplate.opsForValue().set(key,user);        }    }    /**     * findUserById     * @param id     * @return     */    public User findUserById(Integer id)    {        User user = null;        String key = CACHE_KEY_USER+id;        //1 先从redis里面查询，如果有直接返回结果，如果没有再去查询mysql        user = (User) redisTemplate.opsForValue().get(key);        if(user == null)        {            //2 redis里面无，继续查询mysql            user = userMapper.selectByPrimaryKey(id);            if(user == null)            {                //3.1 redis+mysql 都无数据                //你具体细化，防止多次穿透，我们规定，记录下导致穿透的这个key回写redis                return user;            }else{                //3.2 mysql有，需要将数据写回redis，保证下一次的缓存命中率                redisTemplate.opsForValue().set(key,user);            }        }        return user;    }} 

			- 新建controller

			  package com.atguigu.docker.controller;import cn.hutool.core.util.IdUtil;import cn.hutool.core.util.ReferenceUtil;import com.atguigu.docker.entities.User;import com.atguigu.docker.entities.UserDTO;import com.atguigu.docker.service.UserService;import io.swagger.annotations.Api;import io.swagger.annotations.ApiOperation;import io.swagger.models.auth.In;import lombok.extern.slf4j.Slf4j;import org.springframework.beans.BeanUtils;import org.springframework.beans.factory.annotation.Autowired;import org.springframework.web.bind.annotation.*;import javax.annotation.Resource;import java.util.Random;/** * @auther zzyy * @create 2021-05-01 15:02 */@Api(description = "用户User接口")@RestController@Slf4jpublic class UserController{    @Resource    private UserService userService;    @ApiOperation("数据库新增3条记录")    @RequestMapping(value = "/user/add",method = RequestMethod.POST)    public void addUser()    {        for (int i = 1; i <=3; i++) {            User user = new User();            user.setUsername("zzyy"+i);            user.setPassword(IdUtil.simpleUUID().substring(0,6));            user.setSex((byte) new Random().nextInt(2));            userService.addUser(user);        }    }    @ApiOperation("删除1条记录")    @RequestMapping(value = "/user/delete/{id}",method = RequestMethod.POST)    public void deleteUser(@PathVariable Integer id)    {        userService.deleteUser(id);    }    @ApiOperation("修改1条记录")    @RequestMapping(value = "/user/update",method = RequestMethod.POST)    public void updateUser(@RequestBody UserDTO userDTO)    {        User user = new User();        BeanUtils.copyProperties(userDTO,user);        userService.updateUser(user);    }    @ApiOperation("查询1条记录")    @RequestMapping(value = "/user/find/{id}",method = RequestMethod.GET)    public User findUserById(@PathVariable Integer id)    {        return userService.findUserById2(id);    }}  

		- mvn package命令将微服务形成新的jar包
并上传到Linux服务器/mydocker目录下
		- 编写Dockerfile

		  # 基础镜像使用javaFROM java:8# 作者MAINTAINER zzyy# VOLUME 指定临时文件目录为/tmp，在主机/var/lib/docker目录下创建了一个临时文件并链接到容器的/tmpVOLUME /tmp# 将jar包添加到容器中并更名为zzyy_docker.jarADD docker_boot-0.0.1-SNAPSHOT.jar zzyy_docker.jar# 运行jar包RUN bash -c 'touch /zzyy_docker.jar'ENTRYPOINT ["java","-jar","/zzyy_docker.jar"]#暴露6001端口作为微服务EXPOSE 6001  

		- 构建镜像

			- docker build -t zzyy_docker:1.6 .

	- 不用Compose

		- 单独的mysql容器实例

			- 新建mysql容器实例

			  docker run -p 3306:3306 --name mysql57 --privileged=true -v /zzyyuse/mysql/conf:/etc/mysql/conf.d -v /zzyyuse/mysql/logs:/logs -v /zzyyuse/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7 

			- 进入mysql容器实例并新建库db2021+新建表t_user

			   docker exec -it mysql57 /bin/bashmysql -uroot -pcreate database db2021;use db2021;CREATE TABLE `t_user` (  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,  `username` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '用户名',  `password` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '密码',  `sex` TINYINT(4) NOT NULL DEFAULT '0' COMMENT '性别 0=女 1=男 ',  `deleted` TINYINT(4) UNSIGNED NOT NULL DEFAULT '0' COMMENT '删除标志，默认0不删除，1删除',  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',  PRIMARY KEY (`id`)) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='用户表'; 

		- 单独的redis容器实例

		  docker run  -p 6379:6379 --name redis608 --privileged=true -v /app/redis/redis.conf:/etc/redis/redis.conf -v /app/redis/data:/data -d redis:6.0.8 redis-server /etc/redis/redis.conf

		- 微服务工程

		   docker run -d -p 6001:6001 zzyy_docker:1.6

		- 上面三个容器实例依次顺序启动成功

	- swagger测试

		- http://localhost:你的微服务端口/swagger-ui.html#/

	- 上面成功了，有哪些问题?

		- 先后顺序要求固定，先mysql+redis才能微服务访问成功
		- 多个run命令......
		- 容器间的启停或宕机，有可能导致IP地址对应的容器实例变化，映射出错，
要么生产IP写死(可以但是不推荐)，要么通过服务调用

	- 使用Compose

		- 服务编排，一套带走，安排
		- 编写docker-compose.yml文件

		  version: "3" services:  microService:    image: zzyy_docker:1.6    container_name: ms01    ports:      - "6001:6001"    volumes:      - /app/microService:/data    networks:       - atguigu_net     depends_on:       - redis      - mysql   redis:    image: redis:6.0.8    ports:      - "6379:6379"    volumes:      - /app/redis/redis.conf:/etc/redis/redis.conf      - /app/redis/data:/data    networks:       - atguigu_net    command: redis-server /etc/redis/redis.conf   mysql:    image: mysql:5.7    environment:      MYSQL_ROOT_PASSWORD: '123456'      MYSQL_ALLOW_EMPTY_PASSWORD: 'no'      MYSQL_DATABASE: 'db2021'      MYSQL_USER: 'zzyy'      MYSQL_PASSWORD: 'zzyy123'    ports:       - "3306:3306"    volumes:       - /app/mysql/db:/var/lib/mysql       - /app/mysql/conf/my.cnf:/etc/my.cnf       - /app/mysql/init:/docker-entrypoint-initdb.d    networks:      - atguigu_net    command: --default-authentication-plugin=mysql_native_password #解决外部无法访问 networks:    atguigu_net:  

		- 第二次修改微服务工程docker_boot

			- 写YML

			  server.port=6001# ========================alibaba.druid相关配置=====================spring.datasource.type=com.alibaba.druid.pool.DruidDataSourcespring.datasource.driver-class-name=com.mysql.jdbc.Driver#spring.datasource.url=jdbc:mysql://192.168.111.169:3306/db2021?useUnicode=true&characterEncoding=utf-8&useSSL=falsespring.datasource.url=jdbc:mysql://mysql:3306/db2021?useUnicode=true&characterEncoding=utf-8&useSSL=falsespring.datasource.username=rootspring.datasource.password=123456spring.datasource.druid.test-while-idle=false# ========================redis相关配置=====================spring.redis.database=0#spring.redis.host=192.168.111.169spring.redis.host=redisspring.redis.port=6379spring.redis.password=spring.redis.lettuce.pool.max-active=8spring.redis.lettuce.pool.max-wait=-1msspring.redis.lettuce.pool.max-idle=8spring.redis.lettuce.pool.min-idle=0# ========================mybatis相关配置===================mybatis.mapper-locations=classpath:mapper/*.xmlmybatis.type-aliases-package=com.atguigu.docker.entities# ========================swagger=====================spring.swagger2.enabled=true 

				- 通过服务名访问，IP无关

			- mvn package命令将微服务形成新的jar包
并上传到Linux服务器/mydocker目录下
			- 编写Dockerfile

			  # 基础镜像使用javaFROM java:8# 作者MAINTAINER zzyy# VOLUME 指定临时文件目录为/tmp，在主机/var/lib/docker目录下创建了一个临时文件并链接到容器的/tmpVOLUME /tmp# 将jar包添加到容器中并更名为zzyy_docker.jarADD docker_boot-0.0.1-SNAPSHOT.jar zzyy_docker.jar# 运行jar包RUN bash -c 'touch /zzyy_docker.jar'ENTRYPOINT ["java","-jar","/zzyy_docker.jar"]#暴露6001端口作为微服务EXPOSE 6001  

			- 构建镜像

				- docker build -t zzyy_docker:1.6 .

		- 执行 docker-compose up
或者
执行 docker-compose up -d
		- 进入mysql容器实例并新建库db2021+新建表t_user

		   docker exec -it 容器实例id /bin/bashmysql -uroot -pcreate database db2021;use db2021;CREATE TABLE `t_user` (  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,  `username` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '用户名',  `password` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '密码',  `sex` TINYINT(4) NOT NULL DEFAULT '0' COMMENT '性别 0=女 1=男 ',  `deleted` TINYINT(4) UNSIGNED NOT NULL DEFAULT '0' COMMENT '删除标志，默认0不删除，1删除',  `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',  PRIMARY KEY (`id`)) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='用户表'; 

		- 测试通过
		- Compose常用命令

		  Compose常用命令docker-compose -h                           # 查看帮助docker-compose up                           # 启动所有docker-compose服务docker-compose up -d                        # 启动所有docker-compose服务并后台运行docker-compose down                         # 停止并删除容器、网络、卷、镜像。docker-compose exec  yml里面的服务id                 # 进入容器实例内部  docker-compose exec docker-compose.yml文件中写的服务id /bin/bashdocker-compose ps                      # 展示当前docker-compose编排过的运行的所有容器docker-compose top                     # 展示当前docker-compose编排过的容器进程 docker-compose logs  yml里面的服务id     # 查看容器输出日志dokcer-compose config     # 检查配置dokcer-compose config -q  # 检查配置，有问题才有输出docker-compose restart   # 重启服务docker-compose start     # 启动服务docker-compose stop      # 停止服务 

		- 关停

### Docker轻量级可视化工具Portainer

- 是什么

    Portainer 是一款轻量级的应用，它提供了图形化界面，用于方便地管理Docker环境，包括单机环境和集群环境。

- 安装

	- 官网

		- https://www.portainer.io/
		- https://docs.portainer.io/v/ce-2.9/start/install/server/docker/linux

	- 步骤

		- docker命令安装

		   docker run -d -p 8000:8000 -p 9000:9000 --name portainer     --restart=always     -v /var/run/docker.sock:/var/run/docker.sock     -v portainer_data:/data     portainer/portainer 

		- 第一次登录需创建admin，访问地址：xxx.xxx.xxx.xxx:9000

		   用户名，直接用默认admin密码记得8位，随便你写  

		- 设置admin用户和密码后首次登陆
		- 选择local选项卡后本地docker详细信息展示
		- 上一步的图形展示，能想得起对应命令吗？

- 登陆并演示介绍常用操作case

### Docker容器监控之
CAdvisor+InfluxDB+Granfana

- 原生命令

	- 操作

	  docker stats命令的结果 

	- 问题

	    通过docker stats命令可以很方便的看到当前宿主机上所有容器的CPU,内存以及网络流量等数据，一般小公司够用了。。。。 但是， docker stats统计结果只能是当前宿主机的全部容器，数据资料是实时的，没有地方存储、没有健康指标过线预警等功能 

- 是什么

	- 容器监控3剑客

		- 一句话

		   

			- CAdvisor监控收集+InfluxDB存储数据+Granfana展示图表

		- CAdvisor
		- InfluxDB
		- Granfana
		- 总结

- compose容器编排，一套带走

	- 新建目录
	- 新建3件套组合的
docker-compose.yml

	  version: '3.1' volumes:  grafana_data: {} services: influxdb:  image: tutum/influxdb:0.9  restart: always  environment:    - PRE_CREATE_DB=cadvisor  ports:    - "8083:8083"    - "8086:8086"  volumes:    - ./data/influxdb:/data  cadvisor:  image: google/cadvisor  links:    - influxdb:influxsrv  command: -storage_driver=influxdb -storage_driver_db=cadvisor -storage_driver_host=influxsrv:8086  restart: always  ports:    - "8080:8080"  volumes:    - /:/rootfs:ro    - /var/run:/var/run:rw    - /sys:/sys:ro    - /var/lib/docker/:/var/lib/docker:ro  grafana:  user: "104"  image: grafana/grafana  user: "104"  restart: always  links:    - influxdb:influxsrv  ports:    - "3000:3000"  volumes:    - grafana_data:/var/lib/grafana  environment:    - HTTP_USER=admin    - HTTP_PASS=admin    - INFLUXDB_HOST=influxsrv    - INFLUXDB_PORT=8086    - INFLUXDB_NAME=cadvisor    - INFLUXDB_USER=root    - INFLUXDB_PASS=root

	- 启动docker-compose文件

		- docker-compose up

	- 查看三个服务容器是否启动
	- 测试

		- 浏览cAdvisor收集服务，http://ip:8080/

			- 第一次访问慢，请稍等
			- cadvisor也有基础的图形展现功能，这里主要用它来作数据采集

		- 浏览influxdb存储服务，http://ip:8083/
		- 浏览grafana展现服务，http://ip:3000

			- ip+3000端口的方式访问,默认帐户密码（admin/admin）
			- 配置步骤

				- 配置数据源
				- 选择influxdb数据源

				   

				- 配置细节

					- 1
					- 2

					   

				- 配置面板panel

					- 1
					- 2
					- 3
					- 4
					- 5
					- 6

				- 到这里cAdvisor+InfluxDB+Grafana容器监控系统就部署完成了

### 终章の总结

- 知识回顾简单串讲和总结
- 进阶篇：雷丰阳老师的K8S

  加油

*XMind: ZEN - Trial Version*