
from cgitb import grey
from time import timezone
from tkinter import *
from tkinter import font
from tkinter.font import BOLD

def setUp():
    window =Tk() 
    window.title('TP1 ')
    window.geometry("600x500+10+20")
    lbl = Label(window, text = "Contrôle d'une porte d'aération d'une serre", fg='black', font=("Adobe arabic",12,BOLD))
    lbl.place(x= 150,y= 50)

    lbl2 = Label(window, text="Température d'ouverture de la porte : ", fg='black',font=("Adobe arabic",10,BOLD))
    lbl2.place(x = 10, y = 100)

    lbl3 = Label(window, text="Distance d'ouverture de la porte: ", fg='black',font=("Adobe arabic",10,BOLD))
    lbl3.place(x=10, y=125)


    lblControle = Label(window, text="Contrôle:",fg='black',font=("Adobe arabic",10,BOLD,UNDERLINE))
    lblControle.place(x=10,y=150)

    btnAutomatique = Button(window, text="Automatique",fg='black')
    btnAutomatique.place(x=80, y=150)

    btnManuelle = Button(window, text="Manuelle",fg='black')
    btnManuelle.place(x=80, y=180)

    txtfld = Entry(window,text="", bd=5)

    txtfld.place(x=180, y=180)

    lblPourcentage = Label(window,text="%", fg="black", font=("Adobe arabic",15))
    lblPourcentage.place(x=330,y=185)



    btnOuvrir = Button(window, text="Ouvrir la porte!",fg='black')
    btnOuvrir.place(x=80, y=220)

    btnFermer = Button(window, text="Fermer la porte!",fg='black')
    btnFermer.place(x=180, y=220)

    lblMoteur = Label(window,text="Statut du Moteur :", fg='black', font=("Adobe arabic",10,BOLD,UNDERLINE))
    lblMoteur.place(x=10,y=250)

    lblDirection = Label(window, text="Direction : ", fg='black',font=("Adobe arabic", 10 ,  BOLD))
    lblDirection.place(x=10,y=270)
    lbldeDirection = Label(window, text="Gauche ou Droite", fg='black', font=("Adobe arabic",10))
    lbldeDirection.place(x=80,y=271)

    lblVitesse = Label(window, text="Vitesse : ", fg='black', font=("Adobe Arabic",10, BOLD))
    lblVitesse.place(x=250, y=270)

    btnAfficher = Button(window, text="Afficher les logs", fg='black')
    btnAfficher.place(x=200,y=300)

    window.mainloop()


def main():
    setUp()

if __name__ == "__main__":
    main()


