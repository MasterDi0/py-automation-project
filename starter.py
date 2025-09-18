# # import tkinter as tk
# # from tkinter import simpledialog

# # root = tk.Tk()
# # root.withdraw()  # Hide the main window

# # user_input = simpledialog.askstring("Input", "Enter your name:")
# # age_input = simpledialog.askstring("Input", "Enter your age:")
# # loc_input = simpledialog.askstring("Input", "Enter your location:")

# # print("User entered:", user_input,' ',age_input,' ',loc_input)


# # import tkinter as tk

# # def on_submit():
# #     name = name_entry.get()
# #     age = target_word.get()
# #     city = targeted_word.get()
# #     print(f"Name: {name}, Age: {age}, City: {city}")
# #     root.destroy()

# # root = tk.Tk()
# # root.title("Multi Input Form")

# # tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
# # tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
# # tk.Label(root, text="City:").grid(row=2, column=0, padx=5, pady=5)

# # name_entry = tk.Entry(root)
# # age_entry = tk.Entry(root)
# # targeted_word = tk.Entry(root)

# # name_entry.grid(row=0, column=1, padx=5, pady=5)
# # age_entry.grid(row=1, column=1, padx=5, pady=5)
# # targeted_word.grid(row=2, column=1, padx=5, pady=5)

# # submit_btn = tk.Button(root, text="Submit", command=on_submit)
# # submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# # root.mainloop()



# import tkinter as tk

# def open_input_popup():
#     popup = tk.Toplevel(root)
#     popup.title("Enter Details")

#     tk.Label(popup, text="Name:").grid(row=0, column=0, padx=5, pady=5)
#     tk.Label(popup, text="Age:").grid(row=1, column=0, padx=5, pady=5)
#     tk.Label(popup, text="City:").grid(row=2, column=0, padx=5, pady=5)

#     name_entry = tk.Entry(popup)
#     age_entry = tk.Entry(popup)
#     targeted_word = tk.Entry(popup)

#     name_entry.grid(row=0, column=1, padx=5, pady=5)
#     age_entry.grid(row=1, column=1, padx=5, pady=5)
#     targeted_word.grid(row=2, column=1, padx=5, pady=5)

#     def submit():
#         name = name_entry.get()
#         age = age_entry.get()
#         city = targeted_word.get()
#         print(f"Name: {name}, Age: {age}, City: {city}")
#         popup.destroy()

#     submit_btn = tk.Button(popup, text="Submit", command=submit)
#     submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# # Main window
# root = tk.Tk()
# root.title("Main Window")

# main_button = tk.Button(root, text="Open Form", command=open_input_popup)
# main_button.pack(padx=20, pady=20)

# root.mainloop()

# import pyautogui
# import pytesseract
# from PIL import Image
# import time

# # Configure Tesseract OCR path
# pytesseract.pytesseract.tesseract_cmd = r"d:/New folder/tesseract.exe"
# ocr_lang = "ara"

# # Step 1: Pause to let user open the app
# print("⏳ You have 5 seconds to focus the app...")
# time.sleep(5)

# # Step 2: Take a screenshot of the 'الاسم' field
# # You may need to tweak this (x, y, width, height) to match the exact field
# field_region = (0, 0, 1920, 1080)  # Adjust if needed
# screenshot = pyautogui.screenshot(region=field_region)
# screenshot.save("name_field.png")

# # Step 3: OCR to extract text
# field_text = pytesseract.image_to_string(Image.open("name_field.png"), lang=ocr_lang).strip()
# print(f"🔍 Detected text: {field_text}")

# # Step 4: Check and replace
# if "صونده" in field_text:
    
#     corrected_text = field_text.replace("صونده", "صوندة")
#     print(f"✅ Typo found. Replacing with: {corrected_text}")

#     # Step 5: Click the 'الاسم' field and replace the text
#     pyautogui.click(x=screenshot., y=150)  # Coordinates inside the "الاسم" field
#     time.sleep(0.5)
#     pyautogui.hotkey("ctrl", "a")
#     time.sleep(0.2)
#     pyautogui.typewrite(corrected_text, interval=0.05)

# else:
#     print("✅ No typo found.")


# this for english detecting and clicking
# --------------------------------------------------------------------------------
# import pytesseract
# from pytesseract import Output
# import pyautogui
# import cv2
# import time
# pytesseract.pytesseract.tesseract_cmd = r"d:/New folder/tesseract.exe"
# # Take a screenshot
# print("⏳ You have 5 seconds to focus the app...")
# time.sleep(5)
# screenshot = pyautogui.screenshot()
# screenshot.save("screen.png")

# # Load it with OpenCV
# img = cv2.imread("screen.png")

# # Run OCR with bounding boxes
# data = pytesseract.image_to_data(img, output_type=Output.DICT)

# # Search for a word
# target = "Settings"  # the text you want to find
# for i, word in enumerate(data["text"]):
#     if word.strip().lower() == target.lower():
#         x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
        
#         # Move mouse to the center of the word
#         center_x = x + w // 2
#         center_y = y + h // 2
#         pyautogui.moveTo(center_x, center_y, duration=0.5)
#         print(f"Moved mouse to '{target}' at ({center_x}, {center_y})")
#         break
# ---------------------------------------------------------------------------------
import subprocess 
checking_req = subprocess.run(["pip", "check"  ])  # speed up pip commands
if checking_req.returncode !=0:  # if there are broken requirements, install them
    subprocess.run(["G:\py-automation-project\.venv\Scripts\python.exe" ,"-m","pip", "install", "-r", "requirements.txt", "--dry-run"])

