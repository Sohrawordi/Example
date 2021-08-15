# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:35:46 2021

@author: Md. Sohrawordi
"""
from flask import Flask, render_template


def amino_acid_composition(dataset):
    import pandas as pd
    #A list of 21 Amino Acid
    amino_acid="ACDEFGHIKLMNPQRSTWYVX"
    colls=[]  
    #sample = pd.read_csv(dataset)
    
    for i in range (len(amino_acid)):
        colls.append("Amino_acid_"+amino_acid[i])
    #print(colls)
    df=pd.DataFrame(columns=colls)
    for i in range(len(dataset['Sequence'])):
        #print(i)
        row={}
        for acid in amino_acid:
            #print(seq.count(acid))
            row["Amino_acid_"+acid]=dataset['Sequence'][i].count(acid)/len(dataset['Sequence'])
        df=df.append(row,ignore_index=True)

    



    return df


def binary_data(positive_sample):
    import pandas as pd
    amino_acid="ACDEFGHIKLMNPQRSTWYVX"
    binary_code={}
    colls=[]    
    for i in range (len(amino_acid)*len(positive_sample['Sequence'][0])):
        colls.append("Binary"+str(i))

    for i in amino_acid:
        a=[]
        for j in amino_acid:
            if i==j:
                a.append(1)
            else:
                a.append(0)  
        binary_code[i]=a 
        
        
        
    pdf=pd.DataFrame(columns=colls)
    for k in range(len(positive_sample['Sequence'])):
        c=0 
        row_value={}
        for i in positive_sample['Sequence'][k]:
            for j in binary_code[i]:
                row_value["Binary"+str(c)]=j
                c=c+1
        ##row_value["Class"]=1        
        pdf=pdf.append(row_value,ignore_index=True) 
    
    return pdf


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')










if __name__ == "__main__": 
    app.run(debug=True) 