#coding = ctf-8

import urllib
import requests,re,time

def getNews():
    try:
        api = "https://api.github.com/search/repositories?q=CVE-2020&sort=updated"
        req = requests.get(api).text
        cve_total_count=re.findall ('"total_count":*.{1,10}"incomplete_results"',req)[0][14:17]
        cve_description=re.findall ('"description":*.{1,200}"fork"',req)[0].replace("\",\"fork\"",'').replace("\"description\":\"",'')
        cve_url=re.findall ('"svn_url":*.{1,200}"homepage"',req)[0].replace("\",\"homepage\"",'').replace("\"svn_url\":\"",'')

        return cve_total_count,cve_description,cve_url

    except Exception as e:
        print (e,"github链接不通")

def sendNews():
    try:
        while True:
            api = "https://api.github.com/search/repositories?q=CVE-2020&sort=updated"
            #请求API
            req = requests.get(api).text
            #正则获取
            total_count=re.findall ('"total_count":*.{1,10}"incomplete_results"',req)[0][14:17]
            #监控时间间隔3分钟
            time.sleep(180)
            #推送正文内容
            msg = str(getNews())
            #推送标题
            text = r'有新的CVE送达！'
            #server酱请求url
            uri = 'https://sc.ftqq.com/KEY.send?text={}&desp={}'.format(
                   text, msg)

            if total_count!=getNews()[0]:
                send = requests.get(uri)
            else:
                pass


    except Exception as e:
        raise e


if __name__ == '__main__':
    sendNews()