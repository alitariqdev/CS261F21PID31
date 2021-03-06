import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv
import threading
import Algorithms
from Algorithms import AlgorithmsC


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1114, 609)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 1131, 31))
        self.frame.setStyleSheet("background-color: rgb(12, 34, 97);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 47, 31))
        self.label.setStyleSheet(
            "image: url(:/newPrefix/filled_circle_30px.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 47, 31))
        self.label_2.setStyleSheet(
            "image: url(:/newPrefix/filled_circle_30px.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(90, 0, 47, 31))
        self.label_3.setStyleSheet(
            "image: url(:/newPrefix/filled_circle_30px.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(340, 40, 541, 31))
        self.label_4.setStyleSheet("font: 75 21pt \"MS Shell Dlg 2\";\n"
"color: rgb(12, 34, 97);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(330, 70, 501, 20))
        self.label_5.setObjectName("label_5")
        self.widget_9 = QtWidgets.QWidget(Form)
        self.widget_9.setGeometry(QtCore.QRect(20, 160, 841, 51))
        self.widget_9.setStyleSheet("background-color: rgb(12, 34, 97);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 72, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;")
        self.widget_9.setObjectName("widget_9")
        self.label_15 = QtWidgets.QLabel(self.widget_9)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 91, 51))
        self.label_15.setStyleSheet("image: url(:/newPrefix/pro.png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.progressBar = QtWidgets.QProgressBar(self.widget_9)
        self.progressBar.setGeometry(QtCore.QRect(90, 0, 751, 51))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setRange(0, 100)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 110, 161, 21))
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(12, 34, 97);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(70, 130, 141, 20))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(260, 110, 651, 22))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("Link 1")
        self.comboBox.addItem("Link 2")
        self.comboBox.addItem("Link 3")
        self.comboBox.addItem("Link 4")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(70, 240, 161, 21))
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(12, 34, 97);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(70, 260, 141, 20))
        self.label_9.setObjectName("label_9")
        self.widget_10 = QtWidgets.QWidget(Form)
        self.widget_10.setGeometry(QtCore.QRect(30, 290, 841, 281))
        self.widget_10.setStyleSheet("background-color: rgb(12, 34, 97);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 72, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;")
        self.widget_10.setObjectName("widget_10")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_10)
        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 711, 211))
        self.tableWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(235, 235, 235);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: \n"
