# encoding=utf-8

from ability_key_word import ability_key_word
from hero_key_word import hero_key_word

import jieba


def txttohtml(the_text):
    emptylist,ability_list,hero_list,ab_key_word,he_key_word=[],[],[],[],[]
    d={}
    mid_text=jieba.cut(the_text)
    for t in mid_text:
        emptylist.append(t)
    T,sp=0,0
    for t in emptylist:
        if t=='天赋':
            T=1
        if t=='神杖':
            sp=1
        if t in abilitys_text_e:
            ability_list.append(t)
        if t in heros_text_e:
            hero_list.append(t)
    if T==1 and len(hero_list):
        for hero in hero_list:
            d['hero']=hero
            if hero==the_text:
                return
            for t in emptylist:
                he_key_word.append(hero_key_word.get(t))
            key=0
            for he in he_key_word:
                if he:
                    key=1;
                    d[he]=the_text
                    s=['hero',d['hero'],he,d[he]]
                    #s="{{{{Changelogdefinehero\r|newhero=否\r|hero={}\r|{}={}\r}}}}\r".format(d['hero'],he,d[he])
                    return s
            if  key==0:
                he='other'
                d[he]=the_text
                s=['hero',d['hero'],'other',the_text]
                #s="{{{{Changelogdefinehero\r|newhero=否\r|hero={}\r|{}={}\r}}}}\r".format(d['hero'],he,d[he])
                return s



    elif  sp==1 or len(ability_list):
        for ability in ability_list:
            d['ability']=ability
            for t in emptylist:
                ab_key_word.append(ability_key_word.get(t))
            key=0
            for ab in ab_key_word:
                if ab:
                    d[ab]=the_text
                    key=1
                    s=['ability',d['ability'],ab,d[ab]]
                    #s="{{{{ Changelogdefineability\r|ability={}\r|{}={}\r}}}}\r".format(d['ability'],ab,d[ab])
                    return s
            if key==0:
                ab='other effect'
                d[ab]=the_text
                s=['ability',d['ability'],ab,d[ab]]
                #s="{{{{ Changelogdefineability\r|ability={}\r|{}=*{}\r}}}}\r".format(d['ability'],ab,d[ab])
                return s

    elif len(hero_list):
        for hero in hero_list:
            d['hero']=hero
            if hero==the_text:
                return
            for t in emptylist:
                he_key_word.append(hero_key_word.get(t))
            key=0
            for he in he_key_word:
                if he:
                    key=1;
                    d[he]=the_text
                    s=['hero',d['hero'],he,d[he]]
                    #s="{{{{Changelogdefinehero\r|newhero=否\r|hero={}\r|{}={}\r}}}}\r".format(d['hero'],he,d[he])
                    return s
            if  key==0:
                he='other'
                d[he]=the_text
                s=['hero',d['hero'],'other',the_text]
                #s="{{{{Changelogdefinehero\r|newhero=否\r|hero={}\r|{}={}\r}}}}\r".format(d['hero'],he,d[he])
                return s


jieba.load_userdict('dir.txt')


log_object=open('log.txt')
abilitys_object=open('abilitys.txt')
items_object=open('items.txt')
heros_object=open('heros.txt')
transto_text=open('last_log_text.txt','w')



try:
    log_text = log_object.readlines()
finally:
    log_object.close()

try:
    abilitys_text=abilitys_object.readlines()
finally:
    abilitys_object.close()

try:
    heros_text=heros_object.readlines()
finally:
    heros_object.close()

try:
    items_text=items_object.readlines()
finally:
    items_object.close()
log_text_e,abilitys_text_e,heros_text_e,items_text_e=[],[],[],[]

for line in log_text:
    line=line.strip()
    log_text_e.append(line)

#print(log_text_e)

for line in abilitys_text:
    line=line.strip()
    abilitys_text_e.append(line)

