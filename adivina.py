import random
import tkinter as tk

numero_secreto = random.randint(1, 10)
intentos = 0

def adivinar():
    global intentos
    intentos += 1
    numero = int(caja_numero.get())
    if numero == numero_secreto:
        etiqueta_resultado.config(text="¡Felicidades! ¡Adivinaste el número en " + str(intentos) + " intentos!")
    elif numero > numero_secreto:
        etiqueta_resultado.config(text="El número es demasiado alto. Inténtalo de nuevo.")
    else:
        etiqueta_resultado.config(text="El número es demasiado bajo. Inténtalo de nuevo.")
    caja_numero.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Adivina el número")

etiqueta_instrucciones = tk.Label(ventana, text="Adivina un número entre 1 y 10:")
etiqueta_instrucciones.pack()

caja_numero = tk.Entry(ventana)
caja_numero.pack()

boton_adivinar = tk.Button(ventana, text="Adivinar", command=adivinar)
boton_adivinar.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()