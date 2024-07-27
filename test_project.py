from bs4 import BeautifulSoup
from unittest.mock import Mock, patch
import requests
from project import likes, get_request1, data, views, subscriber,likeRatio,viewRatio,verify,title,author,date,isfamily,gen

def test_Like_Ratio():
    assert likeRatio(60,100) == "166.67%" 
    assert likeRatio("luis", 60) == "Like Ratio not found"
    assert likeRatio("asjd", "lskjda") == "Like Ratio not found"
    assert likeRatio(30,"2931") == "Like Ratio not found"
    assert likeRatio("40","20") == "Like Ratio not found"
    assert likeRatio(5000,20000) == "400.00%"

def test_View_Ratio():
    assert viewRatio(5000000,200000) ==  "4.00%"
    assert viewRatio(5000, 1000) == "20.00%" 
    assert viewRatio(500,200) == "40.00%"  
    assert viewRatio("2000", "299") == "Not possible to calculate ViewRatio" 
    assert viewRatio(2000000,"Luis") == "Not possible to calculate ViewRatio"
    assert viewRatio(1.4,"400") == "Not possible to calculate ViewRatio"
    assert viewRatio("200",20) == "Not possible to calculate ViewRatio"
    assert viewRatio(1.400,1.4999999) == "107.14%"
    

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


def test_tittle():
    page = requests.get("https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s")
    html_content = page.content.decode("utf-8")
    soup = BeautifulSoup(html_content, "html.parser")
    assert title(soup) == "How to get the number of Views, Likes, or Comments on a Youtube Video using the Youtube API Tutorial"
    
    page2 = requests.get("https://oxylabs.io/blog/beautiful-soup-parsing-tutorial")
    html_content2 = page2.content.decode("utf-8")
    soup2 = BeautifulSoup(html_content2,"html.parser")
    assert title(soup2) == "tittle not found"

    page3 = requests.get("https://www.youtube.com/watch?v=")
    html_content3 = page3.content.decode("utf-8")
    soup3 = BeautifulSoup(html_content3,"html.parser")
    assert title(soup3) == "tittle not found"
 
    page4 = requests.get("https://youtube.com/watch?v=92348324skd")
    html_content4 = page4.content.decode("utf-8")
    soup4 = BeautifulSoup(html_content4,"html.parser")
    assert title(soup4) == "tittle not found"

def test_author():
    page = requests.get("https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s")
    html_content = page.content.decode("utf-8")
    soup = BeautifulSoup(html_content, "html.parser")
    assert author(soup) == "Automate with Jonathan"
    
    page2 = requests.get("https://oxylabs.io/blog/beautiful-soup-parsing-tutorial")
    html_content2 = page2.content.decode("utf-8")
    soup2 = BeautifulSoup(html_content2,"html.parser")
    assert author(soup2) == "author not found"

    page3 = requests.get("https://www.youtube.com/watch?v=")
    html_content3 = page3.content.decode("utf-8")
    soup3 = BeautifulSoup(html_content3,"html.parser")
    assert author(soup3) == "author not found"
 
    page4 = requests.get("https://youtube.com/watch?v=92348324skd")
    html_content4 = page4.content.decode("utf-8")
    soup4 = BeautifulSoup(html_content4,"html.parser")
    assert author(soup4) == "author not found"


def test_date():
    page = requests.get("https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s")
    html_content = page.content.decode("utf-8")
    soup = BeautifulSoup(html_content, "html.parser")
    assert date(soup) == "2022-09-28"
    
    page2 = requests.get("https://oxylabs.io/blog/beautiful-soup-parsing-tutorial")
    html_content2 = page2.content.decode("utf-8")
    soup2 = BeautifulSoup(html_content2,"html.parser")
    assert date(soup2) == "date not found"

    page3 = requests.get("https://www.youtube.com/watch?v=")
    html_content3 = page3.content.decode("utf-8")
    soup3 = BeautifulSoup(html_content3,"html.parser")
    assert date(soup3) == "date not found"
 
    page4 = requests.get("https://youtube.com/watch?v=92348324skd")
    html_content4 = page4.content.decode("utf-8")
    soup4 = BeautifulSoup(html_content4,"html.parser")
    assert date(soup4) == "date not found"

    page5 = requests.get("https://www.youtube.com/watch?v=KcITJ97TK80")
    html_content5 = page5.content.decode("utf-8")
    soup5 = BeautifulSoup(html_content5,"html.parser")
    assert date(soup5) == "2022-11-02"


def test_isFamily():
    page = requests.get("https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s")
    html_content = page.content.decode("utf-8")
    soup = BeautifulSoup(html_content, "html.parser")
    assert isfamily(soup) == "true"
    
    page2 = requests.get("https://oxylabs.io/blog/beautiful-soup-parsing-tutorial")
    html_content2 = page2.content.decode("utf-8")
    soup2 = BeautifulSoup(html_content2,"html.parser")
    assert isfamily(soup2) == "tag not found"

    page3 = requests.get("https://www.youtube.com/watch?v=")
    html_content3 = page3.content.decode("utf-8")
    soup3 = BeautifulSoup(html_content3,"html.parser")
    assert isfamily(soup3) == "tag not found"
 
    page4 = requests.get("https://youtube.com/watch?v=92348324skd")
    html_content4 = page4.content.decode("utf-8")
    soup4 = BeautifulSoup(html_content4,"html.parser")
    assert isfamily(soup4) == "tag not found"

    page5 = requests.get("https://www.youtube.com/watch?v=KcITJ97TK80")
    html_content5 = page5.content.decode("utf-8")
    soup5 = BeautifulSoup(html_content5,"html.parser")
    assert isfamily(soup5) == "true"

def test_gen():
    page = requests.get("https://www.youtube.com/watch?v=8gDZBfs9Yv4&t=2s")
    html_content = page.content.decode("utf-8")
    soup = BeautifulSoup(html_content, "html.parser")
    assert gen(soup) == "Science & Technology"
    
    page2 = requests.get("https://oxylabs.io/blog/beautiful-soup-parsing-tutorial")
    html_content2 = page2.content.decode("utf-8")
    soup2 = BeautifulSoup(html_content2,"html.parser")
    assert gen(soup2) == "genre not found"

    page3 = requests.get("https://www.youtube.com/watch?v=")
    html_content3 = page3.content.decode("utf-8")
    soup3 = BeautifulSoup(html_content3,"html.parser")
    assert gen(soup3) == "genre not found"
 
    page4 = requests.get("https://youtube.com/watch?v=92348324skd")
    html_content4 = page4.content.decode("utf-8")
    soup4 = BeautifulSoup(html_content4,"html.parser")
    assert gen(soup4) == "genre not found"

    page5 = requests.get("https://www.youtube.com/watch?v=KcITJ97TK80")
    html_content5 = page5.content.decode("utf-8")
    soup5 = BeautifulSoup(html_content5,"html.parser")
    assert gen(soup5) == "Sports"

