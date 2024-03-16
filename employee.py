from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QToolBox,
QWidget,QMessageBox,QTableWidget, QTableWidgetItem,QVBoxLayout,QItemDelegate,QSpinBox,QDateEdit,QAbstractItemView,QTextEdit,QDialog,QHBoxLayout)

import psycopg2
from datetime import datetime, timedelta
import login_page
class SideBar(QGroupBox):
        def __init__(self,Page,employee_instance,empid):
                super(SideBar, self).__init__(Page)
                self.employee=employee_instance
                self.emp_id=empid
                self.page=Page
                self.setObjectName("side_bar")
                self.setGeometry(0, 0, 350, 722)
                self.setMinimumSize(350, 722)
                self.setMaximumSize(350, 722)
                self.setStyleSheet("background-color: rgb(50, 82, 110);")
                self.logo = QLabel(self)
                self.logo.setObjectName(u"logo ")
                self.logo.setGeometry(QRect(0, 20, 341, 191))
                self.logo.setPixmap(QPixmap(u"Images/logo-grey.png"))
                self.logo.setScaledContents(True)
                self.leave_application = QPushButton(self)
                self.leave_application.setObjectName(u"leave_application")
                self.leave_application.setGeometry(QRect(0, 470, 348, 65))
                self.leave_application.setMinimumSize(QSize(348, 65))
                self.leave_application.setMaximumSize(QSize(348, 65))
                self.leave_application.setCursor(QCursor(Qt.PointingHandCursor))
                self.leave_application.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
        "color: rgb(230, 230, 230);")
                self.profile = QPushButton(self)
                self.profile.setObjectName(u"profile")
                self.profile.setGeometry(QRect(0, 210, 348, 65))
                self.profile.setMinimumSize(QSize(348, 65))
                self.profile.setMaximumSize(QSize(348, 65))
                self.profile.setCursor(QCursor(Qt.PointingHandCursor))
                self.profile.setStyleSheet(u"font: 20pt \"Sitka\";\n"
        "color: rgb(230, 230, 230);")
                self.salary = QPushButton(self)
                self.salary.setObjectName(u"salary")
                self.salary.setGeometry(QRect(0, 405, 348, 65))
                self.salary.setMinimumSize(QSize(348, 65))
                self.salary.setMaximumSize(QSize(348, 65))
                self.salary.setCursor(QCursor(Qt.PointingHandCursor))
                self.salary.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
        "color: rgb(230, 230, 230);")
                self.leave_report = QPushButton(self)
                self.leave_report.setObjectName(u"leave_report")
                self.leave_report.setGeometry(QRect(0, 275, 348, 65))
                self.leave_report.setMinimumSize(QSize(348, 65))
                self.leave_report.setMaximumSize(QSize(348, 65))
                self.leave_report.setCursor(QCursor(Qt.PointingHandCursor))
                self.leave_report.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
        "color: rgb(230, 230, 230);")
                self.attendance = QPushButton(self)
                self.attendance.setObjectName(u"attendance")
                self.attendance.setGeometry(QRect(0, 340, 348, 65))
                self.attendance.setMinimumSize(QSize(348, 65))
                self.attendance.setMaximumSize(QSize(348, 65))
                self.attendance.setCursor(QCursor(Qt.PointingHandCursor))
                self.attendance.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
        "color: rgb(230, 230, 230);")
                self.sign_out = QPushButton(self)
                self.sign_out.setObjectName(u"sign_out")
                self.sign_out.setGeometry(QRect(0, 660, 348, 65))
                self.sign_out.setMinimumSize(QSize(348, 65))
                self.sign_out.setMaximumSize(QSize(348, 65))
                self.sign_out.setCursor(QCursor(Qt.PointingHandCursor))
                self.sign_out.setStyleSheet(u"font: italic 18pt \"Sitka\" rgb(255, 255, 255);\n"
        "color: rgb(230, 230, 230);")
                icon = QIcon()
                icon.addFile(u"Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.Off)
                icon.addFile(u"Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.On)
                self.sign_out.setIcon(icon)
                self.sign_out.setIconSize(QSize(30, 30))
                self.sign_out.clicked.connect(self.employee.signout)
                self.translateUI()
        
        def translateUI(self):
                self.setTitle("")
                self.logo.setText("")
                self.leave_application.setText(QCoreApplication.translate("Employee_Page", u"Leave Application", None))
                self.profile.setText(QCoreApplication.translate("Employee_Page", u"Profile", None))
                self.salary.setText(QCoreApplication.translate("Employee_Page", u"Salary", None))
                self.leave_report.setText(QCoreApplication.translate("Employee_Page", u"Leave Report", None))
                self.attendance.setText(QCoreApplication.translate("Employee_Page", u"Attendance", None))
                self.sign_out.setText(QCoreApplication.translate("Employee_Page", u"  Sign Out ", None))

        def setup_connections(self, stacked_widget):
                self.profile.clicked.connect(lambda: self.setprofilepage(stacked_widget))
                self.leave_report.clicked.connect(lambda: self.setleavereportpage(stacked_widget))
                self.attendance.clicked.connect(lambda: self.setattendancepage(stacked_widget))
                self.salary.clicked.connect(lambda: self.setsalarypage(stacked_widget))
                self.leave_application.clicked.connect(lambda: self.setapplicationpage(stacked_widget))

        def setprofilepage(self, stacked_widget):
                current_index = stacked_widget.currentIndex()
                if current_index != -1:
                        current_widget = stacked_widget.widget(current_index)
                        stacked_widget.removeWidget(current_widget)
                        current_widget.deleteLater()
                new_profile_page = Profile(self.page,self.emp_id)
                stacked_widget.addWidget(new_profile_page)
                new_index = stacked_widget.indexOf(new_profile_page)
                stacked_widget.setCurrentIndex(new_index)

        def setleavereportpage(self, stacked_widget):
                current_index = stacked_widget.currentIndex()
                if current_index != -1:
                        current_widget = stacked_widget.widget(current_index)
                        stacked_widget.removeWidget(current_widget)
                        current_widget.deleteLater()
                new_leave_page = leavereportpage(self.page,self.emp_id)
                stacked_widget.addWidget(new_leave_page)
                new_index = stacked_widget.indexOf(new_leave_page)
                stacked_widget.setCurrentIndex(new_index)

        def setattendancepage(self, stacked_widget):
                current_index = stacked_widget.currentIndex()
                if current_index != -1:
                        current_widget = stacked_widget.widget(current_index)
                        stacked_widget.removeWidget(current_widget)
                        current_widget.deleteLater()
                new_attendance_page = attendancepage(self.page,self.emp_id)
                stacked_widget.addWidget(new_attendance_page)
                new_index = stacked_widget.indexOf(new_attendance_page)
                stacked_widget.setCurrentIndex(new_index)

        def setsalarypage(self, stacked_widget):
                current_index = stacked_widget.currentIndex()
                if current_index != -1:
                        current_widget = stacked_widget.widget(current_index)
                        stacked_widget.removeWidget(current_widget)
                        current_widget.deleteLater()
                new_salary_page = salarypage(self.page,self.emp_id)
                stacked_widget.addWidget(new_salary_page)
                new_index = stacked_widget.indexOf(new_salary_page)
                stacked_widget.setCurrentIndex(new_index)

        def setapplicationpage(self, stacked_widget):
                current_index = stacked_widget.currentIndex()
                if current_index != -1:
                        current_widget = stacked_widget.widget(current_index)
                        stacked_widget.removeWidget(current_widget)
                        current_widget.deleteLater()
                new_application_page = applicationpage(self.page,self.emp_id)
                stacked_widget.addWidget(new_application_page)
                new_index = stacked_widget.indexOf(new_application_page)
                stacked_widget.setCurrentIndex(new_index)
    
class Profile(QWidget):
        def __init__(self,Page,id):
                super(Profile, self).__init__(Page)
                self.emp_id=id
                self.setObjectName(u"Profile_Page")
                self.l_name = QGroupBox(self)
                self.l_name.setObjectName(u"l_name")
                self.l_name.setGeometry(QRect(450, 230, 121, 41))
                self.l_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_11 = QHBoxLayout(self.l_name)
                self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
                self.address = QGroupBox(self)
                self.address.setObjectName(u"address")
                self.address.setGeometry(QRect(10, 350, 121, 40))
                self.address.setMinimumSize(QSize(0, 40))
                self.address.setMaximumSize(QSize(16777215, 40))
                self.address.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_13 = QHBoxLayout(self.address)
                self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
                self.salary_input = QGroupBox(self)
                self.salary_input.setObjectName(u"salary_input")
                self.salary_input.setGeometry(QRect(570, 410, 300, 40))
                self.salary_input.setMinimumSize(QSize(300, 40))
                self.salary_input.setMaximumSize(QSize(300, 40))
                self.salary_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_17 = QHBoxLayout(self.salary_input)
                self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
                self.absent_input = QGroupBox(self)
                self.absent_input.setObjectName(u"absent_input")
                self.absent_input.setGeometry(QRect(130, 640, 100, 40))
                self.absent_input.setMinimumSize(QSize(100, 40))
                self.absent_input.setMaximumSize(QSize(100, 40))
                self.absent_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_49 = QHBoxLayout(self.absent_input)
                self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
                self.pending_applications_input = QGroupBox(self)
                self.pending_applications_input.setObjectName(u"pending_applications_input")
                self.pending_applications_input.setGeometry(QRect(770, 580, 100, 40))
                self.pending_applications_input.setMinimumSize(QSize(100, 40))
                self.pending_applications_input.setMaximumSize(QSize(100, 40))
                self.pending_applications_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_50 = QHBoxLayout(self.pending_applications_input)
                self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
                self.f_name_input = QGroupBox(self)
                self.f_name_input.setObjectName(u"f_name_input")
                self.f_name_input.setGeometry(QRect(130, 230, 320, 40))
                self.f_name_input.setMinimumSize(QSize(320, 40))
                self.f_name_input.setMaximumSize(QSize(290, 40))
                self.f_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_18 = QHBoxLayout(self.f_name_input)
                self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
                self.f_name = QGroupBox(self)
                self.f_name.setObjectName(u"f_name")
                self.f_name.setGeometry(QRect(10, 230, 121, 40))
                self.f_name.setMinimumSize(QSize(0, 40))
                self.f_name.setMaximumSize(QSize(16777215, 40))
                self.f_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_19 = QHBoxLayout(self.f_name)
                self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
                self.l_name_input = QGroupBox(self)
                self.l_name_input.setObjectName(u"l_name_input")
                self.l_name_input.setGeometry(QRect(570, 230, 300, 40))
                self.l_name_input.setMinimumSize(QSize(300, 40))
                self.l_name_input.setMaximumSize(QSize(300, 40))
                self.l_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout0 = QHBoxLayout(self.l_name_input)
                self.horizontalLayout0.setObjectName(u"horizontalLayout0")
                self.pending_applications = QGroupBox(self)
                self.pending_applications.setObjectName(u"pending_applications")
                self.pending_applications.setGeometry(QRect(500, 580, 261, 41))
                self.pending_applications.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_51 = QHBoxLayout(self.pending_applications)
                self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
                self.salary_4 = QGroupBox(self)
                self.salary_4.setObjectName(u"salary_4")
                self.salary_4.setGeometry(QRect(450, 410, 121, 40))
                self.salary_4.setMinimumSize(QSize(0, 40))
                self.salary_4.setMaximumSize(QSize(16777215, 40))
                self.salary_4.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout1 = QHBoxLayout(self.salary_4)
                self.horizontalLayout1.setObjectName(u"horizontalLayout1")
                self.email = QGroupBox(self)
                self.email.setObjectName(u"email")
                self.email.setGeometry(QRect(10, 290, 121, 40))
                self.email.setMinimumSize(QSize(0, 40))
                self.email.setMaximumSize(QSize(16777215, 40))
                self.email.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout2 = QHBoxLayout(self.email)
                self.horizontalLayout2.setObjectName(u"horizontalLayout2")
                self.leave = QGroupBox(self)
                self.leave.setObjectName(u"leave")
                self.leave.setGeometry(QRect(250, 640, 121, 41))
                self.leave.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_52 = QHBoxLayout(self.leave)
                self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
                self.contact = QGroupBox(self)
                self.contact.setObjectName(u"contact")
                self.contact.setGeometry(QRect(450, 290, 121, 41))
                self.contact.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout3 = QHBoxLayout(self.contact)
                self.horizontalLayout3.setObjectName(u"horizontalLayout3")
                self.present = QGroupBox(self)
                self.present.setObjectName(u"present")
                self.present.setGeometry(QRect(250, 580, 121, 41))
                self.present.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_53 = QHBoxLayout(self.present)
                self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
                self.current_deduction = QGroupBox(self)
                self.current_deduction.setObjectName(u"current_deduction")
                self.current_deduction.setGeometry(QRect(500, 640, 261, 41))
                self.current_deduction.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_54 = QHBoxLayout(self.current_deduction)
                self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
                self.head_dep = QGroupBox(self)
                self.head_dep.setObjectName(u"head_dep")
                self.head_dep.setGeometry(QRect(10, 60, 561, 40))
                self.head_dep.setMinimumSize(QSize(0, 40))
                self.head_dep.setMaximumSize(QSize(16777215, 40))
                self.head_dep.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 500 18pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_22 = QHBoxLayout(self)
                self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
                self.contact_input = QGroupBox(self)
                self.contact_input.setObjectName(u"contact_input")
                self.contact_input.setGeometry(QRect(570, 290, 300, 40))
                self.contact_input.setMinimumSize(QSize(300, 40))
                self.contact_input.setMaximumSize(QSize(300, 40))
                self.contact_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout4 = QHBoxLayout(self.contact_input)
                self.horizontalLayout4.setObjectName(u"horizontalLayout4")
                self.General_info = QLabel(self)
                self.General_info.setObjectName(u"General_info")
                self.General_info.setGeometry(QRect(0, 130, 925, 60))
                font = QFont()
                font.setPointSize(25)
                font.setBold(True)
                self.General_info.setFont(font)
                self.General_info.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: \"#e6e6e6\";")
                self.General_info.setAlignment(Qt.AlignCenter)

                self.email_input = QGroupBox(self)
                self.email_input.setObjectName(u"email_input")
                self.email_input.setGeometry(QRect(130, 290, 320, 40))
                self.email_input.setMinimumSize(QSize(320, 40))
                self.email_input.setMaximumSize(QSize(320, 40))
                self.email_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout5 = QHBoxLayout(self.email_input)
                self.horizontalLayout5.setObjectName(u"horizontalLayout5")
                self.Current_Month = QLabel(self)
                self.Current_Month.setObjectName(u"Current_Month")
                self.Current_Month.setGeometry(QRect(0, 480, 925, 60))
                self.Current_Month.setFont(font)
                self.Current_Month.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: \"#e6e6e6\";")
                self.Current_Month.setAlignment(Qt.AlignCenter)
                self.department = QGroupBox(self)
                self.department.setObjectName(u"department")
                self.department.setGeometry(QRect(10, 410, 121, 40))
                self.department.setMinimumSize(QSize(0, 40))
                self.department.setMaximumSize(QSize(16777215, 40))
                self.department.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout6 = QHBoxLayout(self.department)
                self.horizontalLayout6.setObjectName(u"horizontalLayout6")
                self.current_deduction_input = QGroupBox(self)
                self.current_deduction_input.setObjectName(u"current_deduction_input")
                self.current_deduction_input.setGeometry(QRect(770, 640, 100, 40))
                self.current_deduction_input.setMinimumSize(QSize(100, 40))
                self.current_deduction_input.setMaximumSize(QSize(100, 40))
                self.current_deduction_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_55 = QHBoxLayout(self.current_deduction_input)
                self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
                self.department_input = QGroupBox(self)
                self.department_input.setObjectName(u"department_input")
                self.department_input.setGeometry(QRect(130, 410, 320, 40))
                self.department_input.setMinimumSize(QSize(320, 40))
                self.department_input.setMaximumSize(QSize(320, 40))
                self.department_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout7 = QHBoxLayout(self.department_input)
                self.horizontalLayout7.setObjectName(u"horizontalLayout7")
                self.leave_input = QGroupBox(self)
                self.leave_input.setObjectName(u"leave_input")
                self.leave_input.setGeometry(QRect(370, 640, 100, 40))
                self.leave_input.setMinimumSize(QSize(100, 40))
                self.leave_input.setMaximumSize(QSize(100, 40))
                self.leave_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_56 = QHBoxLayout(self.leave_input)
                self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
                self.absent = QGroupBox(self)
                self.absent.setObjectName(u"absent")
                self.absent.setGeometry(QRect(10, 640, 121, 40))
                self.absent.setMinimumSize(QSize(0, 40))
                self.absent.setMaximumSize(QSize(16777215, 40))
                self.absent.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_57 = QHBoxLayout(self.absent)
                self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
                self.address_input = QGroupBox(self)
                self.address_input.setObjectName(u"address_input")
                self.address_input.setGeometry(QRect(130, 350, 750, 40))
                self.address_input.setMinimumSize(QSize(750, 40))
                self.address_input.setMaximumSize(QSize(750, 40))
                self.address_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout8 = QHBoxLayout(self.address_input)
                self.horizontalLayout8.setObjectName(u"horizontalLayout8")
                self.Head_name = QGroupBox(self)
                self.Head_name.setObjectName(u"Head_name")
                self.Head_name.setGeometry(QRect(10, 20, 561, 40))
                self.Head_name.setMinimumSize(QSize(0, 40))
                self.Head_name.setMaximumSize(QSize(16777215, 40))
                self.Head_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 24pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_31 = QHBoxLayout(self.Head_name)
                self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
                self.present_input = QGroupBox(self)
                self.present_input.setObjectName(u"present_input")
                self.present_input.setGeometry(QRect(370, 580, 100, 40))
                self.present_input.setMinimumSize(QSize(100, 40))
                self.present_input.setMaximumSize(QSize(100, 40))
                self.present_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_58 = QHBoxLayout(self.present_input)
                self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
                self.total_days = QGroupBox(self)
                self.total_days.setObjectName(u"total_days")
                self.total_days.setGeometry(QRect(10, 580, 121, 40))
                self.total_days.setMinimumSize(QSize(0, 40))
                self.total_days.setMaximumSize(QSize(16777215, 40))
                self.total_days.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_59 = QHBoxLayout(self.total_days)
                self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
                self.total_days_input = QGroupBox(self)
                self.total_days_input.setObjectName(u"total_days_input")
                self.total_days_input.setGeometry(QRect(130, 580, 100, 40))
                self.total_days_input.setMinimumSize(QSize(100, 40))
                self.total_days_input.setMaximumSize(QSize(100, 40))
                self.total_days_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 14pt \"Segoe UI\";\n"
        "")
                self.horizontalLayout_60 = QHBoxLayout(self.total_days_input)
                self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
                self.load_employee_data(self.emp_id)
                self.translateUI()

        def translateUI(self):
                self.l_name.setTitle(QCoreApplication.translate("Employee_Page", u"Last Name", None))
                self.address.setTitle(QCoreApplication.translate("Employee_Page", u"Address", None))
        
                self.f_name.setTitle(QCoreApplication.translate("Employee_Page", u"First Name", None))
                
                self.pending_applications.setTitle(QCoreApplication.translate("Employee_Page", u"Pending Leave Applications", None))
                self.salary_4.setTitle(QCoreApplication.translate("Employee_Page", u"Salary", None))
                self.email.setTitle(QCoreApplication.translate("Employee_Page", u"Email", None))
                self.leave.setTitle(QCoreApplication.translate("Employee_Page", u"Leave", None))
                self.contact.setTitle(QCoreApplication.translate("Employee_Page", u"Contact", None))
                self.present.setTitle(QCoreApplication.translate("Employee_Page", u"Present", None))
                self.current_deduction.setTitle(QCoreApplication.translate("Employee_Page", u"Current Salary Deduction", None))
                
                self.General_info.setText(QCoreApplication.translate("Employee_Page", u" General Information", None))
                self.Current_Month.setText(QCoreApplication.translate("Employee_Page", u"Current Month Details", None))
                self.department.setTitle(QCoreApplication.translate("Employee_Page", u"Department", None))
                self.absent.setTitle(QCoreApplication.translate("Employee_Page", u"Absent", None))
                
                self.total_days.setTitle(QCoreApplication.translate("Employee_Page", u"Total Days", None))

        def load_employee_data(self, employee_id):
                # Connect to the PostgreSQL database
                db_connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
                )

                # Create a cursor object to interact with the database
                cursor = db_connection.cursor()

                # Fetch employee data based on the provided employee_id
                query = f"SELECT * FROM Employee WHERE id = '{employee_id}';"
                cursor.execute(query)
                employee_data = cursor.fetchone()

                if employee_data:
                        # Update the profile page with the retrieved data
                        self.Head_name.setTitle(QCoreApplication.translate("Employee_Page", employee_data[1] + " " + employee_data[2], None))
                        self.head_dep.setTitle(QCoreApplication.translate("Employee_Page", f"{employee_data[6]} Department", None))
                        self.f_name_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[1], None))
                        self.l_name_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[2], None))
                        self.address_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[5], None))
                        self.contact_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[8], None))
                        self.email_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[3], None))
                        self.salary_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[7], None))
                        self.department_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[6], None))

                        # Get the current month and year
                        current_month = datetime.now().strftime('%Y-%m')

                        # Query to get count of presents, absents, pending leaves, and accepted leaves for the current month
                        query = """
                                SELECT
                                        COALESCE((SELECT COUNT(*) FROM Attendance WHERE employee_id = %s AND status = 'P' AND EXTRACT(YEAR FROM date_) = EXTRACT(YEAR FROM TO_DATE(%s, 'YYYY-MM')) AND EXTRACT(MONTH FROM date_) = EXTRACT(MONTH FROM TO_DATE(%s, 'YYYY-MM'))), 0) AS present_count,
                                        COALESCE((SELECT COUNT(*) FROM Attendance WHERE employee_id = %s AND status = 'A' AND EXTRACT(YEAR FROM date_) = EXTRACT(YEAR FROM TO_DATE(%s, 'YYYY-MM')) AND EXTRACT(MONTH FROM date_) = EXTRACT(MONTH FROM TO_DATE(%s, 'YYYY-MM'))), 0) AS absent_count,
                                        COALESCE((SELECT COUNT(*) FROM Leave_Record WHERE employee_id = %s AND status = 'pending' AND (EXTRACT(YEAR FROM start_date) = EXTRACT(YEAR FROM TO_DATE(%s, 'YYYY-MM')) AND EXTRACT(MONTH FROM start_date) = EXTRACT(MONTH FROM TO_DATE(%s, 'YYYY-MM')) OR EXTRACT(YEAR FROM end_date) = EXTRACT(YEAR FROM TO_DATE(%s, 'YYYY-MM')) AND EXTRACT(MONTH FROM end_date) = EXTRACT(MONTH FROM TO_DATE(%s, 'YYYY-MM')))), 0) AS pending_leave_count,
                                        COALESCE((SELECT COUNT(*) FROM Leave_Record WHERE employee_id = %s AND status = 'accepted' AND (EXTRACT(YEAR FROM start_date) = EXTRACT(YEAR FROM TO_DATE(%s, 'YYYY-MM')) AND EXTRACT(MONTH FROM start_date) = EXTRACT(MONTH FROM TO_DATE(%s, 'YYYY-MM')) OR EXTRACT(YEAR FROM end_date) = EXTRACT(YEAR FROM TO_DATE(%s, 'YYYY-MM')) AND EXTRACT(MONTH FROM end_date) = EXTRACT(MONTH FROM TO_DATE(%s, 'YYYY-MM')))), 0) AS accepted_leave_count
                                """

                        # Execute the query
                        params = (
                        employee_id, current_month, current_month,
                        employee_id, current_month, current_month,
                        employee_id, current_month, current_month, current_month, current_month,
                        employee_id, current_month, current_month, current_month, current_month
                        )

                        results = self.execute_query(cursor, query, params)


                        # Display the results
                        present_count, absent_count, pending_leave_count, accepted_leave_count = results
                        deduction = float(employee_data[7]) / 30 * (absent_count - accepted_leave_count)
                        self.absent_input.setTitle(QCoreApplication.translate("Employee_Page", str(absent_count), None))
                        self.total_days_input.setTitle(QCoreApplication.translate("Employee_Page", str(absent_count + present_count), None))
                        self.present_input.setTitle(QCoreApplication.translate("Employee_Page", str(present_count), None))
                        self.current_deduction_input.setTitle(QCoreApplication.translate("Employee_Page", str(deduction), None))
                        self.leave_input.setTitle(QCoreApplication.translate("Employee_Page", str(accepted_leave_count), None))
                        self.pending_applications_input.setTitle(QCoreApplication.translate("Employee_Page", str(pending_leave_count), None))

                # Close the cursor and database connection
                cursor.close()
                db_connection.close()

        def execute_query(self, cursor, query, params=None):
                if params:
                        cursor.execute(query, params)
                else:
                        cursor.execute(query)
                result = cursor.fetchone()
                return result

