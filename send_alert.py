import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "xxx@gmail.com"
password = "xxx"
sms_gateway = "xxxxxxxxxx@text.att.net" 

# Gmail server is used to deliver the message.
# Every email provider has a unique smtp. 
# The port is also provided by email provider.
smtp = "smtp.gmail.com" 
port = 587

# This will start our email server
server = smtplib.SMTP(smtp, port)
server.starttls()
server.login(email, password)

# Use MIME module to structure the message.
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway
msg['Subject'] = "Test Message\n"
body = "Hello World\n"
msg.attach(MIMEText(body, 'plain'))
sms = msg.as_string()
server.sendmail(email,sms_gateway, sms)
server.quit()
