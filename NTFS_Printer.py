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
        self.label_3.setGeometry(QtCore.QRect(311, 111, 151, 61))
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
        self.label_2.setGeometry(QtCore.QRect(319, 23, 261, 61))
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
        self.pushbutton.setGeometry(QtCore.QRect(1210, 50, 131, 61))
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
        self.pushbutton_2.setGeometry(QtCore.QRect(1210, 140, 131, 61))
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
        self.tableWidget.setGeometry(QtCore.QRect(32, 84, 251, 111))
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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "System Drive state"))
        self.label_3.setText(_translate("Dialog", "Input_Path"))
        self.label_2.setText(_translate("Dialog", "Input Physical Drive Name"))
        self.pushbutton.setText(_translate("Dialog", "Search"))
        self.label_4.setText(_translate("Dialog", "Dir & File List"))
        self.pushbutton_2.setText(_translate("Dialog", "Show html"))
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

                # print ("\n[+] Type               : %s" % partition.desc.decode('utf-8'))
                # print ("\t[-] Number         : %d" % partition.start)
                # print ("\t[-] Start Sector   : %d" % partition.start)
                # print ("\t[-] Sector Count   : %d" % partition.len)
                # print ("\t[-] Size           : " + self.partitionsize(partition.len))
                ntfs_list.append(partition.start)
        self.textBrowser.setText(par_type + par_number + par_start_sec + par_sec_cnt + par_size)
        return ntfs_list

    def start(self) :
        global disk, Volume_img, root_path
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
        global in_path_list
        fs = pytsk3.FS_Info(Volume_img, offset = vbr_offset)
        # while True : 
        in_path_list = list()
        # print ("\nInput Path for Search (ex. /) ")
        # set_path = input("  => If you Want Quit, Input the 'q' or 'Q' : ")
        set_path = self.lineEdit_2.text()

        # if (set_path == 'q') or (set_path == 'Q') :
        #     break
        # else :
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
                    dir_path = root_path + set_path + "/" + ((directory.info.name.name).decode('utf-8'))
                    dir_mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.mtime))
                    dir_atime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.atime))
                    dir_ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.crtime))
                    dir_ectime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.ctime))
                    dir_size = str(directory.info.meta.size) + " Bytes"
                    #count += 1
                    dir_list = [dir_type, dir_name, dir_size, dir_path, dir_mtime, dir_atime, dir_ctime, dir_ectime]
                    in_path_list.append(dir_list)

                    # print ("\n[+] Dir : %s" % dir_name)
                    # #print ("\t[-] Dir Entry Address : %d" % dir_EA)
                    # print ("\t[-] Path : %s" % dir_path)
                    # print ("\t[-] Dir modification_time : %s" % dir_mtime)
                    # print ("\t[-] Dir access_time : %s" % dir_atime)
                    # print ("\t[-] Dir create_time : %s" % dir_ctime)
                    # print ("\t[-] Dir entry_change_time : %s" % dir_ectime)
                    # print ("\t[-] Dir Size :  % d " % dir_size)

                else:
                    file_list = list()
                    file_name = (directory.info.name.name).decode('utf-8')
                    file_type = "File"
                    #file_EA = directory.info.meta.addr
                    file_path = root_path + set_path + "/" + ((directory.info.name.name).decode('utf-8'))
                    file_mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.mtime))
                    file_atime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.atime))
                    file_ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.crtime))
                    file_ectime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(directory.info.meta.ctime))
                    file_size = str(directory.info.meta.size) + " Bytes"
                    #count += 1
                    file_list = [file_type, file_name, file_size, file_path, file_mtime, file_atime, file_ctime, file_ectime]
                    in_path_list.append(file_list)

                    # print ("\n[+] File : %s" % file_name)
                    # #print ("\t[-] File Entry Address : %d" % file_EA)
                    # print ("\t[-] Path : %s" % file_path)
                    # print ("\t[-] File modification_time : %s" % file_mtime)
                    # print ("\t[-] File access_time : %s" % file_atime)
                    # print ("\t[-] File create_time : %s" % file_ctime)
                    # print ("\t[-] File entry_change_time : %s" % file_ectime)
                    # print ("\t[-] File Size : %d Bytes" % file_size)
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
        # self.tableWidget_2.resizeColumnsToContents(2)

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
