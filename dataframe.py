import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

employees={
    'ID':[98,65,47,99,90,55],
    'Name':['Tayyab','Zafar','Bilal','Ali','Raza','Wahab'],
    'dept code':['999','888','555','333','111','000'],
    'City':['Karachi','Lahore','Sawat','Pindi','Faisalabad','Islamabad']
}

emptbl= pd.DataFrame(employees)
print(emptbl)
