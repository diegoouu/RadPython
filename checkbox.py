import tkinter as tk

janela = tk.Tk()
janela.title("Islaide das parada")
janela.geometry('300x300+800+300')

def mostrar_valores():
    print(w1.get(), w2.get())
w1 = tk.Scale(janela, from_=0, to=50)
w1.pack()

w2 = tk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)
w2.pack()

tk.Button(janela, text="Mostrar a Escala", command=mostrar_valores).pack()


janela.mainloop()