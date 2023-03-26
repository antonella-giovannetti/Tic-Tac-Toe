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

# Création de la grille de jeu
def create_game_board():
    global buttons
    destroy_widget()
    menu_on_game()
    for i in range(9):
        button = Button(window, text="", font=("Helvetica", 20), height=3, width=6)
        button.grid(row=i // 3, column=i % 3, sticky=NSEW)
        buttons.append(button)

# Désactive les boutons
def disable_all_buttons():
    for button in buttons:
        button.config(state=DISABLED) # désactive le bouton en le mettant dans un état désactivé, l'utilisateur ne peut plus cliquer sur le bouton qui ne répondra plus aux événements de souris

# Verifie qui gagne
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

# ------------- 1 JOUEUR  ------------- 

# --- NIVEAU 1 AVEC RANDOM ---

def one_player_level1_buttons(button):
    global buttons, count, winner
    if not winner:
        if button["text"] == "":
            button["text"] = "O"
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

# Affichage de la grille de jeu pour le niveau 1
def one_player_level1():
    global buttons, clicked, count, winner
    clicked = True
    count = 0
    winner = False
    buttons = []
    create_game_board()
    for button in buttons:
        # if button.winfo_exists(): # vérifie si le widget existe toujours
        button.config(command=lambda button=button: one_player_level1_buttons(button))

# --- NIVEAU 2 AVEC MINIMAX ---
def one_player_level2_buttons(button):
    pass

# Affichage de la grille de jeu pour le niveau 2
def one_player_level2():
    global buttons, clicked, count, winner
    clicked = True
    count = 0
    winner = False
    buttons = []
    create_game_board()
    for button in buttons:
        button.config(command=lambda button=button: one_player_level2_buttons(button))

# Affichade des boutons pour choisir le niveau
def one_player():
    global one, two
    destroy_widget()
    for widget in window.winfo_children():
        widget.destroy()
    level1 = Button(window, text="Niveau 1", font=("Helvetica", 20), height=4, width=20, command=one_player_level1)
    level1.pack()
    level2 = Button(window, text="Niveau 2", font=("Helvetica", 20), height=4, width=20, command=one_player_level2)
    level2.pack()

# ------------- 2 JOUEURS  ------------- 

# Remplissage des cases avec O et X
def two_players_buttons(button):
    global clicked, count, winner 
    if button["text"] == "" and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif button["text"] == "" and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    if count == 9 and winner == False:
        messagebox.showinfo("Jeu du morpion", "Match nul")
        disable_all_buttons()

# Affichage de la grille de jeu pour deux joueurs
def two_players():
    global buttons, clicked, count, winner
    clicked = True
    count = 0
    winner = False
    buttons = []
    create_game_board()
    for button in buttons:
        button.config(command=lambda button=button: two_players_buttons(button))

# ------------- FONCTIONS DU JEU  ------------- 

# Menu dans l'affichage du morpion
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

# Détruit les widgets
def destroy_widget(): 
    for widget in window.winfo_children():
        widget.destroy()

start_game()
window.mainloop()