# -*- coding: utf-8 -*-
import pylab as np
import matplotlib.pyplot as plt

class Chart:
    
    
    
    def __init__(self):
        pass

    @staticmethod
    def plot(N, rg_1, rg_2):
        
        group_1_values = []
        group_2_values = []
        genesNames = [] # W jednej z pętli dodam też nazwy genów
        for key in iter( rg_1.compare( N, rg_2 ) ):
            group_1_values.append( rg_1.getGeneExpression( key ) )
            group_2_values.append( rg_2.getGeneExpression( key ) )
            genesNames.append( key )
            
            
        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        #rects1 = ax.bar(ind, group_1_values, width, color='r', yerr=group_1_Std)
        rects1 = ax.bar(ind, group_1_values, width, color='r')
            
        group_2_Std =   (0.3, 0.5) #Do wykorzystania w przyszłości
        
        rects2 = ax.bar(ind+width, group_2_values, width, color='y')
        # add some
        ax.set_ylabel('Expression')
        ax.set_title('Mean Expression diff between genes by group')
        ax.set_xticks(ind+width)
        
        ax.set_xticklabels( ( genesNames ) )
        
        ax.legend( (rects1[0], rects2[0]), ('GROUP_1', 'GROUP_2') )
        
        def autolabel(rects, values):
            # attach some text labels
            n = 0
            for rect in rects:
                height = values[n]
                n = n + 1
                ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%f'%float(height),
                        ha='center', va='bottom')
        
        autolabel(rects1, group_1_values)
        autolabel(rects2, group_2_values)
        
        plt.show()
