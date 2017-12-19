from IGinformation import IGinformation

class likecrawl(IGinformation):
    def __init__(self,word):

        super().__init__(word)
        self.likeby_url_path='graphql/query/?query_id=17864450716183058&variables='
        #self.Pcode
        #shortcode is a list
        self.Plist={}
        self.LikeBylist=list()
        self.url_likeby=''

    def getURL(self):
        ##"{"shortcode":"BXsT0EhFOsp","first":10,"after":""}"
        Purl=list()
        for PID in self.getPcodeList():
            #list中組合出網址
            
            variable = '{"shortcode":"' + PID + '","first":999}'

            TrueUrl = self.url_host + self.likeby_url_path + variable
            
            Purl.append(TrueUrl)
            #Purl是網址的list
        return Purl
        #we get the plist include all picture_likeby url


    def Crawling_Likeby(self):
        #self.Plist=self.getURL()
        #print(self.Plist)
        try:
            self.Plist = self.getURL()
            #得到的是一個list

            for url in self.Plist[0:100]:
                request = urllib.request.Request(url,headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    })
                response = urllib.request.urlopen(request)
                content = response.read().decode('utf-8','ignore')
                j = json.loads(content)
                print('go to next L2')
                if j['status'] == 'ok' and j['data']['shortcode_media']:
                    items = j['data']['shortcode_media']['edge_liked_by']['edges']
                    for i in items:
                        #print('go to next L3')
                        #self.LikeBylist.append({'username':i['node']['username']})
                        self.LikeBylist.append(i['node']['username'])
                time.sleep(2)
            #print(self.LikeBylist)
            #return self.LikeBylist

        except Exception as e:
            self.wish_list = []
            self.wish_list.append(e)
            print('Crawling_Likeby_Exception ',e)

    def Top10(self):
        self.Crawling_Likeby()
        #print(self.LikeBylist)

        hash = dict()
        for item in self.LikeBylist: 
            if item in hash:
                hash[item] += 1
            else:
                hash[item] = 1

        LikeBydict=hash
        LikeBydict=sorted(LikeBydict.items(),key=lambda item:item[1])
        #result=LikeBydict[0:100]
        print(LikeBydict[-1:-10:-1])

if __name__ == '__main__':
    my_like=likecrawl('instagram')#輸入欲搜尋的id
    my_like.Top10()

