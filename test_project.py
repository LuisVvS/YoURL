from project import verify,likes,Views,ViewRatio,data, subscriber, isfamily, gen, date, author, title
import requests 
from bs4 import BeautifulSoup

def test_status():
    assert requests.get("https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s").status_code == 200
    assert requests.get("https://www.youtube.com/watch?v=9WCE0s3hvhQ").status_code == 200
    assert requests.get("https://www.youtube.com/watch?v=h").status_code == 200

def test_verify():
    assert verify("https://www.youtube.com/watch?v=9WCE0s3hvhQ") == "https://www.youtube.com/watch?v=9WCE0s3hvhQ" 
    assert verify("https://y.youtube.com/watch?v=DFYRQ_zQ-gk") == False
    assert verify("https://ww.youtube.com/watch?v=RTUffsKQFVw") == False 
    assert verify("https://www.youtubee.com/watch?v=dQw4w9WgXcQ") == False
    assert verify("https://www.youtube.com/watch?v=") == "https://www.youtube.com/watch?v=" 
    assert verify("https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s") == "https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s"
    assert verify("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PL9tY0BWXOZFtAk_vlObsc1kYM3Imi2F98&index=3") == "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PL9tY0BWXOZFtAk_vlObsc1kYM3Imi2F98&index=3"
    assert verify("youtu.be/cCnrX1w5luM") == "youtu.be/cCnrX1w5luM"
    assert verify("https://www.youtube.com/v/DFYRQ_zQ-gk?fs=1&hl=en_US") == "https://www.youtube.com/v/DFYRQ_zQ-gk?fs=1&hl=en_US"
    assert verify("https://www.youtube-nocookie.com/embed/DFYRQ_zQ-gk?autoplay=1") == "https://www.youtube-nocookie.com/embed/DFYRQ_zQ-gk?autoplay=1"


def test_likes():
   assert likes("https://www.youtube.com/watch?v=") == "likes not found"
   assert likes("https://www.youtubee.com/watch?v=dQw4w9WgXcQ") == "likes not found"
   

def test_data():
    assert data("kksaiko") == "UCV3XpRxabX2UMbimv2k215Q"
    assert data("typecraft") == "UCo71RUe6DX4w-Vd47rFLXPg"
    assert data("kasljdaslkjd") == "Id not found"
    assert data("https://www.youtube.com/watch?v=") == "Id not found"
    assert data("UCo71RUe6DX4w-Vd47rFLXPg") == "Id not found"

def test_tittle():
    page = requests.get("https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s")
    html_content = page.content.decode("utf-8")
    soup = BeautifulSoup(html_content, "html.parser")
    title_tag = soup.find("meta", itemprop="name")
    
    # assert requests.get("https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s")  == title_tag["content"]
    # assert title()
    

