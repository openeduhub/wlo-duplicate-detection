# -*- coding: utf-8 -*-
import json, os, codecs

textkeys = ["cclom:title", "cm:title", "cm:name", "cclom:general_description", "cm:description"]
kwkeys = ["cclom:general_keyword"]
csv = open('../data/wirlernenonline2-minhash.txt', 'w')

def getText(props):
    text = ""
    for k in textkeys:
        if k in props.keys():
            val = props[k]
            if isinstance(val, list):
                val = " ".join(val)
            text = text + " " + val
    if kwkeys[0] in props.keys():
        text = text + " " + " ".join(props[kwkeys[0]])
    return text.replace('"','')

with open('../data/wirlernenonline_20_05_2021.json') as f:
    for line in f:        
        jline=json.loads(line)
        id = jline['_source']['nodeRef']['id']
        props = jline['_source']['properties']                
        text = getText(props)            
        if (text.strip()!=id):
            csv.write(id + ' ' + text.replace('\n',' ').replace('\r','') + '\n');
        
csv.close()