#print(abilitys_text_e)
for line in heros_text:
    line=line.strip()
    heros_text_e.append(line)

#print(heros_text_e)
#for line in items_text:
 #   line=line.strip()
  #  items_text_e.append(e)
final_log_text=[]
final_text=list(map(txttohtml,log_text_e))
for text in final_text:
    if text is not None:
        #final_log_text.writeline(text)
        final_log_text.append(text)

print(final_log_text)

nowlog0=final_log_text[0][0]
nowlog1=final_log_text[0][1]
log_list=[]
d={
    'ability':'',
    'cooldown':'',
    'mana cost':'',
    'septer':'',
    'other effect':'',
    'hero':'',
    'strength':'',
    'intelligence':'',
    'agility':'',
    'strength growth':'',
    'intelligence growth':'',
    'agility growth':'',
    'attack damage':'',
    'health regen':'',
    'mana regen':'',
    'armor':'',
    'magic resistance':'',
    'movement speed':'',
    'attack range':'',
    'attack point':'',
    'attack backswing':'',
    'base attack time':'',
    'missile speed':'',
    'sight range day':'',
    'sight range night':'',
    'turn rate':'',
    'collision size':'',
    'legs':'',
    'other':'',
    'talent':''
}

final_log_text_length=len(final_log_text)

