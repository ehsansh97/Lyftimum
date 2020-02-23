import pandas as pd
import numpy as np

# df = pd.DataFrame(None, None,columns=['user_id','origin_latitude','origin_longitude','destination_latitude','destination_longitude', 'price', 'hour', 'minute', 'weekday' ,'time'] )
# df.to_csv('temp_database.csv', index = False)


df = pd.read_csv('temp_database.csv')
print(df)