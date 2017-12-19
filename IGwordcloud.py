# encoding=utf-8
from IGinformation import IGinformation
import jieba
import datetime
import sys,os
import matplotlib.pyplot as plt
from wordcloud import WordCloud

if __name__ == '__main__':
    print("Input your ID: ")
    UserID=input()
    Word=IGinformation(UserID)
    allword=Word.get_content_result()

    seg_list=jieba.cut(allword,cut_all=False)
    wl_space_split=" ".join(seg_list)
    my_wordcloud=WordCloud(font_path="setofont.ttf",background_color="white",width=640, height=480, margin=2).generate(wl_space_split)
#支援TTF/OTF
    plt.title(UserID)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.savefig(str(UserID)+'.png',dpi=1000) 
'''    hash={}
    for word in seg_list:
        if word in hash:
            hash[word]+=1
        else:
            hash[word]=1
    json.dump(hash,open("count.json","w"))'''
