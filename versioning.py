#!/usr/bin/env python

#Unpickles differently based on version. Upconverts to newest version if necessary
#Also converts pickle objects to json (since it's more readable)

import json
import pickle

def versionLoad(f,cVersion=0):
    try:
        obj=json.load(f)
    except ValueError:
        f.seek(0)
        obj=pickle.load(f)
    try:
        version=obj['version']
    except KeyError:
        version=0
    return upConvert(obj,version,cVersion)

def upConvert(obj,oldVersion,newVersion):
    v=dict()
    if oldVersion==newVersion:
        return obj
    v=dict()
    while oldVersion < newVersion:
        v[oldVersion]=obj
        t=oldVersion+1
        if oldVersion==0:
            downloaded={ x:[] for x in v[oldVersion].iterkeys() }
            v[t]=dict()
            v[t]['status']=v[oldVersion]
            v[t]['downloaded']=downloaded
            v[t]['version']=1
        elif oldVersion==1:
            raise IndexError
        oldVersion=t
    return v[newVersion]

def dump(f,obj):
    json.dump(f,obj)
