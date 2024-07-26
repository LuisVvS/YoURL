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
    # try:
        url = verify(input("Put the link here: ").strip())
        if not url :
            print("Invalid")
        else:
            page = requests.get(url)
            html_content = page.content.decode('utf-8')
            soup = BeautifulSoup(html_content, "html.parser")

            

            ti = title(soup)
            # des = description(soup)
            aut = author(soup)
            dat = date(soup)
            genre = gen(soup)
            video = video_id(soup)

            #get the subscribers of a channel
            channel_ID = data(aut)
            subs = subscriber(channel_ID)
            like = likes(video)
            view = Views(video)
            vratio = viewRatio(subs,view)
            lratio = likeRatio(view,like)
            if(isfamily(soup) == "true"):
                isf = "yes"
            else:
                isf = "no"

            data_you = [
                ["Name Of Channel", aut],
                ["Title",ti], 
                ["Date of the Video",dat], 
                ["Is Family Frind? ",isf],
                ["Genre",genre],
                ["Subscribers",subs],
                ["Likes",like],
                ["View Ratio", vratio],
                ["Like Ratio", lratio]
                    ]

            print(tabulate(data_you, headers=[Fore.GREEN + Style.BRIGHT + "About the Video" + Style.RESET_ALL, Fore.RED + Style.BRIGHT + "Values" + Style.RESET_ALL], tablefmt="heavy_grid"))
    # except(KeyError, TypeError, ValueError, IndexError):
    #    print("Maybe this is not a valid youtube video, please virify again") 

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
#https://www.youtubee.com/watch?v=dQw4w9WgXcQ


def verify(s):
    #if re.search(r"^(https?:)?(\/\/)?(www\.)?(youtube(\.com)?|youtu.be)(\/)((watch\?v=)?(\w+\??\w+=\w+)?)(&\w+=\S+)?((embed)?\/\w+)?(#\S+)?$",s):
    if re.search(r"^((https?:)?(\/\/))?((www|m)?\.)?((youtube(-nocookie)?\.com|youtu.be)\/)((embed|[\w]+\?v=)|v\/)?(\S+)$", s):
        return s
    else:
        return False 

def title(t):
    try:
        title_tag = t.find("meta", itemprop="name")
        return title_tag["content"]
    except(TypeError, ValueError, IndexError):
        return "tittle not found"

def author(a):
    try:
        container = a.find("div")
        author_tag = container.find("link", itemprop="name")
        return author_tag["content"]
    except(TypeError, ValueError, IndexError):
        return "author not found"

# def description(d):
#     des_tag = d.find("meta", itemprop="description")
#     return des_tag["content"]

def date(dat):
    try:

        date_tag = dat.find("meta", itemprop="datePublished")
        date = date_tag["content"].split("T")
        return date[0]
    except(TypeError,ValueError, IndexError):
        return "date not found"

def isfamily(f):
    try:

        tag_family = f.find("meta", itemprop="isFamilyFriendly")
        return tag_family["content"]
    except(TypeError, ValueError, IndexError):
        return "tag not found"

def gen(g):
    #pra ver como é o html geral, muito util para proximas implementações
    # teste = g.find("div")
    # print(teste.prettify())
    try:
        genre_tag = g.find("meta", itemprop="genre")
        return genre_tag["content"]
    except(TypeError, ValueError, IndexError):
        return "genre not found"

def subscriber(channel):
    try:
        #pego a api_KEY
        api_key = os.getenv("API_KEY")
        
        youtube = build(
            "youtube",
            "v3",
            developerKey=api_key
        )    
        #busco as estatisticas do canal
        request = youtube.channels().list(
            part = "statistics",
            id = channel 
        )
        response = request.execute()
        #vou atras do numero de inscritos 
        subs = int(response["items"][0]["statistics"]["subscriberCount"])
        return subs 
    except(KeyError, IndexError, ValueError):
        return "subscriberCount not found"

def video_id(url):
    try:
        #pego o id do video do youtube pela url
        video_id = url.find("meta", itemprop="identifier")
        vid = video_id["content"]
        return vid
    except (KeyError, TypeError, IndexError):
        return "video id not found"


def likes(vid):
    try:

        # pego a API
        api_key = os.getenv("API_KEY")
        
        #contruo um objeto, utilizo o youtube e o v3, mesmos parametros do string_format, e a chave da API
        youtube = build(
            "youtube",
            "v3",
            developerKey=api_key
        ) 

        #crio o request para acessar os videos, na part de estatisticas e utilizando o id do video
        request = youtube.videos().list(
            part = "statistics",
            id = vid 
        )

        #executo essa request
        response = request.execute()

        #retorno essa request
        like = int(response["items"][0]["statistics"]["likeCount"])
        return like 

    except(TypeError, IndexError, KeyError, ValueError):
        return "likes not found"

def Views(vid):
    try:

        # pego a API
        api_key = os.getenv("API_KEY")
        
        #contruo um objeto, utilizo o youtube e o v3, mesmos parametros do string_format luis, e a chave da API
        youtube = build(
            "youtube",
            "v3",
            developerKey=api_key
        ) 

        #crio o request para acessar os videos, na part de estatisticas e utilizando o id do video
        request = youtube.videos().list(
            part = "statistics",
            id = vid 
        )

        #executo essa request
        response = request.execute()

        #retorno essa request
        return int(response["items"][0]["statistics"]["viewCount"])

    except(KeyError, TypeError, IndexError, ValueError):
        return "View count not found"

def viewRatio(s,v):
    try:
        ratio_v = (v/s)*100

        return "{:.2f}%".format(ratio_v) 
    except(KeyError, TypeError, ValueError):
        return "Not possible to calculate ViewRatio"

def likeRatio(v,l):
    try:
        like_rat = (l/v)*100
        return "{:.2f}%".format(like_rat)
    except(TypeError, ValueError):
        return "Like Ratio not found"
    
def data(name):
    # pesquiso pelo google api com o nome do canal
    string_format = f"https://www.googleapis.com/youtube/v3/search?&q={name.replace(" ", "%20")}&key={os.getenv("API_KEY")}"
    age = requests.get(string_format)
    data = age.json()
    # busco no arquibo json o ID do canal
    try:
        index = 0
        while(True):
            #verifico onde ficar o youtube#channel para pegar o id
            #vou buscando pelo indice, caso não ache em um indice, vou para o proximo
                if data["items"][index]["id"]["kind"] == "youtube#channel":
                    return data["items"][index]["id"]["channelId"]
                else:
                    index+=1
    except(KeyError, IndexError, ValueError):
        return "Id not found"


def get_request1():
    name = "Cellbit"
    fs = f"https://www.googleapis.com/youtube/v3/search?q={name}&key={os.getenv("API_KEY")}"
    response = requests.get(fs)
    if response.ok:
        return response
    else:
        return None

if __name__ == "__main__":    
    main()