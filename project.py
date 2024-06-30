import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from colorama import init, Fore, Style
from googleapiclient.discovery import build

init()

def main():
    url = verify(input("Put the link here: ").strip())
    if not url :
        print("Não é um link valido")
    else:
        print("Link valido")

        page = requests.get(url)
        html_content = page.content.decode('utf-8')
        soup = BeautifulSoup(html_content, "html.parser")

        ti = title(soup)
        des = description(soup)
        aut = author(soup)
        dat = date(soup)
        genre = gen(soup)
        verif(soup)
        likes(aut)
        if(isfamily(soup) == "true"):
            isf = "yes"
        else:
            isf = "no"

    data = [
        ["Name Of Channel", aut],
        ["Title",ti], 
        ["Date of the Video",dat], 
        ["Description",des],
        ["Is Family Frind? ",isf],
        ["Genre",genre ]
            ]
    
    print(tabulate(data, headers=[Fore.GREEN + Style.BRIGHT + "About the Video" + Style.RESET_ALL, Fore.RED + Style.BRIGHT + "Values" + Style.RESET_ALL], tablefmt="heavy_grid"))

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
    #teste = g.find("div")
    #print(teste.prettify())

    genre_tag = g.find("meta", itemprop="genre")
    return genre_tag["content"]

def likes(author):
    api_key = ""
    
    youtube = build(
        "youtube",
        "v3",
        developerKey=api_key
    ) 

    request = youtube.channels().list(
        part = "statistics",
        forUserName = "kksaiko"
    )
    response = request.execute()
    print(response) 

def verif(ver): 
    ...
if __name__=="__main__":
    main()


#saber melhor como funciona a API do youtube
#tentar pegar o ID para utilizar no request para pegar as estatisticas do canal do youtube(caso não dê pelo nome)
#melhorar a saida caso ele não ache o titulo ou outro topico.
#talvez implementar a quantidade de likes que o video tem
#Implementar se o canal é verificado ou não


#começar a implementar os teste{
#Estudar como fazer testes melhores
#experiencia com usuario fazer outras pessoas testarem
#pegas os try e except
#    }