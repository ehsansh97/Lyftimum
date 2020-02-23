import requests
import json
import datetime

def get_price(diction):
    o_latitude = diction['o_latitude']
    o_longitude = diction['o_longitude']
    d_latitude = diction['d_latitude']
    d_longitude = diction['d_longitude']
# TAPSI
    url = 'https://tap33.me/api/v2.1/ride/preview'
    header = {'content-type': 'application/json', 'x-authorization' : 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoyNTY1OTMsInJvbGUiOiJQQVNTRU5HRVIiLCJjaXR5IjoiVEVIUkFOIiwiZGV2aWNlVHlwZSI6IldFQkFQUCJ9LCJpYXQiOjE1Nzk2MTU2MjMsImF1ZCI6ImRvcm9zaGtlOmFwcCIsImlzcyI6ImRvcm9zaGtlOnNlcnZlciIsInN1YiI6ImRvcm9zaGtlOnRva2VuIn0.Pjqcy14qLRbNE6IDbkCcxwBKXlo094SmakUmOCq04JFlq1Tvli7fyT1ZVSrTK3WgcqPI-09MzhruXU05YHneBg'}
    datas = {"origin":{"latitude":o_latitude,"longitude":o_longitude},"destinations":[{"latitude":d_latitude,"longitude":d_longitude}],"hasReturn":'false',"initiatedVia":"WEB"}
    tap30_sr = ServiceRequest(url, header, datas)
    price_tap30 = tap30_sr.tap30_price_checker()
# SNAPP
    url = 'https://web-api.snapp.ir/api/v1/ride/price'
    header = {'authorization' : '24333bb925f41fc32ef10d99a5c5d3261579600718'}
    datas = {"origin_lat":o_latitude,"origin_lng":o_longitude,"round_trip":0,"destination_lat":d_latitude,"destination_lng":d_longitude}
    snapp_sr = ServiceRequest(url, header, datas)
    price_snapp = int(snapp_sr.snapp_price_checker()/10)

    print("2")
    prices = {"TAPSI":price_tap30,"SNAPP":price_snapp}
    return prices


class ServiceRequest():
    def __init__(self, url, header, datas):
        self.url = url
        self.header = header
        self.datas = datas
        self.response_raw = requests.post(self.url, data = json.dumps(datas), headers = self.header)
        self.response_json = json.loads(self.response_raw.text)
            
    def snapp_price_checker(self):
        print(self.response_raw)
        return self.response_json['prices'][0]['final']
        

    def tap30_price_checker(self):
        print(self.response_raw)
        return self.response_json['data']['serviceCategoriesInfo'][0]['priceInfos'][0]['price']
        