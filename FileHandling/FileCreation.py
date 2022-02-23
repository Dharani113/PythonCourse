f=open("dharani.txt","w+")
p=["this is delhi\n","this is paris\n","this is bangolore\n"]
f.write("hello\n")
f.writelines(p)
print("---------------------------------------------------------")
f=open("dharani.txt","r+")
p=["this is delhi\n","this is paris\n","this is bangolore\n"]
r=f.read()
print(r)
print("---------------------------------------------------------")

