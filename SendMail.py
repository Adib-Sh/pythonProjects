import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



username = 'adibpytest@gmail.com'
password = '21101372'


def send_mail(text= 'Email Body', subject = 'Hi there from Adib', from_emails = "Adib's Testing Py <dibpytest@gmail.com>", to_emails = None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('altenative')
    msg['From']= from_emails
    msg['To'] = ", ".join(to_emails)
    msg['Subject']= subject
    
# =============================================================================
#     txt_part = MIMEText(text, 'plain')
#     msg.attach(txt_part)
# =============================================================================

    html_part = MIMEText('<h1> Hi There! This is a HTML Message </h1>', 'html')
    msg.attach(html_part)    
    
    msg_str = msg.as_string()
    
    # Login to SMTP server
    with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_emails, to_emails, msg_str)