
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


dummy = pd.read_csv(r'C:/Users/17329/349_project/JobScraperProj.git/sample100.csv')
dummy.head()


plot1 = sns.barplot(x='salary', y='company',
                    hue = 'location',
                   data= dummy)
