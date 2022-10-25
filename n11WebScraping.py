import requests
from bs4 import BeautifulSoup
import pandas as pd


url = ["https://www.n11.com/bilgisayar/dizustu-bilgisayar","https://www.n11.com/bilgisayar/dizustu-bilgisayar?ipg="]
liste = []
a=1
b=0
while a<=50:

    if a==1:
        r = requests.get(url[0])
        soup = BeautifulSoup(r.content, "lxml")
        urunler = soup.find_all("li",attrs= {"class":"column"})
        for urun in urunler:
            urun_link = urun.a.get("href")
            urun_ozellik = urun.a.get("title")
            urun_img = urun.find("div", attrs = {"class":"cargoCampaign"}).img.get("src")
            urun_price = urun.find("div",attrs={"class":"priceContainer"}).find_all("span",attrs={"class":"priceEventClick"})[1].text.strip()
            r2 = requests.get(urun.a.get("href"))
            soup2= BeautifulSoup(r2.content,"lxml")
            ozellikler = soup2.find_all("li",attrs={"class":"unf-prop-list-item"})
            for ozellik in ozellikler:
                if ozellik.find("p",{"class":"unf-prop-list-title"}).text=="İşlemci":
                    urun_islemci = ozellik.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik.find("p",{"class":"unf-prop-list-title"}).text=="İşletim Sistemi":
                    urun_isletim_sistemi = ozellik.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik.find("p",{"class":"unf-prop-list-title"}).text=="Bellek Kapasitesi":
                    urun_ram = ozellik.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik.find("p",{"class":"unf-prop-list-title"}).text=="Disk Kapasitesi":
                    urun_ssd = ozellik.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik.find("p",{"class":"unf-prop-list-title"}).text=="Ekran Çözünürlüğü":
                    urun_cozunurluk = ozellik.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik.find("p",{"class":"unf-prop-list-title"}).text=="Ekran Boyutu":
                    urun_ekran_boyutu = ozellik.find("p",{"class":"unf-prop-list-prop"}).text
            liste.append([urun_ozellik,urun_link,urun_img,urun_price,urun_islemci,urun_isletim_sistemi,urun_ram,urun_ssd,urun_cozunurluk,urun_ekran_boyutu])
            b+=1
    else:
        r1 = requests.get(url[1]+str(a)) 
        soup1= BeautifulSoup(r1.content,"lxml")
        urunler1 = soup1.find_all("li",attrs={"class":"column"})
        for urun1 in urunler1:
            urun_link1 = urun1.a.get("href")
            urun_ozellik1 = urun1.a.get("title")
            urun_img1 = urun1.find("div",{"class":"cargoCampaign"}).img.get("src")
            urun_price1 = urun1.find("div",attrs={"class":"priceContainer"}).find_all("span",attrs={"class":"priceEventClick"})[1].text.strip()
            r3 = requests.get(urun1.a.get("href"))
            soup3 = BeautifulSoup(r3.content,"lxml")
            ozellikler2 = soup3.find_all("li",attrs={"class":"unf-prop-list-item"})
            for ozellik1 in ozellikler2:
                if ozellik1.find("p",{"class":"unf-prop-list-title"}).text=="İşlemci":
                    urun_islemci1 = ozellik1.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik1.find("p",{"class":"unf-prop-list-title"}).text=="İşletim Sistemi":
                    urun_isletim_sistemi1 = ozellik1.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik1.find("p",{"class":"unf-prop-list-title"}).text=="Bellek Kapasitesi":
                    urun_ram1 = ozellik1.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik1.find("p",{"class":"unf-prop-list-title"}).text=="Disk Kapasitesi":
                    urun_ssd1 = ozellik1.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik1.find("p",{"class":"unf-prop-list-title"}).text=="Ekran Çözünürlüğü":
                    urun_cozunurluk1 = ozellik1.find("p",{"class":"unf-prop-list-prop"}).text
                if ozellik1.find("p",{"class":"unf-prop-list-title"}).text=="Ekran Boyutu":
                    urun_ekran_boyutu1 = ozellik1.find("p",{"class":"unf-prop-list-prop"}).text
                        
            liste.append([urun_ozellik1,urun_link1,urun_img1,urun_price1,urun_islemci1,urun_isletim_sistemi1,urun_ram1,urun_ssd1,urun_cozunurluk1,urun_ekran_boyutu1])
            b+=1
    a+=1        

print(b)
df = pd.DataFrame(liste)
df.columns=["ürün adı","ürün linki","ürün resmi","ürün fiyatı","ürün işlemci","ürün işletim sistemi","ürün ram","ürün ssd","ürün çözünürlük","ürün ekran boyutu"]
df.to_excel("n11ButunVeri.xlsx")

        



    
    



       