@patch("project.requests.get")
def test_data(mock_get_data):

    mock_data = {
    "kind": "youtube#searchListResponse",
    "etag": "HmvWmm0znf9XdMsq8SA2-oEmlo0",
    "nextPageToken": "CAUQAA",
    "regionCode": "US",
    "pageInfo": {
        "totalResults": 1000000,
        "resultsPerPage": 5
    },
    "items": [
        {
            "kind": "youtube#searchResult",
            "etag": "OEDULWkRo_i2Sjhqi8NcmJtxm-I",
            "id": {
                "kind": "youtube#channel",
                "channelId": "78"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "HPLXoe0CqhICu2siP8bH58mLbm4",
            "id": {
                "kind": "youtube#channel",
                "channelId": "78"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "olkaZRt5hj8LWVypKc7DzXuU7mM",
            "id": {
                "kind": "youtube#channel",
                "channelId": "78"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "iQwyEJQRPalPQqjqpna1b_l_KGw",
            "id": {
                "kind": "youtube#playlist",
                "playlistId": "PL7ZwE005lvhoHQfiycYIOxrBniDmGv2db"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "pCudylKk_8kedXRhO-XAdttCwO8",
            "id": {
                "kind": "youtube#video",
                "videoId": "Vrz9zvUF0qE"
            }
        }
    ]
}
    mock_response = Mock()
    mock_response.json.return_value = mock_data
    mock_response.status_code = 200
    mock_get_data.return_value = mock_response

    name = "Luis" 
    result = data(name)
    expected_channel_id = "78"

    assert(result) == expected_channel_id 


@patch("project.build")
def test_likes(mock_build):

    mock_youtube = Mock()
    mock_list = Mock()
    mock_videos = Mock()
                
    mock_data = {
        "kind": "youtube#videoListResponse",
        "etag": "8Kw2pghNc_O2VUN6trsAecscfZs",
        "items": [
            {

                "kind": "youtube#video",
                "etag": "QeucxJQZwJr2QWXtESSmKHhfuSQ",
                "id": "QlHNfcb1f2E",
                "statistics": {
                    "viewCount": "143239",
                    "likeCount": 123,
                    "favoriteCount": "0",
                    "commentCount": "460"    
                }
            }
            ],
            "pageInfo": {
                "totalResults": 1,
                "resultsPerPage": 1
            }
    }

    mock_list.execute.return_value = mock_data
    mock_videos.list.return_value = mock_list
    mock_youtube.videos.return_value = mock_videos
    mock_build.return_value = mock_youtube
    
    result = likes("QlHNfcb1f2E")
    expected_likes = 123 

    assert(result) == expected_likes
    

@patch("project.build")
def test_Views(mock_view):

    mock_youtube = Mock()
    mock_list = Mock()
    mock_videos = Mock()

    mock_data = {
        "kind": "youtube#videoListResponse",
        "etag": "8Kw2pghNc_O2VUN6trsAecscfZs",
        "items": [
            {

                "kind": "youtube#video",
                "etag": "QeucxJQZwJr2QWXtESSmKHhfuSQ",
                "id": "QlHNfcb1f2E",
                "statistics": {
                    "viewCount": 12345,
                    "likeCount": 123,
                    "favoriteCount": "0",
                    "commentCount": "460"    
                }
            }
            ],
            "pageInfo": {
                "totalResults": 1,
                "resultsPerPage": 1
            }
    }

    mock_list.execute.return_value = mock_data 
    mock_videos.list.return_value = mock_list 
    mock_youtube.videos.return_value = mock_videos 
    mock_view.return_value = mock_youtube 

    vv = views("QlHNfcb1f2E")
    expected_views = 12345
    assert(vv) == expected_views 

@patch("project.build")
def test_subscriber(mock_subs):

    mock_list = Mock()
    mock_channels = Mock()
    mock_youtube = Mock()
    
    mock_data = {
        "kind": "youtube#channelListResponse",
        "etag": "qXVC_8pAQ3SJEXA6KR0DbmC7Wj4",
        "pageInfo": {
            "totalResults": 1,
            "resultsPerPage": 5
        },
        "items": [
            {
            "kind": "youtube#channel",
            "etag": "0x58r0xs3T0oJ4EAZi5FlGcTESE",
            "id": "UCV3XpRxabX2UMbimv2k215Q",
            "statistics": {
                "viewCount": 534,
                "subscriberCount": 220,
                "hiddenSubscriberCount": False,
                "videoCount": "800"
            }
            }
        ]
    }

    mock_list.execute.return_value = mock_data
    mock_channels.list.return_value = mock_list
    mock_youtube.channels.return_value = mock_channels
    mock_subs.return_value = mock_youtube

    s1 = subscriber("USLAKSOEJF")
    s2 = subscriber("UCV3XpRxabX2UMbimv2k215Q")
    expected_subs = 220 

    assert(s1) == expected_subs
    assert(s2) == expected_subs

@patch("project.get_request1")
def test_requests1(mock_getr1):

    mock_getr1.return_value.ok = True
    response = get_request1

    assert(response) != None
