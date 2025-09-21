# import pyautogui
# import time
# import pyperclip
# # import get_mouse_live as count

# main_sec = "كغ"
# secondary_sec = "كيس"


# # Copy to clipboard
# # pyperclip.copy(arabic_text)

# # Give some time to switch to the target window
# # time.sleep(3)

# # Paste using Ctrl+V

# # LOL = pyautogui.hotkey('ctrl', 'v')
# def automate_task():
    
#     time.sleep(1)  # Wait so you can focus the right window
#     # x, y = 845, 510  # Coordinates of the pixel to click
#     pyautogui.moveTo(849, 510, duration=0.5)
#     pyautogui.click()
#     pyautogui.click()
#     pyperclip.copy(main_sec)
#     # pyautogui.click()
#     time.sleep(0.5)
#     pyautogui.hotkey('ctrl', 'v')
#     print(f'{ pyautogui.position()}')
#     time.sleep(0.5)
#     pyautogui.moveTo(942, 380, duration=0.3)
#     pyautogui.click()
#     print(f'{ pyautogui.position()}')
#     pyperclip.copy(secondary_sec)
#     pyautogui.hotkey('ctrl', 'v')
#     time.sleep(0.5)
#     pyautogui.press('enter')
#     pyautogui.write('25')
#     time.sleep(0.5)
#     pyautogui.moveTo(829, 254, duration=0.3)
#     pyautogui.click()
#     time.sleep(0.5)
#     # pyautogui.moveTo(1026, 552, duration=0.3)
#     pyautogui.press('enter')
#     time.sleep(0.3)
#     pyautogui.press('enter')



# # count.click_count

# # if __name__ == "__main__":
# for i in range(59):
#     automate_task()

# print(automate_task)


# # import pyautogui
# # import time

# # # Give some time to switch to the target window

# # # Coordinates of the area to check
# # x, y = 500, 400

# # # Get pixel color
# # pixel_color = pyautogui.screenshot().getpixel((x, y))
# # print(f"Color at ({x}, {y}): {pixel_color}")

# # # Compare with expected color (RGB)
# # if pixel_color == (255, 0, 0):  # red, for example
# #     pyautogui.move(x,y)
# #     pyautogui.click(x, y)  # Click if match
# #     print("Clicked!")
# # else:
#     # pyautogui.move(x,y)
#     # pyautogui.position()
#     # print(f'{ pyautogui.position()}')
#     # print("No action taken.")
import tkinter as tk
import threading as th
import time

root = tk.Tk()
root.geometry("300x150")

status_label = tk.Label(root, text="Starting...")
status_label1 = tk.Label(root, text="f...")
status_label.pack(pady=20)
status_label1.pack(pady=3)

stoping = th.Event()
k = 0

def update_label():
    # Toggle start/stop
    if stoping.is_set():
        stoping.clear()
        status_label1.config(text="Stopped")
    else:
        stoping.set()
        status_label1.config(text="Counting...")

def update_label1():
    global k
    while True:  # keep thread alive
        if stoping.is_set():
            k += 1
            root.after(0, lambda val=k: status_label.config(text=f"Count: {val}"))
        time.sleep(1)

tk.Button(root, text="Start/Stop Counting",
          command=lambda: th.Thread(target=update_label, daemon=True).start()
).pack(pady=5)

# Start background counting thread
th.Thread(target=update_label1, daemon=True).start()

root.mainloop()



# import tkinter 
# from tkinter import messagebox
# from tkinter import filedialog

# main_win = tkinter.Tk()
# main_win.geometry("1000x500")
# main_win.sourceFolder = ''
# main_win.sourceFile = ''
# def chooseDir():
#     main_win.sourceFolder =  filedialog.askdirectory(parent=main_win, initialdir= "/", title='Please select a directory')

# b_chooseDir = tkinter.Button(main_win, text = "Chose Folder", width = 20, height = 3, command = chooseDir)
# b_chooseDir.place(x = 50,y = 50)
# b_chooseDir.width = 100


# def chooseFile():
#     main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a directory')

# b_chooseFile = tkinter.Button(main_win, text = "Chose File", width = 20, height = 3, command = chooseFile)
# b_chooseFile.place(x = 250,y = 50)
# b_chooseFile.width = 100

# main_win.mainloop()
# print(main_win.sourceFolder)
# print(main_win.sourceFile )

