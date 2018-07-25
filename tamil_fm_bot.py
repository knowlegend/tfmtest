#Install telegram bot , schedule , wget , beautifulsoup,pandas before deploying
import telegram
import schedule
import time
import requests
import bs4
import os
import wget
import re
import pandas as pd


bot = telegram.Bot(token="579089832:AAFcH3QPjgtVfzPuc-2563hMiMN_izI7aLA")


def tamil_news(area_id,op_filename):
    url = "http://www.newsonair.com/regional-audio.aspx"
    res = requests.get(url)
    soup=bs4.BeautifulSoup(res.text,'lxml')

    area_link = soup.findAll('audio')
    area_link_str=str(area_link)
    src= re.findall("src=[^\s]*", area_link_str)

    string = area_id
    for s in src:
        if string in str(s):
            s_index=src.index(s)
    download_link=src[s_index][5:-1]
    if os.path.isfile(op_filename):
        os.remove(op_filename)
    else:
        filename = wget.download(download_link,out=op_filename)
        bot.send_audio(chat_id="@test_42", audio=open(op_filename, 'rb'),
               title='Tamil FM News',caption=op_filename.split('.')[0],performer='All India Radio')

chennai_mor_id="Chennai-Tamil-0645"
chennai_evening_id="Chennai-Tamil-1830"
trichy_id="Tiruchirapalli-Tamil"
pudhucherry_id="Pudducherry-Tamil"
chennai_mor_filename="Chennai morning news.mp3"
chennai_evening="Chennai evening news.mp3"
trichy_filename="Trichy FM News.mp3"
pudhucherry_filename="Pudhucherry FM News.mp3"


def veg_price():
    
    veg_url="https://www.livechennai.com/Vegetable_price_chennai.asp"
    vg_price=pd.read_html(veg_url)
    df=pd.DataFrame(vg_price[1])
    df=df.loc[:,1:2]
    dfstr=df.to_string(index=False,header=False)
    dfstr=dfstr.replace(' ','')
    dfstr=dfstr.replace('NamePrice(Rs)','Name \t\t\t\t\t\t\t\t\t\t\t Price(Rs.)')
    dfstr='🥦🍆🥕 Chennai Vegetable Prices  🥦🍆🥕   \n'+dfstr
    
    bot.send_message(chat_id="@test_42", text=dfstr)   

#schedule.every(1).minutes.do(veg_price)
schedule.every().day.at("01:00").do(veg_price)  #Every morning 6:15 A.M  - Vegetable price
schedule.every().day.at("01:05").do(tamil_news,chennai_mor_id,chennai_mor_filename)  #Morning news chennai
schedule.every().day.at("08:25").do(tamil_news,trichy_id,trichy_filename)  #Afternoon News - Trichy
schedule.every().day.at("12:49").do(tamil_news,pudhucherry_id,pudhucherry_filename)  #Evening news Pudhucherry
schedule.every().day.at("13:09").do(tamil_news,chennai_evening_id,chennai_evening)  #Evening news chennai


while True:
    try:
        schedule.run_pending()
    except Exception:
        time.sleep(4) # wait 4 seconds


#schedule.every().day.at("06:15").do(veg_price)  #Every morning 6:15 A.M  - Vegetable price
#schedule.every().day.at("06:55").do(tamil_news,chennai_mor_id,chennai_mor_filename)  #Morning news chennai
#schedule.every().day.at("13:51").do(tamil_news,trichy_id,trichy_filename)  #Afternoon News - Trichy
#schedule.every().day.at("18:19").do(tamil_news,pudhucherry_id,pudhucherry_filename)  #Evening news Pudhucherry
#schedule.every().day.at("18:39").do(tamil_news,chennai_evening_id,chennai_evening)  #Evening news chennai
