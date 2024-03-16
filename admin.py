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
QWidget,QMessageBox,QTableWidget, QTableWidgetItem,QVBoxLayout,QItemDelegate,QSpinBox,QDateEdit,QAbstractItemView)
import re
import psycopg2
from functools import partial
import login_page
def is_valid_email(email):
    # Define a regular expression pattern for a basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use re.match to check if the email matches the pattern
    match = re.match(pattern, email)

    # If there is a match, the email is valid
    return match is not None

class CustomSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super(CustomSpinBox, self).__init__(parent)
        
    def textFromValue(self, value):
        if value == 0:
            return "A"
        elif value == 1:
            return "P"
        else:
            return super(CustomSpinBox, self).textFromValue(value)

class Sidebar(QGroupBox):
    def __init__(self,Page,admin_instance):
        self.admin=admin_instance
        super(Sidebar, self).__init__(Page)
        self.page=Page
        self.setObjectName(u"side_bar")
        self.setGeometry(0, -10, 291, 731)
        self.setStyleSheet(u"background-color: rgb(88, 55, 89);")

        self.Dashboard_button = QPushButton(self)
        self.Dashboard_button.setObjectName(u"Dashboard_button")
        self.Dashboard_button.setGeometry(QRect(-10, 137, 301, 81))
        font = QFont()
        font.setFamilies([u"Book Antiqua"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.Dashboard_button.setFont(font)
        self.Dashboard_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Dashboard_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                            
"font: 15pt \"Book Antiqua\";")
        icon = QIcon()
        icon.addFile(u"Images/Dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_button.setIcon(icon)
        self.Dashboard_button.setIconSize(QSize(25, 25))
        

        self.attendance = QPushButton(self)
        self.attendance.setObjectName(u"attendance")
        self.attendance.setGeometry(QRect(0, 218, 291, 81))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.attendance.setFont(font1)
        self.attendance.setCursor(QCursor(Qt.PointingHandCursor))
        self.attendance.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"Images/attendance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.attendance.setIcon(icon1)
        self.attendance.setIconSize(QSize(25, 25))
        self.attendance.setAutoDefault(False)
        self.attendance.setFlat(False)


        self.EandL = QToolBox(self)
        self.EandL.setObjectName(u"EandL")
        self.EandL.setEnabled(True)
        self.EandL.setGeometry(QRect(0, 300, 291, 350))
        self.EandL.setMinimumSize(QSize(250, 300))
        self.EandL.setMaximumSize(QSize(300, 350))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.EandL.setFont(font2)
        self.EandL.setCursor(QCursor(Qt.PointingHandCursor))
        self.EandL.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.EandL.setFrameShape(QFrame.NoFrame)
        self.EandL.setFrameShadow(QFrame.Plain)
        self.EandL.setLineWidth(0)
        self.Employee = QWidget()
        self.Employee.setObjectName(u"Employee")
        self.Employee.setGeometry(QRect(0, 0, 291, 256))
        self.list_employee = QPushButton(self.Employee)
        self.list_employee.setObjectName(u"list_employee")
        self.list_employee.setGeometry(QRect(0, 0, 291, 71))
        font3 = QFont()
        font3.setPointSize(15)
        self.list_employee.setFont(font3)
        self.list_employee.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"Images/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.list_employee.setIcon(icon2)
        self.list_employee.setIconSize(QSize(30, 30))
        self.Add_employee = QPushButton(self.Employee)
        self.Add_employee.setObjectName(u"Add_employee")
        self.Add_employee.setGeometry(QRect(0, 70, 291, 81))
        self.Add_employee.setFont(font3)
        self.Add_employee.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"Images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Add_employee.setIcon(icon3)
        self.Add_employee.setIconSize(QSize(30, 30))
        self.Remove_employee = QPushButton(self.Employee)
        self.Remove_employee.setObjectName(u"Remove_employee")
        self.Remove_employee.setGeometry(QRect(0, 150, 291, 71))
        self.Remove_employee.setFont(font3)
        self.Remove_employee.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"Images/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Remove_employee.setIcon(icon4)
        self.Remove_employee.setIconSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u"Images/Employee.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.EandL.addItem(self.Employee, icon5, u"Employee")
        self.Leave = QWidget()
        self.Leave.setObjectName(u"Leave")
        self.Leave.setGeometry(QRect(0, 0, 291, 256))
        self.Pending = QPushButton(self.Leave)
        self.Pending.setObjectName(u"Pending")
        self.Pending.setGeometry(QRect(0, 0, 291, 81))
        self.Pending.setFont(font3)
        self.Pending.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"Images/pending.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Pending.setIcon(icon6)
        self.Pending.setIconSize(QSize(30, 30))
        self.Approve = QPushButton(self.Leave)
        self.Approve.setObjectName(u"Approve")
        self.Approve.setGeometry(QRect(0, 80, 291, 81))
        self.Approve.setFont(font3)
        self.Approve.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"Images/approve.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Approve.setIcon(icon7)
        self.Approve.setIconSize(QSize(30, 30))
        self.Decline = QPushButton(self.Leave)
        self.Decline.setObjectName(u"Decline")
        self.Decline.setGeometry(QRect(0, 160, 291, 81))
        self.Decline.setFont(font3)
        self.Decline.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"Images/decline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Decline.setIcon(icon8)
        self.Decline.setIconSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u"Images/leave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EandL.addItem(self.Leave, icon9, u"Leave")
        self.Logo = QLabel(self)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(0, 10, 290, 131))
        self.Logo.setPixmap(QPixmap(u"Images/logo.png"))
        self.Logo.setScaledContents(True)
        self.Sign_out_button = QPushButton(self)
        self.Sign_out_button.setObjectName(u"Sign_out_button")
        self.Sign_out_button.setGeometry(QRect(0, 670, 291, 61))
        self.Sign_out_button.setFont(font1)
        self.Sign_out_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(u"Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Sign_out_button.setIcon(icon10)
        self.Sign_out_button.setIconSize(QSize(20, 20))
        self.Sign_out_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Sign_out_button.clicked.connect(self.admin.signout)
        self.translateui()
        
    def translateui(self):
        self.setTitle(QCoreApplication.translate(" Admin_Page", u"GroupBox", None))
        self.Dashboard_button.setText(QCoreApplication.translate(" Admin_Page", u"Dashboard", None))
        self.attendance.setText(QCoreApplication.translate(" Admin_Page", u"Attendance", None))
        self.list_employee.setText(QCoreApplication.translate(" Admin_Page", u"List of Employee", None))
        self.Add_employee.setText(QCoreApplication.translate(" Admin_Page", u"Add Employee", None))
        self.Remove_employee.setText(QCoreApplication.translate(" Admin_Page", u"Remove Employee", None))
        self.EandL.setItemText(self.EandL.indexOf(self.Employee), QCoreApplication.translate(" Admin_Page", u"Employee", None))
        self.Pending.setText(QCoreApplication.translate(" Admin_Page", u"Pending", None))
        self.Approve.setText(QCoreApplication.translate(" Admin_Page", u"Approved", None))
        self.Decline.setText(QCoreApplication.translate(" Admin_Page", u"Declined", None))
        self.EandL.setItemText(self.EandL.indexOf(self.Leave), QCoreApplication.translate(" Admin_Page", u"Leave", None))
        self.Logo.setText("")
        
    def setup_connections(self, stacked_widget):
            self.Sign_out_button.setText(QCoreApplication.translate("Admin_Page", u"  Sign Out", None))
            self.Dashboard_button.clicked.connect(lambda: self.setdashboardpage(stacked_widget))
            self.attendance.clicked.connect(lambda: self.setattendancepage(stacked_widget))
            self.list_employee.clicked.connect(lambda: self.setlistpage(stacked_widget))
            self.Add_employee.clicked.connect(lambda: self.setaddemployeepage(stacked_widget))
            self.Remove_employee.clicked.connect(lambda: self.setremovepage(stacked_widget))
            self.Pending.clicked.connect(lambda: self.setpendingpage(stacked_widget))
            self.Approve.clicked.connect(lambda:self.setapprovepage(stacked_widget))
            self.Decline.clicked.connect(lambda:self.setdeclinepage(stacked_widget))

    def setdashboardpage(self, stacked_widget):
            current_index = stacked_widget.currentIndex()
            if current_index != -1:
                    current_widget = stacked_widget.widget(current_index)
                    stacked_widget.removeWidget(current_widget)
                    current_widget.deleteLater()
            new_dashboard_page = DashboardPage(self.page)
            stacked_widget.addWidget(new_dashboard_page)
            new_index = stacked_widget.indexOf(new_dashboard_page)
            stacked_widget.setCurrentIndex(new_index)
    
    def setattendancepage(self, stacked_widget):
            current_index = stacked_widget.currentIndex()
            if current_index != -1:
                    current_widget = stacked_widget.widget(current_index)
                    stacked_widget.removeWidget(current_widget)
                    current_widget.deleteLater()
            new_attendance_page = AttendancePage(self.page,stacked_widget)
            stacked_widget.addWidget(new_attendance_page)
            new_index = stacked_widget.indexOf(new_attendance_page)
            stacked_widget.setCurrentIndex(new_index)
    
    def setlistpage(self, stacked_widget):
            current_index = stacked_widget.currentIndex()
            if current_index != -1:
                    current_widget = stacked_widget.widget(current_index)
                    stacked_widget.removeWidget(current_widget)
                    current_widget.deleteLater()
            new_list_page = Employee_list_page(self.page,stacked_widget)
            stacked_widget.addWidget(new_list_page)
            new_index = stacked_widget.indexOf(new_list_page)
            stacked_widget.setCurrentIndex(new_index)

    def setaddemployeepage(self, stacked_widget):
            current_index = stacked_widget.currentIndex()
            if current_index != -1:
                    current_widget = stacked_widget.widget(current_index)
                    stacked_widget.removeWidget(current_widget)
                    current_widget.deleteLater()
            new_addemployee_page = Add_Employee_page(self.page)
            stacked_widget.addWidget(new_addemployee_page)
            new_index = stacked_widget.indexOf(new_addemployee_page)
            stacked_widget.setCurrentIndex(new_index)

    def setremovepage(self, stacked_widget):
            current_index = stacked_widget.currentIndex()
            if current_index != -1:
                    current_widget = stacked_widget.widget(current_index)
                    stacked_widget.removeWidget(current_widget)
                    current_widget.deleteLater()
            new_remove_page = Remove_Employee_page(self.page)
            stacked_widget.addWidget(new_remove_page)
            new_index = stacked_widget.indexOf(new_remove_page)
            stacked_widget.setCurrentIndex(new_index)

    def setpendingpage(self, stacked_widget):
            current_index = stacked_widget.currentIndex()
            if current_index != -1:
                    current_widget = stacked_widget.widget(current_index)
                    stacked_widget.removeWidget(current_widget)
                    current_widget.deleteLater()
            new_pending_page = PendingPage(self.page)
            stacked_widget.addWidget(new_pending_page)
            new_index = stacked_widget.indexOf(new_pending_page)
            stacked_widget.setCurrentIndex(new_index)
    
    def setapprovepage(self, stacked_widget):
            current_index = stacked_widget.currentIndex()
            if current_index != -1:
                    current_widget = stacked_widget.widget(current_index)
                    stacked_widget.removeWidget(current_widget)
                    current_widget.deleteLater()
            new_approve_page = ApprovedPage(self.page)
            stacked_widget.addWidget(new_approve_page)
            new_index = stacked_widget.indexOf(new_approve_page)
            stacked_widget.setCurrentIndex(new_index)
    
    def setdeclinepage(self, stacked_widget):
            current_index = stacked_widget.currentIndex()
            if current_index != -1:
                    current_widget = stacked_widget.widget(current_index)
                    stacked_widget.removeWidget(current_widget)
                    current_widget.deleteLater()
            new_decline_page = DeclinedPage(self.page)
            stacked_widget.addWidget(new_decline_page)
            new_index = stacked_widget.indexOf(new_decline_page)
            stacked_widget.setCurrentIndex(new_index)
        

class AttendanceStatusDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.addItems(["A", "P"])
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        editor.setCurrentText("A" if value == 0 else "P")


class AttendancePage(QWidget):
    def __init__(self, page, stacked_widget):
        super(AttendancePage, self).__init__(page)
        font10 = QFont()
        font10.setPointSize(18)
        font11 = QFont()
        font11.setBold(True)

        self.setObjectName(u"Attendance")
        self.Date = QDateEdit(self)
        self.Date.setObjectName(u"Date")
        self.Date.setGeometry(230, 130, 110, 22)
        self.Date.setMaximumDate(QDate(2023, 12, 31))
        self.Date.setMinimumDate(QDate(2023, 1, 1))
        self.Date.setCalendarPopup(True)

        self.Attendance_Bar = QGroupBox(self)
        self.Attendance_Bar.setObjectName(u"Attendance_Bar")
        self.Attendance_Bar.setGeometry(0, 0, 991, 80)
        self.Attendance_Bar.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.Attendance_bar_text = QLabel(self.Attendance_Bar)
        self.Attendance_bar_text.setObjectName(u"Attendance_bar_text")
        self.Attendance_bar_text.setGeometry(33, 22, 261, 31)
        self.Attendance_bar_text.setFont(font10)
        self.Attendance_bar_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Mark_button = QPushButton(self)
        self.Mark_button.setObjectName(u"Mark_button")
        self.Mark_button.setGeometry(QRect(410, 630, 111, 31))
        font13 = QFont()
        font13.setPointSize(10)
        font13.setBold(True)
        self.Mark_button.setFont(font13)
        self.Mark_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Mark_button.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(88, 55, 89);\n"
"color: rgb(255, 255, 255);")
        self.Mark_button.clicked.connect(self.markAttendance)
        self.Select_date = QLabel(self)
        self.Select_date.setObjectName(u"Select_date")
        self.Select_date.setGeometry(110, 130, 121, 21)
        font14 = QFont()
        font14.setPointSize(12)
        font14.setBold(True)
        self.Select_date.setFont(font14)
        self.Select_date.setStyleSheet(u"color: rgb(88, 55, 89);")

        self.Attendance_sheet = QTableWidget(self)
        self.setupTable()
        
        self.Date.dateChanged.connect(self.refreshAndPopulateTable)
        self.refreshAndPopulateTable()  # Populate the table with employee data

    def setupTable(self):
        self.Attendance_sheet.setColumnCount(5)
        
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(True)
        for col, header_text in enumerate(["Employee ID", "First Name", "Last Name", "Date", "Status"]):
            header_item = QTableWidgetItem(header_text)
            header_item.setFont(font11)
            self.Attendance_sheet.setHorizontalHeaderItem(col, header_item)

        self.Attendance_sheet.setObjectName(u"Attendance_sheet")
        self.Attendance_sheet.setGeometry(25, 221, 940, 331)
        self.Attendance_sheet.setMaximumHeight(200)
        self.Attendance_sheet.setStyleSheet(u"QHeaderView::section {\n"
                                "    background-color: rgb(88, 55, 89);\n"
                                "    color: white;\n"
                                "    border: 1px solid rgb(88, 55, 89);\n"
                                "}")
        self.Attendance_sheet.setSelectionBehavior(QAbstractItemView.SelectRows)

    # Set edit triggers
        self.Attendance_sheet.setEditTriggers(QAbstractItemView.AllEditTriggers | QAbstractItemView.EditKeyPressed)

        # Set the delegate for Status column
        self.Attendance_sheet.setItemDelegateForColumn(4, AttendanceStatusDelegate())
        

        # Styling for table rows

        self.Attendance_sheet.setShowGrid(True)
        self.Attendance_sheet.setSortingEnabled(False)
        self.Attendance_sheet.setRowCount(0)
        self.Attendance_sheet.horizontalHeader().setCascadingSectionResizes(False)
        self.Attendance_sheet.horizontalHeader().setDefaultSectionSize(200)
        self.Attendance_sheet.horizontalHeader().setHighlightSections(False)
        self.Attendance_sheet.horizontalHeader().setProperty("showSortIndicator", False)
        self.Attendance_sheet.horizontalHeader().setStretchLastSection(False)
        self.Attendance_sheet.verticalHeader().setCascadingSectionResizes(False)
        self.Attendance_sheet.verticalHeader().setMinimumSectionSize(25)
        self.Attendance_sheet.verticalHeader().setProperty("showSortIndicator", False)
        self.Attendance_sheet.verticalHeader().setStretchLastSection(False)

        # Set the edit trigger to allow editing when a key is pressed
        self.Attendance_sheet.setEditTriggers(QAbstractItemView.AllEditTriggers | QAbstractItemView.EditKeyPressed)
        self.translateui()
    
    def translateui(self):
        self.Attendance_Bar.setTitle("")
        self.Attendance_bar_text.setText(QCoreApplication.translate("Admin_Page", u"Mark Attendance", None))
        self.Select_date.setText(QCoreApplication.translate("Admin_Page", u"Select Date:", None))
        ___qtablewidgetitem4 = self.Attendance_sheet.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Admin_Page", u"Employee ID", None));
        ___qtablewidgetitem5 = self.Attendance_sheet.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Admin_Page", u"First Name", None));
        ___qtablewidgetitem6 = self.Attendance_sheet.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Admin_Page", u"Last Name", None));
        ___qtablewidgetitem7 = self.Attendance_sheet.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Admin_Page", u"Date", None));
        ___qtablewidgetitem8 = self.Attendance_sheet.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Admin_Page", u"Status", None));
        self.Mark_button.setText(QCoreApplication.translate("Admin_Page", u"Mark", None))
    def refreshAndPopulateTable(self):
        # Clear existing data in the table
        self.Attendance_sheet.setRowCount(0)

        # Fetch employee data from the database
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )
            cursor = connection.cursor()

            # Execute a query to fetch employee data
            cursor.execute("SELECT id, Fname, Lname FROM Employee")
            employee_data = cursor.fetchall()

            # Populate the QTableWidget with fetched employee data and the selected date
            selected_date = self.Date.date().toString("yyyy-MM-dd")
            for row_data in employee_data:
                row_num = self.Attendance_sheet.rowCount()
                self.Attendance_sheet.insertRow(row_num)
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    font = QFont()
                    font.setPointSize(13)
                    item.setFont(font)
                    self.Attendance_sheet.setItem(row_num, col, item)

                # Add date column with the selected date
                date_item = QTableWidgetItem(selected_date)
                date_item.setFont(font)
                self.Attendance_sheet.setItem(row_num, 3, date_item)

            connection.commit()
            cursor.close()

        except Exception as e:
            print("Error fetching employee data:", e)

        # Fetch existing attendance data for the selected date
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )
            cursor = connection.cursor()

            # Execute a query to fetch existing attendance data for the selected date
            cursor.execute("SELECT employee_id, status FROM Attendance WHERE date_ = %s", (selected_date,))
            attendance_data = cursor.fetchall()

            # Update the QTableWidget with fetched attendance data
            for row_data in attendance_data:
                employee_id, status = row_data
                # Find the row corresponding to the employee_id
                for row in range(self.Attendance_sheet.rowCount()):
                    if self.Attendance_sheet.item(row, 0).text() == str(employee_id):
                        # Update the status column with the fetched status
                        status_item = QTableWidgetItem(status)
                        font = QFont()
                        font.setPointSize(13)
                        status_item.setFont(font)
                        self.Attendance_sheet.setItem(row, 4, status_item)

            connection.commit()
            cursor.close()

        except Exception as e:
            print("Error fetching attendance data:", e)

        self.adjustTableHeightAndWidth()

    def markAttendance(self):
        # Implement the logic to mark attendance in the database for all rows
        total_rows = self.Attendance_sheet.rowCount()
        selected_date = self.Date.date().toString("yyyy-MM-dd")

        for row in range(total_rows):
            employee_id = self.Attendance_sheet.item(row, 0).text()
            attendance_status_item = self.Attendance_sheet.item(row, 4)
            attendance_status='P'
            if attendance_status_item:
                attendance_status = attendance_status_item.text()
            # Update the attendance table in the database with the selected date, employee_id, and attendance_status
            self.updateAttendanceInDatabase(selected_date, employee_id, attendance_status)

        # Optionally, show a success message
        QMessageBox.information(self, "Success", "Attendance marked successfully!")



    def updateAttendanceInDatabase(self, selected_date, employee_id, attendance_status):
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )
            cursor = connection.cursor()

            # Execute a query to update the attendance table for the specific employee and date
            query = "INSERT INTO Attendance (employee_id, date_, status) VALUES (%s, %s, %s) ON CONFLICT (employee_id, date_) DO UPDATE SET status = %s"
            cursor.execute(query, (employee_id, selected_date, attendance_status, attendance_status))

            connection.commit()
            cursor.close()

        except Exception as e:
            print("Error updating attendance data:", e)
            # Show an error message if the update fails
            QMessageBox.critical(self, "Error", f"Failed to mark attendance:\n{str(e)}")


    def adjustTableHeightAndWidth(self):
        # Adjust the height of the table according to the number of rows
        total_height = sum(self.Attendance_sheet.rowHeight(row) for row in range(self.Attendance_sheet.rowCount()))
        # Add some extra height to account for header and spacing
        total_height += self.Attendance_sheet.horizontalHeader().height() + 10
        # Set the height of the table
        self.Attendance_sheet.setFixedHeight(total_height)

        # Adjust the width of the table according to the content
        for col in range(self.Attendance_sheet.columnCount()):
            self.Attendance_sheet.resizeColumnToContents(col)
            # Increase the width by a fixed amount (adjust the value as needed)
            new_width = self.Attendance_sheet.columnWidth(col) + 85
            self.Attendance_sheet.setColumnWidth(col, new_width)

    

