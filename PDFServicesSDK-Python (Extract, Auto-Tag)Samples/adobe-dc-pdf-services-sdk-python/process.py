import time
import json
import pandas as pd
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth', None)

 
# Opening JSON file
f = open('./structuredData.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
allText = []
for n, i in enumerate(data['elements']):
    if 'Text' in i:
        try:

            print(n, i['Text'])
            allText.append(i['Text'])
            #time.sleep(1)
            print("")
            print("-------------------------")
        except:
            print('error trying to get Text property')
p = pd.DataFrame(allText)
p1 = p[ p[0].str.contains("Consumo Tusd") ]
#print(p1)
#print( p[ (p[0].index == 57) |  (p[0].index == 58) | (p[0].index == 59) | (p[0].index == 60)], p[ (p[0].index == 61) |  (p[0].index == 62) | (p[0].index == 63) | (p[0].index == 64)])
print( p[ (p[0].index >= 57) &  (p[0].index <=100)])
        
    
# Closing file
f.close()