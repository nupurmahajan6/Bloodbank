from hdfs import InsecureClient
import pandas as pd

client_hdfs = InsecureClient('http://localhost:50070')

dff = pd.read_csv("StudentInfo.csv")
# print("dff")
# print(dff)
 # "static/files/"+username+"/"+img1
 
with client_hdfs.write('/in/big.csv', encoding = 'utf-8') as writer:
    dff.to_csv(writer)

with client_hdfs.read('/in/big.csv', encoding = 'utf-8') as reader:
    df = pd.read_csv(reader,index_col=0)
    #print(df)
    
    print('Reaad csv from hdfs')

print("df")
print(df)