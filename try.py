import requests
import os

name = "sound_control.dmg"
URL = "https://staticz.com/download/4297/"

response = requests.get(URL)
open(name, "wb").write(response.content)
os.system(f"sudo hdiutil attach {name}")
os.system("sudo cp -a /Volumes/Sound\ Control/Sound\ Control.app /Applications/")
os.system("sudo hdiutil detach /Volumes/Sound\ Control")
os.system(f"sudo rm {name}")