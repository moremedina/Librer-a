import tkinter as tk

def main():
    #Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ejercicio 2 - More Medina")
    ventana.geometry ("700x700")
    ventana.configure (bg="lightblue")

    #Crear la etiqueta
    etiqueta = tk.Label(ventana, text= "Ejercicio 2", font=("Arial", 16))
    etiqueta.pack() #Coloca la etiqueta en la ventana
    etiqueta = tk.Label(ventana, text= "More Medina", font=("Arial", 16))
    etiqueta.pack()

    #Ejecutar la ventana
    ventana.mainloop()

if __name__=="__main__":
    main()
