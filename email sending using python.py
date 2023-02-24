import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("swamybittu649@gmail.com", "swamypatel@9980")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("swamybittu649@gmail.com", "swamybittu649@gmail.com", message)

# terminating the session
s.quit()
