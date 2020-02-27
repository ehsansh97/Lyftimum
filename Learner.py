import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import math


class LRLearner():

    def __init__(self):
        pass

    def price_predict(self, df, event):
        
        X_event = {'user_id' : event.user_id,
        'origin_latitude' : event.o_latitude,
        'origin_longitude' : event.o_longitude,
        'destination_latitude' : event.d_latitude,
        'destination_longitude' : event.d_longitude,
        'price' : event.price,
        'hour' : event.time.hour,
        'minute' : event.time.minute,
        'weekday' : (event.time.weekday()+2)%7,
        'time' : event.time}
        model_TAPSI = LinearRegression()
        model_SNAPP = LinearRegression()
        X_train = df.drop('price', axis = 1)
        TAPSI_y_train = df['price']['TAPSI']
        SNAPP_y_train = df['price']['SNAPP']
        model_SNAPP.fit(X_train, SNAPP_y_train)
        model_TAPSI.fit(X_train, TAPSI_y_train)

        new_data = pd.DataFrame(data = X_event)
        TAPSI_predict = model_TAPSI.predict(new_data)
        SNAPP_predict = model_SNAPP.predict(new_data)

        return {'TAPSI_predict': int(math.ceil(TAPSI_predict / 500.0) * 500.0), 'SNAPP_predict': int(math.ceil(SNAPP_predict / 500.0) * 500.0)}

        

