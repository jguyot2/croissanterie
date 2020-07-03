import subprocess
import os
import random
import time
random.seed(time.time())           
path_image = "/home/jguyot2/lock/imgs/"
image_name = "lock_screen.png"

image_path = path_image + image_name
commande_screenshot = ["scrot", "-z", image_path]
commande = ["i3lock", "-u", "-pwin", "-i", image_path]
subprocess.run(commande_screenshot)
time.sleep(1)
subprocess.run(commande)

