import os
import sys
from ctypes import CDLL
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
import json

# ------------------------------------------------------------------------#
# Idle games like Overwatch so you can give them bad reviews!
# Maybe recreate this in JAVA or C++ in the future
# This is mainly an experiment to test importing DLLs in python
# ------------------------------------------------------------------------#

# ------------------------------------------------------------------------#
# Helper functions
# ------------------------------------------------------------------------#

# ------------------------------------------------------------------------#
# Get the API and init the game idling
# ------------------------------------------------------------------------#
def get_api_and_init_game(app_id):

    a = "64" if sys.maxsize > 2**32 else ""
    dll_file = f"steam_api{a}.dll"
    steamAPI = CDLL(os.path.join(os.getcwd(), dll_file))

    os.environ["SteamAppId"] = app_id

    if not steamAPI.SteamAPI_Init():
        raise Exception("Failed to initialize Steam API")

    return steamAPI

# ------------------------------------------------------------------------#
# get the data for the GUI, which is the name and the header URL
# ------------------------------------------------------------------------#
def get_game_details_and_image(app_id):

    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&l=english"

    with urlopen(url) as response:
        data = json.load(response)
        game_info = data[str(app_id)]

        if not game_info['success']:
            raise Exception("Failed to retrieve game data")

        return game_info['data']['name'], game_info['data']['header_image']

# ------------------------------------------------------------------------#
# retrieve the URL image
# ------------------------------------------------------------------------#
def fetch_image(url):
    with urlopen(url) as response:
        return Image.open(response)

# ------------------------------------------------------------------------#
# Create the GUI after starting idling
# ------------------------------------------------------------------------#
def setup_gui(app_id, game_name, image):
    gui = tk.Tk()

    gui.title(f"Idling {game_name if game_name else app_id}")

    tk_image = ImageTk.PhotoImage(image)

    gui.geometry(f"{image.width}x{image.height}")

    label = tk.Label(gui, text=f"Idling_{app_id}", image=tk_image)
    label.photo = tk_image
    label.pack()
    
    gui.mainloop()

# ------------------------------------------------------------------------#
# main
# ------------------------------------------------------------------------#
def main():
    if len(sys.argv) > 1:
        app_id = sys.argv[1]
    else:
        app_id = input("AppID: ")

    get_api_and_init_game(app_id)
    name, imgurl = get_game_details_and_image(app_id)
    img = fetch_image(imgurl)
    
    setup_gui(app_id, name, img)

main()
