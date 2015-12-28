
# coding: utf-8

# In[295]:

get_ipython().magic('save fastqc_summary.py')


from pathlib import Path 
import pandas as pd
import jinja2 as ji

#  build pandas table for checking
maindir = Path("./")
datadir = maindir / 'data'
sum_table = pd.DataFrame()
colnames = []
content = []


for folder in datadir.iterdir():
    sumtxt_path = folder / 'summary.txt' 
    '_'.join([s.columns[2].split('_')[x] for x in [0,1,4,5]])
    with sumtxt_path.open() as sumtxt:
        s = pd.read_table(sumtxt)
        col = s["Basic Statistics"]
        sample_name = '_'.join([s.columns[2].split('_')[x] for x in [0,1,4,5]])
        content = content + [[s["PASS"]]] 
        colnames = colnames + [sample_name]
        sum_table = pd.concat([sum_table, s["PASS"]],axis=1)
sum_table.columns = colnames
sum_table.index = [x for x in col]


# class definintion



# jinja template read and render
env = ji.Environment(loader=ji.FileSystemLoader('./'))
template = env.get_template(name = 'template.html')

heads = ['#'] + [x for x in sum_table.columns]
contents = []
for i in range(0,sum_table.shape[0]-1):
    c = [sum_table.index[i]] + [x for x in sum_table.values[i]]
    contents = contents + [c] 

test = open('./jinjatest.html','w')
template_out = template.render(heads=heads, contents=contents)
test.write(template_out)


get_ipython().magic('save fastqc_summary.py')


# In[292]:

folder.name.split('_')


# In[293]:

'_'.join([s.columns[2].split('_')[x] for x in [0,1,4,5]])


# In[283]:

'-'.join([folder.name.split('_')[x] for x in [0,1,4,5]])
    
    


# In[110]:

file= open("/Users/Weian/GitHub/fastqc-summary-project/data/LTS_ID02_373bp_ATCACGA_L001_R1_fastqc/summary.txt")
t = pd.read_table(file)



# In[229]:

dict 


sumtxt_path = folder / 'summary.txt'
with sumtxt_path.open() as sumtxt:
    for line in sumtxt:
        print(line)
        





# In[274]:

class test():
    def __init__(self,name):
        self.name = name
        
    def getName(self):
        return(self.name)
    
    class testtype():
        def __init__(self,testtype,status,png_path):
            self.testtype = testtype
            self.status = status
            self.png_path = png_path

        def getTesttype(self):
            return(self.testtype)

        def getsStatus(self):
            return(self.status)

        def getPngPath(self):
            return(self.png_path)
        
        def getName(self):
            return(self.name)


# In[275]:

a = test('123')


# In[269]:

a.getName()


# In[276]:

b = a.testtype('test1','pass','./')


# In[272]:

b.getPngPath()


# In[277]:

b.getName()


# In[ ]:



