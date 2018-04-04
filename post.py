# -*- coding:utf-8 -*-
import urllib.request
import urllib
import urllib.parse
import re,time,random,json
import sys 
from io import BytesIO
import gzip

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)



def getCookie():
    cookie1=''
    cookie2=''
	
	
    if(random.random()*2>1):
        print("cookie2")
        return cookie2
    else:
        print("cookie2")
        return cookie2

def reply(purl,ptext,fh):

    cookie=getCookie()
    url = purl
    postdata = {
        'message':ptext,
        'posttime':time.time(),
        'formhash':fh,
        'usesig':'1',
        'subject':'',
    }
    postdata = urllib.parse.urlencode(postdata).encode('utf-8')

    req = urllib.request.Request(url, headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':cookie,
        'DNT':'1',
        'Host':'www.miui.com',
        'Referer':'http://www.miui.com/gid-14.html',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        
    },data = postdata,
    )
    
    #oper = urllib.request.urlopen(req,timeout=3000)
    #print (oper)
    with urllib.request.urlopen(req,timeout=3000) as oper:
        data = oper.read()
    print(data.decode("utf-8"))
    m = re.findall('回复发布成功', data.decode('utf-8'))
    if m==[]:
        raise RuntimeError('postFail')

    #m = re.findall('<input type="hidden" name="formhash" value="(.*?)" />', data.decode('utf-8'))
    #print(m)
    #fh=m[0]+':'+m[0][::-1]
    #print(fh)

def gethtml(url):
    
    cookie=getCookie()
    req = urllib.request.Request(url, headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':cookie,
        'DNT':'1',
        'Host':'www.miui.com',
        'Referer':'http://www.miui.com/forum-705-1.html',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        
    },
    )
    #oper = urllib.request.urlopen(req,timeout=3000)
    with urllib.request.urlopen(req,timeout=3000) as oper:
        print(oper.getcode())
        data = oper.read()
        #buff = BytesIO(data)
        #data = gzip.GzipFile(fileobj=buff).read()
    #print(data)
    return(data.decode("utf-8").translate(non_bmp_map))

def main():

    

    listurl="http://www.miui.com/forum-705-"+str(int(random.random()*9)+2)+".html"
    print(listurl)
    listhtml=(gethtml(listurl))
    m = re.findall('<a href="thread-(\d{7,9})-\d-\d\.html" class="xi2">\d\d+</a>', listhtml)
    print(m)
    
    tid=m[int(random.random()*((len(m)-1)))]
    turl='http://www.miui.com/'+'thread-'+str(tid)+'-1-1.html'
    print(turl)
    thtml=(gethtml(turl))
    
    m = re.findall('<meta name="description" content="(.*?)"', thtml)
    print(m[0])

    ptext=gethtml('http://www.tuling123.com/openapi/api?key=0344bd2d86f33bda5654b941f757137a&info='+urllib.parse.quote(m[0]))
    ptext=json.loads(ptext)['text']
    print(ptext)
    #ptext=(urllib.request.urlopen(str('http://www.tuling123.com/openapi/api?key=0344bd2d86f33bda5654b941f757137a&info='+m[0]))).read().decode('utf-8')
    #print(ptext)

    m = re.findall('<input type="hidden" name="formhash" value="(.*?)" />', thtml)
    
    fh=m[0]+':'+m[0][::-1]
    print(fh)
    
    
    purl="http://www.miui.com/forum.php?mod=post&action=reply&fid=5&tid="+str(tid)+"&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"
    
    reply(purl,ptext,fh)
    
    




