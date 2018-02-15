# !/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp949 -*-

# @ Author : L3ad0xFF

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pytsk3
import sys
import os
from struct import *
import datetime
import time
from time import gmtime, localtime, strftime
import wmi

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1369, 833)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(338, 83, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(14, 39, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(315, 112, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(329, 23, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 170, 471, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushbutton = QtWidgets.QPushButton(Dialog)
        self.pushbutton.setGeometry(QtCore.QRect(1210, 70, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushbutton.setFont(font)
        self.pushbutton.setObjectName("pushbutton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushbutton_2 = QtWidgets.QPushButton(Dialog)
        self.pushbutton_2.setGeometry(QtCore.QRect(1210, 150, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushbutton_2.setFont(font)
        self.pushbutton_2.setObjectName("pushbutton_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(420, 760, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(1220, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(33, 80, 221, 94))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 247, 1301, 511))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pushbutton_3 = QtWidgets.QPushButton(Dialog)
        self.pushbutton_3.setGeometry(QtCore.QRect(212, 39, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushbutton_3.setFont(font)
        self.pushbutton_3.setObjectName("pushbutton_3")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(857, 75, 331, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(835, 20, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushbutton_3.clicked.connect(self.maplogicphysic)
        self.pushbutton.clicked.connect(self.start)
        self.pushbutton_2.clicked.connect(self.makehtml)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NTFS_Printer"))
        self.label.setText(_translate("Dialog", "System Drive state"))
        self.label_3.setText(_translate("Dialog", "Input_Path (ex : /, /BoB/)"))
        self.label_2.setText(_translate("Dialog", "Input Physical Drive Name (ex : PhysicalDrive0)"))
        self.pushbutton.setText(_translate("Dialog", "Search"))
        self.label_4.setText(_translate("Dialog", "Dir & File List"))
        self.pushbutton_2.setText(_translate("Dialog", "Save to html"))
        self.label_5.setText(_translate("Dialog", "Best Of the Best 6th Digital Forensic"))
        self.label_6.setText(_translate("Dialog", "@ L3ad0xFF"))
        self.pushbutton_3.setText(_translate("Dialog", "Start"))
        self.label_7.setText(_translate("Dialog", "Drive Basic Information"))

    def maplogicphysic(self) :
        global phylogset
        phylogset = {}
        w = wmi.WMI()
        drivenum = 0
        for drive in w.Win32_LogicalDisk() :
           # print ("\t"+ drive.Caption + " = PhysicalDrive" + str(drivenum))
            phylogset['PhysicalDrive'+str(drivenum)] = drive.Caption
            drivenum += 1

        line_num = len(phylogset)
        self.tableWidget.setRowCount(line_num)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setHorizontalHeaderLabels(["Drive_Name", "PhysicalDrive"])

        value_list = list()

        for value in phylogset.values() :
            value_list.append(value)

        for row in range(0, len(phylogset)) :
            nd_column = value_list[row]
            item = QTableWidgetItem(nd_column)
            self.tableWidget.setItem(row, 0, item)

        for row in range(0, len(phylogset)) :
            st_column = "PhysicalDrive" + str(row)
            item2 = QTableWidgetItem(st_column)
            self.tableWidget.setItem(row, 1, item2)


        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()

    def partitionsize (self, num) :
        size_list = ['B', 'MB', 'KB', 'GB']
        size = num * 512.

        for div_count in range (0, 4) :
            if int(size) > 0 :
                size = size / 1024
            else :
                break
            
        return '%.2f %s' % (size *1024, size_list[div_count])

    def searchPartition (self, PartitionTables) :
        ntfs_list = list()
        for partition in PartitionTables:
            if partition.desc == b'NTFS / exFAT (0x07)' :
                par_type = "[+] Type : " +  partition.desc.decode('utf-8')
                par_number = "\n\t[-] Number : " + str(partition.start)
                par_start_sec = "\n\t[-] Start Sector : " + str(partition.start)
                par_sec_cnt = "\n\t[-] Sector Count : " + str(partition.len)
                par_size = "\n\t[-] Size : " + self.partitionsize(partition.len)
                ntfs_list.append(partition.start)
        self.textBrowser.setText(par_type + par_number + par_start_sec + par_sec_cnt + par_size)
        return ntfs_list

    def start(self) :
        global disk, Volume_img, root_path, vbr_offset, vbr_offset
        drive_cap = self.lineEdit.text()
        root_path = phylogset[drive_cap]
        set_Volume        = "\\\\.\\"+drive_cap
        Volume_img    = pytsk3.Img_Info(set_Volume)
        PartitionTables = pytsk3.Volume_Info(Volume_img)
        ntfs_sector = self.searchPartition(PartitionTables)
        #print (ntfs_sector)
        disk = open(set_Volume, 'rb')
        for sector_no in ntfs_sector :
            vbr_offset = sector_no * 512
            self.find_directory(vbr_offset)

    def find_directory(self, vbr_offset) :
        global in_path_list, set_path, fs
        fs = pytsk3.FS_Info(Volume_img, offset = vbr_offset) 
        set_path = self.lineEdit_2.text()
        in_path_list = list()

        directorys = fs.open_dir(path = set_path)
        # count = 0
        for directory in directorys :
            if ((directory.info.name.name).decode('utf-8') == '.') or ((directory.info.name.name).decode('utf-8') == '..') :
                continue

            try :
                if directory.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR :
                    dir_list = list()
                    dir_name = (directory.info.name.name).decode('utf-8')
                    dir_type = "Directory"
                    #dir_EA = directory.info.meta.addr
                    dir_path = root_path + set_path + ((directory.info.name.name).decode('utf-8'))
                    dir_mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.mtime))
                    dir_atime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.atime))
                    dir_ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.crtime))
                    dir_ectime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.ctime))
                    dir_size = str(directory.info.meta.size) + " Bytes"
                    #count += 1
                    dir_list = [dir_type, dir_name, dir_size, dir_path, dir_mtime, dir_atime, dir_ctime, dir_ectime]
                    in_path_list.append(dir_list)
                else:
                    file_list = list()
                    file_name = (directory.info.name.name).decode('utf-8')
                    file_type = "File"
                    #file_EA = directory.info.meta.addr
                    file_path = root_path + set_path + ((directory.info.name.name).decode('utf-8'))
                    file_mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.mtime))
                    file_atime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.atime))
                    file_ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.crtime))
                    file_ectime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.ctime))
                    file_size = str(directory.info.meta.size) + " Bytes"
                    #count += 1
                    file_list = [file_type, file_name, file_size, file_path, file_mtime, file_atime, file_ctime, file_ectime]
                    in_path_list.append(file_list)
            except :
                pass

        line_num = len(in_path_list)
        self.tableWidget_2.setRowCount(line_num)
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setHorizontalHeaderLabels(["Type", "Name", "Size", "Path", 
            "Modified time", "Access time", "Create time", "EntryChange time"])

        for p_row in range(0, len(in_path_list)) :
            for p_col in range(0, 8) :
                item = QTableWidgetItem(in_path_list[p_row][p_col])
                self.tableWidget_2.setItem(p_row, p_col, item)

        self.tableWidget_2.setSortingEnabled(False)
        t_column = self.tableWidget_2.horizontalHeader()
        t_column.sectionClicked.connect(self.table_column_sort)

        self.tableWidget_2.cellClicked.connect(self.cell_was_clicked)

        # self.tableWidget_2.resizeRowsToContents()
        self.tableWidget_2.setColumnWidth(0, 100)
        self.tableWidget_2.setColumnWidth(1, 170)
        #self.tableWidget_2.setColumnWidth(2, 150)
        self.tableWidget_2.setColumnWidth(3, 250)
        self.tableWidget_2.setColumnWidth(4, 150)
        self.tableWidget_2.setColumnWidth(5, 150)
        self.tableWidget_2.setColumnWidth(6, 150)
        self.tableWidget_2.setColumnWidth(7, 150)

        

    def table_column_sort(self, p_row) :
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setSortingEnabled(False)

    # def cellClick(self, p_row, p_col) :
    #     global new_path
    #     set_clicked_path = self.tableWidget_2.item(p_row, p_col)
    #     if cell is not None :
    #         now_path = cell.text()
    #     else :
    #         pass

    #     self.find_directory()


    def makehtml(self) :
        now_date = time.strftime("%Y-%m-%d", localtime())
        now_time = time.strftime("%H_%M_%S", localtime())
        set_loctime = now_date + " " + now_time
        time_info = "Local time_" + set_loctime
        filename = time_info + ".html"
        print (filename)
        htmlfile = open(filename, 'w')
        head_string = '<!DOCTYPE html><html><head><meta charset="UTF-8"></meta><title>NTFS Printer</title><link href="http://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet" type="text/css"><link href="style2.css" rel="stylesheet"></head>'
        body_string = '<body><div class="window_header"><h2>NTFS Analysis</h2><p>Best Of the Best 6th Digital Forensic</p></div><div class="clickclick">'
        body_t_string = '<table style="width:100%"><tr><th>Number</th><th>Type</th><th>Name</th><th>Size</th><th>Path</th><th>Modified Time</th><th>Access Time</th><th>Create Time</th><th>Entry_Change Time</th></tr>'
        init_string = head_string + body_string + body_t_string
        htmlfile.write(init_string)
        body_tb_string = " "
        for h_row in range(0, len(in_path_list)) :
            body_tb_string += "\n<tr>\n<td>" + str(h_row+1) + "</td>\n"
            for h_col in range(0,8) :
                if h_col == 1 or h_col == 3 :
                    body_tb_string += "\t<td>" + in_path_list[h_row][h_col] + "</td>\n"
                    #print (in_path_list[h_row][h_col])
                else :
                    body_tb_string += "\t<td>" + in_path_list[h_row][h_col] + "</td>\n"
            body_tb_string += "</tr>\n"
        body_tb_string += "</table>"

        footer_string = '<div class="window_footer" style="padding-top: 10px;height: 53.2px;"><a><span>@Author : L3ad0xFF</span> (Moonwon LEE)<br></a><p style="margin-top:5px;"><a href = "https://github.com/BoBpromoto/NTFS_Printer_Tech_01">https://github.com/BoBpromoto/NTFS_Printer_Tech_01</a></p><br></div></body></html>'
        htmlfile.write(body_tb_string)
        htmlfile.write(footer_string)
        htmlfile.close()

        self.msgboxprint()

    def msgboxprint(self) : 
        save_path = os.getcwd()
        now_date = time.strftime("%Y-%m-%d", localtime())
        now_time = time.strftime("%H:%M:%S", localtime())
        set_loctime = now_date + " " + now_time
        time_info = "Local time = " + set_loctime
        infoBox = QMessageBox() 
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("Extract HTML File Success!")
        infoBox.setInformativeText("Save Path = " + save_path)
        infoBox.setWindowTitle("Window Title")
        infoBox.setDetailedText(time_info)
        infoBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        infoBox.setEscapeButton(QMessageBox.Close)
        infoBox.exec_()

    def cell_was_clicked(self, row, column):
        global next_path
        next_path = ""
        for com_row in range (0, len(in_path_list)) :
            for com_col in range (0, 8) :
                if (com_row == row) and (com_col == column) :
                    if self.tableWidget_2.item(row, 0).text() == "Directory" :
                        next_path_str = self.tableWidget_2.item(row, 3).text()
                        next_path = next_path_str[2:] +'/'
                        print ("sel : " + next_path_str)
                        print (next_path)
                    else :
                        print ("Not Directory")

        self.clickeddir()
        return "clicked"

    def clickeddir(self) :
        directorys = fs.open_dir(path = next_path)
        # count = 0
        in_path_list = list()
        for directory in directorys :
            if ((directory.info.name.name).decode('utf-8') == '.') or ((directory.info.name.name).decode('utf-8') == '..') :
                continue

            try :
                if directory.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR :
                    dir_list = list()
                    dir_name = (directory.info.name.name).decode('utf-8')
                    dir_type = "Directory"
                    #dir_EA = directory.info.meta.addr
                    dir_path = root_path + next_path + ((directory.info.name.name).decode('utf-8'))
                    dir_mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.mtime))
                    dir_atime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.atime))
                    dir_ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.crtime))
                    dir_ectime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.ctime))
                    dir_size = str(directory.info.meta.size) + " Bytes"
                    #count += 1
                    dir_list = [dir_type, dir_name, dir_size, dir_path, dir_mtime, dir_atime, dir_ctime, dir_ectime]
                    in_path_list.append(dir_list)

                else:
                    file_list = list()
                    file_name = (directory.info.name.name).decode('utf-8')
                    file_type = "File"
                    #file_EA = directory.info.meta.addr
                    file_path = root_path + next_path + ((directory.info.name.name).decode('utf-8'))
                    file_mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.mtime))
                    file_atime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.atime))
                    file_ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.crtime))
                    file_ectime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.ctime))
                    file_size = str(directory.info.meta.size) + " Bytes"
                    #count += 1
                    file_list = [file_type, file_name, file_size, file_path, file_mtime, file_atime, file_ctime, file_ectime]
                    in_path_list.append(file_list)

            except :
                pass

        line_num = len(in_path_list)
        self.tableWidget_2.setRowCount(line_num)
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setHorizontalHeaderLabels(["Type", "Name", "Size", "Path", 
            "Modified time", "Access time", "Create time", "EntryChange time"])

        for p_row in range(0, len(in_path_list)) :
            for p_col in range(0, 8) :
                item = QTableWidgetItem(in_path_list[p_row][p_col])
                self.tableWidget_2.setItem(p_row, p_col, item)

        self.tableWidget_2.setSortingEnabled(False)
        t_column = self.tableWidget_2.horizontalHeader()
        t_column.sectionClicked.connect(self.table_column_sort)

        # self.tableWidget_2.resizeRowsToContents()
        self.tableWidget_2.setColumnWidth(0, 100)
        self.tableWidget_2.setColumnWidth(1, 170)
        #self.tableWidget_2.setColumnWidth(2, 150)
        self.tableWidget_2.setColumnWidth(3, 250)
        self.tableWidget_2.setColumnWidth(4, 150)
        self.tableWidget_2.setColumnWidth(5, 150)
        self.tableWidget_2.setColumnWidth(6, 150)
        self.tableWidget_2.setColumnWidth(7, 150)

        self.tableWidget_2.cellClicked.connect(self.cell_was_clicked)

    def table_column_sort(self, p_row) :
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setSortingEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
