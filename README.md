# PidChecker
A simple Python project, Deep Learning Training Assistant. It detects the processes you are running and sends you a WeChat message notification if a process ends. 
It also calculates the start monitoring time, end running time, and total running time. You can add a label to easily differentiate which project you are currently monitoring and to help you identify the name of the terminated process.

一个简单的python项目，深度学习训练助手。检测您正在运行的进程，如果进程结束，会给您发送微信消息提醒，并计算开始监控时间和结束运行的时间以及运行的总时间。您可以添加label以方便您区分当前正在监控哪个项目，同时也方便您了解结束运行进程的名称。


**To quickly use** (requires configuring send_message.sh):python pid_ckecker.py -p <pid> -l <label>

## 快速使用
（需要配置send_message.sh):python pid_ckecker.py -p <pid> -l <label>

Detailed instructions and configuration methods will be updated later.
====================================2024/03/03更新====================================
更新计划：
* [ ] 配置写入config文件，方便配置
* [ ] 支持Server酱和Wxpusher
* [ ] 更多可控参数
# 配置方法
## 企业微信配置
1. 注册企业微信后，选择应用中心，创建应用
![image](https://github.com/cr42yhc1/PidChecker/assets/35053568/3c3f0a20-a8c5-42f8-b80b-e7a2893167c1)
2. 起个名字，上传头像，选择自己的号作为可见成员
3. 记住应用ID,secret,前往 “我的企业” 标签页，记录最下面的 企业ID
![image](https://github.com/cr42yhc1/PidChecker/assets/35053568/69426ee4-17d2-42ad-a55d-e0c752149574)
4. 将上述信息填入pidchecker/send_message.sh
5. 返回应用管理，选择之前创建的应用，添加企业可信IP（可能需要先配置企业可信域名，我自己有域名，没域名的随便弄一个应该也行，没试过），IP是发信机器的公网IP。
   例如你家的服务器连接路由器获得的公网IP是A.B.C.D，那么你只需要将该IP加入白名单即可。


