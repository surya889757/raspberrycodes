import smtplib
from email.mime.text import MIMEText#email.mime.text.MIMEText(_text[, _subtype[, _charset]])
from email.mime.multipart import MIMEMultipart

email = 'project.ece222@gmail.com'
password = 'Tk.Ymts#321'
send_to_email = 'project.ece222@gmail.com'
subject = 'email test'
message = 'email test done!!!!!!!!!!'

msg = MIMEMultipart()#Create the container (outer) email message.
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))#attach new  message by using the Message.attach

server = smtplib.SMTP('smtp.gmail.com', 587)# Send the message via local SMTP server.
server.starttls()# sendmail function takes 3 arguments: sender's address, recipient's address and message to send 
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
