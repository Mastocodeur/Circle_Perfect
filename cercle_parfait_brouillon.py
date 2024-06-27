# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:46:49 2023

@author: REMY
"""

### Importation des bibliothèques ###
import selenium
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time as time
import pyautogui

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from time import sleep
print("La version de selenium utilisé est la : ",selenium.__version__)
############################################


chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
#chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('useAutomationExtension', False)

# Connexion à Internet et au site #
#driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)
driver.get("https://neal.fun/perfect-circle/")
print("\n")
print("Je suis connecté au site")
print("\n")
time.sleep(3)
bouton_autoriser = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
bouton_autoriser.click()

print("Taille de votre fenêtre", pyautogui.size())
time.sleep(3)

# Déterminer le centre de la fenêtre
screen_width, screen_height = pyautogui.size()

# Calculer les coordonnées du milieu de l'écran
center_x = screen_width // 2
center_y = screen_height // 2


# On va ensuite déterminer les coordonnées du point centrale avec la commande :
#pyautogui.displayMousePosition()

#x_start = int(input())
#y_start = int(input())
#rayon = int(input())
#On appuie sur le bouton "go" en localisant via le xpath
search_btn = driver.find_element(By.XPATH, "//button[@class='on']")
search_btn.click()


time.sleep(5)
# On obtient : 
# Plus on augmente les x, plus on va à droite, plus on augmente le y plus on descend
#x_start, y_start = 536, 402
x_start, y_start = center_x, center_y 
# Définissons le rayon du cercle
rayon = 200

# Maintenez le clic gauche enfoncé et effectuez un mouvement circulaire :
pyautogui.mouseDown(x_start+rayon, y_start, button='left')
#for angle in range(0,365, 4):
for angle in np.linspace(0,365,12):
#for angle in np.linspace(0, int(2*np.pi), 18):
    x = x_start  + rayon*np.cos(np.radians(angle))
    y = y_start  + rayon*np.sin(np.radians(angle))
    pyautogui.moveTo(x, y, duration=-10)  # Vous pouvez ajuster la durée pour contrôler la vitesse du mouvement
    pyautogui.moveTo(x, y, 0.1, pyautogui.easeInElastic)
    #time.sleep(0.01)  # Ajoutez une petite pause pour ralentir le mouvement (facultatif)
pyautogui.mouseUp(x_start+rayon, y_start+rayon, button='left')

print("J'ai réussi ! A nous le 100% ")


# A noter que si ma souris est en dehors de l'écran chrome, le robot ne fait rien.
# Score max atteint 99.5% (rayon = 240 et 4 points)
# 99.6% avec rayon = 231 et 4 points