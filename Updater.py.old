import tkinter as tk
import pyautogui
import time
import threading
import os
from pypresence import Presence

# Initialize Discord Rich Presence client
RPC = Presence(client_id='REPLACEWITHYOURCLIENTID')
RPC.connect()

previous_image_name = None
start_time = None

# Map image names to emojis
emoji_map = {
    "agility": ("Agility", "🏃"),
    "construction": ("Construction", "👷"),
    "cooking": ("Cooking", "🍯"),
    "farming": ("Farming", "🚜"),
    "firemaking": ("Firemaking", "🔥"),
    "fishing": ("Fishing", "🎣"),
    "herblore": ("Herblore", "🍀"),
    "hunter": ("Hunter", "🐾"),
    "invention": ("Invention", "💡"),
    "magic": ("Magic", "🧙‍"),
    "mining": ("Mining", "⛏️‍"),
    "necromancy": ("Necromancy", "💀‍"),
    "prayer": ("Prayer", "✨‍"),
    "ranged": ("Ranged", "🏹‍"),
    "runecrafting": ("Runecrafting", "🔮‍"),
    "strength": ("Strength", "✊‍"),
    "woodcutting": ("Woodcutting", "🌳‍"),
}

def format_filename(filename):
    filename_without_extension = os.path.splitext(filename)[0]
    capitalized_filename = filename_without_extension.capitalize()
    return capitalized_filename

def find_image_location(image_folder, region):
    for filename in os.listdir(image_folder):
        if filename.endswith('.png'):
            image_path = os.path.join(image_folder, filename)
            try:
                location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8, region=region)
                if location is not None:
                    formatted_filename = format_filename(filename)
                    return location.x, location.y, formatted_filename, filename  # Returning formatted filename and original filename
            except pyautogui.ImageNotFoundException:
                continue
    return None, None, None, None  # Return None for location and filename if no image found

def update_discord_status(image_name, large_image_key, timer):
    # Format timer to hours, minutes, and seconds
    hours = timer // 3600
    minutes = (timer % 3600) // 60
    seconds = timer % 60
    time_str = f"{hours}h {minutes}m"

    # Get emoji and name based on the image name
    emoji_name, emoji = emoji_map.get(image_name.lower(), (image_name, ""))

    # Update Discord Rich Presence status
    RPC.update(state=f"for {time_str}, but who's counting?", details=f"Training {emoji_name} {emoji}", large_image=large_image_key)

def update_presence(image_folder, region, large_image_key):
    global previous_image_name
    global start_time
    while True:
        timer = int(time.time() - start_time) if start_time else 0
        x, y, image_name, image_filename = find_image_location(image_folder, region)  # Retrieve image name
        if x is not None and y is not None:
            if image_name != previous_image_name:
                previous_image_name = image_name
                start_time = time.time()  # Reset timer
            update_discord_status(image_name, large_image_key, timer)  # Update Discord status with timer
        time.sleep(1)  # Update every second

def main():
    global start_time
    image_folder = os.path.join(os.getcwd(), 'images')  # Set image folder to 'images' in current directory
    region = (924, 21, 996 - 924, 78 - 21)  # Define the region coordinates
    large_image_key = 'rslogo'  # Replace with the name of the large image asset in Discord

    start_time = time.time()  # Start time when the program begins

    # Start a thread to update the Discord Rich Presence
    presence_thread = threading.Thread(target=update_presence, args=(image_folder, region, large_image_key), daemon=True)
    presence_thread.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
