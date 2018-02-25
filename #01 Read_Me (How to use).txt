		===============================================================
		|| 	BoB 6th Digital_Forensic 3rd Stage Assignment	     ||
		||							     ||
		||	    Category : Tech 	      No. 01		     ||	
		||							     ||
		||		     @Author : L3ad0xff 		     ||
		||							     ||
		||	      	   NTFS File System Parser		     ||
		||	          Folder Sturcture Analysis		     ||
		===============================================================

  모든 개발은 python3.6 환경에서 이루어졌다.
  아래 python code를 실행 시키기 위해서는 추가 모듈이 필요하다.

======================================= 환경설정 ================================================

  1. Window
	- Window환경에서 python3.6.4를 설치, 실행 경로 지정
	- cmd화면에서 pip install PyQt5을 실행 (PyQt5모듈 설치)
	- cmd화면에서 pip install PyQt5-tools 실행 (PyQt5-tools 모듈 설치)
	- cmd화면에서 pip install wmi 실행 (wmi 모듈 설치)	
	- cmd화면에서 pip install datetime 실행 (datetime 모듈 설치)	
	- cmd화면에서 pip install pytsk3 실행 (pytsk3 모듈 설치)
	- cmd화면에서 pip install pypiwin32 실행 (pypiwin32 모듈 설치)
		* 설치 오류 시, http://landinghub.visualstudio.com/visual-cpp-build-tools 에서
		  c++ 2015 tools 설치
		* net framework 4.5.1 이상 필요


======================================== 실행방법 ===============================================

  1. cmd를 관리자모드로 실행한다.
     - 실행 코드를 포함하여 입력 인자 argv가 총 3개 필요하다.

  2. pythoncode가 있는 경로로 이동 후, python NTFS_Printer.py를 실행한다.

  3. start를 눌러 현재 system 활성화 Disk를 확인 후, 분석할 Volume 명에 맞는 PhysicalDrive 명을 입력한다.
	* 대, 소문자를 꼭 구별하여 입력한다.

  4. 탐색할 폴더 경로를 입력 후 Search Button을 누른다.

  5. html로 저장할 경우, save to html Button을 누른 후, pythoncode를 실행한 경로에 html이 생성됨을 확인한다.













