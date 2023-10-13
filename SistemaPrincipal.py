"""
Desarrollado por: JP        Fecha: 25-08-2023
version: 1.0                version: 3.11
Sistema: GUI
Sistema para Calculos De Area
"""
#Realizar las importaciones de libreia
from tkinter import *
from tkinter import messagebox
#Proceso
def limpiar():
    base.set("")
    altura.set("")
    area.set("")
    perimetro.set("")

def salir():
    quit()

def division():
    try:
        base_valor = float(base.get())
        altura_valor = float(altura.get())

        area_valor = base_valor * altura_valor
        perimetro_valor = 2 * (base_valor + altura_valor)

        area.set(str(area_valor))
        perimetro.set(str(perimetro_valor))

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

#Iniciio
#Creacion de la ventana
ventana = Tk()
ventana.title("Sistema Principal")
ventana.geometry("860x555")
ventana.config(bg="#81d4fa")
ventana.resizable(False,False)
#variables entrada :
base=StringVar()
altura=StringVar()
anime=StringVar()
#variables salida :
area=StringVar()
perimetro=StringVar()
#Creacion de widgets
#   Creacion de las imagenes
imganime = PhotoImage(file="imagenes/anime2.png")
imgbase_altura = PhotoImage(file="imagenes/base_altura.png")
imgcalcular = PhotoImage(file="imagenes/calcular.png")
imglimpiar = PhotoImage(file="imagenes/limpiar.png")
imgsalir = PhotoImage(file="imagenes/salir.png")
#Creacion de la etiqueta
lblanime2= Label(ventana,image=imganime)
lblanime2.place(x=5,y=20)
lblanime2.config(width=360,height=510,bg="#81d4fa")

lblbase_altura = Label(ventana,image=imgbase_altura)
lblbase_altura.place(x=430,y=340)
lblbase_altura.config(width=290,height=180,bg="#81d4fa")

lblcalculo = Label(ventana,text="CALCULO DE AREA")
lblcalculo.place(x=490,y=10)
lblcalculo.config(bg="#81d4fa",font=("Algerian",20,"bold"),fg="blue")

lblbase= Label(ventana,text="Ingrese base: ")
lblbase.place(x=410,y=60)
lblbase.config(bg="#81d4fa",font=("Algerian",13,"bold"),fg="#e040fb")

lblaltura= Label(ventana,text="Ingrese altura: ")
lblaltura.place(x=410,y=90)
lblaltura.config(bg="#81d4fa",font=("Algerian",13,"bold"),fg="#e040fb")

lblarea= Label(ventana,text="El AREA es: ")
lblarea.place(x=410,y=130)
lblarea.config(bg="#81d4fa",font=("Algerian",13,"bold"),fg="#f44336")

lblperimetro= Label(ventana,text="El Perimetro es: ")
lblperimetro.place(x=410,y=160)
lblperimetro.config(bg="#81d4fa",font=("Algerian",13,"bold"),fg="#f44336")

#Creacion de las cajas de texto
txtbase= Entry(ventana,textvariable=base)
txtbase.place(x=580,y=60)
txtbase.config(font=("Algerian",15),width=15,bg="#81d4fa",relief="flat")

txtaltura= Entry(ventana,textvariable=altura)
txtaltura.place(x=580,y=90)
txtaltura.config(font=("Algerian",15),width=15,bg="#81d4fa",relief="flat")

txtarea= Entry(ventana,textvariable=area)
txtarea.place(x=580,y=130)
txtarea.config(font=("Algerian",15),width=15,bg="#81d4fa",relief="flat")

txtperimetro= Entry(ventana,textvariable=perimetro)
txtperimetro.place(x=580,y=160)
txtperimetro.config(font=("Algerian",15),width=15,bg="#81d4fa",relief="flat")

#Creaciojn de botones
btncalcular= Button(ventana,image=imgcalcular,command=division)
btncalcular.place(x=410,y=240)
btncalcular.config(width=70,height=60,bg="#81d4fa",font=("Calibri",50,"bold"),relief="flat")

btnlimpiar= Button(ventana,image=imglimpiar,command=limpiar)
btnlimpiar.place(x=540,y=210)
btnlimpiar.config(width=70,height=60,bg="#81d4fa",font=("Calibri",15,"bold"),relief="flat")

btnsalir= Button(ventana,image=imgsalir,command=salir)
btnsalir.place(x=670,y=240)
btnsalir.config(width=70,height=60,bg="#81d4fa",font=("Calibri",15,"bold"),relief="flat")

#Slida
ventana.mainloop()
#FIN