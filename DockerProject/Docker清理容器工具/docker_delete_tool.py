import requests
import json
import traceback
import docker

class DockerMangement():
    """
    表示的是dockerd 管理的整个工具
    """

    def search_docker_names(self,repo_ip,repo_port):
        """
        查询仓库的docker容器
        :param repo_ip:
        :param repo_port:
        :return:
        """
        docker_images = []
        try:
            url = f"http://{repo_ip}:{str(repo_port)}/v2/_catalog"
            response = requests.get(url).content.strip()
            res_dic = json.loads(response)
            images_type = res_dic['repositories']
            for i in images_type:
                url2 = f"http://{repo_ip}:{str(repo_port)}/v2/{str(i)}//tags/list"
                res2 = requests.get(url2).content.strip()
                res_dic2 = json.loads(res2)
                name = res_dic2['name']
                tags = res_dic2['tags']
                for tag in tags:
                    docker_name = f"{str(repo_ip)}:{str(repo_port)}/{name}/{tag}"
                    docker_images.append(docker_name)
                    print(docker_name)
        except:
            traceback.print_exc()
        return docker_images

    def search_docker_names(self, host, port):
        """
        查询当前服务器上的docker容器
        :param host:
        :param port:
        :return:
        """
        pass

    def delete_docker_names_by_id(self,container_id):
        """
        通过容器的id来删除的镜像
        :param container_id:
        :return:
        """
        pass

    def delete_docker_names_by_label(self,images_label):
        """
        通过容器的标签来删除容器
        :param images_label:
        :return:
        """
        pass

    def delete_docker_names_by_prune(self,delete_cmd):
        """
        清理容器的剩余文件
        :param delete_cmd:
        :return:
        """
        pass

    def delete_docker_names_by_time(self,time):
        """
        指定删除规定时间的容器
        :param time:
        :return:
        """
        pass