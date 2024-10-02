
#Passo a passo - Coisas que vai ter no seu site ou aplicativo 
#Cabeçalho ()
#Grafico Eletomiografia 
#Quatro Botões (1.Calibragem(jogo + volume);2. Acessar GOOGLE; 3.Aplicativos(microssoft-word...); 4.Fidbak- exel ) 
#Varredura 
#Rodapé - configurações administrador -feedback
   
from tkinter import *
from typing import Any
#import plotly.express as px 
#from flet.plotly_chart import PlotlyChart #Grafico
    
import flet as ft #pip install flet -> no terminal 
    
class MyButton(ft.ElevatedButton): #Classe para estilo do botão
    def __init__(self, text, on_click):
        super().__init__()
        self.bcolor = ft.colors.BLUE_400
        self.color = ft.colors.GREEN_800
        self.text = text
        self.on_click = on_click
        self.width=200
        
def main(pagina): # main - função que vai por padrão receber como parametro a pagina do seu aplicativo
    pagina.title = "Aplicativo MuscleCommunication"
    pagina.bgcolor = ft.colors.CYAN_50# Atualiza a cor de fundo da página para cinza
 
    def theme_changed(e): # Interruptor (claro noite) - òsteiormente vai sinalizar a Comunicação hardware e Software
        pagina.theme_mode = (
            ft.ThemeMode.DARK
            if pagina.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        c.label = (
            "Light theme" if pagina.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        pagina.update()
    c = ft.Switch(on_change=theme_changed) #Descubra como Excluir isso!!!
    pagina.add(c)

    pagina.theme_mode = ft.ThemeMode.LIGHT

# DEf do Login  
    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text ="Por favor preencha o seu nome."
            pagina.update()
        else:
            nome = entrada_nome.value
            print(f"Nome: {nome}")
            pagina.clean() #função para limpar a página
            #pagina.add(ft.Text(f"Olá,{nome}")),
#cabeçalho
            pagina.appbar = ft.CupertinoAppBar( 
                bgcolor=ft.colors.BLUE_GREY,
                leading=ft.TextButton((f"Olá, {nome}"),icon=ft.icons.PERSON,  icon_color=ft.colors.WHITE), #Butão para o login
                trailing=ft.Switch( on_change=theme_changed),
                middle=ft.Text("Muscle and Communication", color=ft.colors.WHITE)
               )
#Rodapé
            pagina.navigation_bar = ft.CupertinoNavigationBar( 
                bgcolor=ft.colors.BLUE_GREY,
                inactive_color=ft.colors.GREY,
                active_color=ft.colors.WHITE,
                on_change=lambda e: print("Selected tab:", e.control.selected_index),
                destinations=[
                ft.NavigationDestination(),
                ft.NavigationDestination(),
                ft.NavigationDestination(
                    icon=ft.icons.SETTINGS,
                    selected_icon=ft.icons.SETTINGS,
                    label="Configurações",
                    #label=f"Olá, {nome}",
            ),
        ]
    )
            pagina.add(ft.SafeArea(ft.Text("GRAFICO"))) # Ideia - usar a BIBLIOTECA PANDA 
 #Grafico de eletromiografia 
 # df = px.data.gapminder().query("continent=='Oceania'")
 #   fig = px.line(df, x="year", y="lifeExp", color="country")
 # pagina.add(PlotlyChart(fig, expand=True))
 
#Botões Aqui!!!
            pagina.add(
                ft.ResponsiveRow([
                MyButton (text="Calibração", on_click=abrir_outro_documento), #Jogo + Volume 
                MyButton( text="Google", on_click=abrir_google),
                MyButton(text="Aplicativos", on_click=abrir_aplicativos),
                MyButton(text="Pictogramas", on_click=abrir_google),#Planilha no exel ou uma tabela e posteriormente um Banco de Dados   
               
                ])     
            ) 
            
    
# Empacotando o botão na janela principal 
   
    def abrir_google(e):
        import webbrowser
        webbrowser.open_new("https://www.google.com/")
        janela = ft()
        botao = Button(janela, text="Ir",command=abrir_google)
        botao.pack()
        janela.mainloop()
        pass
    def abrir_outro_documento(e):
        caminho_outro_documento ='main.py'
        import subprocess
        subprocess.Popen(["python", caminho_outro_documento])
        janela = ft()
        botao = Button(janela,text="Abrir outro documento", command=abrir_outro_documento)
        botao.pack()
        janela.mainloop()
    def abrir_aplicativos(e):
        import webbrowser
        webbrowser.open_new("https://www.microsoft365.com")
        janela = ft()
        botao = Button(janela, text="Ir",command=abrir_aplicativos)
        botao.pack()
        janela.mainloop()
        pass
#Coleta dados
    entrada_nome = ft.TextField(label="Digite o seu nome")
    pagina.add(ft.Text("Informe seu Nome:", color="GREEN"))
    pagina.add(
        entrada_nome,
        ft.ElevatedButton("Clique em mim",color="GREEN_800", on_click=login)
    )
#Fim 
    pagina.update()
ft.app(main) #Aplicativo
#ft.app(main, view=ft.WEB_BROWSER) # SITE 