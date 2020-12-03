import pandas as pd
import math

df=pd.read_csv(r'C:\Users\clivo\OneDrive\Desktop\Advent\Day3.txt',header=None)

def advent3(x,y):
    dataset = df*int(math.ceil(((x*len(df))/y)/len(df[0][0])))
    data=[]
    if y % 2 == 1:
        for i in dataset.index:
            text = dataset[0][i]
            data.append(text[(i)*x])
    if y % 2 == 0:
        for i in dataset.index:
            if i%2 == 0:
                text = dataset[0][i]
                data.append(text[int(i/2)])
    return data.count('#')

print('Part 1 =',advent3(3,1))
print('Part 2 =',advent3(1,1)*advent3(3,1)*advent3(5,1)*advent3(7,1)*advent3(1,2))
