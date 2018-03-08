#encoding:utf-8
import time
import sys
reload(sys)
import MySQLdb

sys.setdefaultencoding('utf-8')

start = time.clock()
print '开始：',start
conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='lovewatch',charset='utf8')
# 创建请求
cursor = conn.cursor()

er = open('I:\\loveWhatch\\creatDB\\error.txt','a')
f = open('I:\\loveWhatch\\creatDB\\data.txt','r')
all_utf8 = f.read()
files = unicode(all_utf8, 'utf-8')
k = 0
for line in files.split('[]'):
    # if 50 < k < 500:
    k += 1
    ls = line.split('<>')
    if len(ls) < 11:
        er.write(line)
        continue
    name = ls[0].replace('\n','').replace('\t','')
    othername = ls[1]
    cover = ls[2]
    classify = ls[3]
    language = ls[5]
    area = ls[4]
    releasetime = ls[6]
    duration = ls[7]
    score = ls[8]
    actor = ls[9]
    try:
        director = ls[10]
    except:
        director = ''
    try:
        synopsis = ls[11].replace('"','“')
    except:
        synopsis = ''
    try:
        linkconment = ls[12]
    except:
        continue
    li = 0
    linkinfo = []
    linkinfo = linkconment.split('[&')
    for i in linkinfo:
        li+=1
        # print i
        if 'http://pan.baidu.com/s' in i:
            linkinfo.remove(i)
            # print li
        if len(i) < 1:
            linkinfo.remove(i)
    linkinfos = '[&'.join(linkinfo)
    sql ='insert into tb_movies(m_name,m_othername,m_cover,m_actor,m_director,m_classify,m_area,m_language,m_releasetime,m_duration,m_score,m_linkinfo,m_synopsis)VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%\
         (name,othername,cover,actor,director,classify,area,language,releasetime,duration,score,linkinfos,synopsis)
    sql = sql.encode("utf-8")
    # print sql
    cursor.execute("SET NAMES utf8")
    conn.commit()
    # cursor.execute(sql)
    # conn.commit()
    # print k
    try:
        cursor.execute(sql)
        conn.commit()
        # if k % 200 == 0:
        #     print '第%s执行完毕'%k
        if k>= 200:
            break
    except:
        print k,'此条数据出错'
        print line
        conn.rollback()
        er.write(line)

conn.close()
f.close()
er.close()
end = time.clock()
print 'runnig time: %s scends' % (end-start)