class Add_Employee_page(QWidget):
    def __init__(self,Page):
        super(Add_Employee_page, self).__init__(Page)

        self.setObjectName(u"AddEmployee_Page")
        self.new_employee_title_bar = QGroupBox(self)
        self.new_employee_title_bar.setObjectName(u"new_employee_title_bar")
        self.new_employee_title_bar.setGeometry(QRect(0, 20, 991, 80))
        self.new_employee_title_bar.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.new_employee_text = QLabel(self.new_employee_title_bar)
        self.new_employee_text.setObjectName(u"new_employee_text")
        self.new_employee_text.setGeometry(QRect(33, 22, 261, 31))
        font10 = QFont()
        font10.setPointSize(18)
        self.new_employee_text.setFont(font10)
        self.new_employee_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Department = QComboBox(self)
        self.Department.addItem("")
        self.Department.addItem("")
        self.Department.addItem("")
        self.Department.addItem("")
        self.Department.addItem("")
        self.Department.setObjectName(u"Department")
        self.Department.setGeometry(QRect(210, 160, 210, 30))
        font6=QFont()
        font6.setPointSize(13)
        self.Department.setFont(font6)
        self.Department.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;")
        self.Employee_id = QLineEdit(self)
        self.Employee_id.setObjectName(u"Employee_id")
        self.Employee_id.setGeometry(QRect(660, 160, 210, 30))
        self.Employee_id.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Contact = QLineEdit(self)
        self.Contact.setObjectName(u"Contact")
        self.Contact.setGeometry(QRect(210, 380, 211, 31))
        self.Contact.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Lname = QLineEdit(self)
        self.Lname.setObjectName(u"Lname")
        self.Lname.setGeometry(QRect(660, 270, 211, 31))
        self.Lname.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Fname = QLineEdit(self )
        self.Fname.setObjectName(u"Fname")
        self.Fname.setGeometry(QRect(210, 270, 211, 31))
        self.Fname.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Address = QLineEdit(self )
        self.Address.setObjectName(u"Address")
        self.Address.setGeometry(QRect(660, 380, 211, 31))
        self.Address.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Email = QLineEdit(self )
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(210, 490, 211, 31))
        self.Email.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.password = QLineEdit(self )
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(660, 490, 211, 31))
        self.password.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.password.setEchoMode(QLineEdit.Password)
        self.Department_Text = QLabel(self )
        self.Department_Text.setObjectName(u"Department_Text")
        self.Department_Text.setGeometry(QRect(90, 165, 111, 21))
        font11 = QFont()
        font11.setPointSize(13)
        font11.setBold(True)
        self.Department_Text.setFont(font11)
        self.Employee_id_text = QLabel(self )
        self.Employee_id_text.setObjectName(u"Employee_id_text")
        self.Employee_id_text.setGeometry(QRect(530, 165, 121, 21))
        self.Employee_id_text.setFont(font11)
        self.Fname_text = QLabel(self )
        self.Fname_text.setObjectName(u"Fname_text")
        self.Fname_text.setGeometry(QRect(90, 275, 101, 21))
        self.Fname_text.setFont(font11)
        self.Lname_text = QLabel(self )
        self.Lname_text.setObjectName(u"Lname_text")
        self.Lname_text.setGeometry(QRect(530, 275, 101, 21))
        self.Lname_text.setFont(font11)
        self.Contact_text = QLabel(self )
        self.Contact_text.setObjectName(u"Contact_text")
        self.Contact_text.setGeometry(QRect(90, 385, 101, 21))
        self.Contact_text.setFont(font11)
        self.Address_text = QLabel(self )
        self.Address_text.setObjectName(u"Address_text")
        self.Address_text.setGeometry(QRect(530, 385, 101, 21))
        self.Address_text.setFont(font11)
        self.Email_text = QLabel(self )
        self.Email_text.setObjectName(u"Email_text")
        self.Email_text.setGeometry(QRect(90, 495, 101, 21))
        self.Email_text.setFont(font11)
        self.Password_text = QLabel(self )
        self.Password_text.setObjectName(u"Password_text")
        self.Password_text.setGeometry(QRect(530, 495, 101, 21))
        self.Password_text.setFont(font11)
        
        self.Salary_text = QLabel(self)
        self.Salary_text.setObjectName(u"Salary_text")
        self.Salary_text.setGeometry(QRect(310, 580, 101, 21))
        self.Salary_text.setFont(font11)
        self.Salary = QLineEdit(self)
        self.Salary.setObjectName(u"Salary")
        self.Salary.setGeometry(QRect(390, 575, 211, 31))
        self.Salary.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        
        self.add_button = QPushButton(self)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(420, 650, 111, 31))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        self.add_button.setFont(font12)
        self.add_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_button.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(88, 55, 89);\n"
