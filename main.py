import psi.process 
from colorama import init, Fore
import subprocess
init(autoreset=True) #init colorama 

strandtest = False #Setting the variable to a false value
besed = False # Setting the variable to a false value
twitchmine = False #Setting the variable to a false value
onlinecheck = False # Setting the variable to a false value

low_temp = 45 # Operating temperature threshold
average_temp = 55 # Threshold of elevated temperature
high_temp = 60 # Very high temperature threshold

temp = str(subprocess.check_output('vcgencmd measure_temp', shell=True)).split('"')[1].split("=")[1][:-4]
float_temp = int(float(temp))
print("[===========================]")
if float_temp < low_temp: 
	print("Температура = "+Fore.GREEN+temp+"°C")
elif float_temp < average_temp:
	print("Температура = "+Fore.YELLOW+temp+"°C")
elif float_temp > high_temp:
	print("Температура = "+Fore.RED+temp+"°C")
print("[===========================]")

for p in psi.process.ProcessTable().values(): #Check process list
	if "strandtest.py" in p.command: # Name of ur 1 process
		strandtest = True
		strandtest_pid = str(p.pid) #Get PID
	if "besed.py" in p.command: # Name of ur 2 process
		besed = True
		besed_pid = str(p.pid)#Get PID
	if "SCREEN -d -m -S Twitch_Mining" in p.command: # Name of ur 3 process
		twitchmine = True
		twitchmine_pid = str(p.pid)#Get PID
	if "SCREEN -d -m -S onlinecheck" in p.command: # Name of ur 4 process
		onlinecheck = True
		onlinecheck_pid = str(p.pid)#Get PID
if strandtest:
	print("LED - Контроллер ------ "+Fore.GREEN+"OK"+" ["+strandtest_pid+"]") #if process active print OK and PID
else:
	print("LED - Контроллер ------ "+Fore.RED+"OШИБКА"+" [---]")# if process not active
if besed:
	print("Бот беседы ------------ "+Fore.GREEN+"OK"+" ["+besed_pid+"]")#if process active print OK and PID
else:
	print("Бот беседы ------------ "+Fore.RED+"OШИБКА"+" [---]")# if process not active
if twitchmine:
	print("Майнер твича ---------- "+Fore.GREEN+"OK"+" ["+twitchmine_pid+"]")#if process active print OK and PID
else:
	print("Майнер твича ---------- "+Fore.RED+"OШИБКА"+" [---]")# if process not active
if onlinecheck:
	print("Чекер онлайна --------- "+Fore.GREEN+"OK"+" ["+onlinecheck_pid+"]")#if process active print OK and PID
else:
	print("Чекер онлайна --------- "+Fore.RED+"OШИБКА"+" [---]")# if process not active
print("[===========================]")
