# Single line comment 

'''
Ce ceci est un commentaire multi ligne

'''

from cgitb import grey
from time import timezone
from tkinter import *
from tkinter import font
from tkinter.font import BOLD

   

def main():
    # Window est la variable qui va set la window pour l'interface
    window =Tk() 
    window.title('TP1 ')
    window.geometry("600x600+10+20")
   
   # Variable lbl est la variable qui s'occupe d'afficher le titre de l'application
    lbl = Label(window, text = "Contrôle d'une porte d'aération d'une serre", fg='black', font=("Adobe arabic",12,BOLD))
    lbl.place(x= 150,y= 50)
    #Variable lbl2 est la variable qui s'occupe d'afficher la température de l'ouverture de la porte
    lbl2 = Label(window, text="Température d'ouverture de la porte : ", fg='black',font=("Adobe arabic",10,BOLD))
    lbl2.place(x = 10, y = 100)
    #Variable lbl3 est la variable qui s'occupe d'afficher la distance de la porte du recepteur 
    lbl3 = Label(window, text="Distance d'ouverture de la porte: ", fg='black',font=("Adobe arabic",10,BOLD))
    lbl3.place(x=10, y=125)
    #Variable lblControle est la variable qui s'occupe d'afficher le contôle voulu
    lblControle = Label(window, text="Contrôle:",fg='black',font=("Adobe arabic",10,BOLD,UNDERLINE))
    lblControle.place(x=10,y=150)
    #Variable btnAutomatique est le button qui va afficher automatique et qui va ouvrir la porte de façon automatique
    btnAutomatique = Button(window, text="Automatique",fg='black')
    btnAutomatique.place(x=80, y=150)
    #Variable btnManuelle est le button qui va afficher manuelle et qui va ouvrir la porte de façon manuelle
    btnManuelle = Button(window, text="Manuelle",fg='black')
    btnManuelle.place(x=80, y=180)
    #Variable txtfld est l'espace où l'utilisateur va rentrer le pourcentage dont il veut ouvrir la porte
    txtfld = Entry(window,text="", bd=2, width=5)
    txtfld.place(x=180, y=180)
    #Variable lblPourcentage affiche le signe de %
    lblPourcentage = Label(window,text="%", fg="black", font=("Adobe arabic",15))
    lblPourcentage.place(x=250,y=185)
    #Variable btnOuvrir est le button qui va permettre d'ouvrir la porte 
    btnOuvrir = Button(window, text="Ouvrir la porte!",fg='black')
    btnOuvrir.place(x=80, y=220)
    #Variable btnFermer est le button qui va permettre de fermer la porte
    btnFermer = Button(window, text="Fermer la porte!",fg='black')
    btnFermer.place(x=210, y=220)
    #Variable lblMoteur affiche le statut du moteur
    lblMoteur = Label(window,text="Statut du Moteur :", fg='black', font=("Adobe arabic",10,BOLD,UNDERLINE))
    lblMoteur.place(x=10,y=250)
    #Variable lblDirection affiche la direction que la porte est en train de bouger
    lblDirection = Label(window, text="Direction : ", fg='black',font=("Adobe arabic", 10 ,  BOLD))
    lblDirection.place(x=10,y=270)
    #Variable lbldeDirection affiche la direction gauche ou droite
    lbldeDirection = Label(window, text="Gauche ou Droite", fg='black', font=("Adobe arabic",10))
    lbldeDirection.place(x=80,y=271)
    #Variable lblVitesse affiche la vitesse à laquelle la porte va bouger
    lblVitesse = Label(window, text="Vitesse : ", fg='black', font=("Adobe Arabic",10, BOLD))
    lblVitesse.place(x=250, y=270)
    #Variable btnAfficher est un button qui va afficher les logs 
    btnAfficher = Button(window, text="Afficher les logs", fg='black')
    btnAfficher.place(x=200,y=300)
    #window.mainloop garde la fênetre ouverte 
    window.mainloop()





if __name__ == "__main__":
    main()


