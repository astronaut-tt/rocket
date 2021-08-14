'''
requests:用于请求目标站点
sys:用于解析命令行参数
getopt:用于处理命令行参数
time:用于延时
threading:用于启用多线程
selenium:用于访问指定URL以及截图
'''

import requests,sys,getopt,time
from threading import Thread
from selenium import webdriver

# 程序标识
def banner():
    print("\n********************")
    name = '''
                               _ooOoo_
                              o8888888o
                              88" . "88
                              (| -_- |)
                              O\  =  /O
                           ____/`---'\____
                         .'  \\|     |//   `.
                        /  \\|||  :  |||//   \\
                       /  _||||| -:- |||||-  \\
                       |   | \\\  -  ///  |   |
                       | \_|  ''\---/''  |   |
                       \  .-\__  `-`  ___/-. /
                     ___`. .'  /--.--\  `. . __
                  ."" '<  `.___\_<|>_/___.'  >'"".
                 | | :  `- \`.;`\ _ /`;.`/ - ` : | |
                 \  \ `-.   \_ __\ /__ _/   .-` /  /
            ======`-.____`-.___\_____/___.-`____.-'======
                               `=---='
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    '''
    print(name)
    print("power by 你的屯王")
    print("***********************\n")

# 程序用法
def usage():
    print("用法：")
    print("     -w:网址 (https://www.baidu.com/FUZZ)")
    print("     -t:线程数")
    print("     -f:字典文件")
    print("     -c:剔除指定状态码")

class request_role(Thread):
    #创建线程
    def __init__(self,word,url,hidecode):
        Thread.__init__(self)
        try:
            self.word = word.split('\n')[0]
            self.target_url = url.replace('FUZZ',self.word)
            self.url = self.target_url
            self.hidecode = hidecode
        except Exception as e:
            print(e)
    #发起请求并获取响应
    def run(self):
        try:
            requests_url = requests.get(self.url,timeout=5)
            charts = str(len(requests_url.content))
            scode = str(requests_url.status_code)
            if scode != str(self.hidecode):
                if '200' <= scode < '300':
                    #实例化webdriver
                    driver = webdriver.PhantomJS(executable_path=r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
                    driver.get(self.url)
                    time.sleep(3)
                    driver.set_window_size(1024,768)
                    driver.save_screenshot(self.word+".png")
                print(scode,'\t\t',charts,'\t\t',self.url)
            i[0] = i[0] -1
        except Exception as e:
            print(e)
            
#启动request_role()
def launcher_thread(contents,nums,url,hidecode):
    global i
    i = []
    print("状态码",'\t\t',"字符数",'\t',"网址")
    i.append(0)
    #遍历字典文件中的关键字组合成URL并生成新的线程
    while len(contents):
        try:
            if i[0] < nums:
                content = contents.pop(0)
                i[0] = i[0]+1
                thread = request_role(content,url,hidecode)
                thread.start()
        except KeyboardInterrupt as e:
            print(e)
            sys.exit()
    return True

#用于接收命令行中的参数并将其传递给launch_thread()
def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        opts,args = getopt.getopt(sys.argv[1:],"w:t:f:c:")
    except getopt.GetoptError:
        print(e)
        sys.exit()
    hidecode = 0
    for opt,arg in opts:
        if opt == '-w':
            url = arg
        elif opt == '-f':
            dicts = arg
        elif opt == '-t':
            threads = int(arg)
        elif opt == '-c':
            hidecode = arg
    try:
        f = open(dicts,'r')
        words = f.readlines()
    except Exception as e:
        print(e)
        sys.exit()
    launcher_thread(words,threads,url,hidecode)

if __name__ == '__main__':
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("搞定")