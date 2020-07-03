import pyautogui as pg 
import keyboard as key 
import colorama#импорт ранее установлиного пакета
from colorama import init
init()
from colorama import Fore, Back, Style

print( Back.RED )
print("WARRING!: Starting clicker be careful!")
start_key = input('Please enter start key: ')
stop_key = input('Please enter stop key: ')
button_m = input('Please enter mouse button to click[Left/Right]: ')

while True:
	if key.is_pressed( start_key ):
		print( Back.RED )
		print("Starting!")
		pg.tripleClick( button = button_m )
	if key.is_pressed( stop_key ):
		print( Back.RED )
		print("Stoping")