class leavereportpage(QWidget):
        def __init__(self,Page,id):
                super(leavereportpage, self).__init__(Page)
                self.emp_id=id
                self.setObjectName(u"leave_report")
                self.title = QLabel(self)
                self.title.setObjectName(u"title")
                self.title.setGeometry(QRect(0, 30, 925, 60))
                font = QFont()
                font.setPointSize(25)
                font.setBold(True)
                self.title.setFont(font)
                self.title.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: \"#e6e6e6\";")
                self.remaining_health = QLabel(self)
                self.remaining_health.setObjectName(u"remaining_health")
                self.remaining_health.setGeometry(QRect(570, 160, 30, 41))
                font1 = QFont()
                font1.setFamilies([u"Segoe UI"])
                font1.setPointSize(16)
                font1.setWeight(QFont.DemiBold)
                font1.setItalic(False)
                self.remaining_health.setFont(font1)
                self.remaining_health.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "\n"
        "font: 600 16pt \"Segoe UI\";")
                self.total = QLabel(self)
                self.total.setObjectName(u"total")
                self.total.setGeometry(QRect(290, 130, 120, 40))
                font2 = QFont()
                font2.setFamilies([u"Segoe UI"])
                font2.setPointSize(16)
                font2.setWeight(QFont.Black)
                font2.setItalic(False)
                self.total.setFont(font2)
                self.total.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 900 16pt \"Segoe UI\";")
                self.total_general = QLabel(self)
                self.total_general.setObjectName(u"total_general")
                self.total_general.setGeometry(QRect(450, 130, 30, 40))
                self.total_general.setFont(font1)
                self.total_general.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 600 16pt \"Segoe UI\";")
                self.health = QLabel(self)
                self.health.setObjectName(u"health")
                self.health.setGeometry(QRect(550, 100, 100, 40))
                self.health.setFont(font2)
                self.health.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 900 16pt \"Segoe UI\";")
                self.remaining_general = QLabel(self)
                self.remaining_general.setObjectName(u"remaining_general")
                self.remaining_general.setGeometry(QRect(450, 160, 30, 41))
                self.remaining_general.setFont(font1)
                self.remaining_general.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "\n"
        "font: 600 16pt \"Segoe UI\";")
                self.remaing = QLabel(self)
                self.remaing.setObjectName(u"remaing")
                self.remaing.setGeometry(QRect(270, 160, 120, 41))
                self.remaing.setFont(font2)
                self.remaing.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 900 16pt \"Segoe UI\";")
                self.general = QLabel(self)
                self.general.setObjectName(u"general")
                self.general.setGeometry(QRect(420, 100, 100, 40))
                self.general.setFont(font2)
                self.general.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 900 16pt \"Segoe UI\";")
                self.total_health = QLabel(self)
                self.total_health.setObjectName(u"total_health")
                self.total_health.setGeometry(QRect(570, 130, 30, 40))
                self.total_health.setFont(font1)
                self.total_health.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 600 16pt \"Segoe UI\";")
                self.leave_record = QTableWidget(self)
                if (self.leave_record.columnCount() < 3):
                        self.leave_record.setColumnCount(3)
                brush = QBrush(QColor(85, 55, 89, 255))
                brush.setStyle(Qt.SolidPattern)
                font3 = QFont()
                font3.setPointSize(12)
                font3.setBold(True)
                __qtablewidgetitem = QTableWidgetItem()
                __qtablewidgetitem.setFont(font3)
                __qtablewidgetitem.setBackground(QColor(85, 55, 89))
                __qtablewidgetitem.setForeground(brush)
                self.leave_record.setHorizontalHeaderItem(0, __qtablewidgetitem)
                __qtablewidgetitem1 = QTableWidgetItem()
                __qtablewidgetitem1.setFont(font3)
                __qtablewidgetitem1.setBackground(QColor(85, 55, 89))
                __qtablewidgetitem1.setForeground(brush)
                self.leave_record.setHorizontalHeaderItem(1, __qtablewidgetitem1)
                __qtablewidgetitem2 = QTableWidgetItem()
                __qtablewidgetitem2.setFont(font3)
                __qtablewidgetitem2.setBackground(QColor(85, 55, 89))
                __qtablewidgetitem2.setForeground(brush)
                self.leave_record.setHorizontalHeaderItem(2, __qtablewidgetitem2)
                self.leave_record.setObjectName(u"leave_record")
                self.leave_record.setGeometry(QRect(100, 220, 721, 461))
                self.leave_record.setStyleSheet(u"QHeaderView::section {\n"
        "    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
        "    color: rgb(230, 230, 230); /* Set the text color */\n"
        "};\n"
        "\n"
        "\n"
        "color: rgb(50, 84, 110);\n"
        "background-color: rgb(230, 230, 230);")
                self.leave_record.horizontalHeader().setDefaultSectionSize(237)
                self.load_leave_data(self.emp_id)
                self.translateUI()

        def translateUI(self):
                self.title.setText(QCoreApplication.translate("Employee_Page", u"                                         Leave Report", None))
                
                self.total.setText(QCoreApplication.translate("Employee_Page", u"Total", None))
                self.total_general.setText(QCoreApplication.translate("Employee_Page", u"15", None))
                self.health.setText(QCoreApplication.translate("Employee_Page", u"Health", None))
                
                self.remaing.setText(QCoreApplication.translate("Employee_Page", u"Remaining", None))
                self.general.setText(QCoreApplication.translate("Employee_Page", u"General", None))
                self.total_health.setText(QCoreApplication.translate("Employee_Page", u"10", None))
                ___qtablewidgetitem = self.leave_record.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("Employee_Page", u"Date", None))
                ___qtablewidgetitem1 = self.leave_record.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("Employee_Page", u"Type", None))
                ___qtablewidgetitem2 = self.leave_record.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("Employee_Page", u"Status", None))

        def load_leave_data(self, employee_id):
                # Connect to the PostgreSQL database (adjust connection parameters accordingly)
                connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
                )

                 # Create a cursor
                cursor = connection.cursor()

                # Query to get count of general and health leaves that are accepted
                query = """
                        SELECT
                                COALESCE((SELECT COUNT(*) FROM Leave_Record WHERE employee_id = %s AND category = 'general' AND status = 'accepted'), 0) AS general_leave_count,
                                COALESCE((SELECT COUNT(*) FROM Leave_Record WHERE employee_id = %s AND category = 'health' AND status = 'accepted'), 0) AS health_leave_count
                """

                # Execute the query
                cursor.execute(query, (employee_id, employee_id))

                # Fetch the result
                result = cursor.fetchone()

                self.remaining_health.setText(QCoreApplication.translate("Employee_Page", str(10-result[1]), None))
                self.remaining_general.setText(QCoreApplication.translate("Employee_Page", str(15-result[0]), None))

                    # Query to retrieve leave data for a specific employee
                query = """
                        SELECT start_date, category, status
                        FROM Leave_Record
                        WHERE employee_id = %s
                """

                # Execute the query
                cursor.execute(query, (employee_id,))

                # Fetch all rows
                leave_data = cursor.fetchall()

                # Clear existing items in the table
                self.leave_record.setRowCount(0)

                # Populate the table with data
                for row, (start_date, category, status) in enumerate(leave_data):
                        self.leave_record.insertRow(row)
                        self.leave_record.setItem(row, 0, QTableWidgetItem(str(start_date)))
                        self.leave_record.setItem(row, 1, QTableWidgetItem(category))
                        self.leave_record.setItem(row, 2, QTableWidgetItem(status))
                # Close the cursor and connection
                cursor.close()
                connection.close()

