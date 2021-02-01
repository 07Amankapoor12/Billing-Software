
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pandas as pd
import csv



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowState(QtCore.Qt.WindowMaximized)

        #MainWindow.setStyleSheet("background-color:white")
        MainWindow.setWindowIcon(QIcon("Images/My Icon.jpg"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #3a3a3a;color: #fff;selection-background-color: #b78620;selection-color: #000;")

        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 5, 645, 495))
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)

        setstylesheets = "QHeaderView::section{background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));	border: 1px solid #000;    color: #fff;   text-align: left;	padding: 4px;}"
        self.tableWidget.setStyleSheet(setstylesheets)


        self.Verticalline = QtWidgets.QFrame(self.centralwidget)
        self.Verticalline.setGeometry(QtCore.QRect(640, 5, 20, 700))
        self.Verticalline.setFrameShape(QtWidgets.QFrame.VLine)
        self.Verticalline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Hline_2 = QtWidgets.QFrame(self.centralwidget)
        self.Hline_2.setGeometry(QtCore.QRect(0, 0, 2024, 2))
        self.Hline_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Hline_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Hline_2.setObjectName("line_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(650, 542, 751, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(650, 44, 751, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        #self.tableWidget.setRowCount(100)
        self.tableWidget.setStyleSheet("font-size: 100%")
        self.tableWidget.setFont(QtGui.QFont("Arial",25))
        self.tableWidget.verticalHeader().setVisible(False)



        item = QtWidgets.QTableWidgetItem()
    #    self.tableWidget.setVerticalHeaderItem(0, item)

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setItem(0, 0, item)




        self.TotalLabel = QtWidgets.QLabel(self.centralwidget)
        self.TotalLabel.setGeometry(QtCore.QRect(0,495,648,175))
        self.TotalLabel.setStyleSheet("background-color: transparent;color: #fff;")

        self.header = self.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)



        self.TotalLabel.setObjectName("TotalLabel")

        self.TLabel= QLabel("Total",self.TotalLabel)
        self.TLabel.setGeometry(QtCore.QRect(10,10,70,20))
        self.TLabel.setStyleSheet("font-weight: bold; font-size: 500%")
        self.TLabel.setFont(QtGui.QFont("Georgia",10))
        self.TALabel = QLabel(self.TotalLabel)
        self.TALabel.setStyleSheet("border: 1px solid black;")
        self.TALabel.setGeometry(QRect(85,10,80,20))
        self.Totalbttn = QPushButton("Total",self.TotalLabel)
        self.Totalbttn.clicked.connect(self.Total_bttn)
        self.Totalbttn.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        #self.Totalbttn.setStyleSheet("background-color:red;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;color:white;font: bold 14px;")
        self.Totalbttn.setFont(QtGui.QFont("Georgia",10))
        self.Totalbttn.setGeometry(QRect(450,10,50,50))
        self.QLabel = QLabel("Qty.",self.TotalLabel)
        self.QLabel.setStyleSheet("font-weight: bold; font-size: 500%")
        self.QLabel.setFont(QtGui.QFont("Georgia",10))
        self.QLabel.setGeometry(QRect(10,45,70,20))
        self.QALabel = QLabel(self.TotalLabel)
        self.QALabel.setStyleSheet("border: 1px solid black;")
        self.QALabel.setGeometry(QRect(85,45,65,20))
        self.GTLabel = QLabel("Grand Total",self.TotalLabel)
        self.GTLabel.setStyleSheet("font-weight: bold; font-size: 500%")
        self.GTLabel.setFont(QtGui.QFont("Georgia",14))
        self.GTLabel.setGeometry(QRect(215,100,120,30))
        self.GTALabel = QLabel(self.TotalLabel)
        self.GTALabel.setStyleSheet("border: 1px solid black;")
        self.GTALabel.setGeometry(QRect(350,100,120,30))
        self.GSTLabel= QLabel("GST",self.TotalLabel)

        self.GSTLabel.setGeometry(QtCore.QRect(215,10,50,20))
        self.GSTLabel.setStyleSheet("font-weight: bold; font-size: 500%")
        self.GSTLabel.setFont(QtGui.QFont("Georgia",10))
        self.GSTALabel = QLabel(self.TotalLabel)
        self.GSTALabel.setText(str(12))
        self.GSTALabel.setStyleSheet("border: 1px solid black;")
        self.GSTALabel.setGeometry(QRect(285,10,80,20))



        self.SearchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchBar.setGeometry(QtCore.QRect(780, 10, 491,25))
        self.SearchBar.setObjectName("ItemName_Edit")
#        self.ScrollArea=QScrollArea(self.centralwidget)
    #    self.ScrollArea.setWidget(self.centralwidget)
