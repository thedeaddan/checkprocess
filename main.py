import psi.process 
from colorama import init, Fore
import psutil
init(autoreset=True) #init colorama 

strandtest = False #Setting the variable to a false value
besed = False # Setting the variable to a false value
twitchmine = False #Setting the variable to a false value
onlinecheck = False # Setting the variable to a false value

low_temp = 45 # Operating temperature threshold
average_temp = 55 # Threshold of elevated temperature
high_temp = 60 # Very high temperature threshold

temp = str(psutil.sensors_temperatures().get("cpu_thermal")[0]).split(",")[1].replace(" current=","")[:-2] # Get current temp in str
float_temp = float(str(psutil.sensors_temperatures().get("cpu_thermal")[0]).split(",")[1].replace(" current=","")[:-2]) # We get the current temperature for comparison
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
	if "besed.py" in p.command: # Name of ur 2 process
		besed = True
	if "SCREEN -d -m -S Twitch_Mining" in p.command: # Name of ur 3 process
		twitchmine = True
	if "SCREEN -d -m -S onlinecheck" in p.command: # Name of ur 4 process
		onlinecheck = True

if strandtest:
	print("LED - Контроллер ------ "+Fore.GREEN+"OK") #if process active
else:
	print("LED - Контроллер ------ "+Fore.RED+"OШИБКА")# if process not active
if besed:
	print("Бот беседы ------------ "+Fore.GREEN+"OK")#if process active
else:
	print("Бот беседы ------------ "+Fore.RED+"OШИБКА")# if process not active
if twitchmine:
	print("Майнер твича ---------- "+Fore.GREEN+"OK")#if process active
else:
	print("Майнер твича ---------- "+Fore.RED+"OШИБКА")# if process not active
if onlinecheck:
	print("Чекер онлайна --------- "+Fore.GREEN+"OK")#if process active
else:
	print("Чекер онлайна --------- "+Fore.RED+"OШИБКА")# if process not active
print("[===========================]")
