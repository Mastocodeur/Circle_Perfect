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
import time
import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Affichage de la version de Selenium utilisée
print("La version de selenium utilisée est la : ", selenium.__version__)

############################################

# Configuration des options de Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('useAutomationExtension', False)

# Initialisation du driver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://neal.fun/perfect-circle/")
print("\nJe suis connecté au site\n")

# Pause pour permettre le chargement de la page
time.sleep(3)

# Autorisation des cookies (si nécessaire)
bouton_autoriser = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
bouton_autoriser.click()

# Affichage de la taille de la fenêtre
print("Taille de votre fenêtre", pyautogui.size())
time.sleep(3)

# Déterminer le centre de la fenêtre
screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2

# Localiser et cliquer sur le bouton "go"
search_btn = driver.find_element(By.XPATH, "//button[@class='on']")
search_btn.click()

# Pause pour permettre le chargement de la nouvelle section
time.sleep(5)

# Définir les coordonnées de départ et le rayon du cercle
x_start, y_start = center_x, center_y
rayon = 200

# Maintenir le clic gauche enfoncé et effectuer un mouvement circulaire
pyautogui.mouseDown(x_start + rayon, y_start, button='left')

# Utiliser np.linspace pour une interpolation linéaire plus fluide
angles = np.linspace(0, 360, 36)  # Utiliser plus de points pour un cercle plus lisse
for angle in angles:
    x = x_start + rayon * np.cos(np.radians(angle))
    y = y_start + rayon * np.sin(np.radians(angle))
    pyautogui.moveTo(x, y, duration=0.01)  # Ajuster la durée pour contrôler la vitesse du mouvement

# Relâcher le clic gauche à la fin du tracé
pyautogui.mouseUp()

time.sleep(3)

score = driver.find_element(By.CSS_SELECTOR, 'p[data-v-a6c88336]')
# Récupérez le score de l'élément
text = score.text

percentage = ""
for part in text.split():
    if '%' in part:
        percentage = part
        break

# Ajouter une virgule avant le troisième chiffre
# Supposons que le pourcentage soit au format XX% ou XXX%
if len(percentage) >= 3 and percentage[-1] == '%':
    percentage = percentage[:-2] + ',' + percentage[2] + percentage[-1]
else:
    percentage = percentage

print(f"Nous avons atteint : {percentage}")
