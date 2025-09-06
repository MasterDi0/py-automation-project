import pyautogui
import time
import tkinter as tk
from pynput import mouse,keyboard
import threading as th
import pyperclip
# click_count = 0

# # Function to update label
# def update_label():
#     label.config(text=f"Clicks: {click_count}")

# # Mouse click handler
# def on_click(x, y, button, pressed):
#     global click_count
#     if button == mouse.Button.right:
#             # Stop listener and close GUI
#             print(click_count)
#             listener.stop()
#             label.after(0, root.destroy)  # Close the window safely
#     if pressed:
#         click_count += 1
#         label.after(0, update_label)

       

# # Setup tkinter GUI
# root = tk.Tk()
# root.title("Click Counter")
# root.geometry("200x100")

# label = tk.Label(root, text="Clicks: 0", font=("Arial", 20))
# label.pack(expand=True)

# # Define the listener globally so we can stop it
# listener = mouse.Listener(on_click=on_click)
# time.sleep(3)
# # Run the listener in a separate thread
# listener_thread = threading.Thread(target=listener.start)
# listener_thread.daemon = True
# listener_thread.start()

# # Start the GUI loop
# root.mainloop()

start_fill = False
click_count = 0
clicks= 0
number_of_sec= 0
clicking_enabled = th.Event()
# main_sec = "كغ"
# secondary_sec = "كرتونة"

 # Flag to control when to count clicks

# --- GUI Setup ---
root = tk.Tk()
root.title("Click Counter")
root.geometry("250x300")


label = tk.Label(root, text="Press an option", font=("Arial", 16))
label_count = tk.Label(root,text="screen", font=("Arial", 14))
label_countdown = tk.Label(root,text="countdown", font=("Arial", 14))
label_count.pack(pady=10)
label_countdown.pack(pady=2)
label.pack(pady=20)


def open_input_form():
    form = tk.Toplevel(root)
    form.title("Input Form")
    form.geometry("300x200")

    tk.Label(form, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(form)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form, text="Age:").grid(row=1, column=0, padx=10, pady=5)
    age_entry = tk.Entry(form)
    age_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(form, text="City:").grid(row=2, column=0, padx=10, pady=5)
    city_entry = tk.Entry(form)
    city_entry.grid(row=2, column=1, padx=10, pady=5)

    def submit():
        name = name_entry.get()
        age = age_entry.get()
        city = city_entry.get()
        form.destroy()
        th.Thread(target=run_automation_tasks,args=(name,city,age),daemon=True).start()
        print(f"Name: {name}, Age: {age}, City: {city}")
        
        # for i in range(clicks-1):
        #     automate_task(main_sec=name, secondary_sec=city, number_of_sec=age)

    tk.Button(form, text="Submit", command=submit).grid(row=3, column=0, columnspan=2, pady=15)


# name_entry.grid(row=0, column=1, padx=5, pady=5)
# age_entry.grid(row=1, column=1, padx=5, pady=5)
# city_entry.grid(row=2, column=1, padx=5, pady=5)
def run_automation_tasks(main_sec, secondary_sec, number_of_sec):
    global clicks
    for i in range(clicks-1):
        automate_task(main_sec=main_sec, secondary_sec=secondary_sec, number_of_sec=number_of_sec)
# submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# --- Update the label text ---
def update_label(text):
    label.config(text=text)
def update_label_count(text):
    label_count.config(text=text)
def update_label_countdown(text):
    label_countdown.config(text=text)
# --- Mouse click handler ---
def on_click(x, y, button, pressed):
    print(f"[DEBUG] Clicked: {button}, Pressed: {pressed}, Enabled: {clicking_enabled}")
    global click_count
    global clicks
    if button == mouse.Button.right:
        # Stop listener and close GUI on left click
        print(click_count)
        clicks = click_count
        mouse_listener.stop()
        click_count = 0
        label.after(0, lambda: update_label(f"Clicks: {click_count}"))
        label.after(0,lambda:update_label_countdown (f'count down: {clicks}'))
    if button == mouse.Button.left and pressed and clicking_enabled.is_set():
        click_count += 1
        label.after(0, lambda: update_label(f"Clicks: {click_count}"))

def mouse_pos(x,y,button,pressed):
    # mouse_pos = pyautogui.position()
    while(True):
        time.sleep(0.5)
        if button == mouse.Button.right:
        # Stop listener and close GUI on left click
            print(click_count)
            print(f'pressed :{mouse.Button.right}')
            mouse_listener.stop()
        time.sleep(0.5)
        label.after(0,lambda:update_label_count(f'mouse position: {pyautogui.position()}'))
        
        



# --- Keyboard key press handler ---
# def on_press(key):
#     global clicking_enabled

#     try:
#         if key.char == 's' and not clicking_enabled:
#             clicking_enabled = True
#             label.after(0, lambda: update_label("Clicking started!"))
#             start_mouse_listener()
#     except AttributeError:
#         pass  # Handles special keys (not needed here)

# --- Start mouse listener in thread ---
def start_mouse_listener():
    global mouse_listener
    clicking_enabled.set()
    mouse_listener = mouse.Listener(on_click=mouse_pos)
    mouse_listener.start()
    
def start_click_listener():
    global mouse_listener
    clicking_enabled.set()
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

def exit():
    label.after(0, root.destroy)



def automate_task(number_of_sec,main_sec,secondary_sec,):
    global clicks
    clicks-= 1
    label.after(0,lambda:update_label_countdown (f'count down: {clicks}'))
    pyperclip.copy(main_sec)
    time.sleep(1)  # Wait so you can focus the right window
    # x, y = 845, 510  # Coordinates of the pixel to click
    pyautogui.moveTo(849, 510, duration=0.2)
    pyautogui.click()
    pyautogui.click()
    
    # pyautogui.click()
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    print(f'{ pyautogui.position()}')
    time.sleep(0.3)
    pyautogui.moveTo(942, 380, duration=0.3)
    pyautogui.click()
    print(f'{ pyautogui.position()}')
    pyperclip.copy(secondary_sec)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pyautogui.press('enter')
    pyautogui.write(number_of_sec)
    time.sleep(0.3)
    pyautogui.moveTo(829, 254, duration=0.2)
    pyautogui.click()
    time.sleep(0.3)
    # pyautogui.moveTo(1026, 552, duration=0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('enter')
   

def start_war():
    open_input_form()
    # number_of_sec = input()
    # main_sec = input()
    # secondary_sec = input()
    # time.sleep(1.3)
    # for i in range(clicks-1):
    #     automate_task(number_of_sec = number_of_sec,main_sec= main_sec,secondary_sec=secondary_sec)
# --- Start keyboard listener in thread ---
# def start_keyboard_listener():
#     with keyboard.Listener(on_press=on_press) as listener:
#         listener.join()

# Start the keyboard listener in a background thread
# keyboard_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
# keyboard_thread.start()

tk.Button(root, text="mouse positions", command=start_mouse_listener).pack(pady=5)
# submit_btn = tk.Button(root, text="Submit", command=on_submit)
tk.Button(root, text="click counter", command=start_click_listener).pack(pady=5)
tk.Button(root, text="auto filling filled", command=start_war).pack(pady=5)
tk.Button(root, text="exit", command=exit).pack(pady=5)



# Start the GUI loop
root.mainloop()

# q = 20
# pyautogui.click
# for q in range(q):
#     print(f'{ pyautogui.position()}')
#     time.sleep(4)
# q =pyautogui.KEYBOARD_KEYS
# print(q)
# pyautogui.press('enter')
# pyautogui.hotkey()


