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

def get_email_content():
    # ask user if they want to 
    print('\nEmail Content Selection')
    print('=================================')
    choice = int(input('\n1) Use body.txt for the emails content\n2) Use another file\n3) Input manually\nChoice: '))

    if choice == 1:
        content = import_body('body.txt')
    elif choice == 2:
        file_path = str(input('Enter the filepath: '))
        content = import_body(filepath) 
    elif choice == 3:
        content = str(input('Body: '))
    
    content_type = int(input('\n1) Text file\n2) Html File\nChoice: '))
    if content_type == 1:
        body_type = 'plain'
    elif content_type ==2:
        body_type = 'html'
    # object that returns the file path and the body type
    body_info = {'Content': content, 'Body Type': body_type}

    return body_info


# imports the emails body's content from a external file
def import_body(file):
    f = open(file,'r')
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
    body_info = get_email_content()
    body = body_info['Content']
    email.attach(MIMEText(body,body_info['Body Type']))
    text = email.as_string()
    send_email(user_info['Email'], user_info['Target Email'],text,server)
    

# sends the email
def send_email(senders_email,target_email,email,server):
    server.sendmail(senders_email, target_email, email)
    print("Email sent from {} to {}".format(senders_email,target_email))
    server.quit()

def main():
    '''
        - allow user to attach file(s)
    '''
    # Set up Email server using Gmail
    server = smtplib.SMTP('smtp.gmail.com',587)
    user_data = user_input(server)
    # Start Server
    server.ehlo()
    construct_email(user_data,server)

main()
