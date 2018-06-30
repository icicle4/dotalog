# encoding=utf-8
from item_key_word import item_key_word
import jieba

jieba.load_userdict('dir.txt')

log_object = open('itemlog.txt')
items_object = open('items.txt')
transto_text = open('last_log_text.txt', 'w')

try:
    log_text = log_object.readlines()
finally:
    log_object.close()

try:
    items_text = items_object.readlines()
finally:
    items_object.close()
log_text_e, items_text_e = [aline.strip() for aline in log_text if aline], [aline.strip() for aline in items_text]

jeba_parsered_text = list(map(jieba.cut, log_text_e))

item_list = []

d = {}
d['newitem'] = '否'
d['item'] = ''

for text in jeba_parsered_text:
    k = 0
    d['shop'] = ''
    d['cost'] = ''
    d['recipe cost'] = ''
    d['craft'] = ''
    d['effect'] = ''
    theatom = ''.join(text)
    if theatom in items_text_e:
        item_properity_lines = []
        for line in item_list:
            emptyline = [e for e in line]
            theline = ''.join(emptyline)
            it_key_word = [item_key_word.get(atom) for atom in emptyline]
            k = 0
            for it in it_key_word:
                if it:
                    k = 1
                    d[it] = "\r|{}={}".format(it, theline)
            if k == 0:
                item_properity_lines.append(theline)
            if len(item_properity_lines) > 1:
                d['effect'] = '\r*'.join(item_properity_lines)
            elif len(item_properity_lines) == 1:
                d['effect'] = item_properity_lines[-1]
        if d['effect']:
            d['effect'] = "\r|effect={}".format(d['effect'])
        if d['item']:
            s = "{{{{Changelogdefineitem\r|newitem={}{item}{shop}{cost}{recipecost}{craft}{effect}\r}}}}\r".format(
                d['newitem'], item=d['item'], shop=d['shop'], cost=d['cost'], recipecost=d['recipe cost'],
                craft=d['craft'], effect=d['effect'])
            transto_text.write(s)
        d['item'] = "\r|item={}".format(theatom)
        item_list = []
    else:
        item_list.append(text)

transto_text.close()
