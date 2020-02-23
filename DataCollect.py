import numpy as np
import pandas as pd
import datetime

x = datetime.datetime.now()
print(x)

class Data_Recieved():

    def __init__(self, o_latitude, o_longitude, d_latitude, d_longitude, price, time):

        self.o_latitude = o_latitude
        self.o_longitude = o_longitude
        self.d_latitude = d_latitude
        self.d_longitude = d_longitude
        self.price = price
        self.time = time

    def save_data(self):

        df = pd.DataFrame(data=[(self.o_latitude, self.o_longitude, self.d_latitude, self.d_longitude, self.price, self.time.hour, self.time.minute, (self.time.weekday()+2)%7, self.time)],
        columns=['origin_latitude','origin_longitude','destination_latitude','destination_longitude', 'price', 'hour', 'minute', 'weekday' ,'time'] )
        print(df.head())