import tkinter as tk # GUI package
from tkinter import filedialog, Text # Dialog with the file system
import os # to control the po
import json

from setuptools import Command

root = tk.Tk()  # Main root widget
apps = []  # List of of open files/exec by string path

# get the config informations
with open('config.json', 'r') as json_file:
    json_data = json.load(json_file)
print(json_data)

#######################################################################

# Function to add app to the list
def addApp():
    global apps # Get the list in global var

    # Reset the list in the appListFrame
    for widget in appListFrame.winfo_children():
        widget.destroy()

    # to get the path string of the new file
    # the path is stored in 'filenmane'
    filename = filedialog.askopenfilename(
        initialdir="/.", title="Select File",
        filetypes=(
            ("executables", "*.exe"),
            ("all files", "*.*")
        )       
    )

    apps.append(filename)  # Add the new filename to the liss
    print(filename)  # to consol to check

    # Print all file of the list in the appListFrame
    for app in apps:
        label = tk.Label(
            appListFrame, text=app, bg=json_data["in-list-element-color"])
        label.pack()

# Run all file in the list
def runApps():
    global apps

    for app in apps:
        os.startfile(app)

# Remove all file of the list and clear the appListFrame
def clearApps():
    global apps

    for widget in appListFrame.winfo_children():
        widget.destroy()

    for app in apps:
        apps.clear()

def getUserInput(master, input):
    inp = input.get(1.0, "end-1c")
    with open('saves/' + inp + '.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')

    master.destroy()

# Save the current config
def saveConfig():
    global apps

    f = filedialog.asksaveasfile(
        initialfile='Untitled.txt',
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")],
        initialdir="/./projet/explorer/saves"
    )

    print(f.name)

    with open(f.name, 'w') as f:
        for app in apps:
            f.write(app + ',')

# open config
def openConfig():
    global apps

    for widget in appListFrame.winfo_children():
        # Détruit les widget pour éviter les doublons
        widget.destroy()

    # Récupère le chemin du fichier à ajouter à la liste
    filename = filedialog.askopenfilename(
        initialdir="/./projet/explorer/saves", title="Select File",
        filetypes=(
            ("configurations", "*.txt"),
            ("all files", "*.*")
        )
    )

    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            tempApps = f.read()
            tempApps = tempApps.split(',')
            apps = [x for x in tempApps if x.strip()]
        
    print(apps)
    for app in apps:
        # afficher tout les chemins enregistrés
        label = tk.Label(appListFrame, text=app, bg=json_data["in-list-element-color"])
        label.pack()

#######################################################################

# Frame which contain the element
appListFrame = tk.Frame(
    root,
    height=500, width=500,
    bg=json_data["background-color"]
)

# Frame for the button on top of the app
menuBar = tk.Menu(root)

# Menu widget for the menu bar
menuBar = tk.Menu(root)
fileMenu = tk.Menu(menuBar, tearoff=0)   # Sub Menu File
menuBar.add_cascade(label="File", menu=fileMenu)
devMenu = tk.Menu(menuBar, tearoff=0)    # Sub Menu Edit
menuBar.add_cascade(label="Dev", menu=devMenu)
helpMenu = tk.Menu(menuBar, tearoff=0)   # Sub Menu Edit
menuBar.add_cascade(label="Help", menu=helpMenu)

# Sous menu Fil
fileMenu.add_command(label="Open File...", command=addApp)
fileMenu.add_command(label="Open Config...", command=openConfig)
fileMenu.add_command(label="Clear List", command=clearApps)
fileMenu.add_command(label="Save config...", command=saveConfig)
fileMenu.add_command(label="Run App", command=runApps)
fileMenu.add_command(label="Quit", command=root.destroy)
# Sous menu edit
helpMenu.add_command(label="Help")
helpMenu.add_command(label="?")
# Sous menu Dev
devMenu.add_command(label="Test")

#######################################################################

def init_menu_bar():

    root.config(menu=menuBar)

def init_widgets():

    appListFrame.pack(side="top", fill="both", expand=True)

    root.geometry("500x500")
    root.title("Explorer")

# Run all function to build the app
def init():

    init_widgets()
    init_menu_bar()


#######################################################################

if __name__ == '__main__':

    init()
    root.mainloop()