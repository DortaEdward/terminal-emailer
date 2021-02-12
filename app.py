# Edward Dorta
#This will only work if your gmail account allows less secure apps access. If it doesn't it will not work.

# Dependencies 
import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# gets user's input and logs in with smtp
def user_input(server):
    # Prompts user to for log in information
    print('User Input\n================')
    email, password, target_email, subject = str(input('Email: ')), str(input('Password: ')), str(input('Target Email: ')), str(input('Email Subject: '))
    user_info = {'Email' : email, 'Password': password,'Target Email': target_email, 'Email Subject': subject}
    server.starttls()
    server.login(user_info['Email'],user_info['Password'])
    print('Login was a Success')
    return user_info

# imports the emails body's content from a external file
def import_body():
    f = open('body.txt','r')
    body = f.read()
    return body

# constructs the email
def construct_email(user_info, server):
    # Define the email as multipart to be able to attach multiple stuff to the object
    email = MIMEMultipart()
    # Constructing the Email
    email['From'] = user_info['Email']
    email['To'] = user_info['Target Email']
    email['Subject'] = user_info['Email Subject']
    body = import_body()
    email.attach(MIMEText(body,'plain'))
    text = email.as_string()
    send_email(user_info['Email'], user_info['Target Email'],text,server)
    

# sends the email
def send_email(senders_email,target_email,email,server):
    server.sendmail(senders_email, target_email, email)
    print("Email sent from {} to {}".format(senders_email,target_email))
    server.quit()

def main():
    '''
        Additions needed to be added:
        - let the user choose whether they was to input their log in information or read it in from a file
        - let the user choose whether they want to input the body of the text or read it in from a file
            - if user chooses to read in from a file ask the user whether its plain text or if it is html
    '''
    # Set up Email server using Gmail
    server = smtplib.SMTP('smtp.gmail.com',587)
    user_data = user_input(server)
    # Start Server
    server.ehlo()
    construct_email(user_data,server)

main()
