# Imports 
from bs4 import BeautifulSoup as bs
import requests
import lxml
import re
import json

#global variables

parser = "lxml"


#Give name to namesharing and unbound self
unbound_namesharing_name = "ubn"
unbounds_self_name = 'ubs'
forbidden_name = "banned"
forbidden_unfun_name = "banned_fun"
coforbidden_name = "cobanned"
semiforbidden_name = "semibanned"

# the banlist 

banlist = {
    unbounds_self_name : [],
    unbound_namesharing_name: [],
    forbidden_name: [],
    forbidden_unfun_name: [],
    coforbidden_name: [],
    semiforbidden_name: [],
}


# for unbound 
data = bs(requests.get("https://www.trinityygo.com/unbound").text , parser)
box = data.find_all("ul")
unbounds_self = bs(str(box[2]),parser)
unbound_namesharing = bs(str(box[3]) , parser)
for i in unbounds_self.find_all('li'):
    b = re.findall(r'(>)([\w\s\!\-\.\'\#]+)(<)',str(i))
    if len(b)==3:
        banlist[unbounds_self_name]+= [b[1][1]]
    else:
        continue
for i in unbound_namesharing.find_all('li'):
    b = re.findall(r'(>)([\w\s\!\-\.\'\#]+)(<)',str(i))
    if len(b)==3:
        banlist[unbound_namesharing_name]+= [b[1][1]]
    else:
        continue
# done unbound

# for forbidden
text = requests.get("https://www.trinityygo.com/forbidden-list").text

replaceable = ["(was Unlimited)","(was Co-Forbidden)","(was Semi-Forbidden)","(was Unbound)","(was Forbidden)"]

for i in replaceable:
    text = text.replace(i,'')

data = bs(text , parser)
box = data.find_all("ul")
coforbidden = bs(str(box[3]) , parser)
semiforbidden = bs(str(box[4]) , parser)
forbidden = bs(str(box[5]) , parser)
forbidden_fun = bs(str(box[6]) , parser)

for i in coforbidden.find_all('li'):
    b = re.findall(r'(>)([\w\s\!\-\.\'\#]+)(<)',str(i))
    if len(b)==3:
        banlist[coforbidden_name]+= [b[1][1]]
    else:
        continue

json.dump(banlist,open("banlist.json",'w'))