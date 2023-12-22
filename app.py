from flask import Flask, flash, session, redirect
from flask import render_template,request,send_file
import pymysql
import json ,jsonify
import smtplib
import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import pandas as pd 
from werkzeug.utils import secure_filename
# from hdfs import InsecureClient
# import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'static/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'any random string'




##################################   Mail to blooddoner #########################################################################

def sendemailtouser(usermail,ogpass):   
    fromaddr = "pranalibscproject@gmail.com"
    toaddr = usermail
   
    #instance of MIMEMultipart 
    msg = MIMEMultipart() 
  
    # storing the senders email address   
    msg['From'] = fromaddr 
  
    # storing the receivers email address  
    msg['To'] = toaddr 
  
    # storing the subject  
    msg['Subject'] = " ALTRUISTIC BLOOD BANK APPLICATION (NGO)"
  
    # string to store the body of the mail 
    body = ogpass
  
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # start TLS for security 
    s.starttls() 
  
    # Authentication 
    s.login(fromaddr, "vnsdqlwppigyxvxs") 
  
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
  
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
  
    # terminating the session 
    s.quit()
    



##################################   Mail to blooddoner #########################################################################


##################################   database connection #########################################################################
def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="bloodbank", autocommit=True)
        return connection
    except:
        print("Something went wrong in database Connection")

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")

con = dbConnection()
cursor = con.cursor()

################################## database connection #########################################################################



##################################  ngo login register #########################################################################
@app.route('/ngopyregister', methods=['GET', 'POST'])
def ngopyregister():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")       
        password = request.form.get("password")
        sql1 = "INSERT INTO ngo_register(ngo_username, ngo_email, ngo_password) VALUES (%s, %s, %s);"
        val1 = (username, email, password)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
    
@app.route('/ngopylogin', methods=['GET', 'POST'])
def ngopylogin():
    if request.method == 'POST':
        username = request.form.get("username")
        passw = request.form.get("password")       
        cursor.execute('SELECT * FROM ngo_register WHERE ngo_username = %s AND ngo_password = %s', (username, passw))
        count = cursor.rowcount
        if count == 1:
            return "success"
        else:
            return "Fail"

##################################   ngo login register #########################################################################



##################################  blooddoner login /register#########################################################################
@app.route('/userRegister', methods=['GET', 'POST'])
def userRegister():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")        
        password = request.form.get("password")
        img = request.form.get("upload")
        sql1 = "INSERT INTO register(username, email,mobile, password,img) VALUES (%s, %s, %s, %s, %s);"
        val1 = (username, email, phone, password,img)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
    
    
@app.route('/userLogin', methods=['GET', 'POST'])
def userLogin():
    if request.method == 'POST':
        username = request.form.get("username")
        passw = request.form.get("password")  
        Verify="Verify"
        cursor.execute('SELECT * FROM register WHERE username = %s AND password = %s AND status = %s', (username, passw, Verify))
        count = cursor.rowcount
        if count == 1:
            return "success"
        else:
            return "Fail"
        
##################################   blooddoner login/ register#########################################################################        




##################################   blooddoner book slot register#########################################################################        

@app.route('/adddetails', methods=['GET', 'POST'])
def adddetails():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")     
        UID = request.form.get("UID") 
        address1 = request.form.get("address1")
        gender1 = request.form.get("gender1")
        contact1 = request.form.get("contact1")        
        bloodgroup1 = request.form.get("bloodgroup1")
        Division1 = request.form.get("Division1")
        sql1 = "INSERT INTO addata(username, email,UID, address1,gender1,contact1,bloodgroup1,Division1) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        val1 = (username, email,UID, address1,gender1,contact1,bloodgroup1,Division1)
        cursor.execute(sql1,val1)
        con.commit()
        return "success"
    
##################################   blooddoner book slot register#########################################################################        
    
    
@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST': 
        f2 = request.files['filename']
        filename_secure = secure_filename(f2.filename)
        split_filename = filename_secure.split('_')[-1]
        f2.save(os.path.join(app.config['UPLOAD_FOLDER'], split_filename)) 
        return "success" 
               
   
    
@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    if request.method == 'POST': 
        cursor.execute('SELECT * FROM addata')
        row = cursor.fetchall() 
        jsonObj = json.dumps(row)
        # print(jsonObj)        
        return jsonObj       
           
    
@app.route('/getupload_image', methods=['GET', 'POST'])
def getupload_image():
    if request.method == 'POST':  
        cursor.execute('SELECT * FROM register')
        row = cursor.fetchall() 
        jsonObj = json.dumps(row)
        # print(jsonObj)         
        return jsonObj  
    
##################################  ngo verify register user#########################################################################        
    
    
@app.route('/verifyuser', methods=['GET', 'POST'])
def verifyuser():
    if request.method == 'POST':
        # print("GET")        
        username = request.form.get("username")
        email = request.form.get("email")       
        # print("INPUTS")        
        # print("username",username)
        ccg="Verify"
        con = dbConnection()
        cursor = con.cursor()
        sql1 = "UPDATE register SET status = %s WHERE username = %s  AND email = %s;"
        val1 = (ccg, username ,email)
        cursor.execute(sql1,val1)
        con.commit()
        usermail = email
        ogpass = "An NGO verified your registration. Now you can login."
        sendemailtouser(usermail,ogpass)
        return "success"
    
