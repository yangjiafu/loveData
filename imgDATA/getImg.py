# encoding:utf-8
import httplib, urllib2


def read_img():
    pass


def down_img():
    pass


if __name__ == '__main__':
    # url = '//t.dyxz.la/upload/img/201705/poster_20170519_2290066_b.jpg'
    url = 'http://t.dyxz.la/upload/img/201705/poster_20170519_2290066_b.jpg'
    httplib.HTTPConnection.debuglevel = 1
    request = urllib2.Request(url)
    request.add_header('Accept', '*/*')
    request.add_header('Referer', 'https://www.80s.tw/movie/19365')
    request.add_header('Accept-Language', 'zh-cn')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
    binary_data = urllib2.urlopen(request).read()
    temp_file = open('I:\loveWhatch\loveData\imgDATA\down.jpg', 'wb')
    temp_file.write(binary_data)
    temp_file.close()