for i,log in enumerate(final_log_text):

    if log[1]!=nowlog1 and i!=(final_log_text_length-1):#不相同，不是最后一个 正常处理
        now_key=log_list[0][2]
        emptylist=[]
        l=len(log_list)
        for j,a_log in enumerate(log_list):
            if a_log[2]!=now_key and j!=(l-1):#不相同 不是最后一个
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                emptylist=[]
                emptylist.append(a_log[3])

            elif a_log[2]==now_key and j==(l-1): #相同 最后一个 加进去处理
                emptylist.append(a_log[3])
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                emptylist=[]

            elif a_log[2]!=now_key and j==(l-1): #不相同 最后一个 处理两次
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                d[now_key]='\r|{}={}'.format(now_key,a_log[3])

            elif a_log[2]==now_key and j!=(l-1):
                emptylist.append(a_log[3])
        d[nowlog0]='\r|{}={}'.format(nowlog0,nowlog1)
        if d['ability']:
            s="{{{{Changelogdefineability{ability}{cooldown}{manacost}{septer}{othereffect}\r}}}}\r".format(ability=d['ability'],cooldown=d['cooldown'],manacost=d['mana cost'],septer=d['septer'],othereffect=d['other effect'])
            #print(s)
            transto_text.write(s)
        if d['hero']:
            s="{{{{Changelogdefinehero\r|newhero='否'{hero}{strength}{intelligence}{agility}{strengthgrowth}{intelligencegrowth}{agilitygrowth}{attackdamage}{healthregen}{manaregen}{armor}{magicresistance}{movementspeed}{attackrange}{attackpoint}{attackbackswing}{baseattacktime}{missilespeed}{sightrangeday}{sightrangenight}{turnrate}{collisionsize}{legs}{other}{talent}\r}}}}\r".format(hero=d['hero'],strength=d['strength'],intelligence=d['intelligence'],agility=d['agility'],strengthgrowth=d['strength growth'],intelligencegrowth=d['intelligence growth'],agilitygrowth=d['agility growth'],attackdamage=d['attack damage'],healthregen=d['health regen'],manaregen=d['mana regen'],armor=d['armor'],magicresistance=d['magic resistance'],movementspeed=d['movement speed'],attackrange=d['attack range'],attackpoint=d['attack point'],attackbackswing=d['attack backswing'],baseattacktime=d['base attack time'],missilespeed=d['missile speed'],sightrangeday=d['sight range day'],sightrangenight=d['sight range night'],turnrate=d['turn rate'],collisionsize=d['collision size'],legs=d['legs'],other=d['other'],talent=d['talent'])
            transto_text.write(s)
        nowlog1=log[1]
        nowlog0=log[0]
        d={
            'ability':'',
            'cooldown':'',
            'mana cost':'',
            'septer':'',
            'other effect':'',
            'hero':'',
            'strength':'',
            'intelligence':'',
            'agility':'',
            'strength growth':'',
            'intelligence growth':'',
            'agility growth':'',
            'attack damage':'',
            'health regen':'',
            'mana regen':'',
            'armor':'',
            'magic resistance':'',
            'movement speed':'',
            'attack range':'',
            'attack point':'',
            'attack backswing':'',
            'base attack time':'',
            'missile speed':'',
            'sight range day':'',
            'sight range night':'',
            'turn rate':'',
            'collision size':'',
            'legs':'',
            'other':'',
            'talent':''
            }
        log_list=[]
        log_list.append(log)

    elif i==(final_log_text_length-1) and log[1]==nowlog1:#最后一个 相同 加进去后处理
        log_list.append(log)
        now_key=log_list[0][2]
        emptylist=[]
        l=len(log_list)
        for j,a_log in enumerate(log_list):
            if a_log[2]!=now_key and j!=(l-1):#不相同 不是最后一个
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                emptylist=[]
                emptylist.append(a_log[3])

            elif a_log[2]==now_key and j==(l-1): #相同 最后一个 加进去处理
                emptylist.append(a_log[3])
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                emptylist=[]

            elif a_log[2]!=now_key and j==(l-1): #不相同 最后一个 处理两次
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                d[now_key]='\r|{}={}'.format(now_key,a_log[3])

            elif a_log[2]==now_key and j!=(l-1):
                emptylist.append(a_log[3])
        d[nowlog0]='\r|{}={}'.format(nowlog0,nowlog1)


        if d['ability']:
            s="{{{{Changelogdefineability{ability}{cooldown}{manacost}{septer}{othereffect}\r}}}}\r".format(ability=d['ability'],cooldown=d['cooldown'],manacost=d['mana cost'],septer=d['septer'],othereffect=d['other effect'])
            transto_text.write(s)
        if d['hero']:
            s="{{{{Changelogdefinehero\r|newhero='否'{hero}{strength}{intelligence}{agility}{strengthgrowth}{intelligencegrowth}{agilitygrowth}{attackdamage}{healthregen}{manaregen}{armor}{magicresistance}{movementspeed}{attackrange}{attackpoint}{attackbackswing}{baseattacktime}{missilespeed}{sightrangeday}{sightrangenight}{turnrate}{collisionsize}{legs}{other}{talent}\r}}}}\r".format(hero=d['hero'],strength=d['strength'],intelligence=d['intelligence'],agility=d['agility'],strengthgrowth=d['strength growth'],intelligencegrowth=d['intelligence growth'],agilitygrowth=d['agility growth'],attackdamage=d['attack damage'],healthregen=d['health regen'],manaregen=d['mana regen'],armor=d['armor'],magicresistance=d['magic resistance'],movementspeed=d['movement speed'],attackrange=d['attack range'],attackpoint=d['attack point'],attackbackswing=d['attack backswing'],baseattacktime=d['base attack time'],missilespeed=d['missile speed'],sightrangeday=d['sight range day'],sightrangenight=d['sight range night'],turnrate=d['turn rate'],collisionsize=d['collision size'],legs=d['legs'],other=d['other'],talent=d['talent'])
            transto_text.write(s)


    elif i==(final_log_text_length-1) and log[1]==nowlog1:#最后一个 相同 加进去后处理
        log_list.append(log)
        now_key=log_list[0][2]
        emptylist=[]
        l=len(log_list)
        for j,a_log in enumerate(log_list):
            if a_log[2]!=now_key and j!=(l-1):#不相同 不是最后一个
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                emptylist=[]
                emptylist.append(a_log[3])

            elif a_log[2]==now_key and j==(l-1): #相同 最后一个 加进去处理
                emptylist.append(a_log[3])
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                emptylist=[]

            elif a_log[2]!=now_key and j==(l-1): #不相同 最后一个 处理两次
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                d[now_key]='\r|{}={}'.format(now_key,a_log[3])

            elif a_log[2]==now_key and j!=(l-1):
                emptylist.append(a_log[3])
        d[nowlog0]='\r|{}={}'.format(nowlog0,nowlog1)


        if d['ability']:
            s="{{{{Changelogdefineability{ability}{cooldown}{manacost}{septer}{othereffect}\r}}}}\r".format(ability=d['ability'],cooldown=d['cooldown'],manacost=d['mana cost'],septer=d['septer'],othereffect=d['other effect'])
            transto_text.write(s)
        if d['hero']:
            s="{{{{Changelogdefinehero\r|newhero='否'{hero}{strength}{intelligence}{agility}{strengthgrowth}{intelligencegrowth}{agilitygrowth}{attackdamage}{healthregen}{manaregen}{armor}{magicresistance}{movementspeed}{attackrange}{attackpoint}{attackbackswing}{baseattacktime}{missilespeed}{sightrangeday}{sightrangenight}{turnrate}{collisionsize}{legs}{other}{talent}\r}}}}\r".format(hero=d['hero'],strength=d['strength'],intelligence=d['intelligence'],agility=d['agility'],strengthgrowth=d['strength growth'],intelligencegrowth=d['intelligence growth'],agilitygrowth=d['agility growth'],attackdamage=d['attack damage'],healthregen=d['health regen'],manaregen=d['mana regen'],armor=d['armor'],magicresistance=d['magic resistance'],movementspeed=d['movement speed'],attackrange=d['attack range'],attackpoint=d['attack point'],attackbackswing=d['attack backswing'],baseattacktime=d['base attack time'],missilespeed=d['missile speed'],sightrangeday=d['sight range day'],sightrangenight=d['sight range night'],turnrate=d['turn rate'],collisionsize=d['collision size'],legs=d['legs'],other=d['other'],talent=d['talent'])
            transto_text.write(s)

    elif i==(final_log_text_length-1) and log[1]!=nowlog1:#最后一个 不相同 处理两次
        now_key=log_list[0][2]
        emptylist=[]
        l=len(log_list)
        for j,a_log in enumerate(log_list):
            if a_log[2]!=now_key and j!=(l-1):#不相同 不是最后一个
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                emptylist=[]
                emptylist.append(a_log[3])

            elif a_log[2]==now_key and j==(l-1): #相同 最后一个 加进去处理
                emptylist.append(a_log[3])
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                emptylist=[]

            elif a_log[2]!=now_key and j==(l-1): #不相同 最后一个 处理两次
                tian=''
                if len(emptylist)>1:
                    tian='\r*'.join(emptylist)
                elif len(emptylist)==1:
                    tian=emptylist[-1]
                d[now_key]='\r|{}={}'.format(now_key,tian)
                now_key=a_log[2]
                d[now_key]='\r|{}={}'.format(now_key,a_log[3])

            elif a_log[2]==now_key and j!=(l-1):
                emptylist.append(a_log[3])
        d[nowlog0]='\r|{}={}'.format(nowlog0,nowlog1)
        if d['ability']:
            s="{{{{Changelogdefineability{ability}{cooldown}{manacost}{septer}{othereffect}\r}}}}\r".format(ability=d['ability'],cooldown=d['cooldown'],manacost=d['mana cost'],septer=d['septer'],othereffect=d['other effect'])
            #print(s)
            transto_text.write(s)
        if d['hero']:
            s="{{{{Changelogdefinehero\r|newhero='否'{hero}{strength}{intelligence}{agility}{strengthgrowth}{intelligencegrowth}{agilitygrowth}{attackdamage}{healthregen}{manaregen}{armor}{magicresistance}{movementspeed}{attackrange}{attackpoint}{attackbackswing}{baseattacktime}{missilespeed}{sightrangeday}{sightrangenight}{turnrate}{collisionsize}{legs}{other}{talent}\r}}}}\r".format(hero=d['hero'],strength=d['strength'],intelligence=d['intelligence'],agility=d['agility'],strengthgrowth=d['strength growth'],intelligencegrowth=d['intelligence growth'],agilitygrowth=d['agility growth'],attackdamage=d['attack damage'],healthregen=d['health regen'],manaregen=d['mana regen'],armor=d['armor'],magicresistance=d['magic resistance'],movementspeed=d['movement speed'],attackrange=d['attack range'],attackpoint=d['attack point'],attackbackswing=d['attack backswing'],baseattacktime=d['base attack time'],missilespeed=d['missile speed'],sightrangeday=d['sight range day'],sightrangenight=d['sight range night'],turnrate=d['turn rate'],collisionsize=d['collision size'],legs=d['legs'],other=d['other'],talent=d['talent'])
            transto_text.write(s)
        nowlog1=log[1]
        nowlog0=log[0]
        d={
            'ability':'',
            'cooldown':'',
            'mana cost':'',
            'septer':'',
            'other effect':'',
            'hero':'',
            'strength':'',
            'intelligence':'',
            'agility':'',
            'strength growth':'',
            'intelligence growth':'',
            'agility growth':'',
            'attack damage':'',
            'health regen':'',
            'mana regen':'',
            'armor':'',
            'magic resistance':'',
            'movement speed':'',
            'attack range':'',
            'attack point':'',
            'attack backswing':'',
            'base attack time':'',
            'missile speed':'',
            'sight range day':'',
            'sight range night':'',
            'turn rate':'',
            'collision size':'',
            'legs':'',
            'other':'',
            'talent':''
            }
        log_list=[]
        log_list.append(log)
        now_key=log_list[0][2]
        d[now_key]='\r|{}={}'.format(now_key,log_list[0][3])
        d[nowlog0]='\r|{}={}'.format(nowlog0,nowlog1)

        if d['ability']:
            s="{{{{Changelogdefineability{ability}{cooldown}{manacost}{septer}{othereffect}\r}}}}\r".format(ability=d['ability'],cooldown=d['cooldown'],manacost=d['mana cost'],septer=d['septer'],othereffect=d['other effect'])
            transto_text.write(s)
        if d['hero']:
            s="{{{{Changelogdefinehero\r|newhero='否'{hero}{strength}{intelligence}{agility}{strengthgrowth}{intelligencegrowth}{agilitygrowth}{attackdamage}{healthregen}{manaregen}{armor}{magicresistance}{movementspeed}{attackrange}{attackpoint}{attackbackswing}{baseattacktime}{missilespeed}{sightrangeday}{sightrangenight}{turnrate}{collisionsize}{legs}{other}{talent}\r}}}}\r".format(hero=d['hero'],strength=d['strength'],intelligence=d['intelligence'],agility=d['agility'],strengthgrowth=d['strength growth'],intelligencegrowth=d['intelligence growth'],agilitygrowth=d['agility growth'],attackdamage=d['attack damage'],healthregen=d['health regen'],manaregen=d['mana regen'],armor=d['armor'],magicresistance=d['magic resistance'],movementspeed=d['movement speed'],attackrange=d['attack range'],attackpoint=d['attack point'],attackbackswing=d['attack backswing'],baseattacktime=d['base attack time'],missilespeed=d['missile speed'],sightrangeday=d['sight range day'],sightrangenight=d['sight range night'],turnrate=d['turn rate'],collisionsize=d['collision size'],legs=d['legs'],other=d['other'],talent=d['talent'])
            transto_text.write(s)


    elif i!=(final_log_text_length-1) and log[1]==nowlog1:
        log_list.append(log)
