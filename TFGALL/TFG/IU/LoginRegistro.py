import sys
sys.path.append('/Users/alvaro/Desktop/TFGALL/TFG')
import Usuarios
import main
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def iniciar_sesion():
    # validación de que no haya campos vacíos
    if username_login.get()=="" or password_login.get()=="":
        tk.Label(frame_login, text="Por favor, rellena todos los campos").grid(row=5, column=1, padx=5, pady=5)
    else:
        username = username_login.get()
        password = password_login.get()
        check = Usuarios.gestionUsuarios.comprobarLogin(username, password)
        if check == True:
            main.init(username)
            tk.Label(frame_login, text="Login Correcto").grid(row=5, column=1, padx=5, pady=5)
            ventana.destroy()
            import MainView
            MainView(ventana)
        elif check == False:
            tk.Label(frame_login, text=" Login Incorrecto").grid(row=4, column=1, padx=5, pady=5)


def registrar_usuario():
    #validación de que no haya campos vacíos
    if nombre_registro.get()=="" or apellidos_registro.get()=="" or username_registro.get()=="" or password_registro.get()=="":
        tk.Label(frame_registro, text="Por favor, rellena todos los campos").grid(row=7, column=1, padx=5, pady=5)
    else:
        nombre = nombre_registro.get()
        apellidos = apellidos_registro.get()
        username = username_registro.get()
        contraseña = password_registro.get()
        check = Usuarios.gestionUsuarios.registrarUsuario(nombre, apellidos, username, contraseña)
        if check == True:
            tk.Label(frame_registro, text="Registro Correcto, haga login").grid(row=6, column=1, padx=5, pady=5)
        elif check == False:
            tk.Label(frame_registro, text="Registro Incorrecto").grid(row=6, column=1, padx=5, pady=5)

# Crear la ventana principal
ventana = customtkinter.CTk()
ventana.title("Registro | Login")
ventana.resizable(width=False, height=False)
ventana.configure(background='#FFFFFF')

#Iconos

login = customtkinter.CTkImage(light_image=Image.open("TFG/assets/login.png"),
                                  dark_image=Image.open("TFG/assets/login.png"),
                                  size=(15, 15))

registro = customtkinter.CTkImage(light_image=Image.open("TFG/assets/registro.png"),
                                  dark_image=Image.open("TFG/assets/registro.png"),
                                  size=(11, 15))

# Crear los widgets del login
frame_login = tk.Frame(ventana)
frame_login.pack(side="left", padx=10, pady=10)
tk.Label(frame_login, text="Login", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)
tk.Label(frame_login, text="Usuario").grid(row=1, column=0, padx=5, pady=5)
username_login = customtkinter.CTkEntry(frame_login)
username_login.grid(row=1, column=1, padx=5, pady=5)
tk.Label(frame_login, text="Contraseña").grid(row=2, column=0, padx=5, pady=5)
password_login = customtkinter.CTkEntry(frame_login, show="*")
password_login.grid(row=2, column=1, padx=5, pady=5)
customtkinter.CTkButton(frame_login, text="Iniciar sesión", command=iniciar_sesion, image=login).grid(row=3, columnspan=2, padx=5, pady=5)

# Crear los widgets del registro
frame_registro = tk.Frame(ventana)
frame_registro.pack(side="right", padx=10, pady=10)
tk.Label(frame_registro, text="Registro", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)
tk.Label(frame_registro, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
nombre_registro = customtkinter.CTkEntry(frame_registro)
nombre_registro.grid(row=1, column=1, padx=5, pady=5)
tk.Label(frame_registro, text="Apellidos").grid(row=2, column=0, padx=5, pady=5)
apellidos_registro = customtkinter.CTkEntry(frame_registro)
apellidos_registro.grid(row=2, column=1, padx=5, pady=5)
tk.Label(frame_registro, text="Usuario").grid(row=3, column=0, padx=5, pady=5)
username_registro = customtkinter.CTkEntry(frame_registro)
username_registro.grid(row=3, column=1, padx=5, pady=5)
tk.Label(frame_registro, text="Contraseña").grid(row=4, column=0, padx=5, pady=5)
password_registro = customtkinter.CTkEntry(frame_registro, show="*")
password_registro.grid(row=4, column=1, padx=5, pady=5)
customtkinter.CTkButton(frame_registro, text="Registrar", command=registrar_usuario, image=registro).grid(row=5, columnspan=2, padx=5, pady=5)


ventana.mainloop()