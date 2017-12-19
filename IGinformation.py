import json
import datetime
import sys,os
import urllib.request,urllib.parse

class IGinformation:
    def __init__(self,word):
        self.word=word
        self.url_host='https://www.instagram.com/'
        self.url_path = self.word+'/media?max_id='
        self.max_id=''
        self.IGcontent=''
        self.Pcode=list()
        self.list=list()
        self.wish_list=list()
        #self.counter=0
        self.start()
    def start(self):
        #self.counter+=20
        try:
            url = self.url_host+self.url_path+self.max_id
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8','ignore')
            j=json.loads(content)
            if j['status']=='ok':
                items=j['items']
                for i in items:
#                    self.wish_list.append({'text':i['caption']['text'],'time':i['created_time']})
                    self.max_id=i['id']
#                    print(i['caption']['text'])
                    
                    self.wish_list.append({'url':i['images']['standard_resolution']['url'],'time':i['created_time']})
                    if i['caption']!=None:
                        self.IGcontent=self.IGcontent+str(i['caption']['text'])
                    if i['code']!=None:
                        self.Pcode.append(i['code'])
 #               print(j['more_available'])
                #if self.counter<40:
                if j['more_available']==True:
                    print('go to next')
                    self.start()

        except Exception as e:
            self.wish_list=[]
            self.wish_list.append(e)
            print('Information_Exception ',e)

    def get_content_result(self):
        return self.IGcontent
    def get_PcodeList(self):
        return self.Pcode
    def get_download(self):
        return self.wish_list
