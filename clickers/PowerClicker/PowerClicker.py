
import mouse#импорт библиотек
from time import sleep
import keyboard as key
import colorama#импорт ранее установлиного пакета
from colorama import init
init()
from colorama import Fore, Back, Style

#принемаем данные пользователя

true_f = True
start_key = input("Enter start key: ")
stop_key = input("Enter stop key: ")
click_button = input("Enter click button: ")



while True:#проверяем нажатие start_key
	if key.is_pressed( start_key ):
		print( Back.GREEN )
		print("WARRING: Starting clicker to start key!")
		if true_f == False:
			break
		while True:
			sleep(0.01)#кликаем
			mouse.double_click(button = click_button.lower())

			if key.is_pressed( stop_key ):
				print( Back.RED )
				print("WARRING: Stoping program to stop key!")
				true_f = False
				break 

