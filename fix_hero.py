heros_object=open('heros.txt')
fix_object=open('fix.txt','w')
try:
    heros_text=heros_object.readlines()
finally:
    heros_object.close()


for line in heros_text:
    line=line.strip()
    line="Dota:{}\r{{{{subobjtalent10|   |   }}}}\r{{{{subobjtalent15|    |    }}}}\r{{{{subobjtalent20|    |     }}}}\r{{{{subobjtalent25|     |     }}}}\r\r".format(line)
    fix_object.write(line)