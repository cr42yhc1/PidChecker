# PidChecker
A simple Python project, Deep Learning Training Assistant. It detects the processes you are running and sends you a WeChat message notification if a process ends. 
It also calculates the start monitoring time, end running time, and total running time. You can add a label to easily differentiate which project you are currently monitoring and to help you identify the name of the terminated process.

一个简单的python项目，深度学习训练助手。检测您正在运行的进程，如果进程结束，会给您发送微信消息提醒，并计算开始监控时间和结束运行的时间以及运行的总时间。您可以添加label以方便您区分当前正在监控哪个项目，同时也方便您了解结束运行进程的名称。


**To quickly use** (requires configuring send_message.sh):python pid_ckecker.py -p <pid> -l <label>

**快速使用**（需要配置send_message.sh):python pid_ckecker.py -p <pid> -l <label>

Detailed instructions and configuration methods will be updated later.
详细的使用和配置方法将在后面更新。

原始项目(original project from)：
https://github.com/hqh546020152/weixin_messages_sh
