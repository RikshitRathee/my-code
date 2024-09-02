import numpy as np
import pandas as pd
import time
phone = []
names = []
print("generating random data...")
time.sleep(3)
numbers = [1,2,3,4,5,6,7,8,9]
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



for i in range(50):
    abc = np.random.choice(numbers,10)
    num = ''
    for j in abc:
        num=num+str(j)
    phone.append(num)
phone
for i in range(50):
    abc = np.random.choice(alphabets,10)
    num = ''
    for j in abc:
        num=num+str(j)
    names.append(num)
names
print("Data Generating Successfully")
time.sleep(2)
df = pd.DataFrame({
    'PhoneNumber': phone,
    "Name": names
})
nameoffile = "sample.csv"
df.to_csv(nameoffile,index=False)
print("data save to {}".format(nameoffile))
