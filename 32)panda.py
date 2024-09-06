import numpy as np
import pandas as pd


student_data=[
    [100,200,300,400],
    [1,2,3,4],
    [10,20,30,40],
    [5,6,7,8]
]
print(pd.DataFrame(student_data))
print('-------------------------')

stu_dict={
    'name':['yash'],
    'iq':[100],
    'marks':[80]
}

stu=pd.DataFrame(stu_dict)
print(stu)

# movies.rename(columns={'packege':'ipa',
#                        'marks':'score'})