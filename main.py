import psi.process
from colorama import init, Fore, Style
import subprocess
from rich.traceback import install
import shutil

install()
init(autoreset=True)
#TG_Bot_Max

# Список процессов, которые вы хотите отслеживать
processes = {"TM_thedeaddan", "TM_Mini", "TM_Grisha", "VK_Delete", "TG_Bot_Curs", "Server_Stat", "Log_Server"}

# Функция для проверки температуры
def check_temp():
    temp = str(subprocess.check_output('vcgencmd measure_temp', shell=True)).split('"')[1].split("=")[1][:-4]
    float_temp = int(float(temp))

    # Цветовая карта для разных диапазонов температур
    color_map = {
        range(0, 38): Fore.CYAN,
        range(38, 45): Style.BRIGHT + Fore.GREEN,
        range(45, 55): Style.BRIGHT + Fore.YELLOW,
        range(55, 65): Style.BRIGHT + Fore.RED,
        range(65, 100): Fore.RED
    }

    for temp_range, color in color_map.items():
        if float_temp in temp_range:
            return [color, temp]
    return [Fore.RED, f"!!! {temp} !!!"]

# Функция для генерации строки с отображением температуры
def generate_temp_space():
    color = check_temp()[0]
    space = "[" + "".join([color + "=" + Style.RESET_ALL for _ in range(35)]) + "]"
    return space

# Функция для генерации строки с отображением статуса ботов
def generate_space(bot, status):
    space_len = 20 - len(bot)
    color = Fore.GREEN if status else Fore.RED
    space = "".join([Style.BRIGHT + (color if i % 2 == 0 else Style.RESET_ALL) + "-" + Style.RESET_ALL for i in range(space_len)])
    return space

# Функция для вывода информации о температуре
def print_temp():
    print(f"Температура = {check_temp()[0]}{check_temp()[1]}°C")

# Функция для проверки состояния процессов
def check_process():
    process_table = psi.process.ProcessTable().values()
    for p in process_table:
        for bot in list(processes):
            if bot in p.command:
                processes.remove(bot)
                print(f"{Style.BRIGHT}{bot} {generate_space(bot, True)} {Style.BRIGHT + Fore.GREEN}Работает[{p.pid}]")
    for bot in processes:
        print(f"{Style.BRIGHT}{bot} {generate_space(bot, False)} {Style.BRIGHT + Fore.RED}Не работает[---]")

# Функция для вывода информации о использовании диска
def print_disk_usage():
    drives = [("/", "M2"), ("/media/driveone", "HDD")]

    for drive, name in drives:
        total, used, free = shutil.disk_usage(drive)
        total_gb = round(total / (1024**3), 2)
        used_gb = round(used / (1024**3), 2)
        free_gb = round(free / (1024**3), 2)

        usage_percent = int((used / total) * 100)
        usage_bar = "[" + "=" * (usage_percent // 5) + " " * ((100 - usage_percent) // 5) + "]"

        print(f"{Style.BRIGHT}{name}: {usage_bar}\n{used_gb} GB/{total_gb} GB ({free_gb} GB)")

# Генерация строки для отображения температуры
temp_space = generate_temp_space()
print(f"{temp_space}")
print_temp()
print(f"{temp_space}")

# Проверка состояния процессов
check_process()
print(f"{temp_space}")

# Вывод информации о использовании диска
print_disk_usage()
print(f"{temp_space}")
