parastash=raw_input("dwse parastash\n")
parastash=list(parastash)
op=0
cl=0
flag=True
for i in range(len(parastash)):
    if cl>op:
        flag=False
    if parastash[i]=="(":
      op+=1
    elif parastash[i]==")":
      cl+=1
if (op==cl) and (flag==True):
  print "true"
else:
  print "false"
