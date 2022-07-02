from re import U
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from django.db.utils import IntegrityError
from django.contrib.auth.models import User 
import environ
from rest_framework.authtoken.models import Token
from portal_fresia.lib.autogenerate import generate

#Load PARERNT FOLDER
BASE_DIR = Path(__file__).resolve().parent.parent
print('BASE_DIR: {0}'.format(BASE_DIR))



def build_and_send(toList, username, password, smtp_host, smtp_port, nombre):
    try:
        subject = "POC SEND SUCCESS MAIL"
        mail_body = ""
        # Read template html
        txt_file = open(os.path.join(BASE_DIR, 'sources', 'template', 'mail', 'success-mail.html'))
        mail_body = txt_file.read()
        txt_file.close()
        #print("mail_body: {0}".format(mail_body))
        # Override template html
        mail_body = mail_body.replace('#PERSON_NAME', nombre)
        array = ["element 1", "element 2", "element 3", "element 4"]
        list_a = ""
        for e in array:
            data = "<tr><td>{0}</td></tr>".format(e)
            list_a = list_a + data
        mail_body = mail_body.replace('#LIST', list_a)
        #print("mail_body: {0}".format(mail_body))
        #Set mail paremeters
        mimemsg = MIMEMultipart()
        mimemsg['From'] = username
        mimemsg['To'] = toList
        mimemsg['Subject'] = subject
        mimemsg.attach(MIMEText(mail_body, 'html'))
        connection = smtplib.SMTP(host=smtp_host, port=smtp_port)
        connection.starttls()
        connection.login(username,password)
        #Send mail
        connection.send_message(mimemsg)
        connection.quit()
    except Exception as e:
        print(e)        

def load_email_sender():
    # Initialise environment variables
    env = environ.Env()
    environ.Env.read_env()    
    user_mail = 'portalfresia@outlook.com'
    password_mail = '@Portal123'
    smtp_host_mail = 'm.outlook.com'
    smtp_port_mail = '587'
    print('user_mail: ', user_mail)
    print('password_mail: ', password_mail)
    print('smtp_host_mail: ', smtp_host_mail)
    print('smtp_port_mail: ', smtp_port_mail)
    return user_mail, password_mail, smtp_host_mail, smtp_port_mail        

def create_token(user):
    print('create_token')
    try:
        print('new token')
        token = Token.objects.create(user=user)
        print('token -> {0}'.format(token))
        return token.key
    except IntegrityError as e:
        print('delete token')
        token = Token.objects.get(user=user)
        token.delete()
        print('new token')
        token = Token.objects.create(user=user)
        return token.key  

def build_token_recovery_pass(username, recovery_url):
    try:
        print('username: ', username)
        user = User.objects.get(username=username)
        email = user.email
        print('email: ', email)
        #Create Token
        token = create_token(user)
        print('token: ', token)
        #Load html template mail
        base_dir = Path(__file__).resolve().parent.parent
        mail_path = os.path.join(base_dir, 'template', 'mail', 'token-recovery-pass.html')
        print('mail_path: ', mail_path)
        txt_file = open(mail_path)
        mail_body = txt_file.read()
        #Replace template
        recovery_url = recovery_url + '?username='+username + '&token='+token         
        mail_body = mail_body.replace('#TOKEN_LINK', recovery_url)
        #Load email data web_shopping
        user_mail, password_mail, smtp_host_mail, smtp_port_mail = load_email_sender()
        subject = 'Recuperacion de clave secreta'
        #Send Mail
        build_and_send2(email, user_mail, password_mail, smtp_host_mail, smtp_port_mail, subject, mail_body)
        return 'Sended mail', True
    except Exception as e:
        print(e)
        return 'User not exists', False

def build_user_pass(username, token):
    try:
        user = User.objects.get(username=username)
        email = user.email
        token = Token.objects.get(user=user)
        new_pass = generate(32)
        print('new_pass: ', new_pass)
        user.set_password(new_pass)
        user.save(force_update=True)
        #Load html template mail
        base_dir = Path(__file__).resolve().parent.parent
        mail_path = os.path.join(base_dir, 'template', 'mail', 'new-pass.html')
        print('mail_path: ', mail_path)
        txt_file = open(mail_path)
        mail_body = txt_file.read()
        #Replace template
        mail_body = mail_body.replace('#USERNAME', username)
        mail_body = mail_body.replace('#PASSWORD', new_pass)        
        #Load email data web_shopping
        user_mail, password_mail, smtp_host_mail, smtp_port_mail = load_email_sender()
        subject = 'Actualizacion de clave secreta'
        #Send Mail
        build_and_send2(email, user_mail, password_mail, smtp_host_mail, smtp_port_mail, subject, mail_body)
        return 'Sended mail', True
    except Exception as e:
        print(e)
        return 'User not exists', False     

def build_and_send2(to_list, user_mail, password_mail, smtp_host_mail, smtp_port_mail, subject, body_mail):
    try:
        #Set mail paremeters
        mimemsg = MIMEMultipart()
        mimemsg['From'] = user_mail
        mimemsg['To'] = to_list
        mimemsg['Subject'] = subject
        mimemsg.attach(MIMEText(body_mail, 'html'))
        connection = smtplib.SMTP(host=smtp_host_mail, port=smtp_port_mail)
        connection.starttls()
        connection.login(user_mail,password_mail)
    
        #Send mail
        connection.send_message(mimemsg)
        connection.quit()
    except Exception as e:
        print(e)    