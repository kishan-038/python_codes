def newfile():
    file=open('data.txt','r')
    opf=file.read()
    file.close()
    wc=0
    for i in opf.split():
        wc+=1
    return wc
print(newfile())
