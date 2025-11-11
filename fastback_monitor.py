#𝐅𝐞𝐢𝐭𝐨 𝐩𝐨𝐫 𝐕𝐢𝐧𝐢𝐜𝐢𝐮𝐬 𝐒𝐚𝐧𝐭𝐨𝐬-𝐓𝐞𝐜𝐡
#𝑪𝑨𝑹𝑹 𝑺𝑪𝑹𝑨𝑷𝑷𝑰𝑵𝑮 + 𝑻𝑲𝑰𝑵𝑻𝑬𝑹 V2

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd
import tkinter as tk
import os.path
import pywhatkit

_location = os.path.dirname(__file__)

def Preço_Fast():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    while True:
        try:
            driver.get("https://www.brilhautofiat.com.br/novos/novo-fastback-2026/impetus-t200-hybrid-flex")
            sleep(1)
            Fiat = driver.find_element(By.CSS_SELECTOR, ".showcase-new-cars__info-box-price-title--highlight").text
            tb = {
                "Preço": [Fiat]
            }
            Tabela = pd.DataFrame(tb).to_excel("PreçoFiat.xlsx")
            
            Excel_salvo.configure(text='✅Salvo em Xlsx!')
            label_preço.configure(text=f'Preço: {Fiat}')
            
            pywhatkit.sendwhatmsg_instantly(
                "+55212345678910",
                f"O preço do Fiat Fastback esta: {Fiat}"
            )
            driver.quit()
            break
        except:
            print("")


Tela = tk.Tk()
Tela.geometry("539x450+383+106")
Tela.minsize(120, 1)
Tela.maxsize(1370, 749)
Tela.resizable(0, 0)
Tela.title("Sistema de Preços Fiat")
Tela.configure(background="#030042")
Tela.configure(highlightbackground="black")
Tela.configure(highlightcolor="white")

#--------------------------------------------------
Label2 = tk.Label(Tela)
Label2.place(x=-10, y=60, height=371, width=224)
Label2.configure(activebackground="#d9d9d9")
Label2.configure(activeforeground="black")
Label2.configure(anchor='w')
Label2.configure(background="black")
Label2.configure(compound='left')
Label2.configure(disabledforeground="#3f3f3f")
Label2.configure(foreground="white")
Label2.configure(highlightbackground="black")
Label2.configure(highlightcolor="white")
photo_location = os.path.join(_location,"PYTHON DEVELOPER.png")
_img0 = tk.PhotoImage(file=photo_location)
Label2.configure(image=_img0)
Label2.configure(text='''Label''')
#--------------------------------------------------
Label1 = tk.Label(Tela)
Label1.place(x=240, y=80, height=41, width=234)
Label1.configure(activebackground="#d9d9d9")
Label1.configure(activeforeground="black")
Label1.configure(anchor='w')
Label1.configure(background="#090071")
Label1.configure(compound='left')
Label1.configure(disabledforeground="#090071")
Label1.configure(font="-family {Segoe UI} -size 16 -weight bold -slant italic")
Label1.configure(foreground="white")
Label1.configure(highlightbackground="#090071")
Label1.configure(highlightcolor="white")
Label1.configure(text='''PREÇO FIAT FASTBACK''')
#--------------------------------------------------
Label3 = tk.Label(Tela)
Label3.place(x=0, y=20, height=21, width=264)
Label3.configure(activebackground="#d9d9d9")
Label3.configure(activeforeground="black")
Label3.configure(anchor='w')
Label3.configure(background="black")
Label3.configure(compound='left')
Label3.configure(disabledforeground="#3f3f3f")
Label3.configure(foreground="#f1f0ff")
Label3.configure(highlightbackground="#f1f0ff")
Label3.configure(highlightcolor="white")
Label3.configure(text='''fEITO POR VINICIUS SANTOS-TECH''')
#--------------------------------------------------
Button1 = tk.Button(Tela)
Button1.place(x=270, y=150, height=26, width=167)
Button1.configure(activebackground="#d9d9d9")
Button1.configure(activeforeground="black")
Button1.configure(background="black")
Button1.configure(compound='left')
Button1.configure(disabledforeground="#3f3f3f")
Button1.configure(font="-family {Segoe UI} -size 9 -weight bold -slant italic")
Button1.configure(foreground="#f9f9ff")
Button1.configure(highlightbackground="black")
Button1.configure(highlightcolor="white")
Button1.configure(text='''Buscar Preço''')
Button1.configure(command=Preço_Fast) 
#--------------------------------------------------
label_preço = tk.Label(Tela)
label_preço.place(x=270, y=200, height=40, width=200)
label_preço.configure(background="#030042")
label_preço.configure(foreground="#00FF00")
label_preço.configure(font=("Arial", 12, "bold"))
label_preço.configure(text="Preço aparecerá aqui")
#--------------------------------------------------
Excel_salvo = tk.Label(Tela)
Excel_salvo.place(x=270, y=250, height=20, width=200)
Excel_salvo.configure(background="#030042")
Excel_salvo.configure(foreground="#FF6B00")
Excel_salvo.configure(font=("Arial", 10, "bold"))
Excel_salvo.configure(text="")

Tela.mainloop()
