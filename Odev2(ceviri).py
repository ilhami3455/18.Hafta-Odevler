# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'odev2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 817)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(196, 255, 255);")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(550, 460, 479, 231))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 451, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(170, 180, 141, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 180, 141, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 495, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(170, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_4.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_6.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_8.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(170, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_9.addWidget(self.lineEdit_6)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuSetting.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "CREATE A NEW ACCOUNT"))
        self.groupBox.setTitle(_translate("MainWindow", "TERMS and CONDITIONS"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:7.8pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400;\">I hereby declare that the information furnished righthand side is true, complete and correct to the best of my knowledge and belief. I understand that in the event of my information being found false or incorrect at any stage, my candidature / appointment shall be liable to cancellation / termination without notice or any compensation in lieu thereof.  </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\"> </span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "CREATE ACCOUNT"))
        self.pushButton_2.setText(_translate("MainWindow", "CANCEL"))
        self.label.setText(_translate("MainWindow", "NAME                             :"))
        self.label_2.setText(_translate("MainWindow", "SURNAME                      :"))
        self.label_3.setText(_translate("MainWindow", "GENDER                         :"))
        self.radioButton_2.setText(_translate("MainWindow", "MALE"))
        self.radioButton.setText(_translate("MainWindow", "FEMALE"))
        self.label_4.setText(_translate("MainWindow", "DATE OF BIRTH              :"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Day"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Day"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Month"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Year"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2019"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2018"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "2017"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "2016"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "2015"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "2014"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "2013"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "2012"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "2011"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "2010"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "2009"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "2008"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "2007"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "2006"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "2005"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "2004"))
        self.comboBox_3.setItemText(17, _translate("MainWindow", "2003"))
        self.comboBox_3.setItemText(18, _translate("MainWindow", "2002"))
        self.comboBox_3.setItemText(19, _translate("MainWindow", "2001"))
        self.comboBox_3.setItemText(20, _translate("MainWindow", "2000"))
        self.comboBox_3.setItemText(21, _translate("MainWindow", "1999"))
        self.comboBox_3.setItemText(22, _translate("MainWindow", "1998"))
        self.comboBox_3.setItemText(23, _translate("MainWindow", "1997"))
        self.comboBox_3.setItemText(24, _translate("MainWindow", "1996"))
        self.comboBox_3.setItemText(25, _translate("MainWindow", "1995"))
        self.comboBox_3.setItemText(26, _translate("MainWindow", "1994"))
        self.comboBox_3.setItemText(27, _translate("MainWindow", "1993"))
        self.comboBox_3.setItemText(28, _translate("MainWindow", "1992"))
        self.comboBox_3.setItemText(29, _translate("MainWindow", "1991"))
        self.comboBox_3.setItemText(30, _translate("MainWindow", "1990"))
        self.comboBox_3.setItemText(31, _translate("MainWindow", "1989"))
        self.comboBox_3.setItemText(32, _translate("MainWindow", "1988"))
        self.comboBox_3.setItemText(33, _translate("MainWindow", "1987"))
        self.comboBox_3.setItemText(34, _translate("MainWindow", "1986"))
        self.comboBox_3.setItemText(35, _translate("MainWindow", "1985"))
        self.comboBox_3.setItemText(36, _translate("MainWindow", "1984"))
        self.comboBox_3.setItemText(37, _translate("MainWindow", "1983"))
        self.comboBox_3.setItemText(38, _translate("MainWindow", "1982"))
        self.comboBox_3.setItemText(39, _translate("MainWindow", "1981"))
        self.comboBox_3.setItemText(40, _translate("MainWindow", "1980"))
        self.comboBox_3.setItemText(41, _translate("MainWindow", "1979"))
        self.comboBox_3.setItemText(42, _translate("MainWindow", "1978"))
        self.comboBox_3.setItemText(43, _translate("MainWindow", "1977"))
        self.comboBox_3.setItemText(44, _translate("MainWindow", "1976"))
        self.comboBox_3.setItemText(45, _translate("MainWindow", "1975"))
        self.comboBox_3.setItemText(46, _translate("MainWindow", "1974"))
        self.comboBox_3.setItemText(47, _translate("MainWindow", "1973"))
        self.comboBox_3.setItemText(48, _translate("MainWindow", "1972"))
        self.comboBox_3.setItemText(49, _translate("MainWindow", "1971"))
        self.comboBox_3.setItemText(50, _translate("MainWindow", "1970"))
        self.comboBox_3.setItemText(51, _translate("MainWindow", "1969"))
        self.comboBox_3.setItemText(52, _translate("MainWindow", "1968"))
        self.comboBox_3.setItemText(53, _translate("MainWindow", "1967"))
        self.comboBox_3.setItemText(54, _translate("MainWindow", "1966"))
        self.comboBox_3.setItemText(55, _translate("MainWindow", "1695"))
        self.comboBox_3.setItemText(56, _translate("MainWindow", "1964"))
        self.comboBox_3.setItemText(57, _translate("MainWindow", "1963"))
        self.comboBox_3.setItemText(58, _translate("MainWindow", "1962"))
        self.comboBox_3.setItemText(59, _translate("MainWindow", "1961"))
        self.comboBox_3.setItemText(60, _translate("MainWindow", "1960"))
        self.comboBox_3.setItemText(61, _translate("MainWindow", "1959"))
        self.comboBox_3.setItemText(62, _translate("MainWindow", "1958"))
        self.comboBox_3.setItemText(63, _translate("MainWindow", "1957"))
        self.comboBox_3.setItemText(64, _translate("MainWindow", "1956"))
        self.comboBox_3.setItemText(65, _translate("MainWindow", "1955"))
        self.comboBox_3.setItemText(66, _translate("MainWindow", "1954"))
        self.comboBox_3.setItemText(67, _translate("MainWindow", "1953"))
        self.comboBox_3.setItemText(68, _translate("MainWindow", "1952"))
        self.comboBox_3.setItemText(69, _translate("MainWindow", "1951"))
        self.comboBox_3.setItemText(70, _translate("MainWindow", "1950"))
        self.label_5.setText(_translate("MainWindow", "MARITAL STATUS          :"))
        self.checkBox.setText(_translate("MainWindow", "MARRIED"))
        self.checkBox_2.setText(_translate("MainWindow", "SINGLE"))
        self.checkBox_3.setText(_translate("MainWindow", "DIVORCED"))
        self.label_6.setText(_translate("MainWindow", "E-MAIL                           :"))
        self.label_7.setText(_translate("MainWindow", "CONFIRM E-MAIL           :"))
        self.label_8.setText(_translate("MainWindow", "PASSWOORD                 :"))
        self.label_9.setText(_translate("MainWindow", "CONFIRM PASSWOORD :"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences..."))
        self.actionAbout.setText(_translate("MainWindow", "About...    F1"))