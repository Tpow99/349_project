import plotly.express as px
import pandas as pd

df = pd.read_csv(r'C:/Users/17329/OneDrive/Documents/Fall 2021/CMSCI 349/PROJ/New_Dummy_Data.csv')

barChart = x.bar(df, x='Salary', y='Company', color='Title', title='Dummy Data Jobs')
barChart.show()
