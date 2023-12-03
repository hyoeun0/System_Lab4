from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(5, 150, 80, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(95, 150, 80, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(185, 150, 80, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(185, 200, 80, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(5, 200, 80, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(95, 200, 80, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(185, 250, 80, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(95, 300, 80, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(5, 300, 80, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(5, 250, 80, 40))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(185, 300, 80, 40))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(95, 250, 80, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(275, 150, 80, 40))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(275, 250, 80, 40))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(275, 200, 80, 40))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(275, 300, 80, 40))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(5, 100, 200, 40))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(210, 100, 145, 40))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 5, 350, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{ \n"
"            border : 2px solid black;\n"
"            background : white;\n"
"            }")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "hyoeun 계산기"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_5.setText(_translate("MainWindow", "6"))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_4.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "."))
        self.pushButton_9.setText(_translate("MainWindow", "0"))
        self.pushButton_10.setText(_translate("MainWindow", "7"))
        self.pushButton_11.setText(_translate("MainWindow", "/"))
        self.pushButton_12.setText(_translate("MainWindow", "8"))
        self.pushButton_13.setText(_translate("MainWindow", "*"))
        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_15.setText(_translate("MainWindow", "-"))
        self.pushButton_16.setText(_translate("MainWindow", "="))
        self.pushButton_17.setText(_translate("MainWindow", "Clear"))
        self.pushButton_18.setText(_translate("MainWindow", "Del"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

        # adding action to each of the button
        self.pushButton_15.clicked.connect(self.action_minus)
        self.pushButton_16.clicked.connect(self.action_equal)
        self.pushButton_9.clicked.connect(self.action0)
        self.pushButton.clicked.connect(self.action1)
        self.pushButton_2.clicked.connect(self.action2)
        self.pushButton_3.clicked.connect(self.action3)
        self.pushButton_6.clicked.connect(self.action4)
        self.pushButton_7.clicked.connect(self.action5)
        self.pushButton_5.clicked.connect(self.action6)
        self.pushButton_10.clicked.connect(self.action7)
        self.pushButton_12.clicked.connect(self.action8)
        self.pushButton_4.clicked.connect(self.action9)
        self.pushButton_11.clicked.connect(self.action_div)
        self.pushButton_13.clicked.connect(self.action_mul)
        self.pushButton_14.clicked.connect(self.action_plus)
        self.pushButton_8.clicked.connect(self.action_point)
        self.pushButton_17.clicked.connect(self.action_clear)
        self.pushButton_18.clicked.connect(self.action_del)

    def action_equal(self):

        # get the label text
        equation = self.label.text()

        try:
            # getting the ans
            ans = eval(equation)

            # setting text to the label
            self.label.setText(str(ans))

        except:
            # setting text to the label
            self.label.setText("Wrong Input")

    def action_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")

    def action0(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")

    def action1(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        # clearing the label text
        self.label.setText("")

    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