##################################  ngo verify register user#########################################################################        


################################## NGO REQUEST TO DONATE BLOOD NEAR BY HOSPITALr#########################################################################        
    

@app.route('/bloodnotification', methods=['GET', 'POST'])
def bloodnotification():
    if request.method == 'POST':
        # print("GET")
        hospital = request.form.get("hospital")
        bloodgroup = request.form.get("bloodgroup")
        address = request.form.get("address")
        location = request.form.get("location")
        input_details = request.form.get("input_details")
        input_time_confirm = request.form.get("input_time_confirm")
        email = request.form.get("email")
        username = request.form.get("username")
        # print(email)
        sql1 = "INSERT INTO notificationdonors(hospital, bloodgroup,address, location,input_details,input_time_confirm,email,username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        val1 = (hospital, bloodgroup,address, location,input_details,input_time_confirm,email,username)
        cursor.execute(sql1,val1)
        con.commit()
        
        usermail = email
        s1="dear sir , your slot book now at time  "
        s2=str(input_time_confirm)
        s3="  your location address  "
        s4=location
        s5=input_details
        s6="  hospital name  "
        s7=hospital
        usermail = email
        ogpass = s1+s2+s3+s4+s5+s6+s7
        sendemailtouser(usermail,ogpass)
        return "success"
        


@app.route('/getbloodnotification', methods=['GET', 'POST'])
def getbloodnotification():
    if request.method == 'POST':  
        donor = request.form.get("donor")
        cursor.execute('SELECT * FROM notificationdonors where username= %s;',(donor))
        row = cursor.fetchall() 
        jsonObj = json.dumps(row)
        # print(jsonObj)        
        return jsonObj      
################################## NGO REQUEST TO DONATE BLOOD NEAR BY HOSPITALr#########################################################################        



################################## Donor blood donate in hospital sucessfully#########################################################################        


    
@app.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == 'POST':
        # print("GET")        
        hospital = request.form.get("hospital")
        bloodgroup = request.form.get("bloodgroup")
        input_time_confirm = request.form.get("time") 
        # print("INPUTS")  
        # print()
        ccg="succesful_donaton"
        con = dbConnection()
        cursor = con.cursor()
        sql1 = "UPDATE notificationdonors SET status = %s WHERE hospital = %s  AND bloodgroup = %s  AND input_time_confirm = %s;"
        val1 = (ccg, hospital ,bloodgroup , input_time_confirm)
        cursor.execute(sql1,val1) 
        con.commit()
        con = dbConnection()
        # cursor.execute('SELECT * FROM notificationdonors where hospital= %s AND bloodgroup = %s  AND input_time_confirm = %s;',(hospital,bloodgroup,input_time_confirm))
        # row = cursor.fetchall() 
        # username=row[0][9]
        
        # df = pd.DataFrame.from_records(row)
        
        # df.to_csv('static/data/'+username+'.csv', index=False)
        # dff = pd.read_csv(df)
        
        clients = pd.read_sql('SELECT * FROM notificationdonors where hospital="'+hospital+'"',con)
        print(clients)
        clients.to_csv('static/data/data.csv', index=False)
        ################################here we use hadoop server to store particular donor donation data #############
   
        
        return "success"
    
    
    

@app.route('/getdonation', methods=['GET', 'POST'])
def getdonation():
    if request.method == 'POST':  
        cursor.execute('SELECT * FROM notificationdonors where status="succesful_donaton";')
        row = cursor.fetchall()  
        jsonObj = json.dumps(row)
        print(jsonObj) 
        return jsonObj  

################################## Donor blood donate in hospital sucessfully#########################################################################        
        
    
################################## Ngo get reward to user with help of hospital#########################################################################        
    
@app.route('/rewards', methods=['GET', 'POST'])
def rewards():
    if request.method == 'POST':
        # print("GET")
        hospital =request.form.get("hospital")   
        email = request.form.get("mail")   
        reward = request.form.get("reward")
        ccg=str(reward)
        con = dbConnection()
        cursor = con.cursor()
        sql1 = "UPDATE notificationdonors SET rewards = %s WHERE hospital = %s  AND email = %s;"
        val1 = (ccg, hospital ,email)
        cursor.execute(sql1,val1)
        con.commit()
        usermail = email
        s1= "$Congratulations, you get a reward. +$"
        s2=reward
        ogpass = s1+s2
        sendemailtouser(usermail,ogpass)
        return "success"
    
    
    
    
@app.route('/getrewards', methods=['GET', 'POST'])
def getrewards():
    if request.method == 'POST':  
        donor = request.form.get("donor")
        cursor.execute('SELECT * FROM notificationdonors where username= %s;',(donor))
        row = cursor.fetchall() 
        jsonObj = json.dumps(row)
        # print(jsonObj)   
        return jsonObj       
