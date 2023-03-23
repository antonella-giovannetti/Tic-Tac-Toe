from tkinter import * 
from tkinter import messagebox
import random

window = Tk()
window.title('Jeu du morpion')

# Variables globales
clicked = True
count = 0
winner = False
buttons = []
one = None
two = None

# Désactive les boutons
def disable_all_buttons():
    for button in buttons:
        button.config(state=DISABLED) # désactive le bouton en le mettant dans un état désactivé, l'utilisateur ne peut plus cliquer sur le bouton qui ne répondra plus aux événements de souris

# Verifie si O ou X gagne
def checkifwon():
    global winner
    for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),(2, 5, 8),(0, 4, 8), (2, 4, 6)]: 
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            for button in (buttons[a], buttons[b], buttons[c]):
                button.config(bg="blue")
            winner = True
            messagebox.showinfo("Jeu du morpion", f"Bravo, {buttons[a]['text']} a gagné !")
            disable_all_buttons()

# Reinitialise le jeu de zéro 
def reset(): 
    global buttons, clicked, count, winner
    clicked = True
    count = 0
    winner = False
    for button in buttons:
        button.config(text="", bg="SystemButtonFace", state=NORMAL)

def one_player_level1_buttons(i):
    global buttons, count, winner
    if not winner:
        if buttons[i]["text"] == "":
            buttons[i]["text"] = "O"
            checkifwon()
            count += 1
            if not winner:
                remaining_buttons = []
                for button in buttons:
                    if button["text"] == "":
                        remaining_buttons.append(button)
                # remaining_buttons = [button for button in buttons if button["text"] == ""]
                if remaining_buttons:
                    random_button = random.choice(remaining_buttons)
                    random_button["text"] = "X"
                    checkifwon()
                    count += 1
        if count == 9 and winner == False:
            messagebox.showinfo("Jeu du morpion", "Match nul")
            disable_all_buttons()

def one_player_level1():
    global buttons
    destroy_widget()
    menu_on_game()
    for i in range(9):
        button = Button(window, text="", font=("Helvetica", 20), height=3, width=6, command=lambda i=i: one_player_level1_buttons(i))
        button.grid(row=i // 3, column=i % 3, sticky=NSEW) # sticky NSEW fait en sorte que le bouton occupe tout l'espace disponible dans sa cellule
        buttons.append(button)

def one_player_level2_buttons(i):
    pass

def one_player_level2():
    global buttons
    destroy_widget()
    menu_on_game()
    for i in range(9):
        button = Button(window, text="", font=("Helvetica", 20), height=3, width=6, command=lambda i=i: one_player_level2_buttons(i))
        button.grid(row=i // 3, column=i % 3, sticky=NSEW) # sticky NSEW fait en sorte que le bouton occupe tout l'espace disponible dans sa cellule
        buttons.append(button)

def one_player():
    global one, two
    destroy_widget()
    for widget in window.winfo_children():
        widget.destroy()
    level1 = Button(window, text="Niveau 1", font=("Helvetica", 20), height=4, width=20, command=one_player_level1)
    level2 = Button(window, text="Niveau 2", font=("Helvetica", 20), height=4, width=20, command=one_player_level2)
    level1.pack()
    level2.pack()

def two_players_buttons(i):
    global clicked, count, winner 
    if buttons[i]["text"] == "" and clicked == True:
        buttons[i]["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif buttons[i]["text"] == "" and clicked == False:
        buttons[i]["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    if count == 9 and winner == False:
        messagebox.showinfo("Jeu du morpion", "Match nul")
        disable_all_buttons()

def two_players():
    global one, two
    destroy_widget()
    menu_on_game()
    for i in range(9):
        button = Button(window, text="", font=("Helvetica", 20), height=3, width=6, command=lambda i=i: two_players_buttons(i))
        button.grid(row=i // 3, column=i % 3, sticky=NSEW) # sticky NSEW fait en sorte que le bouton occupe tout l'espace disponible dans sa cellule
        buttons.append(button)

def menu_on_game():
    my_menu = Menu(window) # Création de l'objet de menu 
    window.config(menu=my_menu) # Affiche le menu crée precédement en utilisant la méthode config et en passant le param menu qui prend l'objet de menu crée
    my_menu.add_command(label="Menu", command=start_game)  # Ajoute une option au menu principal "Reset game" et la fonction reset 
    my_menu.add_command(label="Relancer le jeu", command=reset)  # Ajoute une option au menu principal "Reset game" et la fonction reset 

# Démarre le jeu
def start_game():
    global one, two
    destroy_widget()
    one = Button(window, text="Un joueur", font=("Helvetica", 20), height=4, width=20, command=one_player)
    two = Button(window, text="Deux joueurs", font=("Helvetica", 20), height=4, width=20, command=two_players)
    one.pack()
    two.pack()

def destroy_widget(): 
    for widget in window.winfo_children():
        widget.destroy()

start_game()

window.mainloop()