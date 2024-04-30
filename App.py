from Topic_Class import Topic
from Topic_Class import Open_File
import random
from Topic_Class import Save_File

from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt5.QtWidgets import QLabel,QMessageBox, QFileDialog, QInputDialog
from PyQt5.QtGui import QIcon
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QTabWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap,  QDoubleValidator
TP = Topic()

onlyInt = QtGui.QIntValidator()
onlyInt.setRange(1, 10)


class Ui_Widget(object):
    def setupUi(self, Widget):
        #initial config
        
        self.QuesAccess = -1
        Widget.setFixedSize(480, 800)
        Widget.setObjectName("Widget")
        Widget.setEnabled(True)
        Widget.resize(480, 800)
        self.tabWidget = QtWidgets.QTabWidget(Widget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 480, 800))
        self.tabWidget.setObjectName("tabWidget")
        #Variable-OpenFile-----
        self.Topics = Open_File()
        self.Max_Index = len(self.Topics)
        self.IndexAccess = 0
        #---------------------
        icon = QtGui.QIcon("AppData/Icon.png")
        Widget.setWindowIcon(icon)
        #--------------------------------------------
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 480, 800))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Tit_label = QtWidgets.QLabel(self.tab)
        self.Tit_label.setGeometry(QtCore.QRect(20, 10, 240, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.Tit_label.setFont(font)
        self.Tit_label.setObjectName("Tit_label")
        self.Ques_lable = QtWidgets.QLabel(self.tab)
        self.Ques_lable.setGeometry(QtCore.QRect(20, 50, 450, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        self.Ques_lable.setFont(font)
        self.Ques_lable.setWordWrap(True)
        self.Ques_lable.setObjectName("Ques_lable")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(10, 230, 460, 540))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        
        self.T_Ans_label = QtWidgets.QLabel(self.tab)
        self.T_Ans_label.setGeometry(QtCore.QRect(20, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.T_Ans_label.setFont(font)
        self.T_Ans_label.setObjectName("T_Ans_label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(330, 180, 120, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_1 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 180, 120, 25))
        self.pushButton_1.setObjectName("pushButton_1")
        

        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 180, 120, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Index_num_label = QtWidgets.QLabel(self.tab)
        self.Index_num_label.setGeometry(QtCore.QRect(260, 20, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        self.Index_num_label.setFont(font)
        self.Index_num_label.setObjectName("Index_num_label")



        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 480, 800))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.InQues_Tab2_label = QtWidgets.QLabel(self.tab_2)
        self.InQues_Tab2_label.setGeometry(QtCore.QRect(10, 40, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.InQues_Tab2_label.setFont(font)
        self.InQues_Tab2_label.setObjectName("InQues_Tab2_label")
        self.InDex_Tab2_label = QtWidgets.QLabel(self.tab_2)
        self.InDex_Tab2_label.setGeometry(QtCore.QRect(10, 10, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.InDex_Tab2_label.setFont(font)
        self.InDex_Tab2_label.setObjectName("InDex_Tab2_label")

        self.InDex_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.InDex_comboBox.setGeometry(QtCore.QRect(80, 10, 160, 25))
        font = QtGui.QFont()
        font.setPointSize(10)

        font.setItalic(True)
        self.InDex_comboBox.setStyleSheet("color: rgb(250, 0, 0);")
        self.InDex_comboBox.setFont(font)
        self.InDex_comboBox.setObjectName("InDex_comboBox")
        #Add combo box
        for i in range(1,len(self.Topics)):
            self.InDex_comboBox.addItems([str(self.Topics[i].topic)])
        #---------------------------------------------------------
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 10, 90, 25))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 10, 90, 25))
        self.pushButton_6.setObjectName("pushButton_6")


        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 70, 460, 100))
        font = QtGui.QFont()
        font.setPointSize(12)  # Set the font size to 12 points

        # Apply the font to the QPlainTextEdit widget
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.InAns_Tab2_label = QtWidgets.QLabel(self.tab_2)
        self.InAns_Tab2_label.setGeometry(QtCore.QRect(10, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.InAns_Tab2_label.setFont(font)
        self.InAns_Tab2_label.setObjectName("InAns_Tab2_label")

        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 200, 460, 380))
        font = QtGui.QFont()
        font.setPointSize(14)  # Set the font size to 12 points

        # Apply the font to the QPlainTextEdit widget
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(230, 740, 31, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(onlyInt)
        self.InNum_Tab2_label = QtWidgets.QLabel(self.tab_2)
        self.InNum_Tab2_label.setGeometry(QtCore.QRect(10, 740, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.InNum_Tab2_label.setFont(font)
        self.InNum_Tab2_label.setObjectName("InNum_Tab2_label")


        self.List_textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.List_textBrowser.setGeometry(QtCore.QRect(10, 610, 460, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.List_textBrowser .setFont(font)
        self.List_textBrowser .setObjectName("List_textBrowser ")

        self.List_Tab2_label = QtWidgets.QLabel(self.tab_2)
        self.List_Tab2_label.setGeometry(QtCore.QRect(10, 580, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.List_Tab2_label.setFont(font)
        self.List_Tab2_label.setObjectName("List_Tab2_label")



        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 740, 91, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 740, 91, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Widget)
        self.Update_QuesList()

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Ielts Speaking"))
        self.Tit_label.setText(_translate("Widget", "Question"))
        self.Ques_lable.setText(_translate("Widget", "               "))
        self.T_Ans_label.setText(_translate("Widget", "Sample Answer"))
        self.pushButton.setText(_translate("Widget", "Next Question"))

        self.pushButton_1.setText(_translate("Widget", "Display Question"))
        
        self.pushButton_2.setText(_translate("Widget", "See Answer"))
        self.Index_num_label.setText(_translate("Widget", "Topic: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Widget", "Speaking"))
        self.InQues_Tab2_label.setText(_translate("Widget", "Input Question"))
        self.InDex_Tab2_label.setText(_translate("Widget", "Topic:"))
        self.InAns_Tab2_label.setText(_translate("Widget", "Input Answer"))
        self.List_Tab2_label.setText(_translate("Widget", "List of Question"))
        self.InNum_Tab2_label.setText(_translate("Widget", "Number of question to edit: "))
        self.pushButton_3.setText(_translate("Widget", "Choose"))
        self.pushButton_4.setText(_translate("Widget", "Save"))
        self.pushButton_5.setText(_translate("Widget", "Add Topic"))
        self.pushButton_6.setText(_translate("Widget", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Widget", "Input Question"))


        #Action for Display
        self.pushButton_1.clicked.connect(self.Display_Button)
        self.pushButton_2.clicked.connect(self.See_Answer)
        self.pushButton.clicked.connect(self.Next_Question)


        #Active Tab2
        self.pushButton_5.clicked.connect(self.Add_Topic)
    
        self.pushButton_4.clicked.connect(self.Add_Question)

        self.InDex_comboBox.currentTextChanged.connect(self.Update_QuesList)

        self.pushButton_3.clicked.connect(self.Edit_Question)
        
        self.lineEdit.textChanged.connect(self.Line_EditChange)
    
        self.pushButton_6.clicked.connect(self.Delete_Topic)
    #Function for Activate app
        print(len(self.Topics))


    def Line_EditChange(self):
        self.pushButton_3.setText('Choose')
    def Display_Button(self):
        if self.pushButton_1.text() == 'Display Question':
            if(self.IndexAccess != 0):
                self.QuesAccess = -1
                self.pushButton_1.setText("End")
                self.textBrowser.clear()
                Ran = random.randint(1, len(self.Topics)-1)
                self.IndexAccess = Ran
                #self.Ques_lable.setText(self.Topics[1].topic)
                Label_Text = "Topic: " + str(self.Topics[self.IndexAccess].topic)
                self.Index_num_label.setText(Label_Text)
    
        else:
            self.pushButton_1.setText("Display Question")
            self.Ques_lable.setText("               ")
            self.Index_num_label.setText("Topic:")

    def Next_Question(self):
        if self.pushButton_1.text() != 'Display Question':
            self.QuesAccess += 1
            if(self.QuesAccess == len(self.Topics[self.IndexAccess].question)):
                self.QuesAccess -=1
            self.Ques_lable.setText(str(self.Topics[self.IndexAccess].question[self.QuesAccess]))

    def See_Answer(self):
        if self.pushButton_1.text() == 'End' and self.QuesAccess != -1:           
            self.textBrowser.setText(self.Topics[self.IndexAccess].answer[self.QuesAccess])
        else:
            self.textBrowser.setText("Please Display the question before looking for the answer")

    def Data_Update(self):
        self.Topics = Open_File()
        self.Max_Index = len(self.Topics)
        self.Topics[0].topic = "Home Town"
        self.IndexAccess = 0

    def Add_Topic(self):
        text, ok_pressed = QInputDialog.getText(None, "Add New Topic", "Enter topic name:")
        if ok_pressed:
            if text.strip():  # Check if the input text is not empty
                T1 = TP
                T1.topic  = text
                self.Topics.append(T1)
                self.InDex_comboBox.addItems([T1.topic])
                print(len(self.Topics))
                Save_File(self.Topics)
                self.Data_Update()
                print(self.Topics[1].topic)
            else:
                return
    
    def Update_QuesList(self):
        self.List_textBrowser.clear()
        self.IndexAccess = 0
        for i in range(1,len(self.Topics)):
            if self.Topics[i].topic == self.InDex_comboBox.currentText():
                self.IndexAccess = i
                break

        for i in range(0, len(self.Topics[self.IndexAccess].question)):
            Text_display = str(i+1) +". "+str(self.Topics[self.IndexAccess].question[i])
            self.List_textBrowser.append(Text_display)


    def Add_Question(self):
        if self.plainTextEdit.toPlainText() and self.plainTextEdit_2.toPlainText():
            Temp_Index = 0
            for i in range(1,len(self.Topics)):
                if self.Topics[i].topic == self.InDex_comboBox.currentText():
                    Temp_Index = i
                    break

            if Temp_Index == 0:
                print("Error")
                return
            Text_For_Q = str(self.plainTextEdit.toPlainText())
            Text_For_A = str(self.plainTextEdit_2.toPlainText())


            self.Topics[Temp_Index].question.append(Text_For_Q)
            self.Topics[Temp_Index].answer.append(Text_For_A)
            Save_File(self.Topics)
            self.plainTextEdit.clear()
            self.plainTextEdit_2.clear()
            self.Update_QuesList()
        else:
            print("error")
    
    def Update_ComboBox(self):
        for i in range(1,len(self.Topics)):
            self.InDex_comboBox.addItems([str(self.Topics[i].topic)])

    def Edit_Question(self):

        if self.lineEdit.text().strip() == "" or int(self.lineEdit.text()) == 0 or int(self.lineEdit.text()) > len(self.Topics[self.IndexAccess].question) or len(self.Topics) <= 1:
            return
        else:
            if self.pushButton_3.text() == 'Choose':
                self.pushButton_3.setText('Edit')
               
                self.TempIndex = int(self.lineEdit.text()) - 1
                self.plainTextEdit.setPlainText(self.Topics[self.IndexAccess].question[self.TempIndex])
                self.plainTextEdit_2.setPlainText(self.Topics[self.IndexAccess].answer[self.TempIndex])
                self.pushButton_4.setEnabled(False)
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowIcon(QIcon("AppData/Icon.ico"))
                msgBox.setText("Are you sure you want to edit?")
                msgBox.setWindowTitle("Warning")
                msgBox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                msgBox.setDefaultButton(QMessageBox.Cancel)
                ret = msgBox.exec_()
                if ret == QMessageBox.Ok:
                    if not self.plainTextEdit.toPlainText() and not self.plainTextEdit_2.toPlainText():
                        del self.Topics[self.IndexAccess].question[self.TempIndex]
                        del self.Topics[self.IndexAccess].answer[self.TempIndex]
                    else:
                        Text_For_Q = str(self.plainTextEdit.toPlainText())
                        Text_For_A = str(self.plainTextEdit_2.toPlainText())
                        self.Topics[self.IndexAccess].question[self.TempIndex] = Text_For_Q
                        self.Topics[self.IndexAccess].answer[self.TempIndex] = Text_For_A
                    Save_File(self.Topics)
                self.Update_QuesList()
                self.pushButton_3.setText('Choose')
                self.pushButton_4.setEnabled(True)
                
        
    def Delete_Topic(self):
        Temp_Index = 0
        for i in range(1,len(self.Topics)):
            if self.Topics[i].topic == self.InDex_comboBox.currentText():
                Temp_Index = i
                break
        if Temp_Index == 0:
            print("Error")
            return
        msgBox1 = QMessageBox()
        msgBox1.setIcon(QMessageBox.Warning)
        msgBox1.setWindowIcon(QIcon("AppData/Icon.png"))
        text = "Are you sure you want to delete topic "+ str(self.Topics[Temp_Index].topic)+" ?"
        msgBox1.setText(text)
        msgBox1.setWindowTitle("Warning")
        msgBox1.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msgBox1.setDefaultButton(QMessageBox.Cancel)
        ret = msgBox1.exec_()
        if ret == QMessageBox.Ok:
            del self.Topics[Temp_Index]
            self.InDex_comboBox.clear()
            Save_File(self.Topics)
            self.Update_ComboBox()
            self.IndexAccess = 0
            self.plainTextEdit.clear()
            self.plainTextEdit_2.clear()
            self.textBrowser.clear()
            return
        self.pushButton_3.setText('Choose')
        self.pushButton_4.setEnabled(True)
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
