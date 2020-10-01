# -*- coding: utf-8 -*-
from ResearchGroup import *
import pylab as np
import matplotlib.pyplot as plt
"""
Created on Fri Apr 12 10:37:26 2013

@author: Michał Bzowski
"""

#METODY TESTUJĄCE
def assertNotNone(obj):
    if obj == None:
        raise Exception("MyException: None")
    else:
        print("OK")

def asserIsNotEmpty(obj):
    if len(obj) == 0:
        raise Exception("MyException: Pusty kontener")
    else:
        print( "OK", len(obj) )
        
def assertEquals(a, b):
    if a == b:
        print( "OK" )
    else:
        print( a,":",b )
        raise Exception("MyExeption: NOT EQUALS")
    

        
#Wczytaj plik
valuesFile = open("testoweWartosci2.txt",'r')
assertNotNone(valuesFile) #Czy nie jest None?

#Odczytaj z pliku wszystkie linijki
lines = valuesFile.readlines()
firstLine = lines[0] #Zapamiętuję piewszą linię - linię z nagłówkami kolumn
#lines = lines[1:] #Usuwam pierwszą linię - linię z nagłówkami kolumn
lines = lines[2:] #Usuwam pierwszą i drugą linię - linię z nagłówkami kolumn i jakimśczymś
    
#Utwórz obiekty ResearchGroup - Grupa: Badawcza i Kontrolna
rg_1 = ResearchGroup("Badawcza")
rg_2 = ResearchGroup("Kontrolna")


#Zakres badań przeprowadzonych na grupie badawczej (numery kolumn w pliku) 
groupRange1 = [1,3] 
#Dodaje do ResaechGroup wartości ekspresji wszystkich genów grupy badawczej
rg_1.addGenesAndValuesFromLines(lines,groupRange1)

#Zakres badań przeprowadzonych na grupie kontrolnej (numery kolumn w pliku) 
groupRange2 = [4,6]
#Dodaje do ResarchGroup wartościekspresji wszystkich genów grupy kontrolnej
rg_2.addGenesAndValuesFromLines(lines,groupRange2)

#Oblicza śrenią ekspresję każdego genu
rg_1.countMeanExpression();
rg_2.countMeanExpression();


#Zwraca 'N' nawiększych wartości ekspresjii
N = 1
#print( "RG1: ",rg_1.getHighestExpressions(N) );
#
print "RG2: ",rg_2.getHighestExpressions(N)


#Wykres słupkowy na podstawie http://matplotlib.org/examples/api/barchart_demo.html
group_1_values = []
for key in iter( rg_1.getHighestExpressions(N) ):
    group_1_values.append( rg_1.getHighestExpressions(N)[key] )
    
group_1_Std =   (0.2, 0.3) #Do wykorzystania w przyszłości

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, group_1_values, width, color='r', yerr=group_1_Std)


group_2_values = []
for key in iter( rg_2.getHighestExpressions(N) ):
    group_2_values.append( rg_2.getHighestExpressions(N)[key] )
    
group_2_Std =   (0.3, 0.5) #Do wykorzystania w przyszłości

rects2 = ax.bar(ind+width, group_2_values, width, color='y', yerr=group_2_Std)

# add some
ax.set_ylabel('Expression')
ax.set_title('Mean Expression diff between genes by group')
ax.set_xticks(ind+width)
ax.set_xticklabels( ( higestExpressionGene[0], higestExpressionGene[1] ) )

ax.legend( (rects1[0], rects2[0]), ('Experiment', 'Control') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()