import sys
# Install requirements before running the rest of the program
def install_requirements():
    try:
        try:
            import pkg_resources
        except ImportError:
            print("pkg_resources not found. Installing setuptools...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
            import pkg_resources
        with open("requirements.txt") as f:
            packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = [pkg.split('==')[0] for pkg in packages if pkg.split('==')[0].lower() not in installed]
        if missing:
            print(f"Installing missing packages: {missing}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except Exception as e:
        print(f"Error installing requirements: {e}")

install_requirements() 
   
import pytesseract
from pytesseract import Output
import pyautogui
import cv2
import time
import pyperclip
import tkinter as tk
import threading as th 

width, height = pyautogui.size()
print(f"Screen size: {width}x{height}")

global iters 
global target  
global targeted
global checking
checking = True
iters = 0
target   = ""  # word to search
targeted = ""
# --- GUI Setup ---
root = tk.Tk()
root.title("Click Counter")
root.geometry("250x300")


label = tk.Label(root, text="Press an option", font=("Arial", 16))
label_count = tk.Label(root,text="screen", font=("Arial", 14))
label_count.pack(pady=10)
label.pack(pady=20)

def open_input_form(checking):
    if checking==True:
        form = tk.Toplevel(root)
        form.title("Input Form")
        form.geometry("400x200")

        tk.Label(form, text="How many Iterations:").grid(row=0, column=0, padx=10, pady=5)
        iteractions = tk.Entry(form)
        iteractions.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form, text="The word i wanna replace:").grid(row=1, column=0, padx=10, pady=5)
        target_word = tk.Entry(form)
        target_word.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form, text="The word i wanna replace it with:").grid(row=2, column=0, padx=10, pady=5)
        targeted_word = tk.Entry(form)
        targeted_word.grid(row=2, column=1, padx=10, pady=5)

        def submit():
            iters = iteractions.get()
            target   = target_word.get()
            targeted = targeted_word.get()
            form.destroy()
            th.Thread(target=auto_click_and_replace,args=(int(iters),targeted,target),daemon=True).start()
            print(f"iters: {iters}, target: {target}, targeted: {targeted}")

            # for i in range(clicks-1):
            #     automate_task(main_sec=name, secondary_sec=city, number_of_sec=age)

        tk.Button(form, text="Submit", command=submit).grid(row=3, column=0, columnspan=2, pady=15)
    if checking == False:
        root.destroy()
        


# --- Update the label text ---
def update_label(text):
    label.config(text=text)
def update_label_count(text):
    label_count.config(text=text)

# target = "شوتة"  # word to search
# targeted_word = "شوته "
pytesseract.pytesseract.tesseract_cmd = r"g:/New folder/tesseract.exe"
ocr_lang = "ara"
def auto_click_and_replace( iteration,target, targeted_word):
    while iteration >0:
        print("⏳ You have 5 seconds to focus the app...")
        time.sleep(5)
        screenshot = pyautogui.screenshot()  # Adjust region as needed
        screenshot = pyautogui.screenshot(region=(1074, 263, 342, 30))  
        screenshot.save("screen.png")
        img = cv2.imread("screen.png")
        # OCR with Arabic
        data = pytesseract.image_to_data(img, lang="ara", output_type=Output.DICT)

        matches =[]
        # Collect all matches
        try: 
            for i, word in enumerate(data["text"]):
                if target in word:  # substring match (better for Arabic variations)
                    x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                    center_x = x + w // 2
                    center_y = y + h // 2
                    matches.append( (center_x, center_y, word))
                    print(f"Match found: {word} at ({center_x}, {center_y})")
        except Exception as e:
            print("Error during OCR processing:", e)   
        # print(matches[0])
        try:
            pyperclip.copy(targeted_word)
            pyautogui.moveTo(matches[0][0]+1074, matches[0][1]+264, duration=0.5)
            pyautogui.click()
            pyautogui.click()
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.moveTo(800, 254, duration=0.5)
            pyautogui.click()
            pyautogui.press('enter')
            pyautogui.press('enter')
            time.sleep(0.3)
        except Exception as e:
            print("Error during mouse operation:", e)
        iteration -=1
        update_label_count(f"Iterations left: {iteration}")

            




tk.Button(root, text="get starter req", command=lambda: open_input_form(True)).pack(pady=5)
# submit_btn = tk.Button(root, text="Submit", command=on_submit)
tk.Button(root, text="Auto replacing", command=lambda: auto_click_and_replace(iters, target, targeted)).pack(pady=5)
tk.Button(root, text="Stop running", command=lambda: open_input_form(False)).pack(pady=5)
tk.Button(root, text="exit", command=exit).pack(pady=5)
 # The form will only open when the button is clicked
root.mainloop()


#         matches.append((center_x, center_y, word))

# # Show menu
# if not matches:
#     print(f"❌ No matches found for '{target}'")
# else:
#     print(f"✅ Found {len(matches)} matches for '{target}':")
#     for i, (cx, cy, word) in enumerate(matches, 1):
#         print(f"{i}. {word} at ({cx}, {cy})")
    

    # # Ask user which one to select
    # choice = int(input("Select a number: ")) - 1
    # if 0 <= choice < len(matches):
    #     cx, cy, word = matches[choice]
    #     pyautogui.moveTo(cx, cy, duration=0.5)
    #     print(f"🖱️ Mouse moved to '{word}' at ({cx},{cy})")
    # else:
    #     print("❌ Invalid choice")
