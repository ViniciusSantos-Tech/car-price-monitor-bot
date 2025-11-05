#𝐅𝐞𝐢𝐭𝐨 𝐩𝐨𝐫 𝐕𝐢𝐧𝐢𝐜𝐢𝐮𝐬 𝐒𝐚𝐧𝐭𝐨𝐬-𝐓𝐞𝐜𝐡
#𝑪𝑨𝑹𝑹 𝑺𝑪𝑹𝑨𝑷𝑷𝑰𝑵𝑮 + 𝑻𝑲𝑰𝑵𝑻𝑬𝑹

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd
import csv
from tkinter import *
import pywhatkit
import csv
import pandas as pd

def  Preço_Fast():
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
            text2 = '✅Salvo em Xlsx!'
            Excel_salvo.config(text=text2)
            text = f'Preço: {Fiat}'
            Texto_Preço.config(text=text)
            pywhatkit.sendwhatmsg_instantly(
                "+55212345678910",
                f"O preço do Fiat Fastback esta: {Fiat}"
            )
            driver.quit()
            break
        except:
            print("")


Preço = Tk()
Preço.title("Fiat FastBack Price")
Preço.geometry("245x250")  
Preço.resizable(False, False)
Preço.configure(bg="#F0F0F0")

Preço.eval('tk::PlaceWindow . center')

instrucao = Label(Preço, 
                  text="Clique para ver o preço atual:", 
                  font=("Segoe UI", 12, "bold"),
                  bg="#F0F0F0",
                  fg="#333333")
instrucao.grid(column=0, row=0, pady=10)

Botao = Button(Preço, 
               text="🔍 BUSCAR PREÇO", 
               command=Preço_Fast, 
               font=("Segoe UI", 11, "bold"),
               width=15, 
               height=2,
               bg="#4CAF50",
               fg="white",
               relief="raised",
               borderwidth=3)
Botao.grid(column=0, row=1, pady=10)

Texto_Preço = Label(Preço, 
                    text="", 
                    font=("Segoe UI", 14, "bold"),
                    bg="#F0F0F0",
                    fg="#2E8B57")
Texto_Preço.grid(column=0, row=2, pady=10)

Excel_salvo = Label(Preço, 
                    text="", 
                    font=("Segoe UI", 10, "bold"),
                    bg="#F0F0F0",
                    fg="#FF6B00")
Excel_salvo.grid(column=0, row=3, pady=5)

Preço.mainloop()
