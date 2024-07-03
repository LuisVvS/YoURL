import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from colorama import init, Fore, Style
from googleapiclient.discovery import build
import json
import os
from dotenv import load_dotenv

load_dotenv()

init()

def main():
    url = verify(input("Put the link here: ").strip())
    if not url :
        print("Invalid")
    else:
        page = requests.get(url)
        html_content = page.content.decode('utf-8')
        soup = BeautifulSoup(html_content, "html.parser")

        

        ti = title(soup)
        des = description(soup)
        aut = author(soup)
        dat = date(soup)
        genre = gen(soup)

        #get the subscribers of a channel
        channel_ID = data(aut)
        subs = subscriber(channel_ID)
        like = likes(aut)
        if(isfamily(soup) == "true"):
            isf = "yes"
        else:
            isf = "no"

    data_you = [
        ["Name Of Channel", aut],
        ["Title",ti], 
        ["Date of the Video",dat], 
        ["Description",des],
        ["Is Family Frind? ",isf],
        ["Genre",genre ],
        ["Subscribers",subs]
        # ["Likes",like]
            ]

    print(tabulate(data_you, headers=[Fore.GREEN + Style.BRIGHT + "About the Video" + Style.RESET_ALL, Fore.RED + Style.BRIGHT + "Values" + Style.RESET_ALL], tablefmt="heavy_grid"))
    print(like) 

#supported links
#https://www.youtube.com/watch?v=iQeBYPJWtak
#http://youtu.be/cCnrX1w5luM
#http://youtube/cCnrX1w5luM 
#youtu.be/cCnrX1w5luM
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=43s
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&at=25
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1
#https://www.youtube.com/watch?v=dQw4w9WgXcQ#t=1m30s
#https://www.youtube.com/embed/dQw4w9WgXcQ
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PL9tY0BWXOZFtAk_vlObsc1kYM3Imi2F98&index=3
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley
#https://youtu.be/ofmSXnoS7FE?si=FPIUjUDnEqJBzEe4
#https://www.youtube.com/watch?v=hv-hbublepc
#https://www.youtube.com/watch?v=DFYRQ_zQ-gk&feature=featured
#https://m.youtube.com/watch?v=DFYRQ_zQ-gk
#https://www.youtube.com/v/DFYRQ_zQ-gk?fs=1&hl=en_US
#https://www.youtube-nocookie.com/embed/DFYRQ_zQ-gk?autoplay=1


#-----------USAR NOS TESTES de links errados ----------- 
#youtube/cCnrX1w5luM
#https://y.youtube.com/watch?v=DFYRQ_zQ-gk
#https://ww.youtube.com/watch?v=RTUffsKQFVw


def verify(s):
    #if re.search(r"^(https?:)?(\/\/)?(www\.)?(youtube(\.com)?|youtu.be)(\/)((watch\?v=)?(\w+\??\w+=\w+)?)(&\w+=\S+)?((embed)?\/\w+)?(#\S+)?$",s):
    if re.search(r"^((https?:)?(\/\/))?((www|m)?\.)?((youtube(-nocookie)?\.com|youtu.be)\/)((embed|[\w]+\?v=)|v\/)?(\S+)$", s):
        return s
    else:
        return False 

def title(t):
    title_tag = t.find("meta", itemprop="name")
    return title_tag["content"]

def author(a):
    container = a.find("div")
    author_tag = container.find("link", itemprop="name")
    return author_tag["content"]

def description(d):
    des_tag = d.find("meta", itemprop="description")
    return des_tag["content"]

def date(dat):
    date_tag = dat.find("meta", itemprop="datePublished")
    date = date_tag["content"].split("T")
    return date[0]

def isfamily(f):
    tag_family = f.find("meta", itemprop="isFamilyFriendly")
    return tag_family["content"]

def gen(g):
    #pra ver como é o html geral, muito util para proximas implementações
    # teste = g.find("div")
    # print(teste.prettify())

    genre_tag = g.find("meta", itemprop="genre")
    return genre_tag["content"]

def subscriber(channel):
    api_key = os.getenv("API_KEY")
    
    youtube = build(
        "youtube",
        "v3",
        developerKey=api_key
    ) 

    request = youtube.channels().list(
        part = "statistics",
        id = channel 
    )
    response = request.execute()
    
    subs = int(response["items"][0]["statistics"]["subscriberCount"])
    return  f"{subs:,}" 

def likes(name):
    string_format = f"https://www.googleapis.com/youtube/v3/search?&q={name.replace(" ", "%20")}&key=AIzaSyD5GiWNf2zZSpnbB9usmn6U_wIdSVN2n0U"
    age = requests.get(string_format)
    data = age.json()
    cha = data["items"][0]["id"]["channelId"]

    api_key = os.getenv("API_KEY")

    youtube = build(
        "youtube",
        "v3",
        developerKey=api_key
    ) 

    request = youtube.channels().list(
        part = "statistics",
        id = cha 
    )
    response = request.execute()
    
    likes = response
    return likes

def deslikes():
    ...

def subtitle():
    ...

def monetized():
    ...

def data(name):
    string_format = f"https://www.googleapis.com/youtube/v3/search?&q={name.replace(" ", "%20")}&key=AIzaSyD5GiWNf2zZSpnbB9usmn6U_wIdSVN2n0U"
    age = requests.get(string_format)
    data = age.json()
    id_channel = data["items"][0]["id"]["channelId"]
    return id_channel

if __name__=="__main__":
    main()

#antes de dar qualquer commit, preciso saber esconder a chave API que eu tenho
#talvez implementar a quantidade de likes que o video tem
#Implementar se o canal é verificado ou não


#começar a implementar os teste{
#Estudar como fazer testes melhores
#experiencia com usuario fazer outras pessoas testarem
#pegas os try e except
#    }