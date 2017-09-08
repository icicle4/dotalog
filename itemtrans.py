# encoding=utf-8
from item_key_word import item_key_word
from collections import namedtuple
import jieba

jieba.load_userdict('dir.txt')


log_object=open('itemlog.txt')
items_object=open('items.txt')
transto_text=open('last_log_text.txt','w')

try:
    log_text = log_object.readlines()
finally:
    log_object.close()

try:
    items_text=items_object.readlines()
finally:
    items_object.close()
log_text_e,items_text_e=[],[]

for line in log_text:
    aline=line.strip()
    if aline:
        log_text_e.append(aline)

print(log_text_e[0])
for line in items_text:
    aline=line.strip()
    items_text_e.append(aline)


mid_text=list(map(jieba.cut,log_text_e))

item_list=[]

d={}
d['newitem']='否' 
d['item']=''

for text in mid_text:
    k=0
    
    d['shop']=''
    d['cost']=''
    d['recipe cost']=''
    d['craft']=''
    d['effect']=''
    emptylist=[]

    for t in text:
        emptylist.append(t)
    theatom=''.join(emptylist)
    #print(theatom)
    if theatom in items_text_e:
        emptylist1=[]
        emptylist2=[]
        for line in item_list:
            emptyline=[]
            it_key_word=[]
            for e in line:
                emptyline.append(e)
            theline=''.join(emptyline)
            for atom in emptyline:
                it_key_word.append(item_key_word.get(atom))
                #print(atom)
            #print(it_key_word)
            
            #print(theline)
            k=0
            for it in it_key_word:
                if it:
                    k=1
                    d[it]="\r|{}={}".format(it,theline)
                    #print(d[it])
            if k==0:
                emptylist2.append(theline)
            if len(emptylist2)>1:
                d['effect']='\r*'.join(emptylist2)
            elif len(emptylist2)==1:
                d['effect']=emptylist2[-1]
        #s="{{{{Changelogdefineitem\r|newitem={}\r|item={}\r|shop={}\r|cost={}\r|recipe cost={}\r|craft={}\r|effect={}\r}}}}\r".format(d['newitem'],d['last item'],d['shop'],d['cost'],d['recipe cost'],d['craft'],d['effect'])
        #transto_text.write(s)
        item_list=[]
        if d['effect']:
            d['effect']="\r|effect={}".format(d['effect'])
        #s="{{{{Changelogdefineitem\r|newitem={}\r|item={}\r|shop={}\r|cost={}\r|recipe cost={}\r|craft={}\r|effect={}\r}}}}\r".format(d['newitem'],d['item'],d['shop'],d['cost'],d['recipe cost'],d['craft'],d['effect'])
        if d['item']:
            s="{{{{Changelogdefineitem\r|newitem={}{item}{shop}{cost}{recipecost}{craft}{effect}\r}}}}\r".format(d['newitem'],item=d['item'],shop=d['shop'],cost=d['cost'],recipecost=d['recipe cost'],craft=d['craft'],effect=d['effect'])
            transto_text.write(s)
        #d['item']=theatom
        d['item']="\r|item={}".format(theatom)
        #print(d['item'])
        #print(d)
    else:
        item_list.append(emptylist)

transto_text.close()