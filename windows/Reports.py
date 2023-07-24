# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Reports.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#########################################################################
#                                                                       #
#                            UI Generation                              #
#                                                                       #
#########################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication, QDate

import mysql.connector
from PyQt5.QtWidgets import QMessageBox

import datetime

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Enable high DPI scaling
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # Use high DPI icons


class Ui_ReportsDialog(object):
    def setupUi(self, ReportsDialog):
        ReportsDialog.setObjectName("ReportsDialog")
        ReportsDialog.resize(440, 510)
        self.btnClose = QtWidgets.QDialogButtonBox(ReportsDialog)
        self.btnClose.setGeometry(QtCore.QRect(10, 470, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btnClose.setFont(font)
        self.btnClose.setOrientation(QtCore.Qt.Horizontal)
        self.btnClose.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.btnClose.setObjectName("btnClose")
        self.frame = QtWidgets.QFrame(ReportsDialog)
        self.frame.setGeometry(QtCore.QRect(10, 50, 421, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(6, 6, 6, 6)
        self.formLayout.setObjectName("formLayout")
        self.lblSelectSemester = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblSelectSemester.setFont(font)
        self.lblSelectSemester.setObjectName("lblSelectSemester")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSelectSemester)
        self.cmbSelectSemester = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cmbSelectSemester.setFont(font)
        self.cmbSelectSemester.setObjectName("cmbSelectSemester")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbSelectSemester)
        self.lblNumberOfStudents = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblNumberOfStudents.setFont(font)
        self.lblNumberOfStudents.setObjectName("lblNumberOfStudents")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblNumberOfStudents)
        self.txtNumberOfStudents = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtNumberOfStudents.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtNumberOfStudents.setFont(font)
        self.txtNumberOfStudents.setObjectName("txtNumberOfStudents")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtNumberOfStudents)
        self.btnReportStudents = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReportStudents.sizePolicy().hasHeightForWidth())
        self.btnReportStudents.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnReportStudents.setFont(font)
        self.btnReportStudents.setObjectName("btnReportStudents")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btnReportStudents)
        self.lblTitle1 = QtWidgets.QLabel(ReportsDialog)
        self.lblTitle1.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblTitle1.setFont(font)
        self.lblTitle1.setAcceptDrops(False)
        self.lblTitle1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTitle1.setAutoFillBackground(False)
        self.lblTitle1.setStyleSheet("background-color: rgb(22, 9, 88);\n"
"color: rgb(255, 255, 255);")
        self.lblTitle1.setFrameShape(QtWidgets.QFrame.Box)
        self.lblTitle1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTitle1.setLineWidth(2)
        self.lblTitle1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle1.setWordWrap(True)
        self.lblTitle1.setObjectName("lblTitle1")
        self.lblTitle2 = QtWidgets.QLabel(ReportsDialog)
        self.lblTitle2.setGeometry(QtCore.QRect(10, 170, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblTitle2.setFont(font)
        self.lblTitle2.setAcceptDrops(False)
        self.lblTitle2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTitle2.setAutoFillBackground(False)
        self.lblTitle2.setStyleSheet("background-color: rgb(22, 9, 88);\n"
"color: rgb(255, 255, 255);")
        self.lblTitle2.setFrameShape(QtWidgets.QFrame.Box)
        self.lblTitle2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTitle2.setLineWidth(2)
        self.lblTitle2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle2.setWordWrap(True)
        self.lblTitle2.setObjectName("lblTitle2")
        self.lblTitle_3 = QtWidgets.QLabel(ReportsDialog)
        self.lblTitle_3.setGeometry(QtCore.QRect(10, 330, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblTitle_3.setFont(font)
        self.lblTitle_3.setAcceptDrops(False)
        self.lblTitle_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTitle_3.setAutoFillBackground(False)
        self.lblTitle_3.setStyleSheet("background-color: rgb(22, 9, 88);\n"
"color: rgb(255, 255, 255);")
        self.lblTitle_3.setFrameShape(QtWidgets.QFrame.Box)
        self.lblTitle_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTitle_3.setLineWidth(2)
        self.lblTitle_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle_3.setWordWrap(True)
        self.lblTitle_3.setObjectName("lblTitle_3")
        self.frame_2 = QtWidgets.QFrame(ReportsDialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 210, 421, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 421, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(6, 6, 6, 6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblSelectDepartment = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblSelectDepartment.setFont(font)
        self.lblSelectDepartment.setObjectName("lblSelectDepartment")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSelectDepartment)
        self.cmbSelectDepartment = QtWidgets.QComboBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cmbSelectDepartment.setFont(font)
        self.cmbSelectDepartment.setObjectName("cmbSelectDepartment")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbSelectDepartment)
        self.lblNumberOfCourses = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblNumberOfCourses.setFont(font)
        self.lblNumberOfCourses.setObjectName("lblNumberOfCourses")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblNumberOfCourses)
        self.txtNumberOfCourses = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtNumberOfCourses.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtNumberOfCourses.setFont(font)
        self.txtNumberOfCourses.setObjectName("txtNumberOfCourses")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtNumberOfCourses)
        self.btnReportCourses = QtWidgets.QPushButton(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReportCourses.sizePolicy().hasHeightForWidth())
        self.btnReportCourses.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnReportCourses.setFont(font)
        self.btnReportCourses.setObjectName("btnReportCourses")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btnReportCourses)
        self.frame_3 = QtWidgets.QFrame(ReportsDialog)
        self.frame_3.setGeometry(QtCore.QRect(10, 370, 421, 91))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 421, 91))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(6, 6, 6, 6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lblSelectCourse = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblSelectCourse.setFont(font)
        self.lblSelectCourse.setObjectName("lblSelectCourse")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSelectCourse)
        self.cmbSelectCourse = QtWidgets.QComboBox(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cmbSelectCourse.setFont(font)
        self.cmbSelectCourse.setObjectName("cmbSelectCourse")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbSelectCourse)
        self.lblNumberOfClasses = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lblNumberOfClasses.setFont(font)
        self.lblNumberOfClasses.setObjectName("lblNumberOfClasses")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblNumberOfClasses)
        self.txtNumberOfClasses = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.txtNumberOfClasses.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txtNumberOfClasses.setFont(font)
        self.txtNumberOfClasses.setObjectName("txtNumberOfClasses")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtNumberOfClasses)
        self.btnReportClasses = QtWidgets.QPushButton(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReportClasses.sizePolicy().hasHeightForWidth())
        self.btnReportClasses.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnReportClasses.setFont(font)
        self.btnReportClasses.setObjectName("btnReportClasses")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btnReportClasses)
        self.frame.raise_()
        self.btnClose.raise_()
        self.lblTitle1.raise_()
        self.lblTitle2.raise_()
        self.lblTitle_3.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()

        self.retranslateUi(ReportsDialog)
        self.btnClose.accepted.connect(ReportsDialog.accept) # type: ignore
        self.btnClose.rejected.connect(ReportsDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ReportsDialog)

        self.initialSetup()

    def retranslateUi(self, ReportsDialog):
        _translate = QtCore.QCoreApplication.translate
        ReportsDialog.setWindowTitle(_translate("ReportsDialog", "Reports"))
        self.lblSelectSemester.setText(_translate("ReportsDialog", "Select Semester:"))
        self.lblNumberOfStudents.setText(_translate("ReportsDialog", "Total number of Students:"))
        self.btnReportStudents.setText(_translate("ReportsDialog", "Report number of Students"))
        self.lblTitle1.setText(_translate("ReportsDialog", "Total Students in a Semester"))
        self.lblTitle2.setText(_translate("ReportsDialog", "Total Courses in a Department"))
        self.lblTitle_3.setText(_translate("ReportsDialog", "Total Classes for a Course"))
        self.lblSelectDepartment.setText(_translate("ReportsDialog", "Select Department:"))
        self.lblNumberOfCourses.setText(_translate("ReportsDialog", "Total number of Courses:"))
        self.btnReportCourses.setText(_translate("ReportsDialog", "Report number of Courses"))
        self.lblSelectCourse.setText(_translate("ReportsDialog", "Select Course:"))
        self.lblNumberOfClasses.setText(_translate("ReportsDialog", "Total number of Classes:"))
        self.btnReportClasses.setText(_translate("ReportsDialog", "Report number of Classes"))

