import webbrowser
import threading
import time
from tkinter import Tk, Button


# Função para abrir o Google
def open_google():
    webbrowser.open('http://www.google.com')
    
def abrir_outro_documento():
        caminho_outro_documento ='main.py'
        import subprocess
        subprocess.Popen(["python", caminho_outro_documento])

# Função para alternar o foco entre os botões
def scan_buttons(button1, button2, button3,button4, interval):
    while True:
        button1.focus_set()#
        time.sleep(interval)
        button2.focus_set()
        time.sleep(interval)
        button3.focus_set()
        time.sleep(interval)
        button4.focus_set()
        time.sleep(interval)
        

# Configuração da janela principal
root = Tk()
root.title('Varredura de Botões')

# Criação dos botões
button1 = Button(root, text='Botão 1', command=abrir_outro_documento)
button2 = Button(root, text='Botão 2', command=open_google)
button3 = Button(root, text='Botão 3', command=open_google)
button4 = Button(root, text='Botão 4', command=open_google)

# Posicionamento dos botões
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')
button4.pack(side='left')

# Definindo o intervalo de tempo para a varredura (em segundos)
interval = 4

# Iniciando a varredura em uma thread separada para não congelar a interface gráfica
threading.Thread(target=scan_buttons, args=(button1, button2, button3, button4, interval), daemon=True).start()

# Iniciando o loop principal da interface gráfica
root.mainloop()
