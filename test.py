import pyautogui
import time
import pyperclip
# import get_mouse_live as count

main_sec = "كغ"
secondary_sec = "كيس"


# Copy to clipboard
# pyperclip.copy(arabic_text)

# Give some time to switch to the target window
# time.sleep(3)

# Paste using Ctrl+V

# LOL = pyautogui.hotkey('ctrl', 'v')
def automate_task():
    
    time.sleep(1)  # Wait so you can focus the right window
    # x, y = 845, 510  # Coordinates of the pixel to click
    pyautogui.moveTo(849, 510, duration=0.5)
    pyautogui.click()
    pyautogui.click()
    pyperclip.copy(main_sec)
    # pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    print(f'{ pyautogui.position()}')
    time.sleep(0.5)
    pyautogui.moveTo(942, 380, duration=0.3)
    pyautogui.click()
    print(f'{ pyautogui.position()}')
    pyperclip.copy(secondary_sec)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.write('25')
    time.sleep(0.5)
    pyautogui.moveTo(829, 254, duration=0.3)
    pyautogui.click()
    time.sleep(0.5)
    # pyautogui.moveTo(1026, 552, duration=0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('enter')



# count.click_count

# if __name__ == "__main__":
for i in range(59):
    automate_task()

print(automate_task)


# import pyautogui
# import time

# # Give some time to switch to the target window

# # Coordinates of the area to check
# x, y = 500, 400

# # Get pixel color
# pixel_color = pyautogui.screenshot().getpixel((x, y))
# print(f"Color at ({x}, {y}): {pixel_color}")

# # Compare with expected color (RGB)
# if pixel_color == (255, 0, 0):  # red, for example
#     pyautogui.move(x,y)
#     pyautogui.click(x, y)  # Click if match
#     print("Clicked!")
# else:
    # pyautogui.move(x,y)
    # pyautogui.position()
    # print(f'{ pyautogui.position()}')
    # print("No action taken.")