class attendancepage(QWidget):
        def __init__(self,Page,id):
                super(attendancepage, self).__init__(Page)
                self.emp_id=id
                self.setObjectName(u"attendance")
                self.dec = QPushButton(self)
                self.dec.setObjectName(u"dec")
                font3 = QFont()
                font3.setPointSize(12)
                font3.setBold(True)
                self.dec.setGeometry(QRect(830, 170, 90, 30))
                self.dec.setFont(font3)
                self.dec.setCursor(QCursor(Qt.PointingHandCursor))
                self.dec.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.dec.clicked.connect (lambda: self.load_attendance_data('12'))

                self.sep = QPushButton(self)
                self.sep.setObjectName(u"sep")
                self.sep.setGeometry(QRect(529, 170, 92, 30))
                self.sep.setFont(font3)
                self.sep.setCursor(QCursor(Qt.PointingHandCursor))
                self.sep.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.sep.clicked.connect (lambda: self.load_attendance_data('09'))

                self.april = QPushButton(self)
                self.april.setObjectName(u"april")
                self.april.setGeometry(QRect(580, 130, 90, 30))
                self.april.setFont(font3)
                self.april.setCursor(QCursor(Qt.PointingHandCursor))
                self.april.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.april.clicked.connect (lambda: self.load_attendance_data('04'))
                
                self.march = QPushButton(self)
                self.march.setObjectName(u"march")
                self.march.setGeometry(QRect(480, 130, 90, 30))
                self.march.setFont(font3)
                self.march.setCursor(QCursor(Qt.PointingHandCursor))
                self.march.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px\n"
        "")
                self.march.clicked.connect (lambda: self.load_attendance_data('03'))

                self.oct = QPushButton(self)
                self.oct.setObjectName(u"oct")
                self.oct.setGeometry(QRect(630, 170, 90, 30))
                self.oct.setFont(font3)
                self.oct.setCursor(QCursor(Qt.PointingHandCursor))
                self.oct.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.oct.clicked.connect (lambda: self.load_attendance_data('10'))

                self.feb = QPushButton(self)
                self.feb.setObjectName(u"feb")
                self.feb.setGeometry(QRect(380, 130, 90, 30))
                self.feb.setFont(font3)
                self.feb.setCursor(QCursor(Qt.PointingHandCursor))
                self.feb.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.feb.clicked.connect (lambda: self.load_attendance_data('02'))

                self.jan = QPushButton(self)
                self.jan.setObjectName(u"jan")
                self.jan.setGeometry(QRect(280, 130, 90, 30))
                self.jan.setFont(font3)
                self.jan.setCursor(QCursor(Qt.PointingHandCursor))
                self.jan.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.jan.clicked.connect (lambda: self.load_attendance_data('01'))

                self.stackedWidget = QStackedWidget(self)
                self.stackedWidget.setObjectName(u"stackedWidget")
                self.stackedWidget.setGeometry(QRect(40, 230, 741, 481))
                self.stackedWidget.setStyleSheet(u"QHeaderView::section {\n"
        "    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
        "    color: rgb(230, 230, 230); /* Set the text color */\n"
        "};\n"
        "background-color: rgb(230, 230, 230);\n"
        "color: rgb(50, 84, 110);")
                self.first_page = QWidget()
                self.first_page.setObjectName(u"first_page")
                self.table_start = QTableWidget(self.first_page)
                if (self.table_start.columnCount() < 2):
                        self.table_start.setColumnCount(2)
                brush1 = QBrush(QColor(50, 84, 110, 255))
                brush1.setStyle(Qt.SolidPattern)
                font4 = QFont()
                font4.setPointSize(14)
                font4.setBold(True)
                __qtablewidgetitem3 = QTableWidgetItem()
                __qtablewidgetitem3.setFont(font4);
                __qtablewidgetitem3.setBackground(QColor(85, 55, 89));
                __qtablewidgetitem3.setForeground(brush1);
                self.table_start.setHorizontalHeaderItem(0, __qtablewidgetitem3)
                __qtablewidgetitem4 = QTableWidgetItem()
                __qtablewidgetitem4.setFont(font4);
                __qtablewidgetitem4.setBackground(QColor(85, 55, 89));
                __qtablewidgetitem4.setForeground(brush1);
                self.table_start.setHorizontalHeaderItem(1, __qtablewidgetitem4)
                self.table_start.setObjectName(u"table_start")
                self.table_start.setGeometry(QRect(110, 30, 621, 441))
                self.table_start.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
        "color: rgb(50, 84, 110);\n"
        "\n"
        "QHeaderView::section {\n"
        "    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
        "    color: rgb(230, 230, 230); /* Set the text color */\n"
        "};")
                self.table_start.horizontalHeader().setMinimumSectionSize(96)
                self.table_start.horizontalHeader().setDefaultSectionSize(305)
                self.stackedWidget.addWidget(self.first_page)
                self.second_page = QWidget()
                self.second_page.setObjectName(u"second_page")
                self.table_end = QTableWidget(self.second_page)
                if (self.table_end.columnCount() < 2):
                        self.table_end.setColumnCount(2)
                font5 = QFont()
                font5.setPointSize(14)
                font5.setBold(True)
                font5.setKerning(True)
                __qtablewidgetitem5 = QTableWidgetItem()
                __qtablewidgetitem5.setFont(font5);
                __qtablewidgetitem5.setBackground(QColor(230, 230, 230, 10));
                __qtablewidgetitem5.setForeground(brush1);
                self.table_end.setHorizontalHeaderItem(0, __qtablewidgetitem5)
                __qtablewidgetitem6 = QTableWidgetItem()
                __qtablewidgetitem6.setFont(font4);
                __qtablewidgetitem6.setBackground(QColor(230, 230, 230));
                __qtablewidgetitem6.setForeground(brush1);
                self.table_end.setHorizontalHeaderItem(1, __qtablewidgetitem6)
                self.table_end.setObjectName(u"table_end")
                self.table_end.setGeometry(QRect(110, 30, 621, 441))
                self.table_end.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
        "color: rgb(50, 84, 110);")
                self.table_end.horizontalHeader().setDefaultSectionSize(305)
                self.stackedWidget.addWidget(self.second_page)
                self.label = QLabel(self)
                self.label.setObjectName(u"label")
                self.label.setGeometry(QRect(10, 30, 915, 65))
                font6 = QFont()
                font6.setPointSize(25)
                font6.setBold(True)
                font6.setUnderline(False)
                font6.setStrikeOut(False)
                font6.setKerning(True)
                self.label.setFont(font6)
                self.label.setAutoFillBackground(False)
                self.label.setStyleSheet(u"background-color: rgb(50, 84, 110);")
                self.may = QPushButton(self)
                self.may.setObjectName(u"may")
                self.may.setGeometry(QRect(680, 130, 90, 30))
                self.may.setCursor(QCursor(Qt.PointingHandCursor))
                self.may.setFont(font3)
                self.may.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.may.clicked.connect (lambda: self.load_attendance_data('05'))

                self.june = QPushButton(self)
                self.june.setObjectName(u"june")
                self.june.setGeometry(QRect(780, 130, 90, 30))
                self.june.setFont(font3)
                self.june.setCursor(QCursor(Qt.PointingHandCursor))
                self.june.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px\n"
        "")
                self.june.clicked.connect (lambda: self.load_attendance_data('06'))

                self.july = QPushButton(self)
                self.july.setObjectName(u"july")
                self.july.setGeometry(QRect(330, 170, 90, 30))
                self.july.setFont(font3)
                self.july.setCursor(QCursor(Qt.PointingHandCursor))
                self.july.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.july.clicked.connect (lambda: self.load_attendance_data('07'))

                self.aug = QPushButton(self)
                self.aug.setObjectName(u"aug")
                self.aug.setGeometry(QRect(430, 170, 90, 30))
                self.aug.setFont(font3)
                self.aug.setCursor(QCursor(Qt.PointingHandCursor))
                self.aug.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.aug.clicked.connect (lambda: self.load_attendance_data('08'))

                self.nov = QPushButton(self)
                self.nov.setObjectName(u"nov")
                self.nov.setGeometry(QRect(730, 170, 90, 30))
                self.nov.setFont(font3)
                self.nov.setCursor(QCursor(Qt.PointingHandCursor))
                self.nov.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "border:1px solid;\n"
        "border-radius: 10px")
                self.nov.clicked.connect (lambda: self.load_attendance_data('11'))
                self.load_attendance_data("12")
                self.translateui()
        
        def translateui(self):
                self.dec.setText(QCoreApplication.translate("Employee_Page", u"December", None))
                self.sep.setText(QCoreApplication.translate("Employee_Page", u"September", None))
                self.april.setText(QCoreApplication.translate("Employee_Page", u"April", None))
                self.march.setText(QCoreApplication.translate("Employee_Page", u"March", None))
                self.oct.setText(QCoreApplication.translate("Employee_Page", u"October", None))
                self.feb.setText(QCoreApplication.translate("Employee_Page", u"February", None))
                self.jan.setText(QCoreApplication.translate("Employee_Page", u"January", None))
                ___qtablewidgetitem3 = self.table_start.horizontalHeaderItem(0)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("Employee_Page", u"Date", None));
                ___qtablewidgetitem4 = self.table_start.horizontalHeaderItem(1)
                ___qtablewidgetitem4.setText(QCoreApplication.translate("Employee_Page", u"Status", None));
                ___qtablewidgetitem5 = self.table_end.horizontalHeaderItem(0)
                ___qtablewidgetitem5.setText(QCoreApplication.translate("Employee_Page", u"Date", None));
                ___qtablewidgetitem6 = self.table_end.horizontalHeaderItem(1)
                ___qtablewidgetitem6.setText(QCoreApplication.translate("Employee_Page", u"Status", None));
                self.label.setText(QCoreApplication.translate("Employee_Page", u"<html><head/><body><p align=\"center\"><span style=\" color:#e6e6e6;\">Employee Attendance</span></p></body></html>", None))
                self.may.setText(QCoreApplication.translate("Employee_Page", u"May", None))
                self.june.setText(QCoreApplication.translate("Employee_Page", u"June", None))
                self.july.setText(QCoreApplication.translate("Employee_Page", u"July", None))
                self.aug.setText(QCoreApplication.translate("Employee_Page", u"August", None))
                self.nov.setText(QCoreApplication.translate("Employee_Page", u"November", None))

        def load_attendance_data(self, month):
                # Connect to the PostgreSQL database (adjust connection parameters accordingly)
                db_connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
                )

                # Create a cursor
                cursor = db_connection.cursor()

                try:
                        # Fetch attendance data for the selected month
                        select_query = """
                                SELECT date_, status 
                                FROM Attendance 
                                WHERE employee_id = %s AND EXTRACT(MONTH FROM date_) = EXTRACT(MONTH FROM TO_DATE(%s, 'MM'))
                        """
                        cursor.execute(select_query, (self.emp_id, month))
                        attendance_data = cursor.fetchall()

                        # Clear the existing data in the tables
                        self.clear_tables()

                        # Populate the tables with attendance data
                        self.populate_tables(attendance_data)

                except Exception as e:
                        # Handle exceptions or display error messages as needed
                        print(f"Error: {e}")

                finally:
                        # Close the cursor and connection
                        cursor.close()
                        db_connection.close()

        def clear_tables(self):
                # Clear the contents of both tables
                self.table_start.setRowCount(0)
                self.table_end.setRowCount(0)

        i = 0
        def populate_tables(self, attendance_data):
                # Populate the tables with attendance data
                #if i <13:
                        for row, (date_, status) in enumerate(attendance_data):
                                self.table_start.insertRow(row)
                                self.table_start.setItem(row, 0, QTableWidgetItem(str(date_)))
                                self.table_start.setItem(row, 1, QTableWidgetItem(status))
                # else:
                #         for row, (date_, status) in enumerate(attendance_data):
                #                 self.table_end.insertRow(row)
                #                 self.table_end.setItem(row, 0, QTableWidgetItem(str(date_)))
                #                 self.table_end.setItem(row, 1, QTableWidgetItem(status))
                # i+=1

        # The rest of your class remains unchanged
        # ...

