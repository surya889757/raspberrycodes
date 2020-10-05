import smtplib
from email.mime.text import MIMEText#email.mime.text.MIMEText(_text[, _subtype[, _charset]])
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase#email.mime.base.MIMEBase(_maintype(e.g. text or image), _subtype(e.g. plain or gif), **_params(e.g.key/value dictionary))
from email import encoders
import os.path

email = 'project.ece222@gmail.com'
password = 'eceece143@'
send_to_email = 'project.ece222@gmail.com'
subject = 'This is the subject'
message = 'This is my message'
file_location = '//home//pi//Downloads//takeoff.png'
#/home/pi/Downloads/takeoff.png

msg = MIMEMultipart()#Create the container (outer) email message.
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject
 '''as.string()  
 |
 +------------MIMEMultipart  
              |                                                |---content-type  
              |                                   +---header---+---content disposition  
              +----.attach()-----+----MIMEBase----|  
                                 |                +---payload (to be encoded in Base64)
                                 +----MIMEText'''
msg.attach(MIMEText(message, 'plain'))#attach new  message by using the Message.attach

filename = os.path.basename(file_location)#function returns the tail of the path
attachment = open(file_location, "rb") #“rb” (read binary)
part = MIMEBase('application', 'octet-stream')#Content-Type: application/octet-stream , image/png, application/pdf
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)#Content-Disposition: attachment; filename="takeoff.png"

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)# Send the message via local SMTP server.
server.starttls()# sendmail function takes 3 arguments: sender's address, recipient's address and message to send 
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
