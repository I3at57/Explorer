import tkinter as tk # GUI package
from tkinter import filedialog, Text # Dialog with the file system
import os # to control the po
import json

root = tk.Tk()  # Main root widget
apps = []  # List of of open files/exec by string path

# get the config informations
with open('config.json', 'r') as json_file:
    json_data = json.load(json_file)
print(json_data)

#######################################################################

# Function to add app
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

def saveFiles():
    global apps

    inp = textInput.get(1.0, "end-1c")
    with open('saves/' + inp + '.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')

# open config
def openFiles():
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
topBarFrame = tk.Frame(root)

openFile = tk.Button(
    topBarFrame, text="Open File", padx=10,
    pady=5, fg="white", bg=json_data["button-color"], command=addApp
)

runApp = tk.Button(
    topBarFrame, text="Run Apps", padx=10,
    pady=5, fg="white", bg=json_data["button-color"], command=runApps
)

clearApp = tk.Button(
    topBarFrame, text="Clear Apps", padx=10, pady=5,
    fg="white", bg=json_data["button-color"], command=clearApps
)

saveConfig = tk.Button(
    topBarFrame, text="Save Configuration", padx=10, pady=5,
    fg="white", bg=json_data["button-color"], command=saveFiles
)

openConfig = tk.Button(
    topBarFrame, text="Open Configuration", padx=10,
    pady=5, fg="white", bg=json_data["button-color"], command=openFiles
)

# Create the text inputs
textInput = tk.Text(topBarFrame, height=1, width=25)

#######################################################################

# Run once at launch to create the gui
def init_widgets():

    topBarFrame.pack(side="top")
    appListFrame.pack(side="top")
    openFile.pack(side="left")
    runApp.pack(side="left")
    clearApp.pack(side="left")
    saveConfig.pack(side="left")
    textInput.pack(side="left")
    openConfig.pack(side="left")
    appListFrame.pack(side="top")

    root.resizable(0, 0)
    root.title("Explorer")


#######################################################################

if __name__ == '__main__':

    init_widgets()
    root.mainloop()