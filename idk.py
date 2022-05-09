import plotly.figure_factory as ff
import pandas as pd 

df = pd.read_csv( "mobile.csv" )
x = df ["Avg Rating"].tolist()
fig = ff.create_distplot ( [df ["Avg Rating"].tolist() ] , ["Mobile Brand"] , show_hist = False)
fig.show()

#normal distribution