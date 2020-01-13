# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from modal_window import ModalWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setStyleSheet("background-color:rgba(65, 0, 136,0.2)")

        self.minuteDropDown = QtWidgets.QComboBox(MainWindow)
        self.minuteDropDown.setGeometry(QtCore.QRect(220, 90, 171, 32))
        self.minuteDropDown.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.minuteDropDown.setObjectName("minuteDropDown")


        self.hourLabel = QtWidgets.QLabel(MainWindow)
        self.hourLabel.setGeometry(QtCore.QRect(10, 70, 151, 16))
        self.hourLabel.setObjectName("hourLabel")
        self.hourLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.startStopBtn = QtWidgets.QPushButton(MainWindow)
        self.startStopBtn.setGeometry(QtCore.QRect(140, 160, 112, 32))
        self.startStopBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.startStopBtn.setObjectName("startStopBtn")

        self.hourDropDown = QtWidgets.QComboBox(MainWindow)
        self.hourDropDown.setGeometry(QtCore.QRect(10, 90, 171, 32))
        self.hourDropDown.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.hourDropDown.setObjectName("hourDropDown")
        self.add_data_in_drop_down_menu()

        self.minuteLabel = QtWidgets.QLabel(MainWindow)
        self.minuteLabel.setGeometry(QtCore.QRect(220, 70, 151, 16))
        self.minuteLabel.setObjectName("minuteLabel")
        self.minuteLabel.setStyleSheet("color: rgb(255, 255, 255);")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startStopBtn.clicked.connect(lambda: self.start_stop_click_event(self.startStopBtn))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.hourLabel.setText(_translate("MainWindow", "Select Hours"))
        self.startStopBtn.setText(_translate("MainWindow", "Start"))
        self.minuteLabel.setText(_translate("MainWindow", "Select  Minutes"))

    def start_stop_click_event(self, startStopBtn):
        text = startStopBtn.text()
        current_hour = self.hourDropDown.currentText()
        current_minute = self.minuteDropDown.currentText()
        if text == 'Start':
            startStopBtn.setText("Stop")
            print("Its start")
            self.show_popup()
        else:
            startStopBtn.setText("Start")
            print("Stop")

    def add_data_in_drop_down_menu(self):
        # for hour dropDown
        for i in range(24):
            self.hourDropDown.addItem(str(i))

        # for minute dropDown
        for i in range(1, 60):
            self.minuteDropDown.addItem(str(i))

    def show_popup(self):

        tt = ModalWindow()
        tt.exec_()
        # msg = QMessageBox()
        # msg.setWindowTitle("Stretch Time")
        # msg.setText("This is the Main text")
        # msg.setIcon(QMessageBox.Warning)
        #
        # x = msg.exec_()
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
