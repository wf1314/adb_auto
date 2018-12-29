#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ===============================================================================
#  Author: WangFan <sgwf525@126.com>
#  Version: 0.1
#  Description: 使用adb自动操作安卓应用
#  Change Log:
#      2018-12-30
#          0.1 完成
# ===============================================================================

import os
import time
import re

ip = '10.10.9.189'
password = '0805'
os.system('adb connect {}'.format(ip))  # 连接手机
size = os.popen('adb shell wm size')  # 获取手机屏幕分辨率
x, y = re.findall(r"(\d+)x(\d+)", size.read())[0]
x = int(x)
y = int(y)

def unlock(password):
    """
    手机解锁
    :param password:
    :return:
    """
    os.system('adb shell input keyevent 224')  # 亮屏
    os.system('adb shell input swipe 300 1000 300 500')  # 滑动屏幕到输入密码页
    os.system('adb shell input text {}'.format(password))  # 输入密码,华为手机不需要点击确定
    os.system('adb shell input keyevent 164')  # 设置静音

def run_wxxq():
    """
    网易星球自动收钻
    :return:
    """
    #todo
    os.system('adb shell monkey -p com.netease.blockchain -c android.intent.category.LAUNCHER 1')
    time.sleep(5)
    size = os.popen('adb shell wm size')
    x,y = re.findall(r"(\d+)x(\d+)", size.read())[0]
    print(x,y)
    # os.system('adb shell input tap')

def run_qywx(x, y):
    """
    企业微信下班自动打卡
    :param x: 屏幕分辨率
    :param y:
    :return:
    """
    # 运行企业微信
    os.system('adb shell monkey -p com.tencent.wework -c android.intent.category.LAUNCHER 1')
    time.sleep(3)  # 等待页面加载
    os.system('adb shell input tap 700 2060'.format(x-380, y-100))  # 屏幕坐标x,y值
    os.system('adb shell input tap 200 600'.format(x-880, y-1560))
    time.sleep(2)
    os.system('adb shell input tap 600 1600'.format(x-480, y-560))

if __name__ == '__main__':
    unlock(password)
    run_qywx(x, y)
