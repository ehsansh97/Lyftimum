import pandas as pd
import numpy as np

class DataHandler():
    def __init__(self):
        pass

    def read_data(self):
        data = pd.read_csv('temp_database.csv', index_col=False)
        return data

    def add_event(self, event):
        df = self.read_data()
        new_event = {'user_id' : event.user_id,
        'origin_latitude' : event.o_latitude,
        'origin_longitude' : event.o_longitude,
        'destination_latitude' : event.d_latitude,
        'destination_longitude' : event.d_longitude,
        'price' : event.price,
        'hour' : event.time.hour,
        'minute' : event.time.minute,
        'weekday' : (event.time.weekday()+2)%7,
        'time' : event.time}
        new_data = df.append(new_event, ignore_index = True)
        new_data.to_csv('temp_database.csv')
