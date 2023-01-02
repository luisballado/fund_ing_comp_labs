import sys
import numpy as np
import matplotlib.pyplot as plt
import re

def u(t):
    """Unit step function"""
    return 1 * (t >= 0)

#definicion delta function
def imp(t):
    return ((t)==0)*1.0

n = np.arange(-10,10,1)

regex = r'x\[n\]='
i = 0
with open(sys.argv[1],'r',encoding='utf-8') as file:
    for line in file:
        #print("calcular")
        if re.search(regex,line):
            eq = line.split("=",1)[1]
            
            #reemplazar el -1^n por cos(n*pi)
            if re.search(r'-1\^n',eq):
                
                new_string = eq.replace("-1^n","np.cos(n*np.pi)").replace("[","(").replace("]",")")
                
                x = new_string.replace("\n", "")

                plt.figure(i)
                plt.stem(n, eval(x))
                plt.grid()
                plt.savefig('graph'+str(i)+'.png')
                
            elif re.search(r'sigma',eq):
                txt = re.search(r'\((.*?)\)',eq).group(1)
                x = txt.split(",")
                
                g = np.array([0])

                for k in range(int(x[1])):
                    
                    data = -3*k-1
                    g = g + 4*imp(n+data)
    
                plt.figure(2)
                plt.stem(n,g)
                plt.grid()
                plt.savefig('graph.png')
                
            else:
                new_string = eq.replace("[","(").replace("]",")")
                x = new_string.replace("\n", "")
                plt.figure(i)
                plt.stem(n, eval(x))
                plt.grid()
                plt.savefig('graph'+str(i)+'.png')
                
            i = i + 1
            

