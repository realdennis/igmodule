from IGinformation import IGinformation
import datetime
import sys,os
def download(self):
    os.mkdir(self.word)
    counter=0
    for i in self.wish_list:
        counter +=1
        url=i['url']
        time=i['time']
        file_name= self.word+'/'+datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H%M%S')+'.jpg'
        urllib.request.urlretrieve(url, file_name)
        print("now downloading "+str(counter)+ "pic")

    print("Finished!")
if __name__ == '__main__':
    print("Input your ID: ")
    UserID=input()
    file=IGinformation(UserID)
    download(file)


