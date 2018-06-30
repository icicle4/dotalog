import jieba

jieba.load_userdict('dir.txt')

fix_object=open('fix.txt')
abilitys_object=open('abilitys.txt')

transto_text=open('fix2.txt','w')


def txttohtml(the_txt):
    alist=jieba.cut(the_txt)
    emptylist=[]
    for a in alist:
        if a in abilitys_list:
            a="{{{{A|{}}}}}".format(a)
        emptylist.append(a)
    emptylist="".join(emptylist)
    emptylist='{}\r'.format(emptylist)
    transto_text.write(emptylist)

abilitys_list,fix_text=[],[]

try:
    fix_text_e=fix_object.readlines()
finally:
    fix_object.close()
try:
    abilitys_list_e=abilitys_object.readlines()
finally:
    abilitys_object.close()

for line in abilitys_list_e:
    line=line.strip()
    abilitys_list.append(line)

for line in fix_text_e:
    line=line.strip()
    fix_text.append(line)

for aa in fix_text:
    txttohtml(aa)