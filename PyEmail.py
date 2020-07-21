'''Please Note in order to use this script, you need to enable your Gmail,
allow less secure applications use the Gmail services. You can also use other
APIs which are freely available
happy hacking!!!
'''


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

msg = MIMEMultipart()

user_name = raw_input("Enter your user_name: ")
passwd = raw_input("Enter your password: ")
from_email = raw_input("Enter the From email id: ")
to_email = raw_input("Enter the sending/TO email id: ")

msg['From'] = form_email
msg['To'] = to_email
msg['Subject'] = 'this is automated email'

msg.attach( MIMEText("this is the body of email") )
part = MIMEBase('application', "octet-stream")
fo=open('video.mp4',"rb")
part.set_payload(fo.read() )
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="attachment_videos.mp4"')
msg.attach(part)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(user_name, passwd)

server.sendmail(from_email, to_email, msg.as_string())
server.close()
