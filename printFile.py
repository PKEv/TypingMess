#coding: utf-8

from pywinauto.keyboard import send_keys
import time

def main(filePrint):
    #app = Application(backend="uia").connect(title_re=".*Google*")
    time.sleep(10)

    with open(filePrint) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # print("Line {}: {}".format(cnt, line.strip()))
            send_keys(line, with_spaces=True)
            line = fp.readline()
            time.sleep(1)
    pass

if __name__ == '__main__':
    filePrint = "readme.txt"

    main(filePrint)

