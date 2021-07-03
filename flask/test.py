
from passlib.hash import sha256_crypt
#from flask import Flask, request,jsonify,Response
import mysql.connector

#app = Flask(__name__)

mydb = mysql.connector.connect(
   host = "localhost",
   user = "book",
   password = "book",
   database = "mydb"
)

mycursor = mydb.cursor()

# getpwd = "select password from user where email = 'shree@email.com'"
# mycursor.execute(getpwd)
# result = mycursor.fetchone()
# for i in result:
#     mypwd = i
# print(mypwd)
def login():
   getpwd = "select password from user where email = 'shree@email.com'"
   mycursor.execute(getpwd)
   result = mycursor.fetchone()
   for i in result:
        mypwd = unicode(i, 'utf-8') 
   givenpwd = sha256_crypt.encrypt('123456')
   existpwd = sha256_crypt.encrypt(mypwd)
   loged = sha256_crypt.verify(result,'123456')
   if loged == True:
      return "loged in"
   else:
      return "error"

login()
# def user():
#    userID = int(request.json['userID'])
#    name = request.json['name']
#    email = request.json['email']
#    longitude = request.json['longitude']
#    latitude = request.json['latitude']
#    password = request.json['password']
#    role = request.json['role']
#    active = request.json['active']
 
#    return Response(status=201)

# if __name__ == '__main__':
#    app.run(debug = True)