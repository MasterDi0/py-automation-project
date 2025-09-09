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
# #     age = age_entry.get()
# #     city = city_entry.get()
# #     print(f"Name: {name}, Age: {age}, City: {city}")
# #     root.destroy()

# # root = tk.Tk()
# # root.title("Multi Input Form")

# # tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
# # tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
# # tk.Label(root, text="City:").grid(row=2, column=0, padx=5, pady=5)

# # name_entry = tk.Entry(root)
# # age_entry = tk.Entry(root)
# # city_entry = tk.Entry(root)

# # name_entry.grid(row=0, column=1, padx=5, pady=5)
# # age_entry.grid(row=1, column=1, padx=5, pady=5)
# # city_entry.grid(row=2, column=1, padx=5, pady=5)

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
#     city_entry = tk.Entry(popup)

#     name_entry.grid(row=0, column=1, padx=5, pady=5)
#     age_entry.grid(row=1, column=1, padx=5, pady=5)
#     city_entry.grid(row=2, column=1, padx=5, pady=5)

#     def submit():
#         name = name_entry.get()
#         age = age_entry.get()
#         city = city_entry.get()
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


import pytesseract
from pytesseract import Output
import pyautogui
import cv2
import time
import pyperclip
# Take screenshot
b=100
target = "شوتة"  # word to search
targeted_word = "شوته "
pytesseract.pytesseract.tesseract_cmd = r"d:/New folder/tesseract.exe"
ocr_lang = "ara"
while b>0:
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
        pyautogui.moveTo(matches[0][0]+1065, matches[0][1]+264, duration=0.5)
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
    b-=1







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
