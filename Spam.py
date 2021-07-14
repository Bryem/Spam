from pyfade import Fade
from pyfade import Colors
from pycenter import center
from os import name, system
import pyautogui, time
if name == 'nt':
    system("title SPAM TOOLS")

Spam = """
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░  ░  ░  ░░         ░   ▒   ░      ░        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
      ░                 ░  ░       ░                   ░ ░      ░ ░      ░  ░      ░  
                                                                                                                                                                                                                                                        
"""

Spam = center(Spam, 15)

print(Fade.Vertical(Colors.white_to_black, Spam))

while True:
  message = input("Quel mot/phrase voulez vous spam ? > ")
  nombre = input("Combine de fois voulez vous spam ? > ")
  attente = input("Temps d'attente entre les spams (en seconde) >")

  print("Le spam se lance dans 10 secondes")
  time.sleep(10)

  for i in range(0, int(nombre)):
    pyautogui.write(message)
    pyautogui.press('ENTER')
    time.sleep(int(attente))


  print()
  print("Spam effectué")
  print()
