from secretKeys.dataKey import serviceKey
from secretKeys.naverKey import client, clientSecret
from urllib.parse import urlencode
import requests

def etfPriceInfoAPI():
    url = "https://apis.data.go.kr/1160100/service/GetSecuritiesProductInfoService/getETFPriceInfo"
    
    params = {
        "serviceKey": serviceKey,
        "numOfRows": 1,
        "pageNo": 1,
        "resultType": "json"
    }

    res = requests.get(url, params=params)
    return res 

def naverNewsAPI(searchKey:str):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id" : client,
        "X-Naver-Client-Secret" : clientSecret
    }
    params = {
        "query" : searchKey,
        "display" : 100,
        "start" : 1,
        "sort" : "date"
    }
    res = requests.get(url, headers=headers, params=params)
    return res.json()

if __name__=="__main__":
    naverNewsAPI("kodex 200")
    
