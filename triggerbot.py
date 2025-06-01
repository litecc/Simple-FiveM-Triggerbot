import random
import threading
import time
import pyautogui
import keyboard
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import os

version = "1.0.2"
running = True
alive = True
tray_icon = None

kill_script_keybind = "#"

x, y = pyautogui.size().width // 2, pyautogui.size().height // 2

def create_tray_icon():
    def create_image(color):
        image = Image.new("RGB", (64, 64), color)
        draw = ImageDraw.Draw(image)
        return image

    def update_icon():
        tray_icon.icon = create_image("green" if running else "red")

    def toggle_running(icon, item):
        global running
        running = not running
        update_icon()

    def exit_script(icon, item):
        kill_script()

    global tray_icon
    tray_icon = Icon("ProcessLasso", create_image("red"), "ProcessLasso",
                     menu=Menu(
                         MenuItem("ProcessLasso ??ffnen", toggle_running),
                         MenuItem("Beenden", exit_script)
                     ))
    update_icon()
    tray_icon.run()

def check():
    while alive:
        if running:
            try:
                red = pyautogui.pixel(x, y)[0]
                if 192 <= red <= 194:
                    pyautogui.mouseDown()
                    time.sleep(random.uniform(0.01, 0.02))
                    pyautogui.mouseUp()
            except Exception as e:
                print(f"Fehler bei der Farbpr??fung: {e}")
        time.sleep(0.01)

def setup_hotkeys():
    keyboard.add_hotkey(kill_script_keybind, kill_script)

def kill_script():
    global alive
    alive = False
    try:
        if tray_icon:
            tray_icon.stop()
    except Exception as e:
        print(f"Fehler beim Stoppen des Tray-Icons: {e}")
    print("Skript wird beendet...")

icon_thread = threading.Thread(target=create_tray_icon, daemon=True)
icon_thread.start()

check_thread = threading.Thread(target=check, daemon=True)
check_thread.start()

hotkey_thread = threading.Thread(target=setup_hotkeys, daemon=True)
hotkey_thread.start()

while alive:
    time.sleep(0.1)

#lite