class salarypage(QWidget):
        def __init__(self,Page,id):
                super(salarypage, self).__init__(Page)
                self.emp_id=id
                self.setObjectName(u"salary_report")
                self.salary_record = QTableWidget(self)
                if (self.salary_record.columnCount() < 5):
                        self.salary_record.setColumnCount(5)
                __qtablewidgetitem7 = QTableWidgetItem()
                font4 = QFont()
                font4.setPointSize(14)
                font4.setBold(True)
                brush1 = QBrush(QColor(50, 84, 110, 255))
                brush1.setStyle(Qt.SolidPattern)
                __qtablewidgetitem7.setFont(font4);
                __qtablewidgetitem7.setBackground(QColor(85, 55, 89));
                __qtablewidgetitem7.setForeground(brush1);
                self.salary_record.setHorizontalHeaderItem(0, __qtablewidgetitem7)
                __qtablewidgetitem8 = QTableWidgetItem()
                __qtablewidgetitem8.setFont(font4);
                __qtablewidgetitem8.setBackground(QColor(85, 55, 89));
                __qtablewidgetitem8.setForeground(brush1);
                self.salary_record.setHorizontalHeaderItem(1, __qtablewidgetitem8)
                __qtablewidgetitem9 = QTableWidgetItem()
                __qtablewidgetitem9.setFont(font4);
                __qtablewidgetitem9.setBackground(QColor(85, 55, 89));
                __qtablewidgetitem9.setForeground(brush1);
                self.salary_record.setHorizontalHeaderItem(2, __qtablewidgetitem9)
                __qtablewidgetitem10 = QTableWidgetItem()
                __qtablewidgetitem10.setFont(font4);
                __qtablewidgetitem10.setBackground(QColor(81, 55, 89));
                __qtablewidgetitem10.setForeground(brush1);
                self.salary_record.setHorizontalHeaderItem(3, __qtablewidgetitem10)
                __qtablewidgetitem11 = QTableWidgetItem()
                __qtablewidgetitem11.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
                __qtablewidgetitem11.setFont(font4);
                __qtablewidgetitem11.setBackground(QColor(85, 55, 89));
                __qtablewidgetitem11.setForeground(brush1);
                self.salary_record.setHorizontalHeaderItem(4, __qtablewidgetitem11)
                if (self.salary_record.rowCount() < 12):
                        self.salary_record.setRowCount(12)
                __qtablewidgetitem12 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(0, __qtablewidgetitem12)
                __qtablewidgetitem13 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(1, __qtablewidgetitem13)
                __qtablewidgetitem14 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(2, __qtablewidgetitem14)
                __qtablewidgetitem15 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(3, __qtablewidgetitem15)
                __qtablewidgetitem16 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(4, __qtablewidgetitem16)
                __qtablewidgetitem17 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(5, __qtablewidgetitem17)
                __qtablewidgetitem18 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(6, __qtablewidgetitem18)
                __qtablewidgetitem19 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(7, __qtablewidgetitem19)
                __qtablewidgetitem20 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(8, __qtablewidgetitem20)
                __qtablewidgetitem21 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(9, __qtablewidgetitem21)
                __qtablewidgetitem22 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(10, __qtablewidgetitem22)
                __qtablewidgetitem23 = QTableWidgetItem()
                self.salary_record.setVerticalHeaderItem(11, __qtablewidgetitem23)
                font7 = QFont()
                font7.setPointSize(12)
                __qtablewidgetitem24 = QTableWidgetItem()
                __qtablewidgetitem24.setFont(font7);
                self.salary_record.setItem(0, 0, __qtablewidgetitem24)
                __qtablewidgetitem25 = QTableWidgetItem()
                __qtablewidgetitem25.setFont(font7);
                self.salary_record.setItem(1, 0, __qtablewidgetitem25)
                __qtablewidgetitem26 = QTableWidgetItem()
                __qtablewidgetitem26.setFont(font7);
                self.salary_record.setItem(2, 0, __qtablewidgetitem26)
                __qtablewidgetitem27 = QTableWidgetItem()
                __qtablewidgetitem27.setFont(font7);
                self.salary_record.setItem(3, 0, __qtablewidgetitem27)
                __qtablewidgetitem28 = QTableWidgetItem()
                __qtablewidgetitem28.setFont(font7);
                self.salary_record.setItem(4, 0, __qtablewidgetitem28)
                __qtablewidgetitem29 = QTableWidgetItem()
                __qtablewidgetitem29.setFont(font7);
                self.salary_record.setItem(5, 0, __qtablewidgetitem29)
                __qtablewidgetitem30 = QTableWidgetItem()
                __qtablewidgetitem30.setFont(font7);
                self.salary_record.setItem(6, 0, __qtablewidgetitem30)
                __qtablewidgetitem31 = QTableWidgetItem()
                __qtablewidgetitem31.setFont(font7);
                self.salary_record.setItem(7, 0, __qtablewidgetitem31)
                __qtablewidgetitem32 = QTableWidgetItem()
                __qtablewidgetitem32.setFont(font7);
                self.salary_record.setItem(8, 0, __qtablewidgetitem32)
                __qtablewidgetitem33 = QTableWidgetItem()
                __qtablewidgetitem33.setFont(font7);
                self.salary_record.setItem(9, 0, __qtablewidgetitem33)
                font8 = QFont()
                font8.setPointSize(13)
                __qtablewidgetitem34 = QTableWidgetItem()
                __qtablewidgetitem34.setFont(font8);
                self.salary_record.setItem(10, 0, __qtablewidgetitem34)
                __qtablewidgetitem35 = QTableWidgetItem()
                __qtablewidgetitem35.setFont(font7);
                self.salary_record.setItem(11, 0, __qtablewidgetitem35)
                self.salary_record.setObjectName(u"salary_record")
                self.salary_record.setGeometry(QRect(50, 230, 841, 401))
                self.salary_record.setStyleSheet(u"QHeaderView::section {\n"
        "    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
        "    color: rgb(230, 230, 230); /* Set the text color */\n"
        "};\n"
        "\n"
        "color: rgb(50, 84, 110);\n"
        "background-color: rgb(230, 230, 230);\n"
        "\n"
        "")
                self.salary_record.horizontalHeader().setDefaultSectionSize(162)
                self.name_input = QLabel(self)
                self.name_input.setObjectName(u"name_input")
                self.name_input.setGeometry(QRect(240, 130, 500, 30))
                font9 = QFont()
                font9.setFamilies([u"Segoe UI"])
                font9.setPointSize(14)
                font9.setBold(True)
                font9.setItalic(False)
                font9.setUnderline(False)
                self.name_input.setFont(font9)
                self.name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";")
                self.department_input_2 = QLabel(self)
                self.department_input_2.setObjectName(u"department_input_2")
                self.department_input_2.setGeometry(QRect(240, 170, 500, 30))
                font10 = QFont()
                font10.setFamilies([u"Segoe UI"])
                font10.setPointSize(14)
                font10.setBold(True)
                font10.setItalic(False)
                self.department_input_2.setFont(font10)
                self.department_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 14pt \"Segoe UI\";")
                self.title_2 = QLabel(self)
                self.title_2.setObjectName(u"title_2")
                self.title_2.setGeometry(QRect(0, 30, 925, 61))
                font11 = QFont()
                font11.setPointSize(26)
                font11.setBold(True)
                self.title_2.setFont(font11)
                self.title_2.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);")
                self.name = QLabel(self)
                self.name.setObjectName(u"name")
                self.name.setGeometry(QRect(60, 130, 150, 30))
                font2 = QFont()
                font2.setFamilies([u"Segoe UI"])
                font2.setPointSize(16)
                font2.setWeight(QFont.Black)
                font2.setItalic(False)
                self.name.setFont(font2)
                self.name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 900 16pt \"Segoe UI\";")
                self.department_2 = QLabel(self)
                self.department_2.setObjectName(u"department_2")
                self.department_2.setGeometry(QRect(60, 170, 150, 30))
                self.department_2.setFont(font2)
                self.department_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 900 16pt \"Segoe UI\";")
                self.load_salary_data()
                self.translateUI()

        def translateUI (self):
                ___qtablewidgetitem7 = self.salary_record.horizontalHeaderItem(0)
                ___qtablewidgetitem7.setText(QCoreApplication.translate("Employee_Page", u"Months", None));
                ___qtablewidgetitem8 = self.salary_record.horizontalHeaderItem(1)
                ___qtablewidgetitem8.setText(QCoreApplication.translate("Employee_Page", u"Issuance Date", None));
                ___qtablewidgetitem9 = self.salary_record.horizontalHeaderItem(2)
                ___qtablewidgetitem9.setText(QCoreApplication.translate("Employee_Page", u"Deduction", None));
                ___qtablewidgetitem10 = self.salary_record.horizontalHeaderItem(3)
                ___qtablewidgetitem10.setText(QCoreApplication.translate("Employee_Page", u"Salary", None));
                ___qtablewidgetitem11 = self.salary_record.horizontalHeaderItem(4)
                ___qtablewidgetitem11.setText(QCoreApplication.translate("Employee_Page", u"Total Wage", None));
                ___qtablewidgetitem12 = self.salary_record.verticalHeaderItem(0)
                ___qtablewidgetitem12.setText(QCoreApplication.translate("Employee_Page", u"1.", None))
                ___qtablewidgetitem13 = self.salary_record.verticalHeaderItem(1)
                ___qtablewidgetitem13.setText(QCoreApplication.translate("Employee_Page", u"2.", None));
                ___qtablewidgetitem14 = self.salary_record.verticalHeaderItem(2)
                ___qtablewidgetitem14.setText(QCoreApplication.translate("Employee_Page", u"3.", None));
                ___qtablewidgetitem15 = self.salary_record.verticalHeaderItem(3)
                ___qtablewidgetitem15.setText(QCoreApplication.translate("Employee_Page", u"4.", None));
                ___qtablewidgetitem16 = self.salary_record.verticalHeaderItem(4)
                ___qtablewidgetitem16.setText(QCoreApplication.translate("Employee_Page", u"5.", None));
                ___qtablewidgetitem17 = self.salary_record.verticalHeaderItem(5)
                ___qtablewidgetitem17.setText(QCoreApplication.translate("Employee_Page", u"6.", None));
                ___qtablewidgetitem18 = self.salary_record.verticalHeaderItem(6)
                ___qtablewidgetitem18.setText(QCoreApplication.translate("Employee_Page", u"7.", None));
                ___qtablewidgetitem19 = self.salary_record.verticalHeaderItem(7)
                ___qtablewidgetitem19.setText(QCoreApplication.translate("Employee_Page", u"8.", None));
                ___qtablewidgetitem20 = self.salary_record.verticalHeaderItem(8)
                ___qtablewidgetitem20.setText(QCoreApplication.translate("Employee_Page", u"9.", None));
                ___qtablewidgetitem21 = self.salary_record.verticalHeaderItem(9)
                ___qtablewidgetitem21.setText(QCoreApplication.translate("Employee_Page", u"10.", None));
                ___qtablewidgetitem22 = self.salary_record.verticalHeaderItem(10)
                ___qtablewidgetitem22.setText(QCoreApplication.translate("Employee_Page", u"11.", None));
                ___qtablewidgetitem23 = self.salary_record.verticalHeaderItem(11)
                ___qtablewidgetitem23.setText(QCoreApplication.translate("Employee_Page", u"12.", None));

                __sortingEnabled = self.salary_record.isSortingEnabled()
                self.salary_record.setSortingEnabled(False)
                ___qtablewidgetitem24 = self.salary_record.item(0, 0)
                ___qtablewidgetitem24.setText(QCoreApplication.translate("Employee_Page", u"January", None));
                ___qtablewidgetitem25 = self.salary_record.item(1, 0)
                ___qtablewidgetitem25.setText(QCoreApplication.translate("Employee_Page", u"Febuary", None));
                ___qtablewidgetitem26 = self.salary_record.item(2, 0)
                ___qtablewidgetitem26.setText(QCoreApplication.translate("Employee_Page", u"March", None));
                ___qtablewidgetitem27 = self.salary_record.item(3, 0)
                ___qtablewidgetitem27.setText(QCoreApplication.translate("Employee_Page", u"April", None));
                ___qtablewidgetitem28 = self.salary_record.item(4, 0)
                ___qtablewidgetitem28.setText(QCoreApplication.translate("Employee_Page", u"May", None));
                ___qtablewidgetitem29 = self.salary_record.item(5, 0)
                ___qtablewidgetitem29.setText(QCoreApplication.translate("Employee_Page", u"June", None));
                ___qtablewidgetitem30 = self.salary_record.item(6, 0)
                ___qtablewidgetitem30.setText(QCoreApplication.translate("Employee_Page", u"July", None));
                ___qtablewidgetitem31 = self.salary_record.item(7, 0)
                ___qtablewidgetitem31.setText(QCoreApplication.translate("Employee_Page", u"August", None));
                ___qtablewidgetitem32 = self.salary_record.item(8, 0)
                ___qtablewidgetitem32.setText(QCoreApplication.translate("Employee_Page", u"September", None));
                ___qtablewidgetitem33 = self.salary_record.item(9, 0)
                ___qtablewidgetitem33.setText(QCoreApplication.translate("Employee_Page", u"October", None));
                ___qtablewidgetitem34 = self.salary_record.item(10, 0)
                ___qtablewidgetitem34.setText(QCoreApplication.translate("Employee_Page", u"November", None));
                ___qtablewidgetitem35 = self.salary_record.item(11, 0)
                ___qtablewidgetitem35.setText(QCoreApplication.translate("Employee_Page", u"December", None));
                self.salary_record.setSortingEnabled(__sortingEnabled)

                self.name.setText(QCoreApplication.translate("Employee_Page", u"Name", None))
                self.department_2.setText(QCoreApplication.translate("Employee_Page", u"Department", None))
                self.title_2.setText(QCoreApplication.translate("Employee_Page", u"                                Annual Salary Report", None))
               
        def load_salary_data(self):
                # Connect to the PostgreSQL database (adjust connection parameters accordingly)
                db_connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
                )

                 # Create a cursor
                cursor = db_connection.cursor()
                # Query to retrieve salary data for a specific employee
                query = """
                SELECT Fname, Lname, department
                FROM Employee
                WHERE id = %s
                """

                # Execute the query
                cursor.execute(query, (self.emp_id,))

                # Fetch all rows
                emp_data = cursor.fetchall()
                self.name_input.setText(QCoreApplication.translate("Employee_Page", str(emp_data[0][0]) + " " + str(emp_data[0][1]), None))
                self.department_input_2.setText(QCoreApplication.translate("Employee_Page", emp_data[0][2], None))

                # Query to retrieve salary data for a specific employee
                query = """
                                SELECT date_, deduction, amount, total
                                FROM Salary_Record
                                WHERE employee_id = %s
                        """

                # Execute the query
                cursor.execute(query, (self.emp_id,))

                # Fetch all rows
                salary_data = cursor.fetchall()
               

                # Close the cursor and connection
                cursor.close()
                db_connection.close()                

                month_mapping = {
                'January': 11, 'February': 0, 'March': 1, 'April': 2,
                'May': 3, 'June': 4, 'July': 5, 'August': 6,
                'September': 7, 'October': 8, 'November': 9, 'December': 10
                }
                
                for entry in salary_data:
                        date_, deduction, amount, total = entry  # Unpack the tuple
                        month_name = date_.strftime('%B')  # Convert date to month name
                        row_index = month_mapping.get(month_name)
                        if row_index is not None:
                                self.salary_record.setItem(row_index, 0, QTableWidgetItem(month_name))
                                self.salary_record.setItem(row_index, 1, QTableWidgetItem(date_.strftime('%Y-%m-%d')))
                                self.salary_record.setItem(row_index, 2, QTableWidgetItem(str(deduction)))
                                self.salary_record.setItem(row_index, 3, QTableWidgetItem(str(amount)))
                                self.salary_record.setItem(row_index, 4, QTableWidgetItem(str(total)))



