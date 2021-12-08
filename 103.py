import pandas as pd
import plotly.express as px
df=pd.read_csv('corona_csv.csv')
figg=px.scatter(df,x='date',y='cases',color='Country',title='corona data')
figg.show()