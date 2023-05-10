import sys
sys.path.append('/Users/alvaro/Desktop/TFGALL/TFG')
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import main
from Gestos import EstadisticasGestos


def limpiarfechas (lista):
    for i in lista:
        a = i[0:10]
        i = a[0]
    print(lista)
    return lista

data1 = EstadisticasGestos.generarDatos(main.Username)

#Ventana y configuración
root = tk.Tk()
root.title("Visualización de estadísticas de Gestos")
root.geometry("1200x650")
root.resizable(width=False, height=False)

#Frame gráfica izquierda
frame1 = tk.Frame(root, width=400, height=600)
frame1.pack(side="left")

#Frame gráfica derecha
frame2 = tk.Frame(root, width=400, height=600)
frame2.pack(side="right")

#Gráfica de la izquierda -----------------------------------------------------------------------------------------------

#Preparar los datos
lista = data1.values()
labels = ['corazon', 'perfecto', 'suerte', 'unpoco']
sizes = [0,0,0,0]

for i in lista:
    if i == "corazon":
        sizes[0] +=1
    if i == "perfecto":
        sizes[1] +=1
    if i == "suerte":
        sizes[2] +=1
    if i == "unpoco":
        sizes[3] +=1


fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

#Canvas para la gráfica de la izquierda
canvas1 = FigureCanvasTkAgg(fig, master=frame1)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#Toolbar para la gráfica de la izquierda
toolbar1 = NavigationToolbar2Tk(canvas1, frame1)
toolbar1.update()
canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#Gráfica de la derecha -------------------------------------------------------------------------------------------------
fig2 = plt.figure(figsize=(5,5), dpi=100)
plt.hist(list(data1.values()), bins=5)
plt.title("Frecuencia de Gestos")
plt.xlabel("Gestos")
plt.ylabel("Frecuencia")
plt.tight_layout()

#Canvas para la gráfica de la derecha
canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
canvas2.draw()
canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#Toolbar para la gráfica de la derecha
toolbar2 = NavigationToolbar2Tk(canvas2, frame2)
toolbar2.update()
canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


root.mainloop()