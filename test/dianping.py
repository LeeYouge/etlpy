from etlpy.etlpy import *
from etlpy.params import RandomParam as r, ExpParam as exp,  Param, request_param
url = 'https://www.dianping.com'

cookie='''Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8,en;q=0.6
Cache-Control:max-age=0
Connection:keep-alive
Cookie:_hc.v=80a0369c-047c-ebd8-8b24-6b7203fff952.1483109843; __utma=1.669418081.1483109843.1488640538.1492677693.3; __utmz=1.1488640538.2.2.utmcsr=dianping.com|utmccn=(referral)|utmcmd=referral|utmcct=/search/keyword/2/0_%E5%9B%BD%E8%B4%B8; _lxsdk_cuid=15e5ba830aec8-08a516b6c56a2f-31627c01-13c680-15e5ba830aec8; _lxsdk=15e5ba830aec8-08a516b6c56a2f-31627c01-13c680-15e5ba830aec8; PHOENIX_ID=0a010725-15e65d95a1b-ef61ca9; cityid=3; share_ab=shop%3AA%3A3%7Cshopreviewlist%3AA%3A1%7Cmap%3AA%3A1; __mta=156143876.1504776309640.1507538981893.1507539061294.9; _lx_utm=utm_source%3Ddianping.com%26utm_medium%3Dreferral%26utm_content%3D%252Fsearch%252Fkeyword%252F2%252F0_%25E5%259B%25BD%25E8%25B4%25B8; s_ViewType=10; _lx_utm=utm_source%3Ddianping.com%26utm_medium%3Dreferral%26utm_content%3D%252Fsearch%252Fkeyword%252F2%252F0_%25E5%259B%25BD%25E8%25B4%25B8; JSESSIONID=BA60D084A3735A6D0F6A0C6B6A2C5AD4; aburl=1; cy=3; cye=hangzhou; _lxsdk_s=2e1185acd01e200ce0fad7a516ea%7C%7C4
Host:www.dianping.com
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'''
headers= para_to_dict(cookie,'\n',':')
r = request_param
r=r.merge('headers',headers)
t = task().create().url.set(url + '/search/category/3/75/g2878').get(r).pl().pyq('.nc-contain')[0].pyq(
    'a').list().html().cp('url:a').split('"')[1].get().xpath(
    '/html/body/div[6]/div[3]/div[1]/div[1]/div[2]/ul/li').list().html().tree() \
    .cp3('名称').xpath('//div[2]/div[1]/a[1]/h4')[0].text() \
    .cp3('点评').xpath('//div[2]/div[2]/a[1]/b')[0].text() \
    .cp3('平均').xpath('//div[2]/div[2]/a[2]/b')[0].text().num()[0] \
    .cp3('类型').xpath('//div[2]/div[3]/a[1]/span')[0].text() \
    .cp3('位置').xpath('//div[2]/div[3]/a[2]/span')[0].text() \
    .cp3('地址').xpath('//div[2]/div[3]/span')[0].text() \
    .cp3('效果').xpath('//div[2]/span/span[1]/b')[0].text() \
    .cp3('师资').xpath('//div[2]/span/span[2]/b')[0].text() \
    .cp3('环境').xpath('//div[2]/span/span[3]/b')[0].text() \
    .cp3('id').xpath('//@href')[0].cp('id:id0').split('/')[2].cp('id:html').let('html').get(r)\
    .cp3('phone').pyq('.phone')[0].text().let('html') .cp('_:详细').pyq(' .con li').text().rm('a id0 html').let('id 点评').num()[0].mv('点评:点评数').phone.split(' ')[1]



for r in t.take(3):
    print(r['名称'])
    print(r['详细'])

