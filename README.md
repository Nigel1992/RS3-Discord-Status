# RuneScape 3 Discord Rich Presence Integration

![image](https://github.com/Nigel1992/RS3-Discord-Status/assets/5491930/de469f47-c284-40db-b5a9-95e9d44e117e)


This Python script allows you to display your RuneScape 3 activities on your Discord profile using Rich Presence. It monitors a specific region of your screen for in-game images and updates your Discord status accordingly.

## Prerequisites

1. **Python 3.x** installed on your system.
2. A **Discord account** and a registered application with a **client ID**. [https://discord.com/developers/applications]

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

    ```bash
    pip install pyautogui pypresence
    ```

3. Replace `'REPLACEWITHYOURCLIENTID'` in the script with your actual Discord application's client ID.

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. The script will monitor the specified region of your screen for the images you've added.
3. When an image is detected, it will update your Discord Rich Presence status with the relevant activity name and a timer.

## Customization

- Adjust the `region` variable in the script to match the coordinates of the area where you expect the RuneScape 3 activity images to appear.
- Update the `emoji_map` dictionary with the appropriate emoji and activity names for your images.

## Notes

- Make sure your Discord application is running while using this script.
- You can customize the large image key (e.g., `'rslogo'`) to match your Discord assets.
- See: https://discord.com/developers/applications/YOURAPPID/rich-presence/assets]

Feel free to modify and enhance this script according to your needs! 😊
