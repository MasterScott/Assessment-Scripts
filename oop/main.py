import platform, os
from Assessment import *

def main():
    os = platform.system()
    if os == 'Windows':
        assessment = Windows()
    if os == 'Darwin':
        assessment = Mac()
    if os == 'Linux':
        assessment = Linux()

if __name__ == "__main__":
    main()