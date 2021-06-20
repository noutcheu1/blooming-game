# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 754)
        MainWindow.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_bar.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_btn_toggle = QtWidgets.QFrame(self.top_bar)
        self.frame_btn_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_btn_toggle.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.frame_btn_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btn_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn_toggle.setObjectName("frame_btn_toggle")
        self.btn_toggle = QtWidgets.QPushButton(self.frame_btn_toggle)
        self.btn_toggle.setGeometry(QtCore.QRect(0, -1, 70, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet("border:0px solid\n"
"")
        self.btn_toggle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/align-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QtCore.QSize(76, 50))
        self.btn_toggle.setAutoRepeat(False)
        self.btn_toggle.setObjectName("btn_toggle")
        self.horizontalLayout.addWidget(self.frame_btn_toggle)
        self.frame_top = QtWidgets.QFrame(self.top_bar)
        self.frame_top.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.EXIT = QtWidgets.QPushButton(self.frame_top)
        self.EXIT.setGeometry(QtCore.QRect(1030, 0, 40, 40))
        self.EXIT.setMaximumSize(QtCore.QSize(40, 40))
        self.EXIT.setStyleSheet("border:0px solid")
        self.EXIT.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EXIT.setIcon(icon1)
        self.EXIT.setIconSize(QtCore.QSize(40, 20))
        self.EXIT.setAutoExclusive(False)
        self.EXIT.setObjectName("EXIT")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.pushButton_11.setStyleSheet("border-radius:200px;\n"
"background-color: rgb(114, 159, 207);")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.layoutWidget = QtWidgets.QWidget(self.frame_top)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.layoutWidget.raise_()
        self.EXIT.raise_()
        self.pushButton_11.raise_()
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("background-color: rgba(173, 127, 168,60);")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.content)
        self.frame_left_menu.setMaximumSize(QtCore.QSize(1, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 100), stop:1 rgba(255, 178, 102, 100));")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 100), stop:1 rgba(255, 178, 102, 100));")
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.frame_top_menus)
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 100), stop:1 rgba(255, 178, 102, 100));")
        self.widget.setObjectName("widget")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 611, 721))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"font: 57 italic 17pt \"Ubuntu\";\n"
