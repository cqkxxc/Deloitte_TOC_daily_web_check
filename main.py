from CheckView import CheckView
from sendEmail import send_mail

if __name__ == '__main__':
    check_view = CheckView()
    send_mail("chuaxu@deloitte.com.cn","Daily Web Check Result",check_view.main())
