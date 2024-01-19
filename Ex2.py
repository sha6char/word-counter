from collections import Counter
import sys
from tkinter import filedialog
num = int(sys.argv[1])
fpath=filedialog.askopenfile()
fpath=fpath.name
with open(fpath,"rb") as file:
    sentences = file.read()
sentenc =sentences.split()
S=Counter(sentenc)
sortedList = sorted(S.items(),key=lambda S :S[1],reverse=True)
i = 0
while i <num:
    temp =str(sortedList[i][0])
    print(temp[2:-1])
    i+=1 



    

