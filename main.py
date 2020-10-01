import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as dial
from ResearchGroup import *

fileName = ""
canProceed = False
canCheck = False
groupRange = None

def main():
    global entry
    okno = tk.Tk()
    okno.title("MBz")
    ###Definicja labelów
    mainLabelVariable = tk.StringVar()
    mainLabelVariable.set("Open Microarray file")
    mainLabel = ttk.Label(okno, textvariable= mainLabelVariable)
    
    howMuchGenesLabelVariable = tk.StringVar()
    howMuchGenesLabelVariable.set("How Much Genes?")
    howMuchGenesLabel = ttk.Label(okno, textvariable=howMuchGenesLabelVariable)
    
    groupRangeStartVariable = tk.StringVar()
    groupRangeStartVariable.set("Second Group Start's")
    groupRangeStart  = ttk.Label(okno, textvariable=groupRangeStartVariable)
    ###Definicja spinboxu
    N = tk.StringVar()
    howMuchGenes = tk.Spinbox(okno, from_=1.0, to=10.0, textvariable=N)
           
    def openFileName():
        global fileName
        global canCheck, groupRange, TOTAL_EXPERIMENTS_NUMBER
        fileName = dial.askopenfilename(parent=okno, title="Choose a file")
        if fileName != '':
            buttonShowChart.configure(state=tk.ACTIVE)
            mainLabelVariable.set("File opened: "+ fileName.split("/")[-1])
            
            TOTAL_EXPERIMENTS_NUMBER = len(open(fileName).readline().split()) - 1
            groupRangeVar = tk.StringVar()
            groupRange = tk.Spinbox(okno, from_=2.0, to=TOTAL_EXPERIMENTS_NUMBER, textvariable=groupRangeVar)
            groupRangeStart.grid(row=1, column=0, padx=5, pady=5)
            groupRange.grid(row=1, column=1, padx=5, pady=5)
             
            howMuchGenesLabel.grid(row = 2, column=0,  padx = 5, pady =5)
            howMuchGenes.grid(row=2, column=1, padx=5, pady=5)
        else:
            disableAllButtons()
     

    def disableAllButtons():
        buttonShowChart.configure(state=tk.DISABLED)
        
    def showChart():
        global fileName, TOTAL_EXPERIMENTS_NUMBER
    
         
        valuesFile = open(fileName,'r')
        #Odczytaj z pliku wszystkie linijki
        lines = valuesFile.readlines()
        firstLine = lines[0] #Zapamiętuję piewszą linię - linię z nagłówkami kolumn
        lines = lines[1:] #Usuwam pierwszą linię - linię z nagłówkami kolumn
        #lines = lines[2:] #Usuwam pierwszą i drugą linię - linię z nagłówkami kolumn i jakimśczymś
        #Utwórz obiekty ResearchGroup - Grupa: Badawcza i Kontrolna
        rg_1 = ResearchGroup("Badawcza")
        rg_2 = ResearchGroup("Kontrolna")
        
        #Zakres badań przeprowadzonych na grupie badawczej (numery kolumn w pliku) 
        i = int( groupRange.get() ) - 1
        groupRange1 = [1, i] 
        #Dodaje do ResaechGroup wartości ekspresji wszystkich genów grupy badawczej
        rg_1.addGenesAndValuesFromLines(lines,groupRange1)
        #Zakres badań przeprowadzonych na grupie kontrolnej (numery kolumn w pliku) 

        groupRange2 = [i+1,TOTAL_EXPERIMENTS_NUMBER]
        #Dodaje do ResarchGroup wartościekspresji wszystkich genów grupy kontrolnej
        rg_2.addGenesAndValuesFromLines(lines,groupRange2)
        
        #Oblicza śrenią ekspresję każdego genu
        rg_1.countMeanExpression();
        rg_2.countMeanExpression();
        
        #Zwraca 'N' nawiększych wartości ekspresjii
        #Wykres słupkowy na podstawie http://matplotlib.org/examples/api/barchart_demo.html
        Chart.plot(int(N.get()), rg_1, rg_2);
     
    ###Definicja Pryzcisków
    buttonOpen = ttk.Button(okno, text="Open", width=10, command= openFileName)
    buttonShowChart = ttk.Button(okno, text="Show Chart", width=10,command =  showChart, state=tk.DISABLED)
    

    #Layout
    buttonOpen.grid(row=0, column=0, padx=5, pady=5)
    mainLabel.grid(row=0, column=1, padx=5, pady=5)
        
    
    buttonShowChart.grid(row=3, column=0, padx=5, pady=5)
    
    okno.mainloop()

main()