################################## Ngo get reward to user with help of hospital#########################################################################        


################################## user show profile#########################################################################        
               
    
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':  
        user = request.form.get("username")
        cursor.execute('SELECT * FROM register where username= %s;',(user))
        row = cursor.fetchall()
        jsonObj = json.dumps(row)
        # print(jsonObj)
        return jsonObj 
    
################################## user show profile#########################################################################        

    
################################## ngo show near by user on map#########################################################################        
    
@app.route('/nearuser', methods=['GET', 'POST'])
def nearuser():
    if request.method == 'POST':  
        username1 = request.form.get("username")
        latitude1 = request.form.get("lat1")
        longitude1 = request.form.get("lng1")
        cursor.execute('SELECT * FROM location WHERE username = %s', (username1))
        count = cursor.rowcount
        if count == 1:   
            # print("Update")
            sql1 = "UPDATE location SET username = %s,latitude = %s,longitude = %s WHERE username = %s AND latitude = %s AND longitude = %s;"
            val1 = (username1, latitude1, longitude1, username1, latitude1, longitude1)
            cursor.execute(sql1,val1)
        elif count == 0:
            # print("Insert call")
            sql1 = "INSERT INTO location(username, latitude, longitude) VALUES (%s, %s, %s);"
            val1 = ( username1, latitude1, longitude1)
            cursor.execute(sql1,val1)
        con.commit()
        return "success"
    
    
@app.route('/Getnearuser', methods=['GET', 'POST'])
def Getnearuser():
    if request.method == 'POST':  
        cursor.execute('SELECT * FROM location')
        row = cursor.fetchall() 
        jsonObj = json.dumps(row)
        # print(jsonObj)    
        return jsonObj 

################################## ngo show near by user on map#########################################################################        


################################## get feedback to donor booking reject #########################################################################        

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':  
        username = request.form.get("username")
        bloodgroup = request.form.get("bloodgroup")
        emailid = request.form.get("emailid")
        feedback = request.form.get("feedback")
        cursor.execute('SELECT * FROM addata WHERE username = %s AND email = %s ', (username,emailid))
        count = cursor.rowcount
        if count == 1:   
            # print("delte")
            sql1 = "DELETE FROM addata  WHERE username = %s AND bloodgroup1 = %s AND email = %s;"
            val1 = (username, bloodgroup, emailid)
            cursor.execute(sql1,val1)
            # print("Insert call")
            sql1 = "INSERT INTO feedback(usename, bloodgroup, emailid,feedback) VALUES (%s, %s, %s, %s);"
            val1 = (username, bloodgroup, emailid,feedback)
            cursor.execute(sql1,val1)
        con.commit()
        usermail = emailid
        s1= "Your reservation was denied, because: "
        s2=feedback
        ogpass = s1+s2
        sendemailtouser(usermail,ogpass)
        return "success"
    
    
    
        
@app.route('/getfeedback', methods=['GET', 'POST'])
def getfeedback():
    if request.method == 'POST':  
        user = request.form.get("donor")
        cursor.execute('SELECT * FROM feedback where usename= %s;',(user))
        row = cursor.fetchall() 
        jsonObj = json.dumps(row)
        # print(jsonObj) 
        return jsonObj 
    
################################## get feedback to donor booking reject #########################################################################        


        
# @app.route('/file', methods=['GET', 'POST'])
# def file():
#     if request.method == 'POST':
#         con = dbConnection()
#         clients = pd.read_sql('SELECT * FROM notificationdonors' ,con)
#         clients.to_csv('static/data/Clients100914.csv', index=False)          
#         outputFilename = "static/data/Clients100914.csv" 
#         jsonObj = json.dumps(outputFilename)
#         # print(jsonObj)        
#         return jsonObj 
################################## get rate to ngo #########################################################################        


@app.route('/Rating', methods=['GET', 'POST'])
def Rating():
    print("hakhsd")
    if request.method == 'POST':
        username = request.form.get("username") 
        data = request.form.get("Rate")
        hospital = request.form.get("hospital")
        print(username,data,hospital)
        
        cursor.execute('SELECT * FROM notificationdonors WHERE username = %s AND hospital = %s ', (username,hospital))
        count = cursor.rowcount
        if count == 1: 
            # print("Update")
            sql1 = "UPDATE notificationdonors SET rate = %s WHERE username = %s AND hospital = %s ;"
            val1 = (data, username, hospital)
            cursor.execute(sql1,val1)
        elif count == 0:
            
            # print("Insert call")
            sql1 = "UPDATE notificationdonors SET rate = %s WHERE username = %s AND hospital = %s ;"
            val1 = (data, username, hospital)
            con.commit()
        return "success"
        
        
@app.route('/getrate', methods=['GET', 'POST'])
def getrate():
    if request.method == 'POST':  
        cursor.execute('SELECT * FROM notificationdonors')
        row = cursor.fetchall() 
        jsonObj = json.dumps(row)
        # print(jsonObj) 
        return jsonObj 

################################## get rate to ngo  #########################################################################        
        
    
if __name__ == "__main__":
    app.run("0.0.0.0")
