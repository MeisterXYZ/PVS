#goto-Befehl hintereinander und ohne leerzeichen eingeben
goto = "inc(0),dec(1),gotoZ(1,4),goto(0),inc(0),dec(2),gotoZ(2,8),goto(4),stop"

words = goto.replace("),",")),").split("),")   

for i in words:
    print i

i = len(words)
print i

out = "null"

while i > 0:
    out = "cons("+ words[i-1]+","+ out+")"
    i-=1

print out