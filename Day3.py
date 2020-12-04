import pandas as pd
import math

df=pd.read_csv(r'C:\Users\clivo\OneDrive\Desktop\Advent\Day3.txt',header=None)

def count_trees(x,y):
    dataset = df*int(math.ceil(((x*len(df))/y)/len(df[0][0])))
    data=[]
    if y % 2 == 1:
        for i in dataset.index:
            text = dataset[0][i]
            data.append(text[(i)*x])
    if y % 2 == 0:
        for i in dataset.index:
            if i%y == 0:
                text = dataset[0][i]
                data.append(text[int(i/y)*x])
    return data.count('#')

print('Part 1 =',count_trees(3,1))
print('Part 2 =',count_trees(1,1)*count_trees(3,1)*count_trees(5,1)*count_trees(7,1)*count_trees(1,2))
