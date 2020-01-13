# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modal_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog


class ModalWindow(QDialog):
    def __init__(self,):
        super(ModalWindow, self).__init__()
        self.setObjectName("Dialog")
        # self.resize(400, 325)
        self.resize(900,600)
        # self.setWindowOpacity()
        self.closeModal = QtWidgets.QPushButton(self)
        self.closeModal.setGeometry(QtCore.QRect(140, 290, 112, 32))
        self.closeModal.setObjectName("closeModal")
        self.imgLabel = QtWidgets.QLabel(self)
        self.imgLabel.setGeometry(QtCore.QRect(10, 0, 371, 261))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        pixmap = QPixmap('giphy.gif')
        self.imgLabel.setPixmap(pixmap)
        self.imgLabel.adjustSize()
        self.closeModal.adjustSize()

        self.retranslateUi(self)
        self.closeModal.clicked.connect(lambda: self.close_current_window())
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.closeModal.setText(_translate("Dialog", "Close"))

    def close_current_window(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ModalWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
