from __future__ import division
from copy import deepcopy
import csv
import numpy as np
inp = []

def gini_calc(outlook, key, vals,size):
    #vals = ["Rainy", "Sunny", "Overcast"]
    if (len(vals) == 3):
        calc = [[0,0,0] for i in range(0,2)]
    elif (len(vals) == 2):
        calc = [[0,0] for i in range(0,2)]
    #print outlook
    for i in range(0,len(vals)):
        for j in range(0,size):
	    if ((outlook['label'][j] == "Yes") and (outlook[key][j] == vals[i])):
                calc[0][i] += 1
            elif ((outlook['label'][j] == "No") and (outlook[key][j] == vals[i])):
                calc[1][i] += 1
    denom = [(calc[0][i] + calc[1][i]) for i in range(0, len(vals))]
    ginicalc = [1.0 for i in range(0,len(vals))]
    for i in range(0, len(vals)):
        for j in range(0, len(calc)):
            ginicalc[i] -= (calc[j][i]/denom[i])**(2)
    #print ginicalc
    ogini = 0.0
    for i in range(0, len(vals)):
        ogini += ((denom[i]/size)*(ginicalc[i]))
    print ogini

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

def majorityrules(attr, label, labelname, key):
    str=""
    arr = [0, 0]
    for i in range(0, len(attr)):
	if attr[i] == key:
            for j in range(0, len(labelname)):
                if (label[i] == labelname[j]):
                    arr[j] += 1
    if(arr[0]>=arr[1]):
	str="No"
    else:
	str="Yes"
    print "The leaf " + key + " has a value " + str

def gini(ginidict, attributes, attrnames,size):
    cgini = ginidict
    cattr = attributes
    cnames = attrnames
    newattr = {}
    for key in cnames:
        newattr[key] = gini_calc(cgini, key, cattr[key],size)
    minkey = ""
    minval = 0
    for key in newattr:
        if newattr[key] < minval:
            minval = newattr[key]
            minkey = key

    print "the minimum GINI value is " + minkey + " so we split on it"

    recurdict = {}
    for i in cattr[minkey]:
        recurdict = deepcopy(cgini)
        recurattr = deepcopy(cattr)
        recurnname = deepcopy(cnames)
        removelist = []
	
	#if(sset(recurdict[minkey], recurdict['label'], recurattr['label'], i):)

        if samelabel(recurdict[minkey], recurdict['label'], i) == True:
            return
	
        else:
	   majorityrules(recurdict[minkey], recurdict['label'], recurattr['label'], i)
         

	#print recurdict[minkey]
        for j in range(0, len(recurdict[minkey])):
            if (recurdict[minkey][j] == i):
                removelist.append(j)
	
        for key in recurdict:
            recurdict[key] = [v for l, v in enumerate(recurdict[key]) if l not in removelist]
		
	del recurdict[minkey]
        del recurattr[minkey]
	size=len(recurdict[key])        
	print minkey	        
	recurnname.remove(minkey)
	gini(recurdict, recurattr, recurnname,size)


#def sset(attribute, class_label, classname, i):
		



with open("golf.csv", 'rb') as csvfile:
    golfReader = csv.reader(csvfile, delimiter=',')
    for row in golfReader:
        inp.append(row)

ddict = {}
ddict["outlook"] = [inp[i][0] for i in range(0, 14)]
ddict["temp"] = [inp[i][1] for i in range(0, 14)]
ddict["humid"] = [inp[i][2] for i in range(0, 14)]
ddict["windy"] = [inp[i][3] for i in range(0, 14)]
ddict["label"] = [inp[i][4] for i in range(0, 14)]

attr = {}
attr["humid"] = ["High", "Normal"]
attr["outlook"] = ["Rainy", "Sunny", "Overcast"]
attr["temp"] = ["Hot", "Mild", "Cool"]
attr["windy"] = ["True", "False"]
attr["label"] = ["Yes", "No"]

attrnames = ["outlook", "humid", "temp", "windy"]
gini(ddict, attr, attrnames,14)

