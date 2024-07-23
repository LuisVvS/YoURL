import unittest
from unittest.mock import Mock, patch
import requests
from project import likes, get_request1, data, Views, subscriber
import os


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

    vv = Views("QlHNfcb1f2E")
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