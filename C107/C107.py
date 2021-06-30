import pandas as pd
import plotly.express as px
import csv

#student_id    level  attempt

df = pd.read_csv('data.csv')
# mean = df.groupby(("level")["attempt"],as_index=False).mean()
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
 
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()