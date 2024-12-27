import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Fonction pour insérer les données dans la base
def inscrire_utilisateur():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()

    if username == "" or email == "" or password == "":
        messagebox.showerror("Erreur", "Tous les champs sont obligatoires !")
        return

    try:
        # Connexion à la base de données
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="users_db"
        )
        cursor = connection.cursor()

        # Insertion des données
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
        connection.commit()

        messagebox.showinfo("Succès", "Inscription réussie !")

        # Réinitialisation des champs
        entry_username.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)

    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de l'inscription : {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Formulaire d'Inscription")
fenetre.geometry("400x300")

# Widgets du formulaire
label_username = tk.Label(fenetre, text="Nom d'utilisateur")
label_username.pack()
entry_username = tk.Entry(fenetre)
entry_username.pack()

label_email = tk.Label(fenetre, text="Email")
label_email.pack()
entry_email = tk.Entry(fenetre)
entry_email.pack()

label_password = tk.Label(fenetre, text="Mot de passe")
label_password.pack()
entry_password = tk.Entry(fenetre, show="*")
entry_password.pack()

button_submit = tk.Button(fenetre, text="S'inscrire", command=inscrire_utilisateur)
button_submit.pack()

# Lancement de l'application
fenetre.mainloop()