# import tkinter as tk
# from tkinter import simpledialog

# root = tk.Tk()
# root.withdraw()  # Hide the main window

# user_input = simpledialog.askstring("Input", "Enter your name:")
# age_input = simpledialog.askstring("Input", "Enter your age:")
# loc_input = simpledialog.askstring("Input", "Enter your location:")

# print("User entered:", user_input,' ',age_input,' ',loc_input)


# import tkinter as tk

# def on_submit():
#     name = name_entry.get()
#     age = age_entry.get()
#     city = city_entry.get()
#     print(f"Name: {name}, Age: {age}, City: {city}")
#     root.destroy()

# root = tk.Tk()
# root.title("Multi Input Form")

# tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
# tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
# tk.Label(root, text="City:").grid(row=2, column=0, padx=5, pady=5)

# name_entry = tk.Entry(root)
# age_entry = tk.Entry(root)
# city_entry = tk.Entry(root)

# name_entry.grid(row=0, column=1, padx=5, pady=5)
# age_entry.grid(row=1, column=1, padx=5, pady=5)
# city_entry.grid(row=2, column=1, padx=5, pady=5)

# submit_btn = tk.Button(root, text="Submit", command=on_submit)
# submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# root.mainloop()



import tkinter as tk

def open_input_popup():
    popup = tk.Toplevel(root)
    popup.title("Enter Details")

    tk.Label(popup, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(popup, text="Age:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(popup, text="City:").grid(row=2, column=0, padx=5, pady=5)

    name_entry = tk.Entry(popup)
    age_entry = tk.Entry(popup)
    city_entry = tk.Entry(popup)

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    age_entry.grid(row=1, column=1, padx=5, pady=5)
    city_entry.grid(row=2, column=1, padx=5, pady=5)

    def submit():
        name = name_entry.get()
        age = age_entry.get()
        city = city_entry.get()
        print(f"Name: {name}, Age: {age}, City: {city}")
        popup.destroy()

    submit_btn = tk.Button(popup, text="Submit", command=submit)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Main window
root = tk.Tk()
root.title("Main Window")

main_button = tk.Button(root, text="Open Form", command=open_input_popup)
main_button.pack(padx=20, pady=20)

root.mainloop()
