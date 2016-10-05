# -*- coding:utf-8 -*-
# sundayliu
# 2016/10/05

import sys
import os
import urllib2

def download_file(url, filename):
    f = urllib2.urlopen(url)
    data = f.read()
    with open(filename, "wb") as code:
        code.write(data)
        
FONT_FORMAT = ['woff2', 'woff', 'otf']
FONT_TYPE = ['Thin', 'Light', 'Regular', 'Medium', 'Bold', 'Black']
#FONT_NAME = "NotoSansTC"
FONT_NAME = "NotoSansSC"
#FONT_URL_PREFIX = "http://fonts.gstatic.com/ea/notosanstc/v1/"
FONT_URL_PREFIX ="http://fonts.gstatic.com/ea/notosanssc/v1/"

# http://fonts.gstatic.com/ea/notosanstc/v1/NotoSansTC-Thin.woff2
def download_fonts():
    for type_name in FONT_TYPE:
        for format_name in FONT_FORMAT:
            filename = "%s-%s.%s" % (FONT_NAME, type_name, format_name)
            url = "%s%s" % (FONT_URL_PREFIX, filename)
            print("[+] download %s ..." % filename)
            print("[+] url:%s" % url)
            download_file(url, filename)
if __name__ == "__main__":
    print("[+] download fonts ...")
    download_fonts()
    print("[+] end .")