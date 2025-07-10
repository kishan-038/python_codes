with open("data2.txt","w") as f1:
    f1.write("hello world")
    f1.close()
with open("data2.txt","a") as fa:
    st=input('enter to append : ')
    fa.write(st)
    fa.close()
with open("data2.txt","r") as fr:
    print(fr.read())