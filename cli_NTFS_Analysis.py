#!/usr/bin/python
# -*- coding : utf-8 -*-
# -*- coding : cp949 -*-

# @Author L3ad0xFF

import pytsk3
import sys
import os
from struct import *
import datetime
import time
import wmi

#Volumename = sys.argv[1]

def maplogic_physic() :
	global phylogset
	phylogset = {}
	w = wmi.WMI()
	drivenum = 0
	print ("==============Drive_info=============")
	for drive in w.Win32_LogicalDisk() :
		print ("\t"+ drive.Caption + " = PhysicalDrive" + str(drivenum))
		phylogset['PhysicalDrive'+str(drivenum)] = drive.Caption
		drivenum += 1

def partitionsize (num) :
	size_list = ['B', 'MB', 'KB', 'GB']
	size = num * 512.

	for div_count in range (0, 4) :
		if int(size) > 0 :
			size = size / 1024
		else :
			break
		
	return '%.2f %s' % (size *1024, size_list[div_count])

def searchPartition (PartitionTables) :
	ntfs_list = list()
	for partition in PartitionTables:
		if partition.desc == b'NTFS / exFAT (0x07)' :
			print ("\n[+] Type               : %s" % partition.desc.decode('utf-8'))
			print ("\t[-] Number         : %d" % partition.start)
			print ("\t[-] Start Sector   : %d" % partition.start)
			print ("\t[-] Sector Count   : %d" % partition.len)
			print ("\t[-] Size           : " + partitionsize(partition.len))
			ntfs_list.append(partition.start)
	return ntfs_list

def find_directory(vbr_offset) :
	global in_path_list
	fs = pytsk3.FS_Info(Volume_img, offset = vbr_offset)
	while True : 
		in_path_list = list()
		print ("\nInput Path for Search (ex. /) ")
		set_path = input("  => If you Want Quit, Input the 'q' or 'Q' : ")

		if (set_path == 'q') or (set_path == 'Q') :
			break
		else :
			directorys = fs.open_dir(path = set_path)
			count = 0
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
						dir_size = directory.info.meta.size
						count += 1
						dir_list = [count, dir_type, dir_name, dir_size, dir_path, dir_mtime, dir_atime, dir_ctime, dir_ectime]
						in_path_list.append(dir_list)

						print ("\n[+] Dir : %s" % dir_name)
						#print ("\t[-] Dir Entry Address : %d" % dir_EA)
						print ("\t[-] Path : %s" % dir_path)
						print ("\t[-] Dir modification_time : %s" % dir_mtime)
						print ("\t[-] Dir access_time : %s" % dir_atime)
						print ("\t[-] Dir create_time : %s" % dir_ctime)
						print ("\t[-] Dir entry_change_time : %s" % dir_ectime)
						print ("\t[-] Dir Size :  % d " % dir_size)

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
						file_size = directory.info.meta.size
						count += 1
						file_list = [count, file_type, file_name, file_size, file_path, file_mtime, file_atime, file_ctime, file_ectime]
						in_path_list.append(file_list)

						print ("\n[+] File : %s" % file_name)
						#print ("\t[-] File Entry Address : %d" % file_EA)
						print ("\t[-] Path : %s" % file_path)
						print ("\t[-] File modification_time : %s" % file_mtime)
						print ("\t[-] File access_time : %s" % file_atime)
						print ("\t[-] File create_time : %s" % file_ctime)
						print ("\t[-] File entry_change_time : %s" % file_ectime)
						print ("\t[-] File Size : %d Bytes" % file_size)
				except :
					pass
			print ("\n")
			print (in_path_list)	
				#	print ((directory.info.name.name).decode('utf-8'))

if __name__ == '__main__' :
	global disk, disk_data, Volume_img, root_path
	maplogic_physic()
	drive_no = input("\ninput Physical Drive (ex. PhysicalDrive0) : ")
	root_path = phylogset[drive_no]
	set_Volume        = "\\\\.\\"+drive_no
	Volume_img    = pytsk3.Img_Info(set_Volume)
	PartitionTables = pytsk3.Volume_Info(Volume_img)
	ntfs_sector = searchPartition(PartitionTables)
	#print (ntfs_sector)
	disk = open(set_Volume, 'rb')
	for sector_no in ntfs_sector :
		vbr_offset = sector_no * 512
		find_directory(vbr_offset)

	print ("\nfinish!")
