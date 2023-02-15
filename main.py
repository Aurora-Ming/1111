with open("./DATA.csv", "r", encoding="utf-8") as f:
 (username, firstname, lastname, email) = f.readline().split(",", 3)
n= email.count("@")
m=email.count(".")
int(n)
int(m)
while(n!=1) :
    if (m<1 or m>2):
      with open("./error-email.csv", "w", encoding="utf-8") as g:
       g.write(email)
    with open("./DATA.csv", "r", encoding="utf-8") as f:
     (username, firstname, lastname, email) = f.readline().split(",", 3)

with open("./email.csv", "w", encoding="utf-8") as h:
    h.write(email)









