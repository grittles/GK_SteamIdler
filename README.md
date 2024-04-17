# GK_SteamIdler
Simple steam idler so I can give games bad reviews without installing them >:)

## Overview
The `Steam Game Idler` is a Python appl designed to interact with the Steam API to fetch and display game information, including the game's name and header image, using a Tkinter GUI. It demonstrates how to integrate the Steam API with a Python application, particularly for idling games to collect trading cards or simply display game details.

## Features
- Fetches game details using the Steam API.
- Displays game name and header image in a simple GUI.
- Initializes and interacts with Steamworks API via Python.

## Python Requirements
- Version 3.6 or higher.
- `PIL` (Pillow) for image handling.
- `Tkinter` for the GUI (usually comes with Python).
- Access to the internet to fetch data from the Steam API.
- steam_api.dll or steam_api64.dll

## Setup
Before running the script, you need to install Pillow, which can be done via pip:

```bash
pip install Pillow
```
## Usage
In console in the directory this script is located: python steam_game_idler.py <AppID>

## License
This project is open-sourced under the MIT license.

## Acknowledgments
- This project utilizes the Steamworks API to interact with Steam services.
- Images and game details are fetched using the public Steam Storefront API.