class applicationpage(QWidget):
        def __init__(self,Page,id):
                super(applicationpage, self).__init__(Page)
                self.emp_id=id
                self.setObjectName(u"leave_application")
                self.description = QLabel(self)
                self.description.setObjectName(u"description")
                self.description.setGeometry(QRect(50, 310, 161, 31))
                font12 = QFont()
                font12.setFamilies([u"Segoe UI"])
                font12.setPointSize(18)
                font12.setBold(True)
                font12.setItalic(False)
                self.description.setFont(font12)
                self.description.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 18pt \"Segoe UI\";")
                self.end_date = QLabel(self)
                self.end_date.setObjectName(u"end_date")
                self.end_date.setGeometry(QRect(470, 170, 131, 31))
                self.end_date.setFont(font12)
                self.end_date.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 18pt \"Segoe UI\";")
                self.description_input = QTextEdit(self)
                self.description_input.setObjectName(u"description_input")
                self.description_input.setGeometry(QRect(60, 400, 821, 201))
                self.exp = QLabel(self)
                self.exp.setObjectName(u"exp")
                self.exp.setGeometry(QRect(50, 350, 501, 21))
                font13 = QFont()
                font13.setFamilies([u"Segoe UI"])
                font13.setPointSize(12)
                font13.setBold(False)
                font13.setItalic(False)
                self.exp.setFont(font13)
                self.exp.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 12pt \"Segoe UI\";")
                self.category_input = QComboBox(self)
                self.category_input.addItem("")
                self.category_input.addItem("")
                self.category_input.setObjectName(u"category_input")
                self.category_input.setGeometry(QRect(260, 240, 151, 31))
                self.category_input.setStyleSheet(u"font: 12pt \"Segoe UI\";")
                self.end_date_input = QDateEdit(self)
                self.end_date_input.setObjectName(u"end_date_input")
                self.end_date_input.setGeometry(QRect(640, 170, 151, 31))
                self.end_date_input.setStyleSheet(u"font: 12pt \"Segoe UI\";")
                self.end_date_input.setMaximumDate(QDate(2023, 12, 31))
                self.end_date_input.setMinimumDate(QDate(2023, 1, 1))
                self.submit_button = QPushButton(self)
                self.submit_button.setObjectName(u"submit_button")
                self.submit_button.setGeometry(QRect(420, 620, 131, 51))
                font14 = QFont()
                font14.setFamilies([u"Segoe UI"])
                font14.setPointSize(12)
                font14.setBold(True)
                font14.setItalic(False)
                self.submit_button.setFont(font14)
                self.submit_button.setCursor(QCursor(Qt.PointingHandCursor))
                self.submit_button.setStyleSheet(u"border:2px solid;\n"
        "border-radius:20px;\n"
        "background-color:rgb(50, 84, 110);\n"
        "border-color: rgb(230, 230, 230);\n"
        "color: rgb(230, 230, 230);\n"
        "font: 700 12pt \"Segoe UI\";")
                self.submit_button.clicked.connect (lambda: self.load_application_data())

                self.category = QLabel(self)
                self.category.setObjectName(u"category")
                self.category.setGeometry(QRect(50, 230, 141, 41))
                self.category.setFont(font12)
                self.category.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
        "color: rgb(50, 84, 110);")
                self.start_date_input = QDateEdit(self)
                self.start_date_input.setObjectName(u"start_date_input")
                self.start_date_input.setGeometry(QRect(260, 170, 151, 31))
                self.start_date_input.setStyleSheet(u"font: 12pt \"Segoe UI\";")
                self.start_date_input.setMaximumDate(QDate(2023, 12, 31))
                self.start_date_input.setMinimumDate(QDate(2023, 1, 1))
                self.start_date = QLabel(self)
                self.start_date.setObjectName(u"start_date")
                self.start_date.setGeometry(QRect(50, 170, 131, 31))
                self.start_date.setFont(font12)
                self.start_date.setStyleSheet(u"color: rgb(50, 84, 110);\n"
        "font: 700 18pt \"Segoe UI\";")
                self.title_3 = QLabel(self)
                self.title_3.setObjectName(u"title_3")
                self.title_3.setGeometry(QRect(0, 30, 925, 80))
                font15 = QFont()
                font15.setFamilies([u"Segoe UI"])
                font15.setPointSize(32)
                font15.setBold(True)
                font15.setItalic(False)
                self.title_3.setFont(font15)
                self.title_3.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
        "color: rgb(230, 230, 230);\n"
        "font: 700 32pt \"Segoe UI\";")
                self.translateui()

        def translateui(self):
                self.description.setText(QCoreApplication.translate("Employee_Page", u"Description", None))
                self.end_date.setText(QCoreApplication.translate("Employee_Page", u"End Date", None))
                self.exp.setText(QCoreApplication.translate("Employee_Page", u"(Explain reason for leave in 2-5 lines.)", None))
                self.category_input.setItemText(0, QCoreApplication.translate("Employee_Page", u"General", None))
                self.category_input.setItemText(1, QCoreApplication.translate("Employee_Page", u"Health", None))
                self.submit_button.setText(QCoreApplication.translate("Employee_Page", u"SUBMIT", None))
                self.category.setText(QCoreApplication.translate("Employee_Page", u"Category", None))
                self.start_date.setText(QCoreApplication.translate("Employee_Page", u"Start Date", None))
                self.title_3.setText(QCoreApplication.translate("Employee_Page", u"                         Leave Application", None))

        def load_application_data(self):
                # Connect to the PostgreSQL database (adjust connection parameters accordingly)
                db_connection = psycopg2.connect(
                        user="postgres",
                        password="zendagimigzara",
                        host="localhost",
                        port="5432",
                        database="AEMS"
                )

                # Create a cursor
                cursor = db_connection.cursor()

                try:
                        # Get data from UI elements
                        start_date_text = self.start_date_input.date().toString("yyyy-MM-dd")
                        end_date_text = self.end_date_input.date().toString("yyyy-MM-dd")

                        description = self.description_input.toPlainText()
                        category = self.category_input.currentText()

                        # Query to get count of general and health leaves that are accepted
                        query = """
                                SELECT
                                        COALESCE((SELECT COUNT(*) FROM Leave_Record WHERE employee_id = %s AND category = 'general' AND (status = 'accepted' OR status = 'pending')), 0) AS general_leave_count,
                                        COALESCE((SELECT COUNT(*) FROM Leave_Record WHERE employee_id = %s AND category = 'health' AND (status = 'accepted' OR status = 'pending')), 0) AS health_leave_count
                        """

                        # Execute the query
                        
                        cursor.execute(query, (self.emp_id, self.emp_id))

                        # Fetch the result
                        result = cursor.fetchone()

                        # Insert data into Leave_Record table
                        insert_query = """
                        INSERT INTO Leave_Record (employee_id, start_date, end_date, description, category, status)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """

                        # Assume self.emp_id is the employee_id, replace it accordingly
                        employee_id = self.emp_id

                        # Status is assumed to be 'pending' initially, change it if needed
                        status = 'pending'
                        category = category.lower()
                        
                        # Execute the query
                        if category == 'general' and result[0] < 15 or category == 'health' and result[1] < 10:
                                cursor.execute(insert_query, (employee_id, start_date_text, end_date_text, description, category, status))
                                QMessageBox.information(self, "Success", "Application sent successfully!")
                        else:
                                QMessageBox.critical(self, "Error!!", "No " + category + " leave left!")

                        # Commit the changes to the database
                        db_connection.commit()

                except Exception as e:
                        # Handle exceptions or display error messages as needed
                        print(f"Error: {e}")

                finally:
                        # Close the cursor and connection
                        cursor.close()
                        db_connection.close()             
               

