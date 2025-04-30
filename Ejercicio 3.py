import tkinter as tk

def main():
    def saludar():
        eti = str(etiqueta.get())
        t = tk.Label (ventana, text =("Hola!", eti, ", te saluda More!"))
        t.pack()
    
    ventana = tk.Tk()
    ventana.title("Ejercicio 3 - More Medina")
    ventana.geometry ("500x500")
    ventana.configure (bg="#e6b0aa")

    etiqueta_label= tk.Label(ventana, text="Ingrese su nombre", font= ("Arial",16), bg="#d98880")
    etiqueta_label.pack()
    etiqueta=tk.Entry(ventana)
    etiqueta.pack()
    boton = tk.Button(ventana, text="Saludar", font=("Arial", 14),command = saludar, bg="#d98880")
    boton.pack()
    
    ventana.mainloop()


if __name__=="__main__":
    main()