"color: rgb(238, 238, 236);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setIndent(-1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 2, 4)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:1 rgba(255, 178, 102, 255));")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(32, 74, 135))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 3, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 2)
        self.TOTAL_EXPENSE = QtWidgets.QLabel(self.layoutWidget1)
        self.TOTAL_EXPENSE.setText("")
        self.TOTAL_EXPENSE.setObjectName("TOTAL_EXPENSE")
        self.gridLayout.addWidget(self.TOTAL_EXPENSE, 2, 4, 1, 1)
        self.passiv_income = QtWidgets.QProgressBar(self.layoutWidget1)
        self.passiv_income.setProperty("value", 24)
        self.passiv_income.setObjectName("passiv_income")
        self.gridLayout.addWidget(self.passiv_income, 3, 2, 1, 3)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setStyleSheet("font: 57 italic 16pt \"Ubuntu\";\n"
"background-color: rgb(117, 80, 123);\n"
"color: rgb(238, 238, 236);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 2, 2, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidget_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:1 rgba(255, 178, 102, 255));")
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.tableWidget_2, 5, 0, 4, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 2, 1, 1)
        self.TOTAL_EXOENSE = QtWidgets.QLabel(self.layoutWidget1)
        self.TOTAL_EXOENSE.setObjectName("TOTAL_EXOENSE")
        self.gridLayout.addWidget(self.TOTAL_EXOENSE, 7, 3, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 2, 1, 1)
        self.PAYDAY = QtWidgets.QLabel(self.layoutWidget1)
        self.PAYDAY.setObjectName("PAYDAY")
        self.gridLayout.addWidget(self.PAYDAY, 8, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setStyleSheet("background-color: rgb(92, 53, 102);\n"
"color: rgb(238, 238, 236);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 5)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidget_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:1 rgba(255, 178, 102, 255));")
        self.tableWidget_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        item.setFont(font)
        self.tableWidget_3.setItem(3, 1, item)
        self.gridLayout.addWidget(self.tableWidget_3, 10, 0, 1, 2)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidget_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:1 rgba(255, 178, 102, 255));")
        self.tableWidget_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setItem(4, 0, item)
        self.gridLayout.addWidget(self.tableWidget_4, 10, 2, 1, 3)
        self.TOTAL_INCOME = QtWidgets.QLabel(self.layoutWidget1)
        self.TOTAL_INCOME.setObjectName("TOTAL_INCOME")
        self.gridLayout.addWidget(self.TOTAL_INCOME, 6, 3, 1, 2)
        self.CASH = QtWidgets.QLabel(self.layoutWidget1)
        self.CASH.setObjectName("CASH")
        self.gridLayout.addWidget(self.CASH, 5, 3, 1, 2)
        self.verticalLayout_3.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.frame_top_menus)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.content)
        self.frame_pages.setStyleSheet("QFrame#frame_pages{\n"
"border-image: url(:/icons/images.jpeg);\n"
"}")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.boardgame = QtWidgets.QLabel(self.frame_pages)
        self.boardgame.setGeometry(QtCore.QRect(80, 50, 961, 591))
        self.boardgame.setStyleSheet("border-image: url(:/icons/board/hqdefault.jpg);\n"
"\n"
"border-radius:20px;")
        self.boardgame.setText("")
        self.boardgame.setObjectName("boardgame")
        self.label_15 = QtWidgets.QLabel(self.frame_pages)
        self.label_15.setGeometry(QtCore.QRect(800, 30, 321, 471))
        self.label_15.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.487562, y1:0.045, x2:0.493, y2:0.045, stop:0 rgba(117, 80, 123, 196), stop:1 rgba(117, 80, 123, 174));")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setGeometry(QtCore.QRect(800, 30, 321, 481))
        self.stackedWidget.setStyleSheet("\n"
"border-radius:20px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.page_8)
        self.stackedWidget_3.setGeometry(QtCore.QRect(0, -10, 321, 461))
        self.stackedWidget_3.setStyleSheet("background-color: rgba(222, 184, 135, 232);")
        self.stackedWidget_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.stackedWidget_3.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.frame_3 = QtWidgets.QFrame(self.page_10)
        self.frame_3.setGeometry(QtCore.QRect(10, 90, 301, 371))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.title = QtWidgets.QLabel(self.frame_3)
        self.title.setGeometry(QtCore.QRect(20, 60, 261, 20))
        self.title.setStyleSheet("font: 57 bold 13pt \"Ubuntu\";\n"
"color: rgb(117, 80, 123);")
        self.title.setObjectName("title")
        self.dream_Description_2 = QtWidgets.QLabel(self.frame_3)
        self.dream_Description_2.setGeometry(QtCore.QRect(10, 50, 281, 121))
        self.dream_Description_2.setStyleSheet("background-color: rgba(222, 184, 135, 0);")
        self.dream_Description_2.setObjectName("dream_Description_2")
        self.dream_Description_2.raise_()
        self.title.raise_()
        self.btn_prev_1 = QtWidgets.QPushButton(self.page_10)
        self.btn_prev_1.setGeometry(QtCore.QRect(40, 40, 20, 20))
        self.btn_prev_1.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_prev_1.setStyleSheet("border:0px solid\n"
"")
        self.btn_prev_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/chevrons-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_prev_1.setIcon(icon2)
        self.btn_prev_1.setIconSize(QtCore.QSize(20, 20))
        self.btn_prev_1.setObjectName("btn_prev_1")
        self.btn_next_2 = QtWidgets.QPushButton(self.page_10)
        self.btn_next_2.setGeometry(QtCore.QRect(240, 40, 20, 20))
        self.btn_next_2.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_next_2.setStyleSheet("border:0px solid\n"
"")
        self.btn_next_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/chevrons-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next_2.setIcon(icon3)
        self.btn_next_2.setIconSize(QtCore.QSize(20, 20))
        self.btn_next_2.setAutoRepeat(False)
        self.btn_next_2.setObjectName("btn_next_2")
        self.image_Dream_2 = QtWidgets.QLabel(self.page_10)
        self.image_Dream_2.setGeometry(QtCore.QRect(80, 20, 131, 61))
        self.image_Dream_2.setStyleSheet("border-image: url(:/board/rolling-dices.svg);")
        self.image_Dream_2.setText("")
        self.image_Dream_2.setObjectName("image_Dream_2")
        self.Profession_info_2 = QtWidgets.QLabel(self.page_10)
        self.Profession_info_2.setGeometry(QtCore.QRect(20, 290, 291, 151))
        self.Profession_info_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.Profession_info_2.setText("")
        self.Profession_info_2.setObjectName("Profession_info_2")
        self.stackedWidget_3.addWidget(self.page_10)
        self.choose = QtWidgets.QPushButton(self.page_8)
        self.choose.setGeometry(QtCore.QRect(40, 460, 89, 25))
        self.choose.setStyleSheet("background-color: rgb(222, 184, 135);\n"
"color: rgb(117, 80, 123);")
        self.choose.setObjectName("choose")
        self.stackedWidget.addWidget(self.page_8)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.Roll = QtWidgets.QPushButton(self.page_11)
        self.Roll.setGeometry(QtCore.QRect(10, 440, 101, 25))
        self.Roll.setStyleSheet("background-color: rgb(222, 184, 135);\n"
"color: rgb(117, 80, 123);")
        self.Roll.setObjectName("Roll")
        self.frame_5 = QtWidgets.QFrame(self.page_11)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 321, 431))
        self.frame_5.setStyleSheet("background-color: rgba(222, 184, 135, 229);\n"
"border-radius:200px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_9.setGeometry(QtCore.QRect(190, 340, 101, 25))
        self.pushButton_9.setStyleSheet("background-color: rgb(252, 233, 79);\n"
"border-radius:2000px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 340, 101, 25))
        self.pushButton_8.setStyleSheet("background-color: rgb(252, 233, 79);\n"
"\n"
"border-radius:15px;\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setGeometry(QtCore.QRect(10, 90, 301, 221))
        self.frame_8.setStyleSheet("background-color: rgb(222, 184, 135);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.information = QtWidgets.QLabel(self.frame_8)
        self.information.setGeometry(QtCore.QRect(0, -10, 291, 81))
        self.information.setStyleSheet("background-color: rgb(222, 184, 135);")
        self.information.setScaledContents(True)
        self.information.setWordWrap(True)
        self.information.setObjectName("information")
        self.dice_rolling = QtWidgets.QLabel(self.frame_8)
        self.dice_rolling.setGeometry(QtCore.QRect(10, 80, 261, 131))
        self.dice_rolling.setStyleSheet("border-image: url(:/board/board/tenor.gif);\n"
"border-image: url(:/board/board/animated-dice-image-0094.gif);\n"
"border-radius:20px;")
        self.dice_rolling.setText("")
        self.dice_rolling.setWordWrap(False)
        self.dice_rolling.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.dice_rolling.setObjectName("dice_rolling")
        self.label_13 = QtWidgets.QLabel(self.frame_8)
        self.label_13.setGeometry(QtCore.QRect(-10, -100, 319, 441))
        self.label_13.setStyleSheet("background-color: rgba(222, 184, 135, 229);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_13.raise_()
        self.information.raise_()
        self.dice_rolling.raise_()
        self.dice_image = QtWidgets.QLabel(self.frame_5)
        self.dice_image.setGeometry(QtCore.QRect(80, 20, 121, 61))
        self.dice_image.setStyleSheet("border-image: url(:/board/rolling-dices.svg);\n"
"border-radius:20px;")
        self.dice_image.setText("")
        self.dice_image.setObjectName("dice_image")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_12)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 330, 89, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.stackedWidget.addWidget(self.page_12)
        self.player = QtWidgets.QPushButton(self.frame_pages)
        self.player.setGeometry(QtCore.QRect(320, 490, 16, 16))
        self.player.setStyleSheet("border-radius:200px;\n"
"background-color: rgb(114, 159, 207);")
        self.player.setText("")
        self.player.setObjectName("player")
        self.label_4 = QtWidgets.QLabel(self.frame_pages)
        self.label_4.setGeometry(QtCore.QRect(866, 646, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(self.frame_pages)
        self.label_11.setGeometry(QtCore.QRect(880, 660, 251, 41))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.frame_pages.raise_()
        self.frame_left_menu.raise_()
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.stackedWidget)
        self.frame.setGeometry(QtCore.QRect(1090,100,321,491))
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(1)
        #self.Roll.clicked.connect(self.label_13.clear)
        self.choose.clicked.connect(self.start_game)
        self.Roll.clicked.connect(self.start_game)
        self.position = 0
        self.btn_next_2.clicked.connect(self.dream_Description_2.clear)
        self.btn_prev_1.clicked.connect(self.dream_Description_2.clear)
        self.btn_toggle.clicked.connect(self.btn_toggle.animateClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def start_game(self):

        list_race = [(400,440,16,16),(380,400,16,16),(370,360,16,16),(360,310,16,16),
                 (370,270,16,16),(400,230,16,16),(430,190,16,16),(480,180,16,16),(520,160,16,16),
                 (570,170,16,16),(620,180,16,16),(660,200,16,16),(700,230,16,16),(720,270,16,16),(740,310,16,16),(740,360,16,16),(720,400,16,16),
                 (700,440,16,16),(660,470,16,16),(620,490,16,16),(570,500,16,16),(530,510,16,16),(480,490,16,16),(440,470,16,16)]
        list_race1 = [(120, 580, 16, 16), (110, 520, 16, 16), (110, 460, 16, 16), (110, 400, 16, 16),
                     (110, 330, 16, 16), (110, 280, 16, 16), (110, 220, 16, 16), (110, 160, 16, 16),
                      (130, 100, 16, 16),
                     (190, 90, 16, 16), (260, 90, 16, 16), (330, 90, 16, 16), (400, 90, 16, 16), (470, 90, 16, 16),
                     (540, 90, 16, 16), (610, 90, 16, 16), (680, 90, 16, 16),
                     (750, 90, 16, 16), (830, 90, 16, 16), (910, 90, 16, 16), (980, 90, 16, 16),
                      (980, 150, 16, 16),
                     (980, 220, 16, 16), (980, 280, 16, 16), (980, 340, 16, 16), (980, 400, 16, 16)
                      , (980, 460, 16, 16), (980, 520, 16, 16), (980, 580, 16, 16), (910, 580, 16, 16)
                , (830,580, 16, 16), (750, 580, 16, 16), (680, 580, 16, 16), (610, 580, 16, 16),
                      (540,580, 16, 16),(470,580, 16, 16),(400,580, 16, 16),(330,580, 16, 16),
                      (260,580, 16, 16),(190,580, 16, 16),(190,580, 16, 16)
                      ]

        self.player.setGeometry(QtCore.QRect(list_race1[self.position][0], list_race1[self.position][1],list_race1[self.position][2], list_race1[self.position][3]))
        if self.position < len(list_race1) -1 :
                print(self.position,len(list_race1) -1)
                self.position +=1
        else:
                self.position = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_toggle.setShortcut(_translate("MainWindow", "A"))
        self.EXIT.setShortcut(_translate("MainWindow", "Esc"))
        self.label_2.setText(_translate("MainWindow", "INCOME"))
        self.label_5.setText(_translate("MainWindow", "INCREASE PASSIVE INCOME TO ESCAPE    THE RAT RAT RACE"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "interest dividends"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "investissement reel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "cash flow"))
        self.label_6.setText(_translate("MainWindow", "TOTAL EXPENSES:"))
        self.label.setText(_translate("MainWindow", "EXPENSES"))
        self.label_7.setText(_translate("MainWindow", "CASH :"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "interest dividends"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "investissement reel"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "cash flow"))
        self.label_8.setText(_translate("MainWindow", "TOTAL INCOME :"))
        self.label_9.setText(_translate("MainWindow", "TOTAL EXPENSES :"))
        self.TOTAL_EXOENSE.setText(_translate("MainWindow", "$"))
        self.label_10.setText(_translate("MainWindow", "PAYDAY :"))
        self.PAYDAY.setText(_translate("MainWindow", "$"))
        self.label_3.setText(_translate("MainWindow", "ASSETS                                                                    LIABILITIES"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STOCKS /Funds /CDs"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "$/Share"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(3, 0)
        item.setText(_translate("MainWindow", "Real Estate/Business"))
        item = self.tableWidget_3.item(3, 1)
        item.setText(_translate("MainWindow", "Cost"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "MAISON ENGAGE :"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Car Loans :"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Credit Cards :"))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "investissement reel"))
        item = self.tableWidget_4.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Real Estate/Businness"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        item = self.tableWidget_4.item(4, 0)
        item.setText(_translate("MainWindow", "Liability"))
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        self.TOTAL_INCOME.setText(_translate("MainWindow", "$"))
        self.CASH.setText(_translate("MainWindow", "$"))
        self.title.setText(_translate("MainWindow", "Player  choose your DREAM"))
        self.dream_Description_2.setText(_translate("MainWindow", "tu na pas de reve"))
        self.choose.setText(_translate("MainWindow", "CHOOSE"))
        self.Roll.setText(_translate("MainWindow", "Roll"))
        self.pushButton_9.setText(_translate("MainWindow", "Borrow"))
        self.pushButton_8.setText(_translate("MainWindow", "Repay"))
        self.information.setText(_translate("MainWindow", "avant de lancer  verifier votre fiche de finance et regarde si tu peux utiliser ce temp pour rembourser ou preter a la bank "))
        self.pushButton_10.setText(_translate("MainWindow", "Roll"))
        self.label_4.setText(_translate("MainWindow", "CHAT LOG"))
        self.label_11.setText(_translate("MainWindow", "PLAYER STAR  GAME"))

import icons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