class EmployeePage(QDialog):
        def __init__(self,id):
                super(EmployeePage, self).__init__()
                self.emp_id=id
                self.setObjectName(u" Employee_Page")
                self.resize(1280, 720)
                self.setMinimumSize(QSize(1280, 720))
                self.setMaximumSize(QSize(1280, 720))
                self.PAGE = QWidget(self)
                self.PAGE.setObjectName(u"PAGE")

                self.side_bar=SideBar(self.PAGE,self,self.emp_id)
                self.Main_pages = QStackedWidget(self.PAGE)
                self.Main_pages.setObjectName(u"Main_pages")
                self.Main_pages.setEnabled(True)
                self.Main_pages.setGeometry(QRect(350, 0, 930, 720))
                self.Main_pages.setMinimumSize(QSize(930, 720))
                self.Profile_page = Profile(self.PAGE,self.emp_id)
                self.Main_pages.addWidget(self.Profile_page)
                self.side_bar.setup_connections(self.Main_pages)
                self.retranslateUi()
    
        def signout(self):
                self.close()
                login=login_page.LoginPage()
                login.show()
                login.exec_()

        def retranslateUi(self):
                self.setWindowTitle(QCoreApplication.translate("Employee_Page", u"MainWindow", None))
    

def generateSalary():
         # Connect to the PostgreSQL database (adjust connection parameters accordingly)
        db_connection = psycopg2.connect(
        user="postgres",
        password="zendagimigzara",
        host="localhost",
        port="5432",
        database="AEMS"
        )

                # Create a cursor
        cursor = db_connection.cursor()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    global window
    window =  EmployeePage('9')
    window.show()
    sys.exit(app.exec_())