"color: rgb(255, 255, 255);")
        self.add_button.clicked.connect(self.add_employee_to_database)
        self.translateui()
    def translateui(self):
        self.new_employee_title_bar.setTitle("")
        self.new_employee_text.setText(QCoreApplication.translate(" Admin_Page", u"Add New Employee", None))
        self.Department.setItemText(0, QCoreApplication.translate(" Admin_Page", u"    Marketing", None))
        self.Department.setItemText(1, QCoreApplication.translate(" Admin_Page", u"    Accounts", None))
        self.Department.setItemText(2, QCoreApplication.translate(" Admin_Page", u"    Sales", None))
        self.Department.setItemText(3, QCoreApplication.translate(" Admin_Page", u"    Finance", None))
        self.Department.setItemText(4, QCoreApplication.translate(" Admin_Page", u"    Research", None))

        self.Department_Text.setText(QCoreApplication.translate(" Admin_Page", u"Department:", None))
        self.Employee_id_text.setText(QCoreApplication.translate(" Admin_Page", u"Employee ID:", None))
        self.Fname_text.setText(QCoreApplication.translate(" Admin_Page", u"First Name:", None))
        self.Lname_text.setText(QCoreApplication.translate(" Admin_Page", u"Last Name:", None))
        self.Contact_text.setText(QCoreApplication.translate(" Admin_Page", u"Contact #:", None))
        self.Address_text.setText(QCoreApplication.translate(" Admin_Page", u"Address:", None))
        self.Email_text.setText(QCoreApplication.translate(" Admin_Page", u"Email:", None))
        self.Password_text.setText(QCoreApplication.translate(" Admin_Page", u"Password:", None))
        self.add_button.setText(QCoreApplication.translate(" Admin_Page", u"ADD", None))
        self.Salary_text.setText(QCoreApplication.translate(" Admin_Page", u"Salary:", None))

    def add_employee_to_database(self):
        # Get employee data from the form
        department = self.Department.currentText()
        employee_id = self.Employee_id.text()
        fname = self.Fname.text()
        lname = self.Lname.text()
        contact = self.Contact.text()
        address = self.Address.text()
        email = self.Email.text()
        password = self.password.text()
        salary=self.Salary.text()

        

        # You can validate the data here before inserting it into the database

        # Create a dictionary to hold employee data
        employee_data = {
            "department": department,
            "employee_id": employee_id,
            "fname": fname,
            "lname": lname,
            "contact": contact,
            "address": address,
            "email": email,
            "password": password,
            "salary":salary
        }
        empty_fields = [key.capitalize() for key, value in employee_data.items() if not value]
        if empty_fields:
            error_message = f"Please fill in the following fields: {', '.join(empty_fields)}"
            self.show_error_message(error_message)
            return

        if not is_valid_email(email):
            error_message = "Invalid email address. Please enter a valid email."
            self.show_error_message(error_message)
            return
        if not contact.isdigit():
            error_message = "Contact number should be an numbers."
            self.show_error_message(error_message)
            return
        if len(contact)!=11:
            error_message = "Contact number should be of 11 digits."
            self.show_error_message(error_message)
            return
        
        if not salary.isdigit():
            error_message = "Salary number should be an numbers."
            self.show_error_message(error_message)
            return
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )


            cursor = connection.cursor()
            existing_id_query = f"SELECT * FROM Employee WHERE id = '{self.Employee_id.text()}'"
            cursor.execute(existing_id_query)
            existing_id = cursor.fetchone()

            if existing_id:
                error_message = "Employee ID already exists. Please use a different ID."
                self.show_error_message(error_message)
                return

            # Check if the email already exists in the database
            existing_email_query = f"SELECT * FROM Employee WHERE email = '{self.Email.text()}'"
            cursor.execute(existing_email_query)
            existing_email = cursor.fetchone()

            if existing_email:
                error_message = "Email already exists. Please use a different email."
                self.show_error_message(error_message)
                return
                # Insert the employee data into the Employee table
            cursor.execute("""
                INSERT INTO Employee (id, Fname, Lname,email, password, address,department, salary,contact)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
            """, (employee_id, fname, lname,email, password, address,department, salary,contact))

            connection.commit()
            # Close the cursor and connection
            cursor.close()
            connection.close()
            success_message = "Employee added successfully!"
            self.show_success_message(success_message)
            # Reset the form
            self.reset_form()

        except (Exception, psycopg2.Error) as error:
            # Handle database errors
            error_message = f"Error adding employee to the database: {error}"
            self.show_error_message(error_message)
        self.reset_form()

    def reset_form(self):
        # Clear input fields
        self.Department.setCurrentIndex(0)
        self.Employee_id.clear()
        self.Fname.clear()
        self.Lname.clear()
        self.Contact.clear()
        self.Address.clear()
        self.Email.clear()
        self.password.clear()
        self.Salary.clear()
    
    def show_error_message(self, message):
        # Create a QMessageBox to show the error message
        error_box = QMessageBox()
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        error_box.setIcon(QMessageBox.Warning)
        error_box.setStandardButtons(QMessageBox.Ok)

        # Set the window modality to make it a blocking message box
        error_box.setWindowModality(Qt.WindowModal)

        # Show the message box
        error_box.exec_()
    
    def show_success_message(self, message):
        QMessageBox.information(self, "Success", message, QMessageBox.Ok)

