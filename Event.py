import datetime

class Event():
    def __init__(self,user_id, o_latitude, o_longitude, d_latitude, d_longitude, price):
    
        self.user_id = user_id
        self.o_latitude = o_latitude
        self.o_longitude = o_longitude
        self.d_latitude = d_latitude
        self.d_longitude = d_longitude
        self.price = price
        self.time = datetime.datetime.now()