import tkinter as tk
from tkinter import messagebox
from cotacao import main, gravar_em_arquivo

class App():
    def __init__(self, toplevel):
        toplevel.geometry("250x100")
        toplevel.title('Cotação')
        self.frame1 = tk.Frame(toplevel)
        self.frame1.pack(fill='both', padx=10, pady=10)
        self.frame2 = tk.Frame(toplevel)
        self.frame2.pack(fill='both', padx=10, pady=10)

        self.label = tk.Label(self.frame1, text='1-Dolar ou 2-Euro')
        self.label.pack(side='left')
        self.moeda = tk.Entry(self.frame1, width=10)
        self.moeda.pack(side='right')
        self.button = tk.Button(self.frame2, text='Consultar', command=self.consultar)
        self.button.pack(side='left')
        self.label2 = tk.Label(self.frame2, text='')
        self.label2.pack(side='right')

    def consultar(self):
        moeda = self.moeda.get()
        if moeda == '1':
            moeda = 'USD'
        elif moeda == '2':
            moeda = 'EUR'
        else:
            messagebox.showinfo('Digite apenas 1 ou 2.')
          
        valor = f'{moeda} -> R${main(moeda)}'
        self.label2['text'] = valor
        gravar_em_arquivo(valor)



raiz = tk.Tk()
app = App(raiz)
raiz.mainloop()
