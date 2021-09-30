from email.message import EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import imghdr
import sys

def build():
    app = QApplication(sys.argv)
    win = QWidget()
    mail_content = "hello"
    
    msg = QWidget()
    url = "wallhaven-oxeo25.jpg"
    
    url1 = "msg.ico"
    
    
        
    
    def send():
        
        try:
            message = MIMEMultipart()
            message['From'] = box.text()
            message['To'] = box2.text()
            message['Subject'] = Q1.toPlainText()
            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(box.text(), box2.text()) #login with mail_id and password
            text = message.as_string()
            session.sendmail(box.text(),box1.text(), text)
            session.quit()
            
            msg1 = QMessageBox(msg)
            

            msg1.setFixedHeight(50)
            msg1.setFixedWidth(200)
            msg1.setIcon(QIcon(url1))
            msg1.setText("Message has been sent")
            msg1.show()
            
            
        except Exception as e:
            msg2 = QMessageBox(msg) 
            msg2.setIcon(QIcon(url1))
            msg2.setFixedHeight(50)
            msg2.setFixedWidth(200)
            msg2.setText(str(e))
            msg2.show()     
            
        
    
    image = QLabel(win)
    image.setPixmap(QPixmap(url)) 
    image.show()   
        
        
    text = QLabel(win)
    text.setText("Mail Sending Application")
    text.setFont(QFont("Arial",20))
    text.setStyleSheet("background-color:white;color:black")  
    text.setFixedHeight(30)
    text.setFixedWidth(300)
    text.move(250,10)
    text.show() 
    
    
    
    l1= QLabel(win)
    l1.setText("Sender Mail")
    l1.setFont(QFont("Arial",20))
    l1.move(50,100)
    l1.setStyleSheet("color:white")
    
    l2= QLabel(win)
    l2.setText("Receiver Mail")
    l2.setFont(QFont("Arial",20))
    l2.move(50,300)
    l2.setStyleSheet("color:white")
    
    
    l3= QLabel(win)
    l3.setText("Sender Pass")
    l3.setFont(QFont("Arial",20))
    l3.move(50,200)
    l3.setStyleSheet("color:white")
    
    
    Q1 = QTextEdit(win)
    Q1.setFixedHeight(70)
    Q1.setFixedWidth(500)
    Q1.setFont(QFont("Arial",10))
    Q1.setStyleSheet("background-color:White")
    Q1.move(200,390)
    Q1.show()     
    
    
    
    box = QLineEdit(win)
    box.setPlaceholderText("Sender Mail")
    box.setFixedHeight(30)
    box.setFixedWidth(400)
    box.setFont(QFont("Arial",20))
    box.move(250,100)
    box.show()
    
    box2 = QLineEdit(win)
    box2.setEchoMode(QLineEdit.Password)
    box2.setPlaceholderText("Sender password")
    box2.setFixedHeight(30)
    box2.setFixedWidth(400)
    box2.setFont(QFont("Arial",20))
    box2.move(250,200)
    box2.show()
    
    
    
    
    box1 = QLineEdit(win)
    box1.setPlaceholderText("Receiver Mail")
    box1.setFixedHeight(30)
    box1.setFixedWidth(400)
    box1.setFont(QFont("Arial",20))
    box1.move(250,300)
    box1.show()
    
    
    b1 = QPushButton(win)
    b1.setFixedHeight(30)
    b1.setFixedWidth(100)
    b1.move(50,400)
    b1.setFont(QFont("Arial",15))
    b1.setText("Send")
    b1.setStyleSheet("border-radius:10px;background-color:white")
    b1.clicked.connect(send)
    
    
    win.setFixedHeight(500)
    win.setFixedWidth(800)
    win.setWindowTitle("Email Sender")
    win.setWindowIcon(QIcon(url1))
    
    win.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    build()    
    
    
    