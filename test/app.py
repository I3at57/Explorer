import tkinter as tk
from tkinter import filedialog, Text #Permet de discuter avec l'explorateur de fichier
import os

root = tk.Tk() #Le root
apps = [] #Liste des app ouvertes

# if os.path.isfile('save.txt'):
#         with open('save.txt', 'r') as f:
#                 tempApps = f.read()
#                 tempApps = tempApps.split(',')
#                 print(apps)
#                 apps = [x for x in tempApps if x.strip()]

def addApp():
        global apps

        # Ajouter une app à la liste
        for widget in frame.winfo_children():
                # Détruit les widget pour éviter les doublons
                widget.destroy()

        # Récupère le chemin du fichier à ajouter à la liste
        filename = filedialog.askopenfilename(
                initialdir="/.", title="Select File",
                filetypes=(
                        ("executables", "*.exe"),
                        ("all files", "*.*")
                )
        )
        apps.append(filename) # Ajoute le chemin à la liste
        print(filename) # pour vérifier
        for app in apps:
                # afficher tout les chemins enregistrés
                label = tk.Label(frame, text=app, bg="gray")
                label.pack()

def runApps():

        global apps

        for app in apps:
                os.startfile(app)

def clearApps():

        global apps

        for widget in frame.winfo_children():
                # Détruit les widget pour éviter les doublons
                widget.destroy()

        for app in apps:
                apps.clear()


# Create the text inputs
textInput = tk.Text(root, height=1, width=25)

def saveFiles():

        global apps

        inp = textInput.get(1.0, "end-1c")
        with open(inp + '.txt', 'w') as f:
                for app in apps:
                        f.write(app + ',')

def openFiles():

        global apps

        for widget in frame.winfo_children():
                # Détruit les widget pour éviter les doublons
                widget.destroy()

         # Récupère le chemin du fichier à ajouter à la liste
        filename = filedialog.askopenfilename(
            initialdir="/./projet/explorer/test", title="Select File",
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
                label = tk.Label(frame, text=app, bg="gray")
                label.pack()
        


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42") #Canvas de base pour la liste
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(
        root, text="Open File", padx=10,
        pady=5, fg="white", bg="#263D42", command=addApp
)
openFile.pack(side="left")

runApp = tk.Button(
        root, text="Run Apps", padx=10,
        pady=5, fg="white", bg="#263D42", command=runApps
)
runApp.pack(side="left")

clearApp = tk.Button(
        root, text="Clear Apps", padx=10, pady=5,
        fg="white", bg="#263D42", command=clearApps
)
clearApp.pack(side="left")

saveConfig = tk.Button(
        root, text="Save Configuration", padx=10, pady=5,
    fg="white", bg="#263D42", command=saveFiles
)
saveConfig.pack(side="left")
textInput.pack(side="left")

openConfig = tk.Button(
        root, text="Open Configuration", padx=10,
        pady=5, fg="white", bg="#263D42", command=openFiles
)
openConfig.pack(side="left")

print(apps)
root.resizable(0, 0)
root.title("Explorer")
root.mainloop()