# # Import the tkinter module for GUI application
# from tkinter import *
#
# # Create the main window
# root = Tk()
# root.geometry("500x500")  # Set the window size
# root.title("Registration Form")  # Set the window title
#
# # Create a label for the registration form
# label_0 = Label(root, text="Registration Form", width=20, font=("bold", 20))
# label_0.place(x=90, y=60)
#
# # Full Name
# label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
# label_1.place(x=80, y=130)
# entry_1 = Entry(root)
# entry_1.place(x=240, y=130)
#
# # Email
# label_3 = Label(root, text="Email", width=20, font=("bold", 10))
# label_3.place(x=68, y=180)
# entry_3 = Entry(root)
# entry_3.place(x=240, y=180)
#
# # Gender
# label_4 = Label(root, text="Gender", width=20, font=("bold", 10))
# label_4.place(x=70, y=230)
# var = IntVar()  # Holds the selected gender (0 for Male, 1 for Female)
# Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
# Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
#
# # Country
# label_5 = Label(root, text="Country", width=20, font=("bold", 10))
# label_5.place(x=70, y=280)
# list_of_country = ["India", "US", "UK", "Germany", "Austria"]
# c = StringVar()  # Holds the selected country
# droplist = OptionMenu(root, c, *list_of_country)
# droplist.config(width=17)
# c.set("Select your Country")
# droplist.place(x=240, y=280)
# droplist.place(x=240, y=280)
#
# # Language
# label_6 = Label(root, text="Language", width=20, font=("bold", 10))
# label_6.place(x=75, y=330)
# var1 = IntVar()  # Holds the selected language (0 for English, 1 for other)
# # Create Checkbutton widget for language (you can customize this part)
#
# # Run the main loop
# root.mainloop()
import tkinter as tk
from tkinter import messagebox


def login():
    import  signIn
def register_user():
    username = username_entry.get()
    full_name = full_name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    password = password_entry.get()

    # Validate input (you can add more validation logic)
    if username and full_name and email and mobile and password:
        # Save user data or perform other actions (e.g., store in a database)
        # messagebox.showinfo("Registration Successful", "User registered successfully!")
        login()

    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Create the main window
root = tk.Tk()
root.title("Signup Page")
root.geometry("400x300")

# Styling
root.configure(bg="#252425")  # Set background color

# Create input fields
username_label = tk.Label(root, text="Username:", bg="#343638",fg="white")
username_entry = tk.Entry(root)

full_name_label = tk.Label(root, text="Full Name:", bg="#343638",fg="white")
full_name_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email Address:",  bg="#343638",fg="white")
email_entry = tk.Entry(root)

mobile_label = tk.Label(root, text="Mobile Number:",  bg="#343638",fg="white")
mobile_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:", bg="#343638",fg="white")
password_entry = tk.Entry(root, show="*")

# Create signup button
signup_button = tk.Button(root, text="Sign Up", command=register_user, bg="#1e6ba5", fg="white")

# Pack widgets
username_label.pack()
username_entry.pack()

full_name_label.pack()
full_name_entry.pack()

email_label.pack()
email_entry.pack()

mobile_label.pack()
mobile_entry.pack()

password_label.pack()
password_entry.pack()

signup_button.pack(pady=10)

root.mainloop()


