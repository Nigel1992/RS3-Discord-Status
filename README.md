# RuneScape 3 Discord Rich Presence Integration
[made with help from AI]

![image](https://github.com/Nigel1992/RS3-Discord-Status/assets/5491930/de469f47-c284-40db-b5a9-95e9d44e117e)


This Python script allows you to display your RuneScape 3 activities on your Discord profile using Rich Presence.  
It monitors a specific region of your screen for in-game images and updates your Discord status accordingly.  
![image](https://github.com/Nigel1992/RS3-Discord-Status/assets/5491930/af29c507-66f6-4367-9f66-e40b30d6cae7)


## Prerequisites

1. **Python 3.x** installed on your system.
2. A **Discord account** and a registered application with a **client ID**. [see spoiler for details]

<details>
  <summary>How-to</summary>
  
**Adding Discord Developer Assets**
1. Go to the Discord Developer Portal.
2. Create a new application or select an existing one.
3. Navigate to the “Rich Presence” tab.
4. Scroll down to the “Assets” section.
5. Click on “Add Image(s)” to upload your custom images (these can be icons, logos, or other graphics)
   (this will be your Logo below "Playing a game").
7. You’ll need to provide a name for each asset. This name will be used when referencing the asset in your code.
8. After uploading, you’ll see your assets listed under “Rich Presence Assets” on the same page.

**Using Your Assets in Code**
In your Python script (or any other language), use the asset names you provided in the developer portal.
  
</details>

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
- See: https://discord.com/developers/applications/YOURAPPID/rich-presence/assets

Feel free to modify and enhance this script according to your needs! 😊
