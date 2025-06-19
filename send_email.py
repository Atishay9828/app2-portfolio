import smtplib , ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465 

    username= "adishfab@gmail.com"
    password = "rpkl jynv gowk xjve"

    reciever = "adishfab@gmail.com"
    content = ssl.create_default_context()
    with smtplib.SMTP_SSL(host , port , context= content) as server :
        server.login(username,password)
        server.sendmail(username,reciever,message)