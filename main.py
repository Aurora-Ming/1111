f=open("./DATA.csv","r",encoding="utf-8")
for name in f:
 (name ,firstname,lastname,emails)=f.readline().split(",",3)
 n=emails.count("@")
 m=emails.count(".")
 int(n)
 int(m)
 while(n!=1):
  g=open("./invalid-email.csv","w",encoding="utf-8")
  (username,email)=emails.split("@",1)
  g.write(username,",",email)
 while(m<1 or m>2):
   g=open("./invalid-username.csv","w",encoding="utf-8")
   (username,email)=emails.split("@",1)
   g.write(username,",",email)
else:
  k=open("./valid-email.csv","w",encoding="utf-8")
  (username,email)=emails.split("@",1)
  k.write(username)
  k.write(email)











