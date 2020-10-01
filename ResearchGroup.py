# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:37:51 2013

@author: Machcak
"""
from Chart import *
class ResearchGroup:
    __groupName = ""
    __genesAndValues = {}
    __meanGenesExpression = {}
    
    def __init__(self, name):
        self.__groupName = name
        self.__genesAndValues = {}
        self.__meanGenesExpression = {}
        
    def addGenesAndValuesFromLines(self, lines, groupRange):
        if len(lines) > 0:
            try:
                genesFromMicroArray = self.__getGeneNamesFromLines( lines )
                valuesGroup = self.__getExpressionValuesFromLines( lines, groupRange )
                self.__addGenesAndValues( genesFromMicroArray, valuesGroup )
            except Exception as e:
                print( e )
        
    def __getGeneNamesFromLines(self, textLines):
        genesFromMicroArray = []
        firstSpaceIndex = 0
        for genNames in textLines:
            firstSpaceIndex = genNames.index('\t')
            genName = genNames[0:firstSpaceIndex]
            genesFromMicroArray.append( genName )
        return genesFromMicroArray
        
    def __getExpressionValuesFromLines(self, textLines, groupRange):
        expressionValues = []    
        for values in textLines:
            listOfVals = values.split()
            firstIndex =  groupRange[0]
            lastIndex =  groupRange[1]+1
             
            expressionValues.append( listOfVals[firstIndex:lastIndex] )
        return expressionValues
       
    def __addGenesAndValues(self, genes, values):
        if (genes != None and values != None) and (len(genes) != 0 and len(values) != 0):
            i = 0
            for gen in genes:
                self.__genesAndValues[gen] = values[i]
                i=i+1
        else:
            print ( "ERROR" )
            raise AttributeError
      
    
    def getResults(self):
        if self.__genesAndValues == None:
            return {}
        else:
            return self.__genesAndValues
    
    def countMeanExpression(self):
        if self.__genesAndValues != None and len(self.__genesAndValues) != 0: 
            for key in self.__genesAndValues.keys():
                self.__meanGenesExpression[key] = self.__meanFromList(self.__genesAndValues[key])
    
    def __meanFromList(self, valuesList):
        suma = 0.0
        for i in range(len(valuesList)):
            suma = suma + float(valuesList[i])
        return suma / len (valuesList)
    
    def getHighestExpressions(self, numberOfHighest):
        if numberOfHighest == 0:
            raise ValueError("Number is not correct")
        elif numberOfHighest <= len(self.__meanGenesExpression) and numberOfHighest > 0:
            newDic = {}
            meanDic = self.__meanGenesExpression.copy()
            for i in range(numberOfHighest):
                maxKey = max(meanDic)
                newDic[maxKey] = meanDic[maxKey]
                del(meanDic[maxKey])
            return newDic
        else:
            raise ValueError("Len Non Corect")
            
    def name(self):
        return self.__groupName
        
    def getGeneExpression(self, key):
        return self.__meanGenesExpression[key]
        
    def compare(self, N, gr_2):
        absDiffs = {}
        for key in self.__meanGenesExpression.keys():
            diff = self.__meanGenesExpression[key] - gr_2.__meanGenesExpression[key]
            absDiff = abs( diff )
            absDiffs[key] = absDiff 
        
        nMaks = {}
        for i in range(N):
            maksimum = -1
            maksimumKey = ""
            for key in absDiffs.keys():
                if absDiffs[key] > maksimum:
                    maksimum = absDiffs[key]
                    maksimumKey = key
            nMaks[maksimumKey]=maksimum
            del absDiffs[maksimumKey]
            
        return nMaks
            
        
##############################################
#TEST
#Wczytaj plik
#valuesFile = open("testoweWartosci2.txt",'r')
#
##Odczytaj z pliku wszystkie linijki
#lines = valuesFile.readlines()
#firstLine = lines[0] #Zapamiętuję piewszą linię - linię z nagłówkami kolumn
#lines = lines[1:] #Usuwam pierwszą linię - linię z nagłówkami kolumn
##lines = lines[2:] #Usuwam pierwszą i drugą linię - linię z nagłówkami kolumn i jakimśczymś
#    
##Utwórz obiekty ResearchGroup - Grupa: Badawcza i Kontrolna
#rg_1 = ResearchGroup("Badawcza")
#rg_2 = ResearchGroup("Kontrolna")
#
#
##Zakres badań przeprowadzonych na grupie badawczej (numery kolumn w pliku) 
#groupRange1 = [1,3] 
##Dodaje do ResaechGroup wartości ekspresji wszystkich genów grupy badawczej
#rg_1.addGenesAndValuesFromLines(lines,groupRange1)
#
##Zakres badań przeprowadzonych na grupie kontrolnej (numery kolumn w pliku) 
#groupRange2 = [4,6]
##Dodaje do ResarchGroup wartościekspresji wszystkich genów grupy kontrolnej
#rg_2.addGenesAndValuesFromLines(lines,groupRange2)
#
##Oblicza śrenią ekspresję każdego genu
#rg_1.countMeanExpression();
#rg_2.countMeanExpression();
#
#
##Zwraca 'N' nawiększych wartości ekspresjii
#N = 4
#
##Wykres słupkowy na podstawie http://matplotlib.org/examples/api/barchart_demo.html
#Chart.plot(N, rg_1, rg_2);