"0px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.loaddata()

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(16, 99, 51, 51))
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_10.setStyleSheet("image: url(:/newPrefix/data.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(20, 230, 47, 51))
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setStyleSheet("image: url(:/newPrefix/search.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.widget_11 = QtWidgets.QWidget(Form)
        self.widget_11.setGeometry(QtCore.QRect(900, 160, 191, 51))
        self.widget_11.setStyleSheet("background-color: rgb(12, 34, 97);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.028, x2:1, y2:1, stop:0.306818 rgba(0, 0, 72, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius: 10px;")
        self.widget_11.setObjectName("widget_11")
        self.label_12 = QtWidgets.QPushButton(self.widget_11)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 51, 51))
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_12.setStyleSheet("image: url(:/newPrefix/play.png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_12.clicked.connect(self.worker)


        # self.label_12.mousePressEvent(self.ydr)        
        self.label_13 = QtWidgets.QLabel(self.widget_11)
        self.label_13.setGeometry(QtCore.QRect(66, 0, 61, 51))
        self.label_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_13.setStyleSheet("image: url(:/newPrefix/pause.png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget_11)
        self.label_14.setGeometry(QtCore.QRect(130, 0, 61, 51))
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_14.setStyleSheet("image: url(:/newPrefix/stop.png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.widget_12 = QtWidgets.QWidget(Form)
        self.widget_12.setGeometry(QtCore.QRect(900, 290, 191, 281))
        self.widget_12.setStyleSheet("background-color: rgb(12, 34, 97);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.028, x2:1, y2:1, stop:0.306818 rgba(0, 0, 72, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius: 10px;")
        self.widget_12.setObjectName("widget_12")
        self.label_16 = QtWidgets.QLabel(self.widget_12)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 191, 41))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 100 8pt \"MS Shell Dlg 2\";\n"
"")
        self.label_16.setObjectName("label_16")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_12)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 50, 141, 31))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_17 = QtWidgets.QLabel(self.widget_12)
        self.label_17.setGeometry(QtCore.QRect(0, 50, 47, 31))
        self.label_17.setStyleSheet("image: url(:/newPrefix/algor.png);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.widget_12)
        self.label_19.setGeometry(QtCore.QRect(0, 110, 47, 31))
        self.label_19.setStyleSheet("image: url(:/newPrefix/sort.png);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_12)
        self.comboBox_3.setGeometry(QtCore.QRect(50, 110, 141, 31))
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.radioButton = QtWidgets.QRadioButton(self.widget_12)
        self.radioButton.setGeometry(QtCore.QRect(20, 190, 71, 17))
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_12)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 190, 81, 17))
        self.radioButton_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_18 = QtWidgets.QPushButton(self.widget_12)
        self.label_18.setGeometry(QtCore.QRect(80, 240, 47, 31))
        self.label_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_18.setStyleSheet("image: url(:/newPrefix/sort1.png);\n"
"image: url(:/newPrefix/sort2.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(760, 240, 101, 22))
        self.comboBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 240, 441, 21))
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"border: 0.8px solid rgb(0,0,0);\n"
"border-radius: 6px")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
     
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def ydr(self,event:QtGui.QMouseEvent):
            print("yddd")
    def worker(self):
            thread = threading.Thread(target=self.Scrapper,args=())
            thread.start()
    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate(
            "Form", "C E N T R A L  R E A L  E S T A T E"))
        self.label_5.setText(_translate(
            "Form", "__________________________"))  # chang
        self.label_6.setText(_translate("Form", "S C R A P  D A T A"))
        self.label_7.setText(_translate("Form", "_________"))  # chang
        self.comboBox.setItemText(0, _translate("Form", "Link"))
        # self.comboBox.setItemText(1, _translate("Form", "Ali"))
        # self.comboBox.setItemText(2, _translate("Form", "Ali"))
        self.label_8.setText(_translate("Form", "S E A R C H"))
        self.label_9.setText(_translate("Form", "_________"))  # chang
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Area"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Location"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "No of Bedrooms"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "No of Bathrooms"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Description"))
        self.label_16.setText(_translate(
            "Form", "                 A L G O R I T H M"))
        self.comboBox_2.setItemText(0, _translate("Form", "Select Algorithm"))
        self.comboBox_2.setItemText(1, _translate("Form", "Selection"))
        self.comboBox_2.setItemText(2, _translate("Form", "Insertion"))
        self.comboBox_2.setItemText(3, _translate("Form", "Merge"))
        self.comboBox_2.setItemText(4, _translate("Form", "Bubble"))
        self.comboBox_2.setItemText(5, _translate("Form", "Radix"))
        self.comboBox_2.setItemText(6, _translate("Form", "Counting"))
        self.comboBox_3.setItemText(0, _translate("Form", "Sort By"))
        self.comboBox_3.setItemText(1, _translate("Form", "Area"))
        self.comboBox_3.setItemText(2, _translate("Form", "Location"))
        self.comboBox_3.setItemText(3, _translate("Form", "Price"))
        self.comboBox_3.setItemText(4, _translate("Form", "Beds"))
        self.comboBox_3.setItemText(5, _translate("Form", "Bathroom"))
        self.radioButton.setText(_translate("Form", "Ascending"))
        self.radioButton_2.setText(_translate("Form", "Descending"))
        self.comboBox_4.setItemText(0, _translate("Form", "Search By"))
        self.comboBox_4.setItemText(1, _translate("Form", "Area"))
        self.comboBox_4.setItemText(2, _translate("Form", "Loction"))
        self.comboBox_4.setItemText(3, _translate("Form", "Price"))
        self.comboBox_4.setItemText(4, _translate("Form", "Bedrooms"))
        self.comboBox_4.setItemText(5, _translate("Form", "Bathrooms"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Search"))
    def progress(self):
            
            
            for i in range(1000):
                    
                    self.progressBar.setValue(i)
        
    def loaddata(self):

        property_titel = []
        area = []
        price = []
        location = []
        bedroom = []
        bathroom = []
        discryption = []

        with open('Property_Data.csv', encoding='cp850', mode='r')as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                        property_titel.append(lines[0])
                        discryption.append(lines[1])
                        price.append(lines[2])
                        bedroom.append(lines[3])
                        bathroom.append(lines[4])
                        location.append(lines[5])
                        area.append(lines[6])

        row = 0
        self.tableWidget.setRowCount(len(property_titel))
        for title in property_titel:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
            row = row+1
        row = 0
        for ar in area:
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
            row = row+1
        row = 0
        for lo in location:
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
            row = row+1
        row = 0
        for pr in price:
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
            row = row+1
        row = 0
        for bd in bedroom:
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
            row = row+1
        row = 0
        for ba in bathroom:
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
            row = row+1
        row = 0
        for ds in discryption:
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
            row = row+1

    def Scrapper(self):
        print("YD")
        driver = webdriver.Chrome(
        executable_path=r"C:\Users\Ali tariq\Downloads\chromedriver_win32\chromedriver.exe")

        Prices = []
        Locations = []
        Titles = []
        Descriptions = []
        Areas=[]
        BedRooms=[]
        BathRooms=[]

        i=0
        for page in range(1,3): 
                
        #     https://www.zameen.com/Homes/Peshawar-17-165.html
                driver.get("https://www.zameen.com/Homes/Peshawar-17-"+str(page)+".html")
                content = driver.page_source
                soup = BeautifulSoup(content)

                Area = driver.find_elements_by_css_selector(".b6a29bc0 span")
                for b in Area:
                        Areas.append(b.text)

                for a in soup.findAll('div',attrs={'class':'_1d4d62ed'}):
                        
                        
                        Price =  (a.find('span',attrs={'class':'f343d9ce'}).text)
                        Location =  (a.find('div',attrs={'class':'_162e6469'}).text)
                        Title =  (a.find('h2',attrs={'class':'c0df3811'}).text)
                        Description =  (a.find('div',attrs={'class':'ee550b27'}).text)
                        
                        Bedroom=(a.find('div',attrs={'class':'_22b2f6ed'})).findChildren()[0].findChildren()[1].text
                        lenght=len(Bedroom)
                        if(lenght)  ==1:
                                Bedroom=(a.find('div',attrs={'class':'_22b2f6ed'})).findChildren()[0].findChildren()[1].text
                        else:
                                Bedroom="0"
                        
                        
                        Bathroom=(a.find('div',attrs={'class':'_22b2f6ed'})).findChildren()[5].text
                        lenght=len(Bathroom)
                        if(lenght)  ==1:
                                
                                Bathroom=(a.find('div',attrs={'class':'_22b2f6ed'})).findChildren()[5].text
                        else:
                                Bathroom="0"
                        
                        
                        
                        Prices.append(Price)
                        Locations.append(Location)
                        Titles.append(Title)
                        Descriptions.append(Description)
                        BathRooms.append(Bathroom)
                        BedRooms.append(Bedroom)
                        
                        self.progressBar.setValue(i)
                        i+=1
                        
                        
                        dataset = [Titles, Descriptions, Prices, BedRooms, BathRooms, Locations, Areas]
                        df = pd.DataFrame(data = dataset).T
                        df.columns = ["Ttitle" , "Description" , "Price" , "Bedrooms" , "Bathrooms" , "Location" , "Area" ]
                        df.to_csv("HELLO1.csv" ,index=False)    


    def sort(self):
            
            
            beds=[]
            with open('Property_Data.csv', encoding='cp850', mode='r')as file:
                      
                     csvFile = csv.reader(file)
                     for lines in csvFile:
                             beds.append(lines[3])
                             
            algo= self.comboBox_2.currentText()
            by= self.comboBox_3.currentText()
            if algo=="Insertion" and by=="Beds":
                    
                    Sorted = AlgorithmsC.insertion_sort(beds)
                    self.tableWidget.setItem
                    row = 0
                    for bd in sorted:
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                        row = row+1

        
        
        
import icon_resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    print(end)