#        self.ScrollArea.setWidgetResizable(True)
    #    completers_ItemName = QtWidgets.QCompleter(Item_Name_)
    #    self.ItemName_Edit.editingFinished.connect(self.ItemEntry)
    #    self.ItemName_Edit.setCompleter(completers_ItemName)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")


        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
    #### Main Screen Button Section #####
        self.firstbttn = QtWidgets.QPushButton("Men",self.gridLayoutWidget)
        self.firstbttn.setObjectName("firstbttn")
        self.firstbttn.setStyleSheet("border-image:url(Images/men.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.firstbttn.setFont(QtGui.QFont("Georgia",10))

        self.firstbttn.setMinimumHeight(140)
        self.firstbttn.setMinimumWidth(70)
        self.gridLayout_2.addWidget(self.firstbttn, 1, 0)
        self.secondbttn = QtWidgets.QPushButton("HomeAppliances",self.gridLayoutWidget)
        self.secondbttn.setObjectName("secondbttn")
        self.secondbttn.setStyleSheet("border-image:url(Images/HomeAppliances.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.secondbttn.setFont(QtGui.QFont("Georgia",10))
        self.secondbttn.setMinimumWidth(70)
        self.secondbttn.setMinimumHeight(140)
        self.gridLayout_2.addWidget(self.secondbttn, 1,  1)
        self.thirdbttn = QtWidgets.QPushButton("Women",self.gridLayoutWidget)
        self.thirdbttn.setAutoDefault(False)
        self.thirdbttn.setDefault(False)
        self.thirdbttn.setFlat(False)
        self.thirdbttn.setStyleSheet("border-image:url(Images/women1.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.thirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.thirdbttn.setMinimumHeight(140)
        self.thirdbttn.setMinimumWidth(70)
        self.thirdbttn.clicked.connect(self.Third_bttn)
        self.thirdbttn.setObjectName("thirdbttn")
        self.gridLayout_2.addWidget(self.thirdbttn, 1, 2)
        self.fourthbttn = QtWidgets.QPushButton("Kids",self.gridLayoutWidget)
        self.fourthbttn.setObjectName("fourthbttn")
        self.fourthbttn.setStyleSheet("border-image:url(Images/kids.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.fourthbttn.setFont(QtGui.QFont("Georgia",10))
        #self.fourthbttn.setStyleSheet("background-image: url(Images/kids.jpg);")

        #self.fourthbttn.setPixmap(QtGui.QPixmap("Images/kids.jpg"))
        #self.fourthbttn.setScaledContents(True)
        self.fourthbttn.setMinimumHeight(140)
        self.fourthbttn.setMinimumWidth(70)
        self.fourthbttn.clicked.connect(self.Fourth_bttn)
        self.gridLayout_2.addWidget(self.fourthbttn, 2, 0)
        self.fivthbttn = QtWidgets.QPushButton("food and Grocery",self.gridLayoutWidget)
        self.fivthbttn.setObjectName("fivthbttn")
        self.fivthbttn.setStyleSheet("border-image:url(Images/Food and Grocery.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.fivthbttn.setFont(QtGui.QFont("Georgia",10))
        self.fivthbttn.setMinimumHeight(140)
        self.fivthbttn.setMinimumWidth(70)
        self.fivthbttn.clicked.connect(self.fivth_bttn)
        self.gridLayout_2.addWidget(self.fivthbttn, 2, 1)
        self.Sixthbttn = QtWidgets.QPushButton("Home and Furniture",self.gridLayoutWidget)
        self.Sixthbttn.setObjectName("Sixthbttn")
        self.Sixthbttn.setMinimumHeight(140)
        self.Sixthbttn.setMinimumWidth(70)
        self.Sixthbttn.clicked.connect(self.Sixth_bttn)
        self.Sixthbttn.setStyleSheet("border-image:url(Images/Homeandfurniture.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_2.addWidget(self.Sixthbttn, 2, 2)
        self.Seventhbttn = QtWidgets.QPushButton("Electronics",self.gridLayoutWidget)
        self.Seventhbttn.setObjectName("Seventhbttn")
        self.Seventhbttn.setMinimumHeight(140)
        self.Seventhbttn.setMinimumWidth(70)
        self.Seventhbttn.setStyleSheet("border-image:url(Images/Electronics.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Seventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.Seventhbttn.clicked.connect(self.Seventh_bttn)
        self.gridLayout_2.addWidget(self.Seventhbttn, 3, 0)
        self.Eightbttn = QtWidgets.QPushButton("Books and Stationary",self.gridLayoutWidget)
        self.Eightbttn.setObjectName("Seventhbttn")
        self.Eightbttn.setMinimumHeight(140)
        self.Eightbttn.setMinimumWidth(70)
        self.Eightbttn.clicked.connect(self.Eight_bttn)
        self.Eightbttn.setStyleSheet("border-image:url(Images/BooksandStationary.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Eightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_2.addWidget(self.Eightbttn, 3, 1)
        self.Ninthbttn = QtWidgets.QPushButton("Sports",self.gridLayoutWidget)
        self.Ninthbttn.setObjectName("Seventhbttn")
        self.Ninthbttn.setMinimumHeight(140)
        self.Ninthbttn.setMinimumWidth(70)
        self.Ninthbttn.clicked.connect(self.Ninth_bttn)
        self.Ninthbttn.setStyleSheet("border-image:url(Images/Sports.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ninthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_2.addWidget(self.Ninthbttn, 3, 2)




        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 25))
#        self.menubar.setStyleSheet("QMenuBar::{item ackground-color: transparent;}")
#        self.menubar.setStyleSheet("QMenuBar::item:selected {	background-color: rgba(183, 134, 32, 20%);border: 1px solid #b78620;	color: #fff;}")
#        self.menubar.setStyleSheet("QMenuBar::item:pressed {	background-color: rgb(183, 134, 32);	border: 1px solid #b78620;	color: #fff;}")
    #    self.menubar.setStyleSheet("QMenubar{background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));border: 1px solid #000;color: #fff;}")
        self.menubar.setStyleSheet("""
        QMenuBar
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));
	border: 1px solid #000;
	color: #fff;

}
QMenuBar::item
{
	background-color: transparent;

}
QMenuBar::item:selected
{
	background-color: rgba(183, 134, 32, 20%);
	border: 1px solid #b78620;
	color: #fff;

}
QMenuBar::item:pressed
{
	background-color: rgb(183, 134, 32);
	border: 1px solid #b78620;
	color: #fff;

}

QMenu
{
background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));
border: 1px solid #222;
padding: 4px;
color: #fff;

}


QMenu::item
{
background-color: transparent;
padding: 2px 20px 2px 20px;

}


QMenu::separator
{
background-color: rgb(183, 134, 32);
height: 1px;

}


QMenu::item:disabled
{
color: #555;
background-color: transparent;
padding: 2px 20px 2px 20px;

}


QMenu::item:selected
{
background-color: rgba(183, 134, 32, 20%);
border: 1px solid #b78620;
color: #fff;

}
""")

        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)

        self.menuFile.setObjectName("menuFile")
        self.menubar.setFont(QtGui.QFont("Georgia",10))
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionNew_Page = QtWidgets.QAction(MainWindow)
        self.actionNew_Page.setObjectName("actionNew_Page")
        self.actionsupoort = QtWidgets.QAction(MainWindow)
        self.actionsupoort.setObjectName("actionsupoort")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_Page)
        self.menuEdit.addAction(self.actionCopy)
        self.menuHelp.addAction(self.actionsupoort)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.printAction = QAction(QIcon('E:/Pic/print.png'),'Print',MainWindow)
        self.printAction.triggered.connect(self.printDialog)
        self.printAction.setShortcut('Ctrl+P')
        self.menuFile.addAction(self.printAction)
        self.menuFile.addAction(self.printAction)

        self.exporeAction = QAction("Explore",MainWindow)
        self.exporeAction.triggered.connect(self.export_to_csv)
        self.menuFile.addAction(self.exporeAction)

        self.printperviewAction = QAction(QIcon('E:/Pic/printperview.jpg'),'Print Preview',MainWindow)
        self.printperviewAction.triggered.connect(self.printpreviewDialog)
        #self.menuFile.addAction(self.printperviewAction)
        self.menuFile.addAction(self.printperviewAction)

        self.BillndPay = QtWidgets.QPushButton("Bill Pay",self.centralwidget)
        self.BillndPay.setGeometry(QtCore.QRect(690,600,80,30))
        self.BillndPay.setObjectName("BillndPay")
        self.BillndPay.setFont(QtGui.QFont("Georgia",10))
        self.BillndPay.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        self.Cancel = QtWidgets.QPushButton("Cancel",self.centralwidget)
        self.Cancel.setGeometry(QtCore.QRect(950,600,80,30))
        self.Cancel.setObjectName("Cancel")
        self.Cancel.setFont(QtGui.QFont("Georgia",10))
        self.Cancel.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        self.retranslateUi(MainWindow)
        self.backf = QtWidgets.QPushButton("back",self.centralwidget)
        self.backf.setGeometry(QtCore.QRect(650, 29, 75, 23))
        self.backf.setObjectName("back")
        self.backf.clicked.connect(self.backf_bttn)
        self.backf.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        self.Columncount = self.tableWidget.columnCount()

        self.secondbttn.clicked.connect(self.Second_bttn)
        self.firstbttn.clicked.connect(self.first_bttn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.rowCount = self.tableWidget.rowCount()

    def Total_bttn(self, column):

        datastring = []
        dataint=[]
        Qtys = []
        Qtyin=[]

        for i in range(self.tableWidget.rowCount()):
            datastring.append(self.tableWidget.item(i, column+3).text())
            Qtys.append(self.tableWidget.item(i,column+1).text())

            print(" ")
        for j,k in zip(datastring,Qtys):
            dataint.append(int(j))
            Qtyin.append(int(k))
        GstInclude = sum(dataint)*12/100
        Totalsum = sum(dataint)+GstInclude
        self.TALabel.setText(str(sum(dataint)))

        self.GTALabel.setText(str(Totalsum))
        self.QALabel.setText(str(sum(Qtyin)))

    def export_to_csv(self):
        try:
            with open('Expense Report.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((self.tableWidget.horizontalHeaderItem(0).text(), self.tableWidget.horizontalHeaderItem(1).text()))
                for rowNumber in range(self.tableWidget.rowCount()):
                    writer.writerow([self.tableWidget.item(rowNumber, 0).text(), self.tableWidget.item(rowNumber, 1).text()])
                    print('CSV file exported.')
                file.close()
        except Exception as e:
            print(e)

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self.tableWidget)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.tableWidget.print_(printer)

    def printpreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer,MainWindow)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self,printer):
        self.tableWidget.print_(printer)



    def _addRow(self):
        self.rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)





    def _removeRow(self):
        button = self.tableWidget.sender()

        if button:
            row = self.tableWidget.indexAt(button.pos()).row()
            self.tableWidget.removeRow(row)
    def backf_bttn(self):
        self.groupBox_3.setVisible(False)

    def backs_bttn(self):
        #self.groupBox_2.setVisible(False)
        self.groupBox_2.setVisible(False)
        self.backs.setVisible(False)
    def backFf_bttn(self):
        self.groupBox_4.setVisible(False)
        self.backff.setVisible(False)
        self.groupBox_3.setVisible(True)
    def Second_bttn(self):
        self.backs = QtWidgets.QPushButton("back",self.centralwidget)
        self.backs.setGeometry(QtCore.QRect(650, 29, 75, 23))
        self.backs.setObjectName("back")
        self.backs.clicked.connect(self.backs_bttn)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_2.setObjectName("groupBox")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Small Kitchen Appliances",self.gridLayoutWidget_2)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/SmllKitApp.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        self.Sfirstbttn.clicked.connect(self.SndFirst_bttn)
        self.gridLayout_3.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Cooling and Heating",self.gridLayoutWidget_2)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/CoolingndHeating.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.Ssecondbttn.clicked.connect(self.SndSecond_bttn)
        self.gridLayout_3.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Large Appliances",self.gridLayoutWidget_2)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.clicked.connect(self.SndThird_bttn)
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/Large Appliances.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_3.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Garments Care",self.gridLayoutWidget_2)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/GarmentCare.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_3.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Parts and Accessories",self.gridLayoutWidget_2)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/HmAppPatandAcces.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfivthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_3.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("Home Lighting",self.gridLayoutWidget_2)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("border-image:url(Images/HomeLigthing.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_3.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_2)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_3.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_2)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_3.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_2)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_3.addWidget(self.SNinthbttn, 3, 2)



        self.groupBox_2.setVisible(True)
        self.backs.setVisible(True)



    def first_bttn(self):
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_3.setObjectName("groupBox")

        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Clothes",self.gridLayoutWidget_3)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/menClothe.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_4.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Shoes",self.gridLayoutWidget_3)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/menshoes.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.gridLayout_4.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Watchs",self.gridLayoutWidget_3)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/menwatches.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_4.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Wallet & Belt",self.gridLayoutWidget_3)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/menWalletndBelt.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_4.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("SunGlasses",self.gridLayoutWidget_3)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/mensunglasses.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_4.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_3)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_4.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_3)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_4.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_3)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_4.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_3)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_4.addWidget(self.SNinthbttn, 3, 2)
        self.groupBox_3.setVisible(True)
        self.backf.setVisible(True)

    def fstfirst_bttn(self):
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_4.setObjectName("groupBox")

        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Shirts",self.gridLayoutWidget_4)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/menShirts.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.clicked.connect(self.Shirts)
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_5.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Suits",self.gridLayoutWidget_4)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/mensuit.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.Ssecondbttn.clicked.connect(self.Suits)
        self.gridLayout_5.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Jackets",self.gridLayoutWidget_4)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.clicked.connect(self.Jackets)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/menJackets.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_5.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Jeans",self.gridLayoutWidget_4)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.clicked.connect(self.Jeans)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/menJeans.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_5.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Pants",self.gridLayoutWidget_4)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.clicked.connect(self.Pants)
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/menPants.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfivthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_5.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("T-Shirts",self.gridLayoutWidget_4)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.clicked.connect(self.T_Shirts)
        self.SSixthbttn.setStyleSheet("border-image:url(Images/menTShirts.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_5.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_4)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_5.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_4)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_5.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_4)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_5.addWidget(self.SNinthbttn, 3, 2)
        self.backff = QtWidgets.QPushButton("back",self.centralwidget)
        self.backff.setGeometry(QRect(650, 29, 75, 23))
        self.backff.clicked.connect(self.backFf_bttn)
        self.groupBox_4.setVisible(True)
        self.backff.setVisible(True)


    def fivth_bttn(self):
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_5.setObjectName("groupBox")

        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_5)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget")

        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Vegetables and Fruits",self.gridLayoutWidget_5)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/FruitsandVegetables.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_6.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Bread and Bakery",self.gridLayoutWidget_5)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/BreadandBakery.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.gridLayout_6.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Beverages",self.gridLayoutWidget_5)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/Beverages.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_6.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Dry Goods",self.gridLayoutWidget_5)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/DryGoods.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_6.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Dairy Items",self.gridLayoutWidget_5)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/DairyItems.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_6.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("Oils",self.gridLayoutWidget_5)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("border-image:url(Images/Oils.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_6.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("Cleaners",self.gridLayoutWidget_5)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("border-image:url(Images/Cleaners.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_6.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_5)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_6.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_5)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_6.addWidget(self.SNinthbttn, 3, 2)
        self.backfi = QtWidgets.QPushButton("back",self.centralwidget)
        self.backfi.setGeometry(QRect(650, 29, 75, 23))
        self.backfi.clicked.connect(self.backFi_bttn)
        self.groupBox_5.setVisible(True)
        self.backfi.setVisible(True)

    def backFi_bttn(self):
        self.groupBox_5.setVisible(False)
        self.backfi.setVisible(False)

    def SndFirst_bttn(self):

        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_6.setObjectName("groupBox")

        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_6)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget")

        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Blender And Juicer",self.gridLayoutWidget_6)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/BlenderndJuiceMixer.jpeg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        self.Sfirstbttn.clicked.connect(self.Juicer)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_7.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Oven and Toster",self.gridLayoutWidget_6)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/Oven and Toster.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.Ssecondbttn.clicked.connect(self.OvenToster)
        self.gridLayout_7.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Rice Cooker",self.gridLayoutWidget_6)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.clicked.connect(self.RicCooker)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/Rice Cooker.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_7.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Coffee Maker",self.gridLayoutWidget_6)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.clicked.connect(self.CoffeeMaker)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/CoffeeMaker.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_7.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Sandwich Maker",self.gridLayoutWidget_6)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/ElectricSandwichMaker.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_7.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("Microwave",self.gridLayoutWidget_6)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("border-image:url(Images/Microwaves.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_7.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("Elec. Kattel",self.gridLayoutWidget_6)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("border-image:url(Images/ElectricKattle.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_7.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_6)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_7.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_6)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_7.addWidget(self.SNinthbttn, 3, 2)
        self.backSf = QPushButton("back",self.centralwidget)
        self.backSf.setGeometry((QRect(650, 29, 75, 23)))
        self.backSf.clicked.connect(self.backSf_bttn)
        self.groupBox_6.setVisible(True)
        self.backSf.setVisible(True)
    def backSf_bttn(self):
        self.groupBox_6.setVisible(False)
        self.backSf.setVisible(False)
        self.groupBox_2.setVisible(True)

    def SndSecond_bttn(self):

        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_7.setObjectName("groupBox")

        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_7)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget")

        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_8.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Fan",self.gridLayoutWidget_7)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/Fans.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_8.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Air Conditioner",self.gridLayoutWidget_7)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/AirConditioner.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.Ssecondbttn.clicked.connect(self.AirConditioner)
        self.gridLayout_8.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Room Heater",self.gridLayoutWidget_7)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/RoomHeater.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_8.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Air Cooler",self.gridLayoutWidget_7)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/AirCooler.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_8.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Air Purifer",self.gridLayoutWidget_7)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/AirPurifier.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_8.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("Water Heater",self.gridLayoutWidget_7)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("border-image:url(Images/WaterHeater.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_8.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_7)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_8.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_7)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_8.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_7)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_8.addWidget(self.SNinthbttn, 3, 2)
        self.backSs = QPushButton("back",self.centralwidget)
        self.backSs.setGeometry((QRect(650, 29, 75, 23)))
        self.backSs.clicked.connect(self.backSs_bttn)
        self.groupBox_7.setVisible(True)
        self.backSs.setVisible(True)
    def backSs_bttn(self):
        self.groupBox_7.setVisible(False)
        self.backSs.setVisible(False)
        self.groupBox_2.setVisible(True)

    def SndThird_bttn(self):

        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_8.setObjectName("groupBox")

        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_8)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget")

        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_9.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Redrigerator",self.gridLayoutWidget_8)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/Refrigerator.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_9.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Television",self.gridLayoutWidget_8)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/Television.jpeg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.Ssecondbttn.clicked.connect(self.Television)
        self.gridLayout_9.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Washing Machine",self.gridLayoutWidget_8)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/WashingMachine.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_9.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Freezer",self.gridLayoutWidget_8)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/Freezer.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_9.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Cooktops & Ranges",self.gridLayoutWidget_8)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/CookingTapandRanges.jpeg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_9.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("Vaccum Cleaner ",self.gridLayoutWidget_8)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("border-image:url(Images/VaccumCleaner.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_9.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_8)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_9.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_8)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_9.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_8)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_9.addWidget(self.SNinthbttn, 3, 2)
        self.backSt = QPushButton("back",self.centralwidget)
        self.backSt.setGeometry((QRect(650, 29, 75, 23)))
        self.backSt.clicked.connect(self.backSt_bttn)
        self.groupBox_8.setVisible(True)
        self.backSt.setVisible(True)
    def backSt_bttn(self):
        self.groupBox_8.setVisible(False)
        self.backSt.setVisible(False)
        self.groupBox_2.setVisible(True)

    def Sixth_bttn(self):

        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_9.setObjectName("groupBox")

        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.groupBox_9)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget")

        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_10.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Kitchenware",self.gridLayoutWidget_9)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/Kitchenware.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_10.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Furniture",self.gridLayoutWidget_9)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/Furniture.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.gridLayout_10.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Furnishing",self.gridLayoutWidget_9)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/Furnishing.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_10.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Home Decor",self.gridLayoutWidget_9)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/Home Decor.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_10.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Pet Supplies",self.gridLayoutWidget_9)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/Pet Supplies.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_10.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("None ",self.gridLayoutWidget_9)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_10.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_9)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_10.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_9)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_10.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_9)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_10.addWidget(self.SNinthbttn, 3, 2)
        self.backsi = QPushButton("back",self.centralwidget)
        self.backsi.setGeometry((QRect(650, 29, 75, 23)))
        self.backsi.clicked.connect(self.backSix_bttn)
        self.groupBox_9.setVisible(True)
        self.backsi.setVisible(True)
    def backSix_bttn(self):
        self.groupBox_9.setVisible(False)
        self.backsi.setVisible(False)

    def Seventh_bttn(self):

        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_10.setObjectName("groupBox")

        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.groupBox_10)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget")

        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_11.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Mobiles",self.gridLayoutWidget_10)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/Mobiles.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_11.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Desktop Pcs",self.gridLayoutWidget_10)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/DesktopPcs.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.gridLayout_11.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Laptop",self.gridLayoutWidget_10)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/Laptop.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_11.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Camera",self.gridLayoutWidget_10)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/Camera.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_11.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Speakers",self.gridLayoutWidget_10)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/Speakers.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_11.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("Mobile Accessories ",self.gridLayoutWidget_10)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("border-image:url(Images/MobileAccessories.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_11.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("Computer Accessories",self.gridLayoutWidget_10)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("border-image:url(Images/ComputerAccessories.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_11.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_10)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_11.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_10)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_11.addWidget(self.SNinthbttn, 3, 2)
        self.backse = QPushButton("back",self.centralwidget)
        self.backse.setGeometry((QRect(650, 29, 75, 23)))
        self.backse.clicked.connect(self.backSev_bttn)
        self.groupBox_10.setVisible(True)
        self.backse.setVisible(True)
    def backSev_bttn(self):
        self.groupBox_10.setVisible(False)
        self.backse.setVisible(False)

    def Eight_bttn(self):

        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_11.setObjectName("groupBox")

        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.groupBox_11)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget")

        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_12.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("NoteBook nd Diaries",self.gridLayoutWidget_11)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/NoteBookndDiaries.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_12.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Colors",self.gridLayoutWidget_11)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/Colors.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.gridLayout_12.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Geometry Box",self.gridLayoutWidget_11)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/GeometryBox.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_12.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Calculator",self.gridLayoutWidget_11)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/Calculator.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_12.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Pens",self.gridLayoutWidget_11)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/Pens.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfivthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_12.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("None ",self.gridLayoutWidget_11)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_12.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_11)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_12.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_11)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_12.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_11)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_12.addWidget(self.SNinthbttn, 3, 2)
        self.backei = QPushButton("back",self.centralwidget)
        self.backei.setGeometry((QRect(650, 29, 75, 23)))
        self.backei.clicked.connect(self.backEig_bttn)
        self.groupBox_11.setVisible(True)
        self.backei.setVisible(True)
    def backEig_bttn(self):
        self.groupBox_11.setVisible(False)
        self.backei.setVisible(False)

    def Third_bttn(self):

        self.groupBox_12 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_12.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_12.setObjectName("groupBox")

        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.groupBox_12)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget")

        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_13.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Clothing",self.gridLayoutWidget_12)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/WomenCloting.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_13.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("FootWear",self.gridLayoutWidget_12)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/WomenFootwear.jpeg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.gridLayout_13.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Beauty and Grooming",self.gridLayoutWidget_12)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/Beauty nd Gromming.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_13.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Jewellery",self.gridLayoutWidget_12)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/WomenJewellery.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_13.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Watches",self.gridLayoutWidget_12)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/Womenwatche.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfivthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_13.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("Accessories ",self.gridLayoutWidget_12)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("border-image:url(Images/WomenAccessories.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_13.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_12)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_13.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_12)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_13.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_12)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_13.addWidget(self.SNinthbttn, 3, 2)
        self.backth = QPushButton("back",self.centralwidget)
        self.backth.setGeometry((QRect(650, 29, 75, 23)))
        self.backth.clicked.connect(self.backTh_bttn)
        self.groupBox_12.setVisible(True)
        self.backth.setVisible(True)
    def backTh_bttn(self):
        self.groupBox_12.setVisible(False)
        self.backth.setVisible(False)

    def Fourth_bttn(self):

        self.groupBox_13 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_13.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_13.setObjectName("groupBox")

        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.groupBox_13)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget")

        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_14.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Clothes",self.gridLayoutWidget_13)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/kidsClothing.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_14.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("FootWear",self.gridLayoutWidget_13)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/kidsFootwear.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.gridLayout_14.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Toys",self.gridLayoutWidget_13)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/kidsToys.jpeg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_14.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Baby Care",self.gridLayoutWidget_13)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/Kids BabyCare.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_14.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton(" None",self.gridLayoutWidget_13)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.Sfivthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_14.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("None ",self.gridLayoutWidget_13)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_14.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_13)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_14.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_13)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_14.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_13)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_14.addWidget(self.SNinthbttn, 3, 2)
        self.backfo = QPushButton("back",self.centralwidget)
        self.backfo.setGeometry((QRect(650, 29, 75, 23)))
        self.backfo.clicked.connect(self.backFor_bttn)
        self.groupBox_13.setVisible(True)
        self.backfo.setVisible(True)
    def backFor_bttn(self):
        self.groupBox_13.setVisible(False)
        self.backfo.setVisible(False)

    def Ninth_bttn(self):

        self.groupBox_14 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_14.setGeometry(QtCore.QRect(650, 51, 710, 500))
        self.groupBox_14.setObjectName("groupBox")

        self.gridLayoutWidget_14 = QtWidgets.QWidget(self.groupBox_14)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(0, 0, 710, 490))
        self.gridLayoutWidget_14.setObjectName("gridLayoutWidget")

        self.gridLayout_15 = QtWidgets.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_15.setObjectName("gridLayout_2")
        #### FirstButton Screen Button Section
        self.Sfirstbttn = QtWidgets.QPushButton("Cricket Kit",self.gridLayoutWidget_14)
        self.Sfirstbttn.setObjectName("firstbttn")
        self.Sfirstbttn.setStyleSheet("border-image:url(Images/CircketKit.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sfirstbttn.setMinimumWidth(70)
        self.Sfirstbttn.setMinimumHeight(140)
        ##self.Sfirstbttn.clicked.connect(self.fstfirst_bttn)
        self.gridLayout_15.addWidget(self.Sfirstbttn, 1, 0)
        self.Ssecondbttn = QtWidgets.QPushButton("Sport Balls",self.gridLayoutWidget_14)
        self.Ssecondbttn.setObjectName("secondbttn")
        self.Ssecondbttn.setStyleSheet("border-image:url(Images/Sport Balls.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Ssecondbttn.setFont(QtGui.QFont("Georgia",10))
        self.Ssecondbttn.setMinimumWidth(70)
        self.Ssecondbttn.setMinimumHeight(140)
        self.gridLayout_15.addWidget(self.Ssecondbttn, 1, 1)
        self.Sthirdbttn = QtWidgets.QPushButton("Skating Items",self.gridLayoutWidget_14)
        self.Sthirdbttn.setAutoDefault(False)
        self.Sthirdbttn.setDefault(False)
        self.Sthirdbttn.setFlat(False)
        self.Sthirdbttn.setMinimumWidth(70)
        self.Sthirdbttn.setMinimumHeight(140)
        self.Sthirdbttn.setStyleSheet("border-image:url(Images/Skatingitems.jpeg);text-align:bottom;color:red;font: bold 14px;")
        self.Sthirdbttn.setFont(QtGui.QFont("Georgia",10))
        self.Sthirdbttn.setObjectName("thirdbttn")
        self.gridLayout_15.addWidget(self.Sthirdbttn, 1, 2)
        self.Sfourthbttn = QtWidgets.QPushButton("Camping and Hiking",self.gridLayoutWidget_14)
        self.Sfourthbttn.setObjectName("fourthbttn")
        self.Sfourthbttn.setMinimumHeight(140)
        self.Sfourthbttn.setMinimumWidth(70)
        self.Sfourthbttn.setStyleSheet("border-image:url(Images/Camping.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfourthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_15.addWidget(self.Sfourthbttn, 2, 0)
        self.Sfivthbttn = QtWidgets.QPushButton("Badminton",self.gridLayoutWidget_14)
        self.Sfivthbttn.setObjectName("fivthbttn")
        self.Sfivthbttn.setMinimumHeight(140)
        self.Sfivthbttn.setMinimumWidth(70)
        self.Sfivthbttn.setStyleSheet("border-image:url(Images/Badminton.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.Sfirstbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_15.addWidget(self.Sfivthbttn, 2, 1)
        self.SSixthbttn = QtWidgets.QPushButton("Fitness Items ",self.gridLayoutWidget_14)
        self.SSixthbttn.setObjectName("Sixthbttn")
        self.SSixthbttn.setMinimumHeight(140)
        self.SSixthbttn.setMinimumWidth(70)
        self.SSixthbttn.setStyleSheet("border-image:url(Images/FitnessItems.jpg);text-align:bottom;color:red;font: bold 14px;")
        self.SSixthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_15.addWidget(self.SSixthbttn, 2, 2)
        self.SSeventhbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_14)
        self.SSeventhbttn.setObjectName("Seventhbttn")
        self.SSeventhbttn.setMinimumHeight(140)
        self.SSeventhbttn.setMinimumWidth(70)
        self.SSeventhbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SSeventhbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_15.addWidget(self.SSeventhbttn, 3, 0)
        self.SEightbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_14)
        self.SEightbttn.setObjectName("Seventhbttn")
        self.SEightbttn.setMinimumHeight(140)
        self.SEightbttn.setMinimumWidth(70)
        self.SEightbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SEightbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_15.addWidget(self.SEightbttn, 3, 1)
        self.SNinthbttn = QtWidgets.QPushButton("None",self.gridLayoutWidget_14)
        self.SNinthbttn.setObjectName("Seventhbttn")
        self.SNinthbttn.setMinimumHeight(140)
        self.SNinthbttn.setMinimumWidth(70)
        self.SNinthbttn.setStyleSheet("text-align:bottom;color:red;font: bold 14px;")
        self.SNinthbttn.setFont(QtGui.QFont("Georgia",10))
        self.gridLayout_15.addWidget(self.SNinthbttn, 3, 2)
        self.backni = QPushButton("back",self.centralwidget)
        self.backni.setGeometry((QRect(650, 29, 75, 23)))
        self.backni.clicked.connect(self.backNin_bttn)
        self.groupBox_14.setVisible(True)
        self.backni.setVisible(True)
    def backNin_bttn(self):
        self.groupBox_14.setVisible(False)
        self.backni.setVisible(False)

### TableItem Button
    def Shirts(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a = self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Shirt"))

        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("240"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("240"))




        #self.tableWidget.setCellWidget(self.rowCount, 1, "Shirt")

    def T_Shirts(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("T-Shirts"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("300"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("300"))


    def Suits(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Suits"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("1500"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("1500"))


    def Jackets(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Jackets"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("800"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("800"))


    def Pants(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Pants"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("500"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("500"))


    def Jeans(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
            #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Jeans"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("400"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("400"))


    def Juicer(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Juicer Mixer"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("5000"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("5000"))


    def OvenToster(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Oven and Toster"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("6000"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("6000"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("6000"))

    def RicCooker(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Rice Cooker"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("1800"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("1800"))


    def CoffeeMaker(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("CoffeMaker"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("7000"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("7000"))


    def AirConditioner(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Air Conditioner"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("10000"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("10000"))


    def Television(self):
        self.rowCount = self.tableWidget.rowCount()


        self.tableWidget.insertRow(self.rowCount )
        remove = QtWidgets.QPushButton('X', self.tableWidget)
        #remove.clicked.connect(lambda _, x=(self.rowCount)+1: print('button', x))
        remove.clicked.connect(self._removeRow)
        self.tableWidget.setCellWidget(self.rowCount, 4, remove)
        remove.setStyleSheet("QPushButton"
                             "{"
                             "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));color: #ffffff;	min-width: 80px;	border-style: solid;border-width: 1px;	border-radius: 3px;	border-color: #051a39;	padding: 5px;"

                             "}"
                             "QPushButton::pressed"
                             "{"
                            "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));border: 1px solid #b78620;}"
                             )
        a=self.rowCount
        self.tableWidget.setItem(a,0,QTableWidgetItem("Televisions"))
        self.tableWidget.setItem(a,1,QTableWidgetItem("1"))
        self.tableWidget.setItem(a,2,QTableWidgetItem("12000"))
        self.tableWidget.setItem(a,3,QTableWidgetItem("12000"))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Billing Software"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Items"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Qty."))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Remove"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()



        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit "))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionNew_Page.setText(_translate("MainWindow", "New Page"))
        self.actionsupoort.setText(_translate("MainWindow", "supoort"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit "))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionNew_Page.setText(_translate("MainWindow", "New Page"))
        self.actionsupoort.setText(_translate("MainWindow", "supoort"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
