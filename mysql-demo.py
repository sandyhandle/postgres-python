# from re import S
import psycopg2


conn = psycopg2.connect(database="postgres", user="postgres", password="root123", host="127.0.0.1", port="5432")

c = conn.cursor()
# print(conn)

# print(c)
# c.execute("insert into users values('hari','1993hari','Hari S');")


while True:
  u_name = input("Enter your Username: ")
  if u_name == "exit()":
    break
  passward = input("Enter your Passward: ")
  name = input("Enter your Name: ")
  
  if len(u_name) <= 20 and len(passward) <= 20 and len(name) <= 20:
    c.execute("select (username) from users where username = '%s'"%(u_name))
    s = c.fetchall()
    if s == []:
      c.execute("insert into users values('%s','%s','%s')"%(u_name,passward,name))
      conn.commit()
      c.close()
      break
    else:
      print("User name is already present..\nPlease try another username")
  else:
    print("your input must be lesser than 20")
  


# print(i==0)



# c.execute("SELECT name,username from users")

# r = c.fetchall()
# for i,j in r:
#   print("{}, {}".format(i,j))  
# # conn.commit()
# c.close()



# print(conn)




# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root123"
# )

# print(mydb)