class Employee_list_page(QWidget):
    def __init__(self, Page,stacked_widget):
        super(Employee_list_page, self).__init__(Page)
        self.stack_widget=stacked_widget
        self.setObjectName(u"Employeelist_page")
        self.List_title_bar = QGroupBox(self)
        self.List_title_bar.setObjectName(u"List_title_bar")
        self.List_title_bar.setGeometry(QRect(0, 40, 991, 80))
        self.List_title_bar.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.List_employee_text = QLabel(self.List_title_bar)
        self.List_employee_text.setObjectName(u"List_employee_text")
        self.List_employee_text.setGeometry(QRect(33, 22, 261, 31))
        font10 = QFont()
        font10.setPointSize(18)
        self.List_employee_text.setFont(font10)
        self.List_employee_text.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.List = QTableWidget(self)
        self.setupTable()
        self.adjustTableHeightAndWidth()

        self.refreshDataFromDatabase()
        self.translateui()
    def translateui(self):
        self.List_title_bar.setTitle("")
        self.List_employee_text.setText(QCoreApplication.translate("Admin_Page", u"List of Employess", None))
        ___qtablewidgetitem = self.List.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Admin_Page", u"Employee ID", None))
        ___qtablewidgetitem1 = self.List.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Admin_Page", u"First Name", None))
        ___qtablewidgetitem2 = self.List.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Admin_Page", u"Last Name", None))
        ___qtablewidgetitem3 = self.List.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Admin_Page", u"Email", None))

    def setupTable(self):
        if self.List.columnCount() < 5:  # Increase column count to accommodate the "Details" button
            self.List.setColumnCount(5)

        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(True)

        for col, header_text in enumerate(["ID", "First Name", "Last Name", "Department", "Details"]):
            header_item = QTableWidgetItem(header_text)
            header_item.setFont(font11)
            self.List.setHorizontalHeaderItem(col, header_item)

        self.List.setObjectName(u"List")
        self.List.setGeometry(25, 221, 940, 331)
        self.List.setMaximumHeight(200)
        self.List.setStyleSheet(u"QHeaderView::section {\n"
                                "    background-color: rgb(88, 55, 89);\n"
                                "    color: white;\n"
                                "    border: 1px solid rgb(88, 55, 89);\n"
                                "}")
        self.List.setShowGrid(True)
        self.List.setSortingEnabled(False)
        self.List.setRowCount(0)
        self.List.horizontalHeader().setCascadingSectionResizes(False)
        self.List.horizontalHeader().setDefaultSectionSize(200)
        self.List.horizontalHeader().setHighlightSections(False)
        self.List.horizontalHeader().setProperty("showSortIndicator", False)
        self.List.horizontalHeader().setStretchLastSection(False)
        self.List.verticalHeader().setCascadingSectionResizes(False)
        self.List.verticalHeader().setMinimumSectionSize(25)
        self.List.verticalHeader().setProperty("showSortIndicator", False)
        self.List.verticalHeader().setStretchLastSection(False)
        self.List.setEditTriggers(QAbstractItemView.NoEditTriggers)
        

    def refreshDataFromDatabase(self):
        # Clear existing data
        self.setupTable()
        self.adjustTableHeightAndWidth()
        self.List.setRowCount(0)

        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )
            cursor = connection.cursor()

            # Execute a query to fetch employee data
            cursor.execute("SELECT id, Fname, Lname, email FROM Employee")
            data = cursor.fetchall()

            # Populate the QTableWidget with fetched data
            for row_num, row_data in enumerate(data):
                self.List.insertRow(row_num)
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    font = QFont()
                    font.setPointSize(13)
                    item.setFont(font)
                    self.List.setItem(row_num, col, item)

                # Add "Details" button to the last column
                details_button = QPushButton("Details", self)
                details_button.setStyleSheet(u"border-radius:15px;\n"
                                            "background-color: rgb(50, 55, 89);\n"
                                            "color: rgb(255, 255, 255);")
                details_button.setCursor(QCursor(Qt.PointingHandCursor))
                details_button.clicked.connect(partial(self.showDetails, row_num))



                self.List.setCellWidget(row_num, 4, details_button)  # Use the correct column index

            connection.commit()
            cursor.close()

        except Exception as e:
            print("Error:", e)

        # Adjust table height and width after fetching new data
        self.adjustTableHeightAndWidth()

    def adjustTableHeightAndWidth(self):
        # Adjust the height of the table according to the number of rows
        total_height = sum(self.List.rowHeight(row) for row in range(self.List.rowCount()))
        # Add some extra height to account for header and spacing
        total_height += self.List.horizontalHeader().height() + 20
        # Set the height of the table
        self.List.setFixedHeight(total_height)

        # Adjust the width of the table according to the content
        for col in range(self.List.columnCount()):
            max_width = max(self.List.sizeHintForColumn(col), self.List.columnWidth(col))
            max_width -= 12
            self.List.setColumnWidth(col, max_width)

    def showDetails(self, row):
        # Get the employee ID from the selected row
        employee_id = self.List.item(row, 0).text()

        # Create an instance of the EmployeeDetailsPage with the employee ID
        details_page = Employee_detail_page(employee_id,self.stack_widget)
        details_page.View_Edit.setTitle("")
        details_page.View_edit_text.setText(QCoreApplication.translate("Admin_Page", u"View and Edit Employee", None))
        details_page.Password_text_2.setText(QCoreApplication.translate("Admin_Page", u"Password:", None))
        details_page.Contact_text_2.setText(QCoreApplication.translate("Admin_Page", u"Contact #:", None))
        details_page.Employee_id_text_2.setText(QCoreApplication.translate("Admin_Page", u"Employee ID:", None))
        details_page.Email_text_2.setText(QCoreApplication.translate("Admin_Page", u"Email:", None))
        details_page.Save_button.setText(QCoreApplication.translate("Admin_Page", u"Save", None))
        details_page.Lname_text_2.setText(QCoreApplication.translate("Admin_Page", u"Last Name:", None))
        details_page.Fname_text_2.setText(QCoreApplication.translate("Admin_Page", u"First Name:", None))
        details_page.Salary_text_2.setText(QCoreApplication.translate("Admin_Page", u"Salary:", None))
        details_page.Address_text_2.setText(QCoreApplication.translate("Admin_Page", u"Address:", None))
        details_page.Department_Text_2.setText(QCoreApplication.translate("Admin_Page", u"Department:", None))
        details_page.back_button.setText(QCoreApplication.translate("Admin_Page", u"Back", None))
        self.stack_widget.addWidget(details_page)
        self.stack_widget.setCurrentIndex(1)

class Employee_detail_page(QWidget):
    def __init__(self,id,stacked_widget):
        super(Employee_detail_page, self).__init__()
        self.empid=id
        self.stack_widget=stacked_widget
        font10 = QFont()
        font10.setPointSize(18)
        font12 = QFont()
        font12.setPointSize(13)
        font12.setBold(True)
        font13 = QFont()
        font13.setPointSize(10)
        font13.setBold(True)
        self.setObjectName(u"Employee_Detail_Page")
        self.Email_2 = QLineEdit(self)
        self.Email_2.setObjectName(u"Email_2")
        self.Email_2.setGeometry(QRect(210, 455, 211, 31))
        self.Email_2.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Address_2 = QLineEdit(self)
        self.Address_2.setObjectName(u"Address_2")
        self.Address_2.setGeometry(QRect(660, 345, 211, 31))
        self.Address_2.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Salary_2 = QLineEdit(self)
        self.Salary_2.setObjectName(u"Salary_2")
        self.Salary_2.setGeometry(QRect(390, 540, 211, 31))
        self.Salary_2.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Contact_2 = QLineEdit(self)
        self.Contact_2.setObjectName(u"Contact_2")
        self.Contact_2.setGeometry(QRect(210, 345, 211, 31))
        self.Contact_2.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Department_Text_2 = QLabel(self)
        self.Department_Text_2.setObjectName(u"Department_Text_2")
        self.Department_Text_2.setGeometry(QRect(90, 130, 111, 21))
        self.Department_Text_2.setFont(font12)
        self.Lname_2 = QLineEdit(self)
        self.Lname_2.setObjectName(u"Lname_2")
        self.Lname_2.setGeometry(QRect(660, 235, 211, 31))
        self.Lname_2.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Fname_2 = QLineEdit(self)
        self.Fname_2.setObjectName(u"Fname_2")
        self.Fname_2.setGeometry(QRect(210, 235, 211, 31))
        self.Fname_2.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.View_Edit = QGroupBox(self)
        self.View_Edit.setObjectName(u"View_Edit")
        self.View_Edit.setGeometry(QRect(0, -15, 991, 80))
        self.View_Edit.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.View_edit_text = QLabel(self.View_Edit)
        self.View_edit_text.setObjectName(u"View_edit_text")
        self.View_edit_text.setGeometry(QRect(33, 30, 261, 31))
        self.View_edit_text.setFont(font10)
        self.View_edit_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password_2 = QLineEdit(self)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(660, 455, 211, 31))
        self.password_2.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.password_2.setEchoMode(QLineEdit.Password)
        self.Employee_id_2 = QLineEdit(self)
        self.Employee_id_2.setObjectName(u"Employee_id_2")
        self.Employee_id_2.setGeometry(QRect(660, 125, 210, 30))
        self.Employee_id_2.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Password_text_2 = QLabel(self)
        self.Password_text_2.setObjectName(u"Password_text_2")
        self.Password_text_2.setGeometry(QRect(530, 460, 101, 21))
        self.Password_text_2.setFont(font12)
        self.Contact_text_2 = QLabel(self)
        self.Contact_text_2.setObjectName(u"Contact_text_2")
        self.Contact_text_2.setGeometry(QRect(90, 350, 101, 21))
        self.Contact_text_2.setFont(font12)
        self.Employee_id_text_2 = QLabel(self)
        self.Employee_id_text_2.setObjectName(u"Employee_id_text_2")
        self.Employee_id_text_2.setGeometry(QRect(530, 130, 121, 21))
        self.Employee_id_text_2.setFont(font12)
        self.Email_text_2 = QLabel(self)
        self.Email_text_2.setObjectName(u"Email_text_2")
        self.Email_text_2.setGeometry(QRect(90, 460, 101, 21))
        self.Email_text_2.setFont(font12)
        self.Save_button = QPushButton(self)
        self.Save_button.setObjectName(u"Save_button")
        self.Save_button.setGeometry(QRect(420, 615, 111, 31))
        self.Save_button.setFont(font13)
        self.Save_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Save_button.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(88, 55, 89);\n"
"color: rgb(255, 255, 255);")
        self.Save_button.clicked.connect(self.updateDataToDatabase)
        self.Lname_text_2 = QLabel(self)
        self.Lname_text_2.setObjectName(u"Lname_text_2")
        self.Lname_text_2.setGeometry(QRect(530, 240, 101, 21))
        self.Lname_text_2.setFont(font12)
        self.Fname_text_2 = QLabel(self)
        self.Fname_text_2.setObjectName(u"Fname_text_2")
        self.Fname_text_2.setGeometry(QRect(90, 240, 101, 21))
        self.Fname_text_2.setFont(font12)
        self.Salary_text_2 = QLabel(self)
        self.Salary_text_2.setObjectName(u"Salary_text_2")
        self.Salary_text_2.setGeometry(QRect(310, 545, 101, 21))
        self.Salary_text_2.setFont(font12)
        self.Address_text_2 = QLabel(self)
        self.Address_text_2.setObjectName(u"Address_text_2")
        self.Address_text_2.setGeometry(QRect(530, 350, 101, 21))
        self.Address_text_2.setFont(font12)
        self.Department_2 = QLineEdit(self)
        self.Department_2.setObjectName(u"Department_2")
        self.Department_2.setGeometry(QRect(210, 125, 210, 30))
        self.Department_2.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.back_button = QPushButton(self)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(40, 80, 111, 31))
        self.back_button.setFont(font13)
        self.back_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(88, 55, 89);\n"
"color: rgb(255, 255, 255);")
        self.back_button.clicked.connect(self.back_to_list)
        self.fetchDataFromDatabase() 
    def back_to_list(self):
        # Assuming you have a QStackedWidget named stackedWidget and the current index is currentIndex
        current_index = self.stack_widget.currentIndex()
        current_page = self.stack_widget.widget(current_index)
        self.stack_widget.removeWidget(current_page)
        QTimer.singleShot(0, lambda: self.processRemoval(current_page, current_index))

    def processRemoval(self, current_page, current_index):
        # Remove the current page from the stack widget and delete it
        self.stack_widget.removeWidget(current_page)
        current_page.deleteLater()

        # Set the current index after the removal and deletion are processed
        self.stack_widget.setCurrentIndex(2)

    def fetchDataFromDatabase(self):
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )
            cursor = connection.cursor()

            # Execute a query to fetch employee data based on employee_id
            query = "SELECT * FROM Employee WHERE id = %s"
            cursor.execute(query, (self.empid,))
            data = cursor.fetchone()

            # Display the fetched data in the line edits
            if data:
                self.Employee_id_2.setText(str(data[0]))
                self.Fname_2.setText(data[1])
                self.Lname_2.setText(data[2])
                self.Email_2.setText(data[3])
                self.password_2.setText(data[4])
                self.Address_2.setText(data[5])
                self.Department_2.setText(data[6])
                self.Salary_2.setText(data[7])
                self.Contact_2.setText(data[8])
                
                
                
                
                
                # Similarly, set other line edits with respective data

            connection.commit()
            cursor.close()

        except Exception as e:
            print("Error:", e)
    def updateDataToDatabase(self):
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )
            cursor = connection.cursor()

            # Get data from line edits
            emp_id = self.Employee_id_2.text()
            department = self.Department_2.text()
            fname = self.Fname_2.text()
            lname = self.Lname_2.text()
            contact = self.Contact_2.text()
            address = self.Address_2.text()
            email = self.Email_2.text()
            password = self.password_2.text()
            salary = self.Salary_2.text()

            # Execute a query to update employee data
            query = """
                UPDATE Employee 
                SET  Fname = %s, Lname = %s, email = %s, password = %s, 
                    address = %s,department = %s, salary = %s,contact = %s
                WHERE id = %s
            """
            cursor.execute(query, (fname, lname,email, password, address,department, salary,contact, emp_id))

            connection.commit()
            cursor.close()
            QMessageBox.information(self, "Success", "Employee details updated successfully!")

        except Exception as e:
            print("Error:", e)

class Remove_Employee_page(QWidget):
    def __init__(self, Page):
        super(Remove_Employee_page, self).__init__(Page)
        self.setObjectName(u"Removeemployee_page")
        self.Remove_bar = QGroupBox(self)
        self.Remove_bar.setObjectName(u"Remove_bar")
        self.Remove_bar.setGeometry(QRect(0, 0, 991, 80))
        self.Remove_bar.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.new_employee_text_2 = QLabel(self.Remove_bar)
        self.new_employee_text_2.setObjectName(u"new_employee_text_2")
        self.new_employee_text_2.setGeometry(QRect(60, 20, 261, 31))
        font10=QFont()
        font10.setPointSize(18)
        self.new_employee_text_2.setFont(font10)
        self.new_employee_text_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Enter_ID = QLabel(self)
        self.Enter_ID.setObjectName(u"Enter_ID")
        self.Enter_ID.setGeometry(QRect(320, 260, 311, 51))
        font4=QFont()
        font4.setPointSize(20)
        self.Enter_ID.setFont(font4)
        self.Enter_ID.setStyleSheet(u"background-color: rgb(88, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.Enter_ID.setAlignment(Qt.AlignCenter)
        self.ID_box = QLineEdit(self)
        self.ID_box.setObjectName(u"ID_box")
        self.ID_box.setGeometry(QRect(370, 370, 201, 31))
        self.ID_box.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Remove = QPushButton(self)
        self.Remove.setObjectName(u"Remove")
        self.Remove.setGeometry(QRect(425, 440, 90, 30))
        font11=QFont()
        font11.setBold(True)
        self.Remove.setFont(font11)
        self.Remove.setCursor(QCursor(Qt.PointingHandCursor))
        self.Remove.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(175, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Remove.clicked.connect(self.remove_employee_from_database)
        self.translateui()
    def translateui(self):
        self.Remove_bar.setTitle("")
        self.new_employee_text_2.setText(QCoreApplication.translate("Admin_Page", u"Remove Employee", None))
        self.Enter_ID.setText(QCoreApplication.translate("Admin_Page", u"Enter Employee ID", None))
        self.Remove.setText(QCoreApplication.translate("Admin_Page", u"Remove", None))
        
    def remove_employee_from_database(self):
        # Get the employee ID from the input box
        employee_id = self.ID_box.text()

        # Validate if the ID is not empty
        if not employee_id:
            error_message = "Please enter the Employee ID."
            self.show_error_message(error_message)
            return

        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )
            cursor = connection.cursor()

            # Check if the employee ID exists in the database
            existing_id_query = f"SELECT * FROM Employee WHERE id = '{employee_id}'"
            cursor.execute(existing_id_query)
            existing_id = cursor.fetchone()

            if not existing_id:
                error_message = "Employee ID does not exist."
                self.show_error_message(error_message)
                return

            # Execute a query to remove the employee from the database
            remove_query = f"DELETE FROM Employee WHERE id = '{employee_id}'"
            cursor.execute(remove_query)

            connection.commit()
            cursor.close()

            success_message = "Employee removed successfully!"
            self.show_success_message(success_message)
            # Clear the input box
            self.ID_box.clear()

        except (Exception, psycopg2.Error) as error:
            # Handle database errors
            error_message = f"Error removing employee from the database: {error}"
            self.show_error_message(error_message)

    def show_error_message(self, message):
        # Create a QMessageBox to show the error message
        error_box = QMessageBox()
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        error_box.setIcon(QMessageBox.Warning)
        error_box.setStandardButtons(QMessageBox.Ok)

        # Set the window modality to make it a blocking message box
        error_box.setWindowModality(Qt.WindowModal)

        # Show the message box
        error_box.exec_()
    
    def show_success_message(self, message):
        QMessageBox.information(self, "Success", message, QMessageBox.Ok)

class DashboardPage(QWidget):
    def __init__(self,Page):
        super(DashboardPage, self).__init__(Page)

        self.setObjectName(u"dashboard_page")
        self.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.title_bar = QGroupBox(self)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setGeometry(QRect(0, 60, 991, 80))
        self.Dashboard_text = QLabel(self.title_bar)
        self.Dashboard_text.setObjectName(u"Dashboard_text")
        self.Dashboard_text.setGeometry(QRect(30, 20, 181, 31))
        font4 = QFont()
        font4.setPointSize(20)
        self.Dashboard_text.setFont(font4)
        self.home_text = QLabel(self.title_bar)
        self.home_text.setObjectName(u"home_text")
        self.home_text.setGeometry(QRect(220, 27, 91, 21))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.home_text.setFont(font5)
        self.home_text.setStyleSheet(u"color: rgb(88, 55, 89);")
        self. Admin_dashboard_text = QLabel(self.title_bar)
        self. Admin_dashboard_text.setObjectName(u" Admin_dashboard_text")
        self. Admin_dashboard_text.setGeometry(QRect(320, 27, 171, 21))
        font6 = QFont()
        font6.setPointSize(13)
        self. Admin_dashboard_text.setFont(font6)
        

        self.active_employee = QGroupBox(self)
        # ... (Rest of the initialization code for active_employee group box)
        self.active_employee.setObjectName(u"active_employee")
        self.active_employee.setGeometry(QRect(80, 190, 350, 200))
        self.active_employee.setStyleSheet(u"background-color:rgb(169,169,169);\n"
"\n"
"border-radius:30px;\n"
"")
        self.active_employee_text = QLabel(self.active_employee)
        self.active_employee_text.setObjectName(u"active_employee_text")
        self.active_employee_text.setGeometry(QRect(70, 20, 271, 41))
        font7 = QFont()
        font7.setPointSize(25)
        font7.setBold(False)
        self.active_employee_text.setFont(font7)
        self.active_employee_text.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.active_employee_count = QLabel(self.active_employee)
        self.active_employee_count.setObjectName(u"active_employee_count")
        self.active_employee_count.setGeometry(QRect(140, 80, 81, 91))
        font8 = QFont()
        font8.setPointSize(50)
        self.active_employee_count.setFont(font8)
        self.active_employee_count.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.active_employee_logo = QLabel(self.active_employee)
        self.active_employee_logo.setObjectName(u"active_employee_logo")
        self.active_employee_logo.setGeometry(QRect(10, 20, 51, 41))
        self.active_employee_logo.setPixmap(QPixmap(u"Images/toppng.com-free-twitter-white-icon-employee-icon-white-537x501.png"))
        self.active_employee_logo.setScaledContents(True)
        

        self.pending_leaves = QGroupBox(self)
        # ... (Rest of the initialization code for pending_leaves group box)
        self.pending_leaves.setObjectName(u"pending_leaves")
        self.pending_leaves.setGeometry(QRect(540, 190, 350, 200))
        self.pending_leaves.setStyleSheet(u"\n"
"background-color: rgb(116, 118, 128);\n"
"border-radius:30px;")
        self.pending_leaves_text = QLabel(self.pending_leaves)
        self.pending_leaves_text.setObjectName(u"pending_leaves_text")
        self.pending_leaves_text.setGeometry(QRect(90, 20, 241, 41))
        font9 = QFont()
        font9.setPointSize(25)
        self.pending_leaves_text.setFont(font9)
        self.pending_leaves_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pending_leaves_logo = QLabel(self.pending_leaves)
        self.pending_leaves_logo.setObjectName(u"pending_leaves_logo")
        self.pending_leaves_logo.setGeometry(QRect(20, 20, 47, 41))
        self.pending_leaves_logo.setPixmap(QPixmap(u"Images/pending_logo.png"))
        self.pending_leaves_logo.setScaledContents(True)
        self.pending_leaves_count = QLabel(self.pending_leaves)
        self.pending_leaves_count.setObjectName(u"pending_leaves_count")
        self.pending_leaves_count.setGeometry(QRect(150, 100, 101, 61))
        self.pending_leaves_count.setFont(font8)
        self.pending_leaves_count.setStyleSheet(u"color: rgb(255, 255, 255);")
        

        self.approved_leaves = QGroupBox(self)
        # ... (Rest of the initialization code for approved_leaves group box)
        self.approved_leaves.setObjectName(u"approved_leaves")
        self.approved_leaves.setGeometry(QRect(80, 460, 350, 200))
        self.approved_leaves.setStyleSheet(u"background-color: rgb(140, 146, 172);\n"
"border-radius:30px;")
        self.approved_leaves_logo = QLabel(self.approved_leaves)
        self.approved_leaves_logo.setObjectName(u"approved_leaves_logo")
        self.approved_leaves_logo.setGeometry(QRect(10, 20, 47, 41))
        self.approved_leaves_logo.setPixmap(QPixmap(u"Images/approve_logo.png"))
        self.approved_leaves_logo.setScaledContents(True)
        self.approved_leaves_text = QLabel(self.approved_leaves)
        self.approved_leaves_text.setObjectName(u"approved_leaves_text")
        self.approved_leaves_text.setGeometry(QRect(70, 20, 261, 41))
        self.approved_leaves_text.setFont(font9)
        self.approved_leaves_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.approved_leaves_count = QLabel(self.approved_leaves)
        self.approved_leaves_count.setObjectName(u"approved_leaves_count")
        self.approved_leaves_count.setGeometry(QRect(150, 80, 61, 81))
        self.approved_leaves_count.setFont(font8)
        self.approved_leaves_count.setStyleSheet(u"color: rgb(255, 255, 255);")
        

        self.declined_leaves = QGroupBox(self)
        # ... (Rest of the initialization code for declined_leaves group box)
        self.declined_leaves.setObjectName(u"declined_leaves")
        self.declined_leaves.setGeometry(QRect(540, 460, 350, 200))
        self.declined_leaves.setStyleSheet(u"background-color: rgb(98, 112, 156);\n"
"border-radius:30px;")
        self.declined_leaves_logo = QLabel(self.declined_leaves)
        self.declined_leaves_logo.setObjectName(u"declined_leaves_logo")
        self.declined_leaves_logo.setGeometry(QRect(10, 10, 61, 51))
        self.declined_leaves_logo.setPixmap(QPixmap(u"Images/Decline_logo.png"))
        self.declined_leaves_logo.setScaledContents(True)
        self.declined_leaves_text = QLabel(self.declined_leaves)
        self.declined_leaves_text.setObjectName(u"declined_leaves_text")
        self.declined_leaves_text.setGeometry(QRect(70, 10, 251, 51))
        self.declined_leaves_text.setFont(font9)
        self.declined_leaves_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.declined_leaves_count = QLabel(self.declined_leaves)
        self.declined_leaves_count.setObjectName(u"declined_leaves_count")
        self.declined_leaves_count.setGeometry(QRect(140, 90, 91, 61))
        self.declined_leaves_count.setFont(font8)
        self.declined_leaves_count.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.translateui()
        self.set_values()
    def set_values(self):
        connection = psycopg2.connect(
            user="postgres",
            password="zendagimigzara",
            host="localhost",
            port="5432",
            database="AEMS"
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        try:
            query = "SELECT * FROM Leave_Record WHERE status = 'accepted';"
            cursor.execute(query)

            # Fetch all the rows
            records = cursor.fetchall()
            approve_count=len(records)

            query = "SELECT * FROM Leave_Record WHERE status = 'rejected';"
            cursor.execute(query)

            # Fetch all the rows
            records = cursor.fetchall()
            decline_count=len(records)

            query = "SELECT * FROM Leave_Record WHERE status = 'pending';"
            cursor.execute(query)

            # Fetch all the rows
            records = cursor.fetchall()
            pending_count=len(records)

            query = "SELECT * FROM Employee;"
            cursor.execute(query)

            # Fetch all the rows
            records = cursor.fetchall()
            employee_count=len(records)

            self.approved_leaves_count.setText(str(approve_count))
            self.declined_leaves_count.setText(str(decline_count))
            self.pending_leaves_count.setText(str(pending_count))
            self.active_employee_count.setText(str(employee_count))
        except Exception as e:
            print(f"Error fetching approved leave records: {e}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
        

    def translateui(self):
        self.title_bar.setTitle("")
        self.Dashboard_text.setText(QCoreApplication.translate(" Admin_Page", u"Dashboard", None))
        self.home_text.setText(QCoreApplication.translate(" Admin_Page", u"Home  /", None))
        self. Admin_dashboard_text.setText(QCoreApplication.translate(" Admin_Page", u" Admin's  Dashboard", None))
        self.active_employee.setTitle("")
        self.active_employee_text.setText(QCoreApplication.translate(" Admin_Page", u"Active Employees", None))
        self.active_employee_count.setText(QCoreApplication.translate(" Admin_Page", u"10", None))
        self.active_employee_logo.setText("")
        self.pending_leaves.setTitle("")
        self.pending_leaves_text.setText(QCoreApplication.translate(" Admin_Page", u"Pending Leaves", None))
        self.pending_leaves_logo.setText("")
        self.pending_leaves_count.setText(QCoreApplication.translate(" Admin_Page", u"4", None))
        self.approved_leaves.setTitle("")
        self.approved_leaves_logo.setText("")
        self.approved_leaves_text.setText(QCoreApplication.translate(" Admin_Page", u"Approved Leaves", None))
        self.approved_leaves_count.setText(QCoreApplication.translate(" Admin_Page", u"5", None))
        self.declined_leaves.setTitle("")
        self.declined_leaves_logo.setText("")
        self.declined_leaves_text.setText(QCoreApplication.translate(" Admin_Page", u"Declined Leaves", None))
        self.declined_leaves_count.setText(QCoreApplication.translate(" Admin_Page", u"11", None))

class PendingPage(QWidget):
    def __init__(self,Page):
        super(PendingPage, self).__init__(Page)
        self.setObjectName(u"pending_leave")
        self.pending_bar = QGroupBox(self)
        self.pending_bar.setObjectName(u"pending_bar")
        self.pending_bar.setGeometry(QRect(0, 0, 991, 80))
        self.pending_bar.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.pending_text = QLabel(self.pending_bar)
        self.pending_text.setObjectName(u"pending_text")
        self.pending_text.setGeometry(QRect(33, 22, 261, 31))
        font10 = QFont()
        font10.setPointSize(18)
        self.pending_text.setFont(font10)
        self.pending_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Pending_table = QTableWidget(self)
        if (self.Pending_table.columnCount() < 7):
            self.Pending_table.setColumnCount(7)
        __qtablewidgetitem9 = QTableWidgetItem()
        font11 = QFont()
        font11.setBold(True)
        __qtablewidgetitem9.setFont(font11);
        self.Pending_table.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font11);
        self.Pending_table.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font11);
        self.Pending_table.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font11);
        self.Pending_table.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font11);
        self.Pending_table.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font11);
        self.Pending_table.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font11);
        self.Pending_table.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        self.Pending_table.setObjectName(u"Pending_table")
        self.Pending_table.setGeometry(QRect(25, 230, 925, 331))
        self.Pending_table.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(88, 55, 89); /* Set your desired background color */\n"
"    color: white; /* Set the text color */\n"
"    border: 1px solid rgb(88, 55, 89); /* Set the border color */\n"
"}")
        self.Pending_table.setShowGrid(True)
        self.Pending_table.setSortingEnabled(False)
        self.Pending_table.setRowCount(0)
        self.Pending_table.horizontalHeader().setCascadingSectionResizes(False)
        self.Pending_table.horizontalHeader().setDefaultSectionSize(131)
        self.Pending_table.horizontalHeader().setHighlightSections(False)
        self.Pending_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.Pending_table.horizontalHeader().setStretchLastSection(False)
        self.Pending_table.verticalHeader().setCascadingSectionResizes(False)
        self.Pending_table.verticalHeader().setMinimumSectionSize(25)
        self.Pending_table.verticalHeader().setProperty("showSortIndicator", False)
        self.Pending_table.verticalHeader().setStretchLastSection(False)
        self.Total_text = QLabel(self)
        self.Total_text.setObjectName(u"Total_text")
        self.Total_text.setGeometry(QRect(90, 120, 111, 31))
        font15 = QFont()
        font15.setPointSize(20)
        font15.setBold(True)
        self.Total_text.setFont(font15)
        self.Total_text.setStyleSheet(u"color: rgb(88, 55, 89);")
        self.Total_input = QLabel(self)
        self.Total_input.setObjectName(u"Total_input")
        self.Total_input.setGeometry(QRect(180, 125, 121, 21))
        font4 = QFont()
        font4.setPointSize(20)
        self.Total_input.setFont(font4)
        self.translateui()
        self.Pending_table.setColumnCount(9)
        self.Pending_table.setHorizontalHeaderItem(7, QTableWidgetItem("Actions"))
        self.Pending_table.setHorizontalHeaderItem(8, QTableWidgetItem("Actions"))
        self.populate_pending_table()
    def populate_pending_table(self):
        # Connect to the database
        connection = psycopg2.connect(
            user="postgres",
            password="zendagimigzara",
            host="localhost",
            port="5432",
            database="AEMS"
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        try:
            # Execute the SELECT query to fetch approved leave records
            query = "SELECT leave_id, employee_id, start_date, end_date, category, description, status FROM Leave_Record WHERE status = 'pending';"
            cursor.execute(query)

            # Fetch all the rows
            records = cursor.fetchall()

            # Set the number of rows in the table
            self.Pending_table.setRowCount(len(records))

            # Populate the table with the fetched data
            for row, record in enumerate(records):
                for col, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.Pending_table.setItem(row, col, item)

                # Add buttons for each row to change status
                approve_button = QPushButton("Approve")
                decline_button = QPushButton("Decline")

                # Connect button click events to corresponding methods
                approve_button.clicked.connect(self.create_approve_button_click_handler(row))
                decline_button.clicked.connect(self.create_decline_button_click_handler(row))

                # Add buttons to separate cells in the last column
                self.Pending_table.setCellWidget(row, 7, approve_button)
                self.Pending_table.setCellWidget(row, 8, decline_button)



            total_count = len(records)
            self.Total_input.setText(str(total_count))

        except Exception as e:
            print(f"Error fetching approved leave records: {e}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
        
        self.adjustTableHeightAndWidth()
    def create_approve_button_click_handler(self, row):
        def handler():
            self.change_status(row, "accepted")
        return handler

    def create_decline_button_click_handler(self, row):
        def handler():
            self.change_status(row, "rejected")
        return handler
    def adjustTableHeightAndWidth(self):
        # Adjust the height of the table according to the number of rows
        total_height = sum(self.Pending_table.rowHeight(row) for row in range(self.Pending_table.rowCount()))
        # Add some extra height to account for header and spacing
        total_height += self.Pending_table.horizontalHeader().height() + 20
        # Set the height of the table
        self.Pending_table.setFixedHeight(total_height)

        # Adjust the width of the table according to the content
        for col in range(self.Pending_table.columnCount()):
            max_width = max(self.Pending_table.sizeHintForColumn(col), self.Pending_table.columnWidth(col))
            max_width -= 2
            self.Pending_table.setColumnWidth(col, max_width)
    
    def change_status(self, row, new_status):
        leave_id_item = self.Pending_table.item(row, 0)
        leave_id = leave_id_item.text()


        # Connect to the database
        connection = psycopg2.connect(
            user="postgres",
            password="zendagimigzara",
            host="localhost",
            port="5432",
            database="AEMS"
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        try:
            # Execute the UPDATE query to change the leave status
            query = "UPDATE Leave_Record SET status = %s WHERE leave_id = %s;"
            cursor.execute(query, (new_status, leave_id))

            # Commit the transaction
            connection.commit()

            # Update the UI
            self.populate_pending_table()

        except Exception as e:
            print(f"Error changing leave status: {e}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()


    def translateui(self):
        self.pending_bar.setTitle("")
        self.pending_text.setText(QCoreApplication.translate("Admin_Page", u"Pending Leaves", None))
        ___qtablewidgetitem9 = self.Pending_table.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Admin_Page", u"Leave_ID", None));
        ___qtablewidgetitem10 = self.Pending_table.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Admin_Page", u"Employee_ID", None));
        ___qtablewidgetitem11 = self.Pending_table.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Admin_Page", u"Start_date", None));
        ___qtablewidgetitem12 = self.Pending_table.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Admin_Page", u"Email", None));
        ___qtablewidgetitem13 = self.Pending_table.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Admin_Page", u"Category", None));
        ___qtablewidgetitem14 = self.Pending_table.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Admin_Page", u"Description", None));
        ___qtablewidgetitem15 = self.Pending_table.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Admin_Page", u"Status", None));
        self.Total_text.setText(QCoreApplication.translate("Admin_Page", u"Total:", None))
        self.Total_input.setText(QCoreApplication.translate("Admin_Page", u"20", None))
        
class ApprovedPage(QWidget):
    def __init__(self,Page):
        super(ApprovedPage, self).__init__(Page)
        self.setObjectName(u"approved_leave")
        self.approved_bar = QGroupBox(self)
        self.approved_bar.setObjectName(u"approved_bar")
        self.approved_bar.setGeometry(QRect(0, -10, 991, 80))
        self.approved_bar.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.Approved_text = QLabel(self.approved_bar)
        self.Approved_text.setObjectName(u"Approved_text")
        self.Approved_text.setGeometry(QRect(33, 22, 261, 31))
        font10 = QFont()
        font10.setPointSize(18)
        self.Approved_text.setFont(font10)
        self.Approved_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Total_input_2 = QLabel(self)
        self.Total_input_2.setObjectName(u"Total_input_2")
        self.Total_input_2.setGeometry(QRect(180, 115, 121, 21))
        font4 = QFont()
        font4.setPointSize(20)
        self.Total_input_2.setFont(font4)
        self.Approved_table = QTableWidget(self)
        if (self.Approved_table.columnCount() < 7):
            self.Approved_table.setColumnCount(7)
        __qtablewidgetitem16 = QTableWidgetItem()
        font11 = QFont()
        font11.setBold(True)
        __qtablewidgetitem16.setFont(font11);
        self.Approved_table.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font11);
        self.Approved_table.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font11);
        self.Approved_table.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font11);
        self.Approved_table.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font11);
        self.Approved_table.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font11);
        self.Approved_table.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font11);
        self.Approved_table.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        self.Approved_table.setObjectName(u"Approved_table")
        self.Approved_table.setGeometry(QRect(25, 220, 925, 331))
        self.Approved_table.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(88, 55, 89); /* Set your desired background color */\n"
"    color: white; /* Set the text color */\n"
"    border: 1px solid rgb(88, 55, 89); /* Set the border color */\n"
"}")
        self.Approved_table.setShowGrid(True)
        self.Approved_table.setSortingEnabled(False)
        self.Approved_table.setRowCount(0)
        self.Approved_table.horizontalHeader().setCascadingSectionResizes(False)
        self.Approved_table.horizontalHeader().setDefaultSectionSize(131)
        self.Approved_table.horizontalHeader().setHighlightSections(False)
        self.Approved_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.Approved_table.horizontalHeader().setStretchLastSection(False)
        self.Approved_table.verticalHeader().setCascadingSectionResizes(False)
        self.Approved_table.verticalHeader().setMinimumSectionSize(25)
        self.Approved_table.verticalHeader().setProperty("showSortIndicator", False)
        self.Approved_table.verticalHeader().setStretchLastSection(False)
        self.Total_text_2 = QLabel(self)
        self.Total_text_2.setObjectName(u"Total_text_2")
        self.Total_text_2.setGeometry(QRect(90, 110, 111, 31))
        font15 = QFont()
        font15.setPointSize(20)
        font15.setBold(True)
        self.Total_text_2.setFont(font15)
        self.Total_text_2.setStyleSheet(u"color: rgb(88, 55, 89);")
        self.translateui()
        self.populate_approved_table()

    
    def populate_approved_table(self):
        # Connect to the database
        connection = psycopg2.connect(
            user="postgres",
            password="zendagimigzara",
            host="localhost",
            port="5432",
            database="AEMS"
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        try:
            # Execute the SELECT query to fetch approved leave records
            query = "SELECT leave_id, employee_id, start_date, end_date, category, description, status FROM Leave_Record WHERE status = 'accepted';"
            cursor.execute(query)

            # Fetch all the rows
            records = cursor.fetchall()

            # Set the number of rows in the table
            self.Approved_table.setRowCount(len(records))

            # Populate the table with the fetched data
            for row, record in enumerate(records):
                for col, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.Approved_table.setItem(row, col, item)

            total_count = len(records)
            self.Total_input_2.setText(str(total_count))

        except Exception as e:
            print(f"Error fetching approved leave records: {e}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
        self.adjustTableHeightAndWidth()

    def adjustTableHeightAndWidth(self):
        # Adjust the height of the table according to the number of rows
        total_height = sum(self.Approved_table.rowHeight(row) for row in range(self.Approved_table.rowCount()))
        # Add some extra height to account for header and spacing
        total_height += self.Approved_table.horizontalHeader().height() + 20
        # Set the height of the table
        self.Approved_table.setFixedHeight(total_height)

        # Adjust the width of the table according to the content
        for col in range(self.Approved_table.columnCount()):
            max_width = max(self.Approved_table.sizeHintForColumn(col), self.Approved_table.columnWidth(col))
            max_width -= 2
            self.Approved_table.setColumnWidth(col, max_width)
    def translateui(self):
        self.approved_bar.setTitle("")
        self.Approved_text.setText(QCoreApplication.translate("Admin_Page", u"Approved Leaves", None))
        self.Total_input_2.setText(QCoreApplication.translate("Admin_Page", u"20", None))
        ___qtablewidgetitem16 = self.Approved_table.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Admin_Page", u"Leave_ID", None));
        ___qtablewidgetitem17 = self.Approved_table.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Admin_Page", u"Employee_ID", None));
        ___qtablewidgetitem18 = self.Approved_table.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Admin_Page", u"Start_date", None));
        ___qtablewidgetitem19 = self.Approved_table.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Admin_Page", u"End_date", None));
        ___qtablewidgetitem20 = self.Approved_table.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Admin_Page", u"Category", None));
        ___qtablewidgetitem21 = self.Approved_table.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Admin_Page", u"Description", None));
        ___qtablewidgetitem22 = self.Approved_table.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Admin_Page", u"Status", None));
        self.Total_text_2.setText(QCoreApplication.translate("Admin_Page", u"Total:", None))

class DeclinedPage(QWidget):
    def __init__(self,Page):
        super(DeclinedPage, self).__init__(Page)
        self.setObjectName(u"declined_leave")
        self.Total_input_3 = QLabel(self)
        self.Total_input_3.setObjectName(u"Total_input_3")
        self.Total_input_3.setGeometry(QRect(180, 115, 121, 21))
        font10 = QFont()
        font10.setPointSize(18)
        font4 = QFont()
        font4.setPointSize(20)
        self.Total_input_3.setFont(font4)
        self.Declined_table = QTableWidget(self)
        if (self.Declined_table.columnCount() < 7):
            self.Declined_table.setColumnCount(7)
        __qtablewidgetitem23 = QTableWidgetItem()
        font11 = QFont()
        font11.setBold(True)
        __qtablewidgetitem23.setFont(font11);
        self.Declined_table.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font11);
        self.Declined_table.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font11);
        self.Declined_table.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font11);
        self.Declined_table.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font11);
        self.Declined_table.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font11);
        self.Declined_table.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font11);
        self.Declined_table.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        self.Declined_table.setObjectName(u"Declined_table")
        self.Declined_table.setGeometry(QRect(25, 220, 925, 331))
        self.Declined_table.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(88, 55, 89); /* Set your desired background color */\n"
"    color: white; /* Set the text color */\n"
"    border: 1px solid rgb(88, 55, 89); /* Set the border color */\n"
"}")
        self.Declined_table.setShowGrid(True)
        self.Declined_table.setSortingEnabled(False)
        self.Declined_table.setRowCount(0)
        self.Declined_table.horizontalHeader().setCascadingSectionResizes(False)
        self.Declined_table.horizontalHeader().setDefaultSectionSize(131)
        self.Declined_table.horizontalHeader().setHighlightSections(False)
        self.Declined_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.Declined_table.horizontalHeader().setStretchLastSection(False)
        self.Declined_table.verticalHeader().setCascadingSectionResizes(False)
        self.Declined_table.verticalHeader().setMinimumSectionSize(25)
        self.Declined_table.verticalHeader().setProperty("showSortIndicator", False)
        self.Declined_table.verticalHeader().setStretchLastSection(False)
        self.Declined_bar = QGroupBox(self)
        self.Declined_bar.setObjectName(u"Declined_bar")
        self.Declined_bar.setGeometry(QRect(0, -10, 991, 80))
        self.Declined_bar.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.Declined_text = QLabel(self.Declined_bar)
        self.Declined_text.setObjectName(u"Declined_text")
        self.Declined_text.setGeometry(QRect(33, 25, 261, 31))
        self.Declined_text.setFont(font10)
        self.Declined_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Total_text_3 = QLabel(self)
        self.Total_text_3.setObjectName(u"Total_text_3")
        self.Total_text_3.setGeometry(QRect(90, 110, 111, 31))
        font15 = QFont()
        font15.setPointSize(20)
        font15.setBold(True)
        self.Total_text_3.setFont(font15)
        self.Total_text_3.setStyleSheet(u"color: rgb(88, 55, 89);")
        self.translateui()
        self.populate_declined_table()
    def populate_declined_table(self):
        # Connect to the database
        connection = psycopg2.connect(
            user="postgres",
            password="zendagimigzara",
            host="localhost",
            port="5432",
            database="AEMS"
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        try:
            # Execute the SELECT query to fetch approved leave records
            query = "SELECT leave_id, employee_id, start_date, end_date, category, description, status FROM Leave_Record WHERE status = 'rejected';"
            cursor.execute(query)

            # Fetch all the rows
            records = cursor.fetchall()

            # Set the number of rows in the table
            self.Declined_table.setRowCount(len(records))

            # Populate the table with the fetched data
            for row, record in enumerate(records):
                for col, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.Declined_table.setItem(row, col, item)

            total_count = len(records)
            self.Total_input_3.setText(str(total_count))

        except Exception as e:
            print(f"Error fetching approved leave records: {e}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
        self.adjustTableHeightAndWidth()

    def adjustTableHeightAndWidth(self):
        # Adjust the height of the table according to the number of rows
        total_height = sum(self.Declined_table.rowHeight(row) for row in range(self.Declined_table.rowCount()))
        # Add some extra height to account for header and spacing
        total_height += self.Declined_table.horizontalHeader().height() + 20
        # Set the height of the table
        self.Declined_table.setFixedHeight(total_height)

        # Adjust the width of the table according to the content
        for col in range(self.Declined_table.columnCount()):
            max_width = max(self.Declined_table.sizeHintForColumn(col), self.Declined_table.columnWidth(col))
            max_width -= 2
            self.Declined_table.setColumnWidth(col, max_width)

    def translateui(self):
        self.Total_input_3.setText(QCoreApplication.translate("Admin_Page", u"20", None))
        ___qtablewidgetitem23 = self.Declined_table.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Admin_Page", u"Leave_ID", None));
        ___qtablewidgetitem24 = self.Declined_table.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Admin_Page", u"Employee_ID", None));
        ___qtablewidgetitem25 = self.Declined_table.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Admin_Page", u"Start_date", None));
        ___qtablewidgetitem26 = self.Declined_table.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Admin_Page", u"Email", None));
        ___qtablewidgetitem27 = self.Declined_table.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Admin_Page", u"Category", None));
        ___qtablewidgetitem28 = self.Declined_table.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Admin_Page", u"Description", None));
        ___qtablewidgetitem29 = self.Declined_table.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Admin_Page", u"Status", None));
        self.Declined_bar.setTitle("")
        self.Declined_text.setText(QCoreApplication.translate("Admin_Page", u"Declined Leaves", None))
        self.Total_text_3.setText(QCoreApplication.translate("Admin_Page", u"Total:", None))

               
class  AdminPage(QMainWindow):
    def __init__(self):
        super(AdminPage, self).__init__()

        self.setObjectName(u" Admin_Page")
        self.resize(1280, 720)
        self.setMinimumSize(QSize(1280, 720))
        self.setMaximumSize(QSize(1280, 720))
        self.PAGE = QWidget(self)
        self.PAGE.setObjectName(u"PAGE")


        # Create instances of your pages
        


        self.side_bar = Sidebar(self.PAGE,self)
        self.Main_pages = QStackedWidget(self.PAGE)
        self.Main_pages.setObjectName(u"Main_pages")
        self.Main_pages.setEnabled(True)
        self.Main_pages.setGeometry(QRect(290, 0, 990, 720))
        self.Main_pages.setMinimumSize(QSize(990, 720))
        self.dashboard_page = DashboardPage(self.PAGE)
        self.Main_pages.addWidget(self.dashboard_page)
        self.side_bar.setup_connections(self.Main_pages)
        self.setCentralWidget(self.PAGE)

        self.retranslateUi()

    def retranslateUi(self):
        # ... (Rest of the retranslation code)
        self.setWindowTitle(QCoreApplication.translate(" Admin_Page", u"MainWindow", None))
    def signout(self):
            self.close()
            login=login_page.LoginPage()
            login.show()
            login.exec_()
    # retranslateUi
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window =  AdminPage()
    window.show()
    sys.exit(app.exec_())
