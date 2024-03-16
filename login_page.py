admin_email='admin'
admin_pass="admin"
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget,QMessageBox,QRadioButton)
import employee
import admin
import psycopg2

class Ui_Login_page(object):
    def setupUi(self, Login_page):
        if not Login_page.objectName():
            Login_page.setObjectName(u"Login_page")
        Login_page.resize(1280, 720)
        Login_page.setMinimumSize(QSize(1280, 720))
        Login_page.setMaximumSize(QSize(1280, 720))
        Login_page.setMouseTracking(False)
        Login_page.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Login_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 920))
        self.centralwidget.setMaximumSize(QSize(1280, 920))
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.login_image = QLabel(self.centralwidget)
        self.login_image.setObjectName(u"login_image")
        self.login_image.setGeometry(QRect(530, 0, 751, 721))
        self.login_image.setPixmap(QPixmap(u"Images/login_image.jpg"))
        self.login_image.setScaledContents(True)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(-10, 40, 531, 251))
        self.logo.setPixmap(QPixmap(u"Images/logo-black.png"))
        self.logo.setScaledContents(True)
        self.sign_in_text = QLabel(self.centralwidget)
        self.sign_in_text.setObjectName(u"sign_in_text")
        self.sign_in_text.setGeometry(QRect(200, 260, 111, 41))
        font = QFont()
        font.setFamilies([u"Ebrima"])
        font.setPointSize(20)
        font.setBold(True)
        self.sign_in_text.setFont(font)
        self.sign_in_text.setStyleSheet(u"color: rgb(50, 82, 110);")
        self.HR_ID = QLabel(self.centralwidget)
        self.HR_ID.setObjectName(u"HR_ID")
        self.HR_ID.setGeometry(QRect(120, 340, 71, 21))
        font1 = QFont()
        font1.setFamilies([u"Catamaran ExtraLight"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.HR_ID.setFont(font1)
        self.HR_ID.setStyleSheet(u"color: rgb(50, 82, 110);")
        self.Password = QLabel(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(40, 430, 201, 21))
        font2 = QFont()
        font2.setFamilies([u"Catamaran ExtraLight"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.Password.setFont(font2)
        self.Password.setStyleSheet(u"margin-left:76px;\n"
"color: rgb(50, 82, 110);")
        self.HR_ID_BOX = QLineEdit(self.centralwidget)
        self.HR_ID_BOX.setObjectName(u"HR_ID_BOX")
        self.HR_ID_BOX.setGeometry(QRect(40, 380, 350, 30))
        self.HR_ID_BOX.setMinimumSize(QSize(350, 25))
        self.HR_ID_BOX.setMaximumSize(QSize(350, 30))
        self.HR_ID_BOX.setStyleSheet(u"margin-left:80px;\n"
"border:1px solid;\n"
"border-radius:10px\n"
"")
        self.password_box = QLineEdit(self.centralwidget)
        self.password_box.setObjectName(u"password_box")
        self.password_box.setGeometry(QRect(40, 460, 350, 30))
        self.password_box.setMaximumSize(QSize(350, 30))
        self.password_box.setStyleSheet(u"margin-left:80px;\n"
"border:1px solid;\n"
"border-radius:10px")
        self.password_box.setEchoMode(QLineEdit.Password)
        self.Sign_in_button = QPushButton(self.centralwidget)
        self.Sign_in_button.setObjectName(u"Sign_in_button")
        self.Sign_in_button.setGeometry(QRect(190, 560, 111, 41))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.Sign_in_button.setFont(font3)
        self.Sign_in_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Sign_in_button.setStyleSheet(u"border:2px solid;\n"
"border-radius:10px;\n"
"background-color:rgb(50, 82, 110);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Sign_in_button.clicked.connect(self.check_credentials)
        Login_page.setCentralWidget(self.centralwidget)
        self.employee_radio_button = QRadioButton(self.centralwidget)
        self.employee_radio_button.setObjectName(u"employee_radio_button")
        self.employee_radio_button.setGeometry(QRect(130, 520, 111, 31))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.employee_radio_button.setFont(font4)
        self.employee_radio_button.setStyleSheet(u"color: rgb(50, 82, 110);")
        self.employee_radio_button.setText(QCoreApplication.translate("Login_page", u"Employee", None))

        self.admin_radio_button = QRadioButton(self.centralwidget)
        self.admin_radio_button.setObjectName(u"admin_radio_button")
        self.admin_radio_button.setGeometry(QRect(270, 520, 111, 31))
        self.admin_radio_button.setFont(font4)
        self.admin_radio_button.setStyleSheet(u"color: rgb(50, 82, 110);")
        self.admin_radio_button.setText(QCoreApplication.translate("Login_page", u"Admin", None))

        self.Sign_in_button.clicked.connect(self.check_credentials)

        Login_page.setCentralWidget(self.centralwidget)
        self.retranslateUi(Login_page)

        QMetaObject.connectSlotsByName(Login_page)

        self.retranslateUi(Login_page)

        QMetaObject.connectSlotsByName(Login_page)
    # setupUi

    def check_credentials(self):
        
        
        is_employee = self.employee_radio_button.isChecked()
        is_admin = self.admin_radio_button.isChecked()
        email = self.HR_ID_BOX.text()
        password = self.password_box.text()
        if is_employee and not is_admin:
            self.connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )

            # Create a cursor object to execute SQL queries
            self.cursor = self.connection.cursor()


            # Execute the SELECT query
            query = "SELECT * FROM Employee WHERE email = %s AND password = %s;"
            self.cursor.execute(query, (email, password))

            # Fetch the result
            result = self.cursor.fetchone()
            self.cursor.close()
            self.connection.close()
            if result:
                id=result[0]
                self.authenticate_user(id)
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")

        elif is_admin and not is_employee:
            if email==admin_email and password==admin_pass:
                self.authenticate_admin()
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")
        else:
            QMessageBox.warning(self, "Login Failed", "Please select either Employee or Admin.")
    def authenticate_user(self,employee_id):

        self.close()
        
        # Pass the employee ID to the EmployeePage instance
        employee_page = employee.EmployeePage(employee_id)
        employee_page.show()
    
    def authenticate_admin(self):
        self.close()
        admin_page = admin.AdminPage()
        admin_page.show()
        admin_page.exec_()     

            
        

    def retranslateUi(self, Login_page):
        Login_page.setWindowTitle(QCoreApplication.translate("Login_page", u"MainWindow", None))
        self.login_image.setText("")
        self.logo.setText("")
        self.sign_in_text.setText(QCoreApplication.translate("Login_page", u"Sign In", None))
        self.HR_ID.setText(QCoreApplication.translate("Login_page", u"Email.", None))
        self.Password.setText(QCoreApplication.translate("Login_page", u"Password.", None))
        self.HR_ID_BOX.setPlaceholderText(QCoreApplication.translate("Login_page", u"Enter your ID", None))
        self.password_box.setPlaceholderText(QCoreApplication.translate("Login_page", u"Enter password", None))
        self.Sign_in_button.setText(QCoreApplication.translate("Login_page", u"Sign In", None))

    # retranslateUi


class LoginPage(QMainWindow, Ui_Login_page):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)

        

    

if __name__ == "__main__":
    app = QApplication([])
    login_page = LoginPage()
    login_page.show()
    app.exec_()