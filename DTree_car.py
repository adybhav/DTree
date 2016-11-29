from __future__ import division
from copy import deepcopy
import csv
import numpy as np
inp = []

def samelabel(attr, label, key):
    initVal = label[0]
    endVal = label[0]
    for i in range(0, len(attr)):
        if (attr[i] == key):
            endVal = label[i]
	    if endVal!=initVal:
		break
    if (initVal == endVal):
        print "This is a leaf node " + key + " and the outcome is " + initVal
    return (initVal == endVal)

def checkclass(cgini):
    if len(set(cgini)) == 1:
	print "This is a leaf node with value "+ cgini[0]
	return True


  
def find_subset(mk,attr, label, labelname, key):
    str=""
    arr = [0, 0]
    for i in range(0, len(attr)):
	if attr[i] == key:
            for j in range(0, len(labelname)):
                if (label[i] == labelname[j]):
                    arr[j] += 1
    if(arr[0]>=arr[1]):
	str="unacc"
    else:
	str="acc"
    print "The Edge " + key +" from Node "+mk+ " has a value " + str

def gini_index(atttr, key, vals,size): #------------GINI Index valueulator
    if (len(vals) == 3):
        value = [[0,0,0] for i in range(0,2)]
    elif (len(vals) == 2):
        value = [[0,0] for i in range(0,2)]
    for i in range(0,len(vals)):
        for j in range(0,size):
	    if ((atttr['label'][j] == "acc") and (atttr[key][j] == vals[i])):
                value[0][i] += 1
            elif ((atttr['label'][j] == "unacc") and (atttr[key][j] == vals[i])):
                value[1][i] += 1
    denom = [(value[0][i] + value[1][i]) for i in range(0, len(vals))]
    ginivalue = [1.0 for i in range(0,len(vals))]
    for i in range(0, len(vals)):
        for j in range(0, len(value)):
		if denom[i]!=0:
	            ginivalue[i] -= (value[j][i]/denom[i])**(2)
    #print ginivalue
    ginival = 0.0
    for i in range(0, len(vals)):
	ginival += ((denom[i]/size)*(ginivalue[i]))
    print ginival


def gini(ginidict, attributes, attrnames,size):
    cgini = ginidict
    cattr = attributes
    cnames = attrnames
    newattr = {}
    if(checkclass(cgini['label'])==True): #------------check if records belong to same class
	return
    else:
	    for key in cnames:
		newattr[key] = gini_index(cgini, key, cattr[key],size) #---- value GINI Index
	    minkey = ""
	    minval = 0
	    for key in newattr:
		if newattr[key] < minval:
		    minval = newattr[key]
		    minkey = key

	    print "the minimum GINI value is " + minkey + " so we split on it"

	    recurdict = {}
	    for i in cattr[minkey]: #----------------each possible v of F
		recurdict = deepcopy(cgini)
		recurattr = deepcopy(cattr)
		recurnname = deepcopy(cnames)
		removelist = []
	
	
		if samelabel(recurdict[minkey], recurdict['label'], i) == True:
		    return
	
		else:
		   find_subset(minkey,recurdict[minkey], recurdict['label'], recurattr['label'], i) #--------------Subset of v in F
		 

		#print recurdict[minkey]
		for j in range(0, len(recurdict[minkey])):
		    if (recurdict[minkey][j] == i):
		        removelist.append(j)
	
		for key in recurdict:
		    recurdict[key] = [v for l, v in enumerate(recurdict[key]) if l not in removelist]
		
		del recurdict[minkey]
		del recurattr[minkey]
		size=len(recurdict[key])        
		recurnname.remove(minkey)
		gini(recurdict, recurattr, recurnname,size)  #----------recursively calling Dtree



with open("car.csv", 'rb') as csvfile:
    golfReader = csv.reader(csvfile, delimiter=',')
    for row in golfReader:
        inp.append(row)

headers = {}
headers["wheels"] = [inp[i][0] for i in range(0, 1728)]
headers["size"] = [inp[i][1] for i in range(0, 1728)]
headers["price"] = [inp[i][2] for i in range(0, 1728)]
headers["label"] = [inp[i][3] for i in range(0, 1728)]

columns = {}
columns["wheels"] = ["2","4", "more"]
columns["size"] = ["small", "med", "big"]
columns["price"] = ["low", "med", "high"]
columns["label"] = ["unacc", "acc"]

attrnames = ["wheels", "size", "price", "label"]
gini(headers, columns, attrnames,1728)
