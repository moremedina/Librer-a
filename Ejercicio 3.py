import tkinter as tk

def main():
    #Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ejercicio 3 - More Medina")
    ventana.geometry ("500x500")
    ventana.configure (bg="#641c34")

    etiqueta= tk.Label(ventana, text="Ingrese su nombre", font= ("Arial",16))
    etiqueta.pack()
    etiqueta=tk.Entry (ventana)
    etiqueta.pack()
    def saludar():
        
    etiqueta= tk.Button(ventana, text="Enviar",command=saludar)
    etiqueta.pack()


   
    #Ejecutar laventana
    ventana.mainloop()


if __name__=="__main__":
    main()
