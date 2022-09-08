import smtplib
from email.mime.text import MIMEText

mail_host = 'shintsmtp.deloitte.com.cn'
mail_user = 'TOCpyScripts'
mail_postfix = 'deloitte.com.cn'


def send_mail(to_list, subject, content):
    """
        发送电子邮件
    """
    me = "CN TOC WEB CHECK" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list

    s = smtplib.SMTP()
    s.connect(mail_host)
    s.sendmail(me, to_list, msg.as_string())
    s.close()
