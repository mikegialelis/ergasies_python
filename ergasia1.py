a=raw_input("dwse protash\n")
a=list(a)
for k in enumerate(a):
    for i, j in enumerate(a):
        try:
            if (j  == "!") and (a[i+1]!=None) and (a[i+1]!="!") :
                del a[i]
        except:
            pass
a="".join(a)
print a
