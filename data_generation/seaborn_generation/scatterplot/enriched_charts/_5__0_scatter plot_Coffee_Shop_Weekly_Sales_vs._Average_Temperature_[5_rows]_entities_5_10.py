
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data_csv = """Region,Book,Readers
North,BookA,1800
North,BookB,2300
North,BookC,1600
East,BookA,2200
East,BookB,1910
East,BookC,2140
South,BookA,1720
South,BookB,1610
South,BookC,1488
West,BookA,1640
West,BookB,1920
West,BookC,1699
Central,BookA,2130
Central,BookB,1870
Central,BookC,1540
North,BookD,2000
East,BookD,2500
South,BookD,2100
West,BookD,2200
Central,BookD,2400"""

data = pd.read_csv(pd.compat.StringIO(data_csv))

plt.figure(figsize=(14, 9))
scatter_plot = sns.scatterplot(
    data=data,
    x='Region', 
    y='Readers', 
    hue='Book', 
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],  # New color scheme
    s=120  # Adjusted marker size
)

scatter_plot.set_title('Regional Book Readership', fontsize=20, pad=20)
scatter_plot.set_xlabel('Region', fontsize=15)
scatter_plot.set_ylabel('Number of Readers', fontsize=15)

# Show the plot
plt.show()