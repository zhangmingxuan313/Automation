import re
import sys
import signal

# def quit(signum, frame):
#     print('Stop pressing the CTRL+C!')
#     sys.exit()

def funtion():
    # signal.signal(signal.SIGINT, quit)
    # signal.signal(signal.SIGTERM, quit)
    while True:
        a=input()
        print(a)

if __name__ == '__main__':
    funtion()