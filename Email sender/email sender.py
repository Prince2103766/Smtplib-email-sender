import smtplib

email='stevendozie9@gmail.com'

password='stevendozie_123'

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email,password) 
    msg='helo guys'
    smtp.sendmail(email,"stevendozie9@gmail.com",msg)