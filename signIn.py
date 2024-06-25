import customtkinter as ctk
import tkinter.messagebox as tkmb

# Set appearance mode (dark theme)
ctk.set_appearance_mode("dark")

# Set default color theme (blue)
ctk.set_default_color_theme("blue")

# Create the main app window
app = ctk.CTk()
app.geometry("400x300")
app.title("Modern Login UI using CustomTkinter")


# Login function
def login():
    username = "lucky"
    password = "12345"

    if user_entry.get() == username and user_pass.get() == password:
        # tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
        ctk.CTkLabel(app, text="longed in").pack()
        mainpage()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password', message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username', message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")


def mainpage():
    import TextEditer


def signUP():
    import signup


# Create widgets
ctk.CTkLabel(app, text="Username:").pack()
user_entry = ctk.CTkEntry(app)
user_entry.pack()

ctk.CTkLabel(app, text="Password:").pack()
user_pass = ctk.CTkEntry(app, show="*")
user_pass.pack()

ctk.CTkLabel(app, text="  ").pack()
login_button = ctk.CTkButton(app, text="Login", command=login, )
login_button.pack()

ctk.CTkLabel(app, text="    ").pack()
signUp = ctk.CTkButton(app, text="SignUp", command=signUP)
signUp.pack()
ctk.CTkLabel(app, text="    ").pack()
guest = ctk.CTkButton(app, text="Guest", command=mainpage)
guest.pack()
# Run the app
app.mainloop()
