import errno
import os
import sys
import argparse
import time
import datetime
from time import strftime


# send_message.sh的路径
path = './'


def pid_exists(pid):
    pid = int(pid)
    if pid < 0:
        return False
    if pid == 0:
        raise ValueError('invalid PID 0')
    try:
        os.kill(pid, 0)
    except OSError as err:
        if err.errno == errno.ESRCH:
            # ESRCH == No such process
            return False
        elif err.errno == errno.EPERM:
            # EPERM clearly means there's a process to deny access to
            return True
        else:
            # According to "man 2 kill" possible error values are
            # (EINVAL, EPERM, ESRCH)
            raise
    else:
        return True


def gen_text(label, s_time, e_time):
    s_time = s_time.strftime("%Y-%m-%d,%H:%M:%S")
    e_time = e_time.strftime("%Y-%m-%d,%H:%M:%S")
    if label:
        text = label + "执行完毕,监控开始时间:" + s_time + "监控结束时间:" + e_time
    else:
        text = "您的任务执行完毕,监控开始时间:" + s_time + "监控结束时间:" + e_time
    return text


parser = argparse.ArgumentParser(description='checker')
parser.add_argument('-p', '--pid', default=0, help='pid you want to check')
parser.add_argument('-l', '--label', default=None, help='label')
arg = parser.parse_args()

pid_checker_path = os.path.join(path, "send_message.sh")
# 获取开始时间
start_time = datetime.datetime.now()
# 开始监控
os.system(pid_checker_path + " " + arg.label + "监控开始")


flag = True
while flag:
    if pid_exists(arg.pid):
        time.sleep(5)
    else:
        flag = False
        end_time = datetime.datetime.now()
        t = gen_text(arg.label, start_time, end_time)
        os.system(pid_checker_path + " " + t)
# t = gen_text(arg.label, start_time, start_time)
# os.system("./source/send_message.sh \"任务执行完成\"")
# os.system(pid_checker_path + " " + t)
