f=open("./Programming - MOCK_DATA - Programming - MOCK_DATA.csv","r",encoding="utf-8")
with open("./valid-email.csv","w",encoding="utf-8")as g:
  g.write("[username domain]\n")
with open("./invalid-email.csv","w",encoding="utf-8")as k:
  k.write("[username domain]\n")
line=f.readline()
for line in f:
  (username,firstname,lastname,emails)=line.split(",",3)
  int=a=emails.count("@")
  int=b=emails.count(".")
  (name,domains)=emails.split("@",1)
  (domain,other)=domains.split(".",1)
  if a!=1:
    with open("./invalid-email.csv","a",encoding="utf-8")as k:
      k.write(emails)
  elif b<1 or b>2:
     with open("./invalid-email.csv","a",encoding="utf-8")as k:
      k.write(emails)
  else:
      with open("./valid-email.csv","a",encoding="utf-8")as g:
        g.write(name+" "+domain+"\n")
      print(str(name+" "+domain))










