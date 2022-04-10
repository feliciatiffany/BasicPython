import smtplib, ssl
import os
dir=os.path.dirname(os.path.realpath(__file__)) #to get directory that the program exist in, reference : https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = 'feliciatiffany@gmail.com'  
password = ''
context = ssl.create_default_context()
server=smtplib.SMTP_SSL(smtp_server, port, context=context) 
server.login(sender_email, password)

filename=dir+'/receiver_list.txt'
f= open (filename, 'r')
file_data=f.read().splitlines() #to erase \n, reference : https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
for email in file_data:
    print ("from : "+sender_email)
    receiver_email = email  # Enter receiver address
    print("to : "+receiver_email+"\n")
    subject =input ('Enter subject : ')
    text =input('Enter your message : ')
    message = 'Subject: {}\n\n{}'.format(subject,text)  #to send with subject, reference : https://stackoverflow.com/questions/7232088/python-subject-not-shown-when-sending-email-using-smtplib-module
    server.sendmail(sender_email, receiver_email, message) #to erase error for verification, reference : https://accounts.google.com/b/0/DisplayUnlockCaptcha
    print ("============================================\n")


print("EMAIL BERHASIL TERKIRIM!")


#reference : https://realpython.com/python-send-email/#:~:text=Python%20comes%20with%20the%20built,apply%20to%20other%20email%20services.