import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "swamybittu649@gmail.com"
receiver_email = "swamybittu649@gmail.com"
password = input("Plz Enter Your App Password:") #in input we can use anything.. i used password.. [my app password is dpdxlgyffvtlpcgh]

message = MIMEMultipart("alternative")
message["Subject"] = "Sending mails using the smtp library in python"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
swamy
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
    <h3>swamy is the python and php fullstack  webdeveloper  swamy has skilled in the python and php and laravel django sql mysql html css js bootstrap</h3>
  </p> </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print('Email has been sent to the user..')