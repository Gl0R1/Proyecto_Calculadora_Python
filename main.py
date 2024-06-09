from tkinter import *
import tkinter.font as tkFont

#ventana va a ser la raiz
ventana = Tk()

font_negrita = tkFont.Font(family="Times New Roman", size=15, weight="bold")
font_boton = tkFont.Font(family="Times New Roman", size=11, weight="bold")
ventana.configure(background='#ffea93')
ventana.title('Calculadora')
ventana.geometry('305x410') #ancho x alto
ventana.resizable(0, 0) #es para que el ususario no modifique el tamaño de la ventana

i = 0
datos = Entry(ventana, font=font_negrita)
datos.grid(row=0 , column=0, columnspan=4, ipadx=45, ipady=15, pady=(8, 4))


#Funciones
def click_boton(valor):
  global i
  datos.insert(i,valor)
  i += 1
   
def borrar():
  datos.delete(0, END)    
  i = 0
  
def operacion():
  ecuacion = datos.get()
  resultado = eval(ecuacion)
  datos.delete(0, END)
  datos.insert(0, resultado)
  i = 0  
              
#botones
boton_borrar = Button(ventana, text='C', bg='#ff820f', fg='white', font=font_boton, width=5, height=2, command= lambda:  borrar())
boton_parentesis1 = Button(ventana, text='(', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5,height=2, command= lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text=')', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2, command= lambda: click_boton(")"))
boton_punto = Button(ventana, text='.', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2, command= lambda: click_boton("."))

boton0= Button(ventana, text='0', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2, command= lambda: click_boton(0))
boton1= Button(ventana, text='1', bg='#f3f3f3', fg='#ff7705',font=font_boton,  width=5, height=2, command= lambda: click_boton(1))
boton2= Button(ventana, text='2', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2, command= lambda: click_boton(2))
boton3= Button(ventana, text='3', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2,command= lambda: click_boton(3))
boton4= Button(ventana, text='4', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2,command= lambda: click_boton(4))
boton5= Button(ventana, text='5', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2,command= lambda: click_boton(5))
boton6= Button(ventana, text='6', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2,command= lambda: click_boton(6))
boton7= Button(ventana, text='7', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2,command= lambda: click_boton(7))
boton8= Button(ventana, text='8', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2,command= lambda: click_boton(8))
boton9= Button(ventana, text='9', bg='#f3f3f3', fg='#ff7705', font=font_boton, width=5, height=2,command= lambda: click_boton(9))

boton_div= Button(ventana, text='/', bg='#ff820f', fg='white', font=font_boton, width=5, height=2,command= lambda: click_boton("/"))
boton_multi= Button(ventana, text='x', bg='#ff820f', fg='white', font=font_boton, width=5, height=2,command= lambda: click_boton("*"))
boton_suma= Button(ventana, text='+', bg='#ff820f', fg='white', font=font_boton, width=5, height=2,command= lambda: click_boton("+"))
boton_resta= Button(ventana, text='-', bg='#ff820f', fg='white', font=font_boton, width=5, height=2,command= lambda: click_boton("-"))
boton_igual= Button(ventana, text='=', bg='#ff820f', fg='white', font=font_boton, width=5, height=2,command= lambda: operacion())


#botones en pantalla
boton_borrar.grid(row=1, column=0, ipadx=5, ipady=5, padx=5)
boton_parentesis1.grid(row=1, column=1, ipadx=5, ipady=5, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, ipadx=5, ipady=5, padx=5, pady=5)
boton_div.grid(row=1, column=3, ipadx=5, ipady=5, padx=5, pady=5)

boton7.grid(row=2, column=0, ipadx=5, ipady=5,padx=5)
boton8.grid(row=2, column=1, ipadx=5, ipady=5, padx=5, pady=5)
boton9.grid(row=2, column=2, ipadx=5, ipady=5, padx=5, pady=5)
boton_multi.grid(row=2, column=3, ipadx=5, ipady=5, padx=5, pady=5)


boton4.grid(row=3, column=0, ipadx=5, ipady=5, padx=5)
boton5.grid(row=3, column=1, ipadx=5, ipady=5, padx=5, pady=5)
boton6.grid(row=3, column=2, ipadx=5, ipady=5, padx=5, pady=5)
boton_suma.grid(row=3, column=3, ipadx=5, ipady=5, padx=5, pady=5)

boton1.grid(row=4, column=0, ipadx=5, ipady=5, padx=5)
boton2.grid(row=4, column=1, ipadx=5, ipady=5, padx=5, pady=5)
boton3.grid(row=4, column=2, ipadx=5, ipady=5, padx=5, pady=5)
boton_resta.grid(row=4, column=3, ipadx=5, ipady=5, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, ipadx=40, ipady=5, padx=5)
boton_punto.grid(row=5, column=2, ipadx=5, ipady=5, padx=5, pady=5)
boton_igual.grid(row=5, column=3, ipadx=5, ipady=5, padx=5, pady=5)

ventana.mainloop()