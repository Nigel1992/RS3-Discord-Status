import tkinter as tk
from tkinter import ttk, Entry, messagebox
import pyautogui
import time
import threading
import os
from pypresence import Presence
import json

# Global variables
image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')  # Example path relative to the executable
region = (924, 21, 996 - 924, 78 - 21)  # Define the region coordinates
settings_file = "settings.json"  # Settings file path
client_id = ''  # Default client_id
large_image_key = ''  # Default large_image_key
RPC = None
previous_image_name = None
start_time = None
running = False
update_interval = 1  # Update interval in seconds

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

# Function to format filename
def format_filename(filename):
    filename_without_extension = os.path.splitext(filename)[0]
    capitalized_filename = filename_without_extension.capitalize()
    return capitalized_filename

# Function to find image location
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

# Function to update Discord status
def update_discord_status(image_name, large_image_key, timer):
    # Format timer to hours, minutes, and seconds
    hours = timer // 3600
    minutes = (timer % 3600) // 60
    seconds = timer % 60
    time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

    # Get emoji and name based on the image name
    emoji_name, emoji = emoji_map.get(image_name.lower(), (image_name, ""))

    # Update Discord Rich Presence status
    if RPC:
        RPC.update(state=f"Playing for {time_str}", details=f"Training {emoji_name} {emoji}", large_image=large_image_key)

# Function to update presence continuously
def update_presence():
    global previous_image_name, start_time, running

    while running:
        timer = int(time.time() - start_time) if start_time else 0
        x, y, image_name, image_filename = find_image_location(image_folder, region)  # Retrieve image name
        if x is not None and y is not None:
            if image_name != previous_image_name:
                previous_image_name = image_name
                start_time = time.time()  # Reset timer
            update_discord_status(image_name, large_image_key, timer)  # Update Discord status with timer
            
        time.sleep(update_interval)  # Update every second

# Function to start updating presence and save settings
def start_update(client_id_entry, large_image_key_entry):
    global running, start_time, RPC, client_id, large_image_key

    client_id = client_id_entry.get().strip()  # Get client_id from entry
    large_image_key = large_image_key_entry.get().strip()  # Get large_image_key from entry

    if not client_id:
        messagebox.showerror("Error", "Please enter a valid Client ID!")
        return

    if RPC is None:
        RPC = Presence(client_id=client_id)
        RPC.connect()

    # Save settings to JSON file
    save_settings()

    if not running:
        running = True
        start_time = time.time()
        # Start a thread to update the Discord Rich Presence
        presence_thread = threading.Thread(target=update_presence, daemon=True)
        presence_thread.start()

# Function to stop updating presence
def stop_update():
    global running
    running = False

# Function to save settings to JSON file
def save_settings():
    global client_id, large_image_key

    settings = {
        "client_id": client_id,
        "large_image_key": large_image_key
    }

    with open(settings_file, 'w') as f:
        json.dump(settings, f)

# Function to load settings from JSON file
def load_settings():
    global client_id, large_image_key

    try:
        with open(settings_file, 'r') as f:
            settings = json.load(f)
            client_id = settings.get("client_id", "")
            large_image_key = settings.get("large_image_key", "")
    except FileNotFoundError:
        # If settings file doesn't exist, create it with default values
        save_settings()

# GUI setup
def create_gui():
    root = tk.Tk()
    root.title("RuneScape Discord Rich Presence Updater")
    root.geometry("400x200")

    # Styling
    style = ttk.Style()

    # Configure TButton style for dark green
    style.configure('DarkGreen.TButton',
                    font=('Arial', 10, 'bold'),
                    foreground='white',
                    background='#4CAF50',  # Dark green background
                    padding=5)

    # Configure TLabel style
    style.configure('TLabel', 
                    font=('Arial', 12, 'bold'), 
                    foreground='white', 
                    background='#404040')  # Dark grey background for labels

    # Configure TFrame style
    style.configure('TFrame', 
                    background='#404040')  # Dark grey background for frames

    # Configure TEntry style
    style.configure('TEntry', 
                    background='white', 
                    foreground='black')  # Entry widgets

    # Load settings from JSON file
    load_settings()

    # Main frame
    main_frame = ttk.Frame(root, padding=(10, 10, 10, 10), style='TFrame')
    main_frame.pack(expand=True, fill=tk.BOTH)

    # Title label
    title_label = ttk.Label(main_frame, text="Discord Rich Presence Updater", style='TLabel')
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Client ID entry
    client_id_label = ttk.Label(main_frame, text="Enter your Discord Client ID:", style='TLabel')
    client_id_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')

    client_id_entry = ttk.Entry(main_frame, width=30)
    client_id_entry.grid(row=1, column=1, padx=10, pady=5)
    client_id_entry.insert(0, client_id)  # Set initial value

    # Large Image Key entry
    large_image_key_label = ttk.Label(main_frame, text="Enter Large Image Key:", style='TLabel')
    large_image_key_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')

    large_image_key_entry = ttk.Entry(main_frame, width=30)
    large_image_key_entry.grid(row=2, column=1, padx=10, pady=5)
    large_image_key_entry.insert(0, large_image_key)  # Set initial value

    # Start button
    start_button = ttk.Button(main_frame, text="Start", command=lambda: start_update(client_id_entry, large_image_key_entry), style='DarkGreen.TButton')
    start_button.grid(row=3, column=0, padx=10, pady=10)

    # Stop button
    stop_button = ttk.Button(main_frame, text="Stop", command=stop_update, style='TButton')
    stop_button.grid(row=3, column=1, padx=10, pady=10)

    # Set window to be non-resizable
    root.resizable(False, False)

    # Center the window
    window_width = 500
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')

    return root

def main():
    gui = create_gui()
    gui.mainloop()

if __name__ == '__main__':
    main()
