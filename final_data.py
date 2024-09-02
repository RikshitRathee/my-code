import pandas as pd
import numpy as np
df= pd.read_csv('sample.csv')
print("data loaded successfully")
df["status"]=0
df["result"]="unhandled"
print("data processed successfully")

nameoffile='data.csv'
df.to_csv(nameoffile,index=False)
print("data saved to {}".format(nameoffile))