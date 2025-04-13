import pystray
from pystray import MenuItem as item
from PIL import Image
import yaml
import sys
import os, subprocess
from functools import partial

# ico
try:
    icon = Image.open('icon.ico')
except FileNotFoundError:
    print('icon.ico not found')
    sys.exit()
except:
    print('icon.ico error')
    sys.exit()

# config
try:
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
except FileNotFoundError:
    print('config.yaml not found')
    sys.exit()
except:
    print('config.yaml error')
    sys.exit()

def cb(i,icon,menuitem):
    subprocess.Popen(i['cmd'])
    
def call_exit():
    icon.stop()
    sys.exit()
def open_settings():
    os.startfile('config.yaml')

# menu&icon
menu = []
for i in config:
    menu.append(item(i['name'], partial(cb, i)))
menu.append(pystray.Menu.SEPARATOR)
menu.append(item('Settings', open_settings))
menu.append(item('Exit', call_exit))
icon = pystray.Icon('TrayOpen', icon, "TrayOpen", menu)

icon.run()