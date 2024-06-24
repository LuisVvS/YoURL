import re
import requests
from bs4 import BeautifulSoup




def main():
    url = verify( input("Put the link here: ").strip())
    if(url == False):
        print("Não é um link valido")
    else:
        page = requests.get(url)
        html_content = page.content
        soup = BeautifulSoup(html_content, "html.parser")
        title(soup)
        description(soup)
#supported links
#https://www.youtube.com/watch?v=iQeBYPJWtak
#http://youtu.be/cCnrX1w5luM
#http://youtube/cCnrX1w5luM 
#youtube/cCnrX1w5luM
#youtu.be/cCnrX1w5luM
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=43s
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&at=25
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1
#https://www.youtube.com/watch?v=dQw4w9WgXcQ#t=1m30s
#https://www.youtube.com/embed/dQw4w9WgXcQ
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PL9tY0BWXOZFtAk_vlObsc1kYM3Imi2F98&index=3
#https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley


def verify(s):
    if re.search(r"^(https?:)?(\/\/)?(www\.)?(youtube(\.com)?|youtu.be)(\/)((watch\?v=)?\w+)(&\w+=\S+)?((embed)?\/\w+)?(#\S+)?$",s):
        return s
    else:
        return False 

def title(t,):
    title_tag = t.find("meta", itemprop="name")
    print(title_tag["content"])

def author(a):
    ...

def description(d):
    des_tag = d.find("meta", itemprop="description")
    print(des_tag["content"])

def date(dat):
    ...

if __name__=="__main__":
    main()

#fazer o autor e a data de postagem do video