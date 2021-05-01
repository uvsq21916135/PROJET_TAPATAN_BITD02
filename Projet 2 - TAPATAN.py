import tkinter as tk

racine = tk.Tk()


def menu():
    """ Fonction qui crée:
        -une fenetre de taille 400*400
        - 4 boutons: PvP, PvIA, IAvIA et Exit
        -Exit détruit la fenetre
    """
    racine = tk.Tk()
    racine.title("Menu")
    btn_PVP = tk.Button(racine, command=game_window_1, text="Player vs Player")
    btn_PVP.pack()
    btn_PVIA = tk.Button(racine, command=game_window_3, text="Player vs IA")
    btn_PVIA.pack()
    btn_IAVIA = tk.Button(racine, command=game_window_2, text="IA vs IA")
    btn_IAVIA.pack()
    btn_quit = tk.Button(racine, command=racine.destroy, text="Quitter")
    btn_quit.pack()


def game_window_1():
    """Fonction qui creer:
        -une nouvelle fenetre avec un canvas 800*800
        -avec le plateau (carre centré) 600*600
        -lignes et ronds au intersections
        -Utilisé pour le PVP
    """
    racine = tk.Tk()
    racine.title("TAPANTA")
    canvas = tk.Canvas(racine, bg="pale goldenrod", height=800, width=1000)
    canvas.grid(row=0, rowspan=5, column=0, columnspan=3)
    canvas.create_rectangle(100, 700, 700, 100, width=4, fill="pale goldenrod")

    # LIGNES
    canvas.create_line(100, 100, 700, 700, width=4, fill="black")
    canvas.create_line(100, 700, 700, 100, width=4, fill="black")
    canvas.create_line(400, 100, 400, 700, width=4, fill="black")
    canvas.create_line(100, 400, 700, 400,  width=4, fill="black")

    # ROND SUPERIEUR
    canvas.create_oval(90, 90, 110, 110, fill="black")
    canvas.create_oval(390, 90, 410, 110, fill="black")
    canvas.create_oval(690, 90, 710, 110, fill="black")

    # ROND MILLIEU
    canvas.create_oval(90, 390, 110, 410, fill="black")
    canvas.create_oval(390, 390, 410, 410, fill="black")
    canvas.create_oval(690, 390, 710, 410, fill="black")

    # ROND BAS
    canvas.create_oval(90, 690, 110, 710, fill="black")
    canvas.create_oval(390, 690, 410, 710, fill="black")
    canvas.create_oval(690, 690, 710, 710, fill="black")

    # LABEL SCORE
    label_J1 = tk.Label(racine, bg="pale goldenrod", text="Score Joueur 1 :" + "......")
    label_J1.grid(row=4, column=0)
    label_J2 = tk.Label(racine, bg="pale goldenrod", text="Score Joueur 2 :" + "......")
    label_J2.grid(row=4, column=1)

    # BOUTON
    btn_SAVE = tk.Button(racine, bg="pale goldenrod", command=None, text="Sauvegarder")
    btn_SAVE.grid(row=1, column=2)
    btn_LOAD = tk.Button(racine, bg="pale goldenrod", command=None, text="Charger")
    btn_LOAD.grid(row=2, column=2)
    btn_MENU = tk.Button(racine, bg="pale goldenrod", command=menu, text="Menu")
    btn_MENU.grid(row=3, column=2)


def game_window_2():
    """Fonction qui creer:
        -une nouvelle fenetre avec un canvas 800*1000
        -avec le plateau (carre centré) 600*600
        -lignes et ronds au intersections
        -4 boutons
        -Utilisé pour le IA V IA
    """
    racine = tk.Tk()
    racine.title("TAPANTA")
    canvas = tk.Canvas(racine, bg="pale goldenrod", height=800, width=1000)
    canvas.grid(row=0, rowspan=5, column=0, columnspan=3)
    canvas.create_rectangle(100, 700, 700, 100, width=4, fill="pale goldenrod")

    # LIGNES
    canvas.create_line(100, 100, 700, 700, width=4, fill="black")
    canvas.create_line(100, 700, 700, 100, width=4, fill="black")
    canvas.create_line(400, 100, 400, 700, width=4, fill="black")
    canvas.create_line(100, 400, 700, 400,  width=4, fill="black")

    # ROND SUPERIEUR
    canvas.create_oval(90, 90, 110, 110, fill="black")
    canvas.create_oval(390, 90, 410, 110, fill="black")
    canvas.create_oval(690, 90, 710, 110, fill="black")

    # ROND MILLIEU
    canvas.create_oval(90, 390, 110, 410, fill="black")
    canvas.create_oval(390, 390, 410, 410, fill="black")
    canvas.create_oval(690, 390, 710, 410, fill="black")

    # ROND BAS
    canvas.create_oval(90, 690, 110, 710, fill="black")
    canvas.create_oval(390, 690, 410, 710, fill="black")
    canvas.create_oval(690, 690, 710, 710, fill="black")

    # LABEL SCORE
    label_J1 = tk.Label(racine, bg="pale goldenrod", text="Score Joueur :" + "......")
    label_J1.grid(row=4, column=0)
    label_J2 = tk.Label(racine, bg="pale goldenrod", text="Score Ordinateur :" + "......")
    label_J2.grid(row=4, column=1)

    # BOUTON
    btn_SAVE = tk.Button(racine, bg="pale goldenrod", command=None, text="Sauvegarder")
    btn_SAVE.grid(row=1, column=2)
    btn_LOAD = tk.Button(racine, bg="pale goldenrod", command=None, text="Charger")
    btn_LOAD.grid(row=2, column=2)
    btn_MENU = tk.Button(racine, bg="pale goldenrod", command=menu, text="Menu")
    btn_MENU.grid(row=3, column=2)
    btn_PAUSE = tk.Button(racine, bg="pale goldenrod", command=None, text="PAUSE")
    btn_PAUSE.grid(row=4, column=2)


def game_window_3():
    """Fonction qui creer:
        -une nouvelle fenetre avec un canvas 800*1000
        -avec le plateau (carre centré) 600*600
        -lignes et ronds au intersections
        -4 boutons
        -Utilisé pour le IA V IA
    """
    racine = tk.Tk()
    racine.title("TAPANTA")
    canvas = tk.Canvas(racine, bg="pale goldenrod", height=800, width=1000)
    canvas.grid(row=0, rowspan=5, column=0, columnspan=3)
    canvas.create_rectangle(100, 700, 700, 100, width=4, fill="pale goldenrod")

    # LIGNES
    canvas.create_line(100, 100, 700, 700, width=4, fill="black")
    canvas.create_line(100, 700, 700, 100, width=4, fill="black")
    canvas.create_line(400, 100, 400, 700, width=4, fill="black")
    canvas.create_line(100, 400, 700, 400,  width=4, fill="black")

    # ROND SUPERIEUR
    canvas.create_oval(90, 90, 110, 110, fill="black")
    canvas.create_oval(390, 90, 410, 110, fill="black")
    canvas.create_oval(690, 90, 710, 110, fill="black")

    # ROND MILLIEU
    canvas.create_oval(90, 390, 110, 410, fill="black")
    canvas.create_oval(390, 390, 410, 410, fill="black")
    canvas.create_oval(690, 390, 710, 410, fill="black")

    # ROND BAS
    canvas.create_oval(90, 690, 110, 710, fill="black")
    canvas.create_oval(390, 690, 410, 710, fill="black")
    canvas.create_oval(690, 690, 710, 710, fill="black")

    # LABEL SCORE
    label_J1 = tk.Label(racine, bg="pale goldenrod", text="Score Ordinateur 1 :" + "......")
    label_J1.grid(row=4, column=0)
    label_J2 = tk.Label(racine, bg="pale goldenrod", text="Score Ordinateur 2 :" + "......")
    label_J2.grid(row=4, column=1)

    # BOUTON
    btn_SAVE = tk.Button(racine, bg="pale goldenrod", command=None, text="Sauvegarder")
    btn_SAVE.grid(row=1, column=2)
    btn_LOAD = tk.Button(racine, bg="pale goldenrod", command=None, text="Charger")
    btn_LOAD.grid(row=2, column=2)
    btn_MENU = tk.Button(racine, bg="pale goldenrod", command=menu, text="Menu")
    btn_MENU.grid(row=3, column=2)
    btn_PAUSE = tk.Button(racine, bg="pale goldenrod", command=None, text="PAUSE")
    btn_PAUSE.grid(row=4, column=2)


menu()
# game_window_1()
# game_window_2()
# game_window_3()
racine.mainloop()