#####################     End UI Generation     #####################

    def initialSetup(self):
        self.setupEvents()
        self.setupDatabase()
        self.setupSemesterCombobox()
        self.setupDepartmentCombobox()
        self.setupCourseCombobox()

    #########################################################################
    #                                                                       #
    #                            Events                                     #
    #                                                                       #
    #########################################################################

    def setupEvents(self):
        self.btnReportStudents.clicked.connect(self.btnReportStudents_clicked)
        self.btnReportCourses.clicked.connect(self.btnReportCourses_clicked)
        self.btnReportClasses.clicked.connect(self.btnReportClasses_clicked)

    def setupSemesterCombobox(self):
        semesterList = self.retrieveSemesters()

        # Place semester options within combo box
        self.cmbSelectSemester.clear()
        for semester in semesterList:
            self.cmbSelectSemester.addItem(str(semester[0]) + ". " + str(semester[1]) + " " + str(semester[2]))

        self.cmbSelectSemester.setCurrentIndex(-1)


    def setupDepartmentCombobox(self):
        departmentList = self.retrieveDepartments()

        # Place department options within combo box
        self.cmbSelectDepartment.clear()
        for department in departmentList:
            self.cmbSelectDepartment.addItem(str(department[0]))

        self.cmbSelectDepartment.setCurrentIndex(-1)


    def setupCourseCombobox(self):
        classList = self.retrieveCourses()

        # Place class options within combo box
        self.cmbSelectCourse.clear()
        for class_ in classList:
            self.cmbSelectCourse.addItem(str(class_[0]) + ". " + str(class_[1]))

        self.cmbSelectCourse.setCurrentIndex(-1)

    # Total Students in a Semester:
    # This report is crucial as it aids in capacity planning and forecasting resources
    # based on student numbers. It helps understand enrollment trends, which are key for
    # financial planning and scheduling decisions.

    def btnReportStudents_clicked(self):
        # Check if combobox is selected
        if self.cmbSelectSemester.currentIndex() == -1:
            QMessageBox.warning(None, "Select Row", "Please select a semester first")
            return

        # Retrieve selected semester from combobox by taking the numbers before .
        semester = int(self.cmbSelectSemester.currentText().split(".")[0])
        print(semester)

        numStudents = self.reportStudents(semester)
        self.txtNumberOfStudents.setText(str(numStudents[0]))

    # Total Courses in a Department:
    # This report gives insights into the variety of courses a department offers.
    # It's instrumental for academic planning and advising students about their course choices.

    def btnReportCourses_clicked(self):
        # Check if combobox is selected
        if self.cmbSelectDepartment.currentIndex() == -1:
            QMessageBox.warning(None, "Select Row", "Please select a department first")
            return

        # Retrieve selected department from combobox
        department = self.cmbSelectDepartment.currentText()
        print(department)

        numCourses = self.reportCourses(department)
        self.txtNumberOfCourses.setText(str(numCourses[0]))

    # Total Classes for a Course:
    # This report helps understand the frequency of a particular course being taught,
    # indicating resource allocation effectiveness. High student demand may call for additional
    # resources, while low enrollment could suggest a need to redistribute resources.

    def btnReportClasses_clicked(self):
        # Check if combobox is selected
        if self.cmbSelectCourse.currentIndex() == -1:
            QMessageBox.warning(None, "Select Row", "Please select a course first")
            return

        # Retrieve selected course from combobox by taking the numbers before .
        course = int(self.cmbSelectCourse.currentText().split(".")[0])
        print(course)

        numClasses = self.reportClasses(course)
        self.txtNumberOfClasses.setText(str(numClasses[0]))


    #########################################################################
    #                                                                       #
    #                            Database                                   #
    #                                                                       #
    #########################################################################

    def setupDatabase(self):
        self.connect()

    def connect(self):
        self.cnx = mysql.connector.connect(user="root",
                                            password="12345678",
                                            host="127.0.0.1",
                                            database="tracle")

    def retrieveSemesters(self):
        cursor = self.cnx.cursor()

        query = "Select * From semester Order by Semester_ID Asc"

        cursor.execute(query)

        semesterList = []

        for(Semester_ID, Semester, Year) in cursor:
            semesterList.append([Semester_ID, Semester, Year])

        cursor.close()

        return semesterList


    def retrieveDepartments(self):
        cursor = self.cnx.cursor()

        query = "Select Department From courses Group by Department Order by Department Asc "

        cursor.execute(query)

        departmentList = []

        for(Department) in cursor:
            departmentList.append(Department)

        cursor.close()

        return departmentList


    def retrieveCourses(self):
        cursor = self.cnx.cursor()

        query = "Select * From courses Order by ID Asc "

        cursor.execute(query)

        classList = []

        for(Course_ID, Title, Credits, Department) in cursor:
            classList.append([Course_ID, Title])

        cursor.close()

        return classList


    def reportStudents(self, semester):
        cursor = self.cnx.cursor()

        query = "SELECT count(students.ID) " \
                "FROM students " \
                "INNER JOIN attendance ON students.ID = attendance.Student_ID " \
                "INNER JOIN class ON attendance.Class_ID = class.Class_ID " \
                "WHERE class.Semester_ID = %s"

        cursor.execute(query, (semester,))

        numStudents = 0

        for (count) in cursor:
            numStudents = count

        cursor.close()

        return numStudents


    def reportCourses(self, department):
        cursor = self.cnx.cursor()

        query = "Select count(*) " \
                "From courses " \
                "Where Department = %s"

        cursor.execute(query, (department,))

        numCourses = 0

        for (count) in cursor:
            numCourses = count

        cursor.close()

        return numCourses


    def reportClasses(self, course):
        cursor = self.cnx.cursor()

        query = "Select count(*) " \
                "From class " \
                "Where Course_ID = %s"

        cursor.execute(query, (course,))

        numClasses = 0

        for (count) in cursor:
            numClasses = count

        cursor.close()

        return numClasses


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReportsDialog = QtWidgets.QDialog()
    ui = Ui_ReportsDialog()
    ui.setupUi(ReportsDialog)
    ReportsDialog.show()
    sys.exit(app.exec_())
