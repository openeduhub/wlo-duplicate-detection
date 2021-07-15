# -*- coding: utf-8 -*-
import json, os, codecs

textkeys = ["cclom:title", "cm:title", "cm:name", "cclom:general_description", "cm:description"]
#kwkeys = ["cclom:general_keyword"]
urlkeys = ["ccm:wwwurl"]

csv = open('wirlernenonline2-dedup.txt', 'w')

def getText(props):
    text = ""
    for k in textkeys:
        if k in props.keys():
            val = props[k]
            if isinstance(val, list):
                val = " ".join(val)
            text = text + " " + val
    #if kwkeys[0] in props.keys():
    #    text = text + " " + " ".join(props[kwkeys[0]])
    return text.replace('"','').strip()

def getUrl(props):
    url = "_"
    for k in urlkeys:
        if k in props.keys():
            url = props[k]                
    return url.replace('"','').strip().replace(' ','+')


with open('wirlernenonline_20_05_2021.json') as f:
    for line in f:        
        jline=json.loads(line)
        id = jline['_source']['nodeRef']['id']
        props = jline['_source']['properties']                
        text = getText(props) 
        url = getUrl(props)
        if (text.strip()!=id):
            csv.write(id + ' ' + url + ' ' + text.replace('\n',' ').replace('\r','') + '\n');
        
csv.close()