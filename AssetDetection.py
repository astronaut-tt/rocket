#!/usr/bin/python3
#Browser: https://npm.taobao.org/mirrors/phantomjs
#Author astronaut-tt

import requests, sys, getopt, time
from threading import Thread
from selenium import webdriver

def usage():
    print("usage:")
    print("-w: website")
    print("-t: thread_count")
    print("-f: dict")
    print("-c: clear status_code")
    print("for ex1: python AssetDetection.py -w http://target.com/FUZZ -t 5 -f dict.txt -c 404")
    print("for ex2: python AssetDetection.py -w http://target.com/victim.jsp?method=FUZZ -t 5 -f dict.txt -c 404")

class request_role(Thread):
    def __init__(self, word, url, hidecode):
        Thread.__init__(self)
        try:
            self.word = word.split('\n')[0]
            self.target_url = url.replace('FUZZ',self.word)
            self.url = self.target_url
            self.hidecode = hidecode
        except Exception as e:
            print(e)
    def run(self):
        try:
            requests_url = requests.get(self.url, timeout=5)
            charts = str(len(requests_url.content))
            scode = str(requests_url.status_code)
            if scode != str(self.hidecode):
                if '200' <= scode < '300':
                    driver = webdriver.PhantomJS(executable_path = r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
                    driver.get(self.url)
                    time.sleep(3)
                    driver.set_window_size(1024, 768)
                    driver.save_screenshot(self.word + ".png")
                print(scode, '\t\t', charts, '\t\t\t', self.url)
            i[0] = i[0] - 1
        except Exception as e:
            print(e)

def launcher_thread(contents, nums, url, hidecode):
    global i
    i = []
    print("status_code", '\t', "content_length", '\t',"website")
    i.append(0)
    while len(contents):
        try:
            if i[0] < nums:
                content = contents.pop(0)
                i[0] = i[0] + 1
                thread = request_role(content, url, hidecode)
                thread.start()
        except KeyboardInterrupt as e:
            print(e)
            sys.exit()
    return True

def start(argv):
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "w:t:f:c:")
    except getopt.GetoptError as e:
        print(e)
        sys.exit()
    hidecode = 0
    for opt, arg in opts:
        if opt == '-w':
            url = arg
        elif opt == '-t':
            threads = int(arg)
        elif opt == '-f':
            dicts = arg
        elif opt == '-c':
            hidecode = arg
    try:
        f = open(r'dict.txt')
        words = f.readlines()
    except Exception as e:
        print(e)
        sys.exit()
    launcher_thread(words, threads, url, hidecode)

if __name__ == '__main__':
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt as e:
        print(e)
        sys.exit()