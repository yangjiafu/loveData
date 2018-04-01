# encoding:utf-8
import httplib, urllib2
import re


def read_img():
    f = open('I:\\loveWhatch\\creatDB\\data.txt', 'r')
    er = open('I:\\loveWhatch\\loveData\\imgDATA\\imgerr.txt', 'a')
    all_utf8 = f.read()
    files = unicode(all_utf8, 'utf-8')
    k = 0
    for line in files.split('[]'):
        # if 50 < k < 500:
        k += 1
        ls = line.split('<>')
        cover = ls[2]
        down_img(cover)
        if k > 5:
            break


def down_img(url):
    print url
    httplib.HTTPConnection.debuglevel = 1
    req = urllib2.Request(url.replace('https', 'http'))
    req.add_header('Accept', '*/*')
    req.add_header('Referer', 'https://www.80s.tw/movie/19365')
    req.add_header('Accept-Language', 'zh-cn')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
    binary_data = urllib2.urlopen(req).read()
    temp_file = open('I:\\loveWhatch\\loveData\\imgDATA\\imgFile\\'+re.findall(r'[^/*?]+$',url)[0], 'wb')
    temp_file.write(binary_data)
    temp_file.close()



if __name__ == '__main__':
    # url = '//t.dyxz.la/upload/img/201705/poster_20170519_2290066_b.jpg'
    # url = 'http://t.dyxz.la/upload/img/201705/poster_20170519_2290066_b.jpg'
    # httplib.HTTPConnection.debuglevel = 1
    # request = urllib2.Request(url)
    # request.add_header('Accept', '*/*')
    # request.add_header('Referer', 'https://www.80s.tw/')
    # request.add_header('Accept-Language', 'zh-cn')
    # request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
    # binary_data = urllib2.urlopen(request).read()
    # temp_file = open('I:\loveWhatch\loveData\imgDATA\down2.jpg', 'wb')
    # temp_file.write(binary_data)
    # temp_file.close()
    read_img()
