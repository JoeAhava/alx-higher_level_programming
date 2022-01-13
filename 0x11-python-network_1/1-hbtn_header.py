#!/usr/bin/python3
'''print header'''

if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
