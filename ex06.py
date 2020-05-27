import re
import test1 as te
from test1 import inp
import pickle


custlist=[]
page=-1
with open('info.txt','rb') as f :
    data = pickle.load(f)
custlist=data
page= len(data)-1

while True:
    choice=te.print1()

    if choice=="I":
        custlist,page = inp(custlist,page)
    elif choice=="C":
        te.view1(custlist,page)

    elif choice == 'P':
        page = te.view2(custlist,page)
            
    elif choice == 'N':
        page = te.view3(custlist,page)

    elif choice=='D':
        custlist = te.del1(custlist)

    elif choice=="U": 
        custlist = te.change(custlist)
            
    elif choice=="Q":

        with open('info.txt','wb') as f:
            pickle.dump(custlist,f)
        break
