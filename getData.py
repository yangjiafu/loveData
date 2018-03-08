#encoding:utf-8
import os
import sys
import re
from bs4 import BeautifulSoup
import requests

reload(sys)
sys.setdefaultencoding('utf-8')


def get_list_pinfo(src,headers,info_f,error_f,l,k):
    print '开始第',l,'页,第',k,'条的数据爬取'
    src = 'http://www.80s.so%s'%(src)
    try:
        html = requests.get(src, headers=headers, verify=False, timeout=60)
        html = BeautifulSoup(html.text, 'html.parser')
        if len(html.find_all(id='mainbody')) != 0:
            try:
                name = html.find_all('li',class_='actived')[0].string
                try:
                    other_name = html.find_all(id='movie_aka')[0].string
                except:
                    other_name =''
                cover = html.find_all(id='poster')[0].find_all('img')[0].attrs['src']
                m_basic_Info = html.find_all('p',class_='movie-info')[0].text.replace('\n',',')
                # print re.findall("类型(.*|\n*)*地区",m_basic_Info)
                try:
                    m_classfy = re.findall(u"类型：,(.+)地区", m_basic_Info)[0].replace(',,','')
                except:
                    m_classfy = ''
                try:
                    m_area = re.findall(u"地区：,,(.+)语言", m_basic_Info)[0].replace(',,',',').replace(' ','')
                except:
                    m_area = ''
                try:
                    m_languge = re.findall(u"语言：,,(.+)片长", m_basic_Info)[0].replace(',,', ',').replace(' ', '')
                    m_duration = re.findall(u"片长：(.+)上映日期", m_basic_Info)[0].replace(',', '').replace(' ', '')
                    m_releacetime = re.findall(u"上映日期：(.+)资源更新", m_basic_Info)[0].replace(',', '').replace(' ', '')
                except:
                    try:
                        m_languge = re.findall(u"语言：,,(.+)上映日期", m_basic_Info)[0].replace(',,', ',').replace(' ', '')
                    except:
                        m_languge = ''
                    m_duration = ''
                    m_releacetime = ''
                try:
                    m_score = re.findall(u"豆瓣评分：(.+)分", m_basic_Info)[0].replace(',','').replace(' ','')
                except:
                    m_score = ''
                try:
                    m_actor_director = html.find_all('p',class_='movie-info')[1].text.replace('\n',',')
                    m_actor = re.findall(u",演员：(.+)导演", m_actor_director)[0].replace(',','').replace(' ','').replace('/',',')
                    m_director = re.findall(u",导演：(.+)", m_actor_director)[0].replace(',,','')
                except:
                    try:
                        m_actor=html.find_all('p',class_='movie-info')[1].a.string
                    except:
                        m_actor = ''
                    m_director=''
                m_Info = html.find_all(id='movie_description')[0].string.replace('\n','')
                m_links_info = html.find_all(class_='td-dl-links')
                m_linksAll = ''
                lk= 0
                for links in m_links_info:
                    lk += 1
                    try:
                        m_linksAll += '%s<<%s<<%s<<%s[&' % (links.find_all('span')[0].string, links.find_all('span')[2].string, links.a.get('href'),links.a.get('href_original'))
                    except:
                        m_linksAll += '%s<<%s<<%s<<%s[&' % (' ', ' ', links.a.get('href'), links.a.get('href_original'))


                allInfo = '%s<>%s<>%s<>%s<>%s<>%s<>%s<>%s<>%s<>%s<>%s<>%s<>%s[]\n'\
                          %(name,other_name,cover,m_classfy,m_area,m_languge,m_duration,m_releacetime,m_score,m_actor,m_director,m_Info,m_linksAll)
                info_f.write(allInfo)
                print '第',l,'页,第',k,'条的数据爬取结束'
            except:
                error_f.write('第%d页，第%d条的数据出错--><>%s[]\n'%(l,k,src))
                print '第', l, '页,第', k, '条的数据爬取出错了了了了了'
        else:
            print '页面错误'
            pass
    except:
        pass

def get_list_pages(srcp,headers,info_f,error_f,l):
    html = requests.get(srcp, headers=headers, verify=False, timeout=60)
    html = BeautifulSoup(html.text,'html.parser')
    # html.encoding('utf-8')
    k= 0
    link_p = html.find_all('div',class_='list_mov_title')
    for i in link_p:
        k+=1
        print k
        get_list_pinfo(i.find_all('a')[0].attrs['href'],headers,info_f,error_f,l,k)
    # get_list_pinfo('','')




def get_list(src, headers):
    print u'打开文件...'
    info_f = open('J:\\loveWhatch\\newBuildData\\data.txt','a')
    error_f =open('J:\\loveWhatch\\newBuildData\\error.txt','a')
    l = 457
    for p in range(457,458):
        l+=1
        # print index
        get_list_pages('%s%s'%(src,p),headers,info_f,error_f,l)
    # pass
    print u'关闭文件。。。'
    info_f.close()
    error_f.close()


if __name__ =='__main__':
    src = 'http://www.80s.so/html/movie/1-0-0-0-0-0?page='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    print u'开始执行文件...'
    get_list(src,headers)
    print u'执行完毕...'