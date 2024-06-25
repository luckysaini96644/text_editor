import sys
from tkinter import filedialog

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"lucky - {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"lucky - {filepath}")


    

def new_file():
    # Clear text area and reset filename
    txt_edit.delete("1.0", tk.END)
    filename = None

def save():
    """Save the current file (existing or new)."""
    global filename
    if filename:
        # Save to existing file
        with open(filename, "w") as file:
            file.write(txt_edit.get(1.0, tk.END))
    else:
        # Prompt user for a new filename
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as file:
            file.write(txt_edit.get(1.0, tk.END))
        filename = filepath
    window.title(f"Lucky - {filename}")

# def save():
#     global filename
#     if filename:
#         # Save to existing file
#         with open(filename, "w") as file:
#             file.write(txt_edit.get("1.0", tk.END))
#     else:
#         # Prompt user for file path
#         filename = filedialog.asksaveasfilename()
#         with open(filename, "w") as file:
#             file.write(txt_edit.get("1.0", tk.END))

def exit():

    sys.exit()


window = tk.Tk()

window.title("lucky")


window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save_as = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_new = tk.Button(fr_buttons, text="New" , command=new_file )
btn_save = tk.Button(fr_buttons, text="Save" , command=save)
btn_exit = tk.Button(fr_buttons, text="Exit" , command=exit )

# save_button = Button(root, text="Save", command=save_file)
# save_button.pack()

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save_as.grid(row=1, column=0, sticky="ew", padx=5)
btn_save.grid(row=2, column=0, sticky="ew", padx=5)
btn_new.grid(row=3, column=0, sticky="ew", padx=5)
btn_exit.grid(row=4, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
