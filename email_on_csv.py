import json
import requests
from requests.auth import HTTPBasicAuth 
import re
import unidecode
import time
import pandas as pd  
k=0
namedata=[]
emaildata=[]
for j in range (400):
    url="https://api.github.com/repos/laravel/laravel/stargazers?per_page=100&page="+str(j)
    responce=requests.get(url,headers={'Authorization': 'a631efb5a58c7fb9d2e509384f13146058b4b1f0'})
    k+=1
    print("request1")
    data1=responce.json()
    for i in data1:
        print('request2')
        nameurl="https://api.github.com/users/"+i["login"]#get the login name
        k+=1
        nresponce=requests.get(nameurl,headers={'Authorization': 'a631efb5a58c7fb9d2e509384f13146058b4b1f0'})
        data=nresponce.json()
        

        emurl='https://api.github.com/users/'+i["login"]+'/events/public'#get the email json
        k+=1
        eresponce=requests.get(emurl,headers={'Authorization': 'a631efb5a58c7fb9d2e509384f13146058b4b1f0'})
        edata=eresponce.json()
        email=json.dumps(edata)
        print('request k='+str(k))
        if 'email'in email:#check if emil exist or not
            e=re.search(r'[\w\.-]+@[\w\.-]+', email)#extract email
            time.sleep(5)
            print('inside if')
            emaildata.append(str(e.group(0)))
            namedata.append(str(data["name"]))
            print(k)    

d={'name':namedata,'email':emaildata}
df = pd.DataFrame(d)
# saving the dataframe 
df.to_csv('file1.csv') 
print("done")

#for each entry 3 api call are going on so after some time get blocked
#so i hv used a break after 25 api calls