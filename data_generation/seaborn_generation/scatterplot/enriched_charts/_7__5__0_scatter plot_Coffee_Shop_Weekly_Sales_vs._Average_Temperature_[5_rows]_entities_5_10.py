
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data_csv = """Region,Species,Observations
Forest,SpeciesA,340
Forest,SpeciesB,275
Forest,SpeciesC,450
Forest,SpeciesD,300
Forest,SpeciesE,210
Desert,SpeciesA,120
Desert,SpeciesB,310
Desert,SpeciesC,150
Desert,SpeciesD,190
Desert,SpeciesE,280
Ocean,SpeciesA,500
Ocean,SpeciesB,410
Ocean,SpeciesC,380
Ocean,SpeciesD,550
Ocean,SpeciesE,450
Mountain,SpeciesA,430
Mountain,SpeciesB,330
Mountain,SpeciesC,290
Mountain,SpeciesD,370
Mountain,SpeciesE,220
Plains,SpeciesA,210
Plains,SpeciesB,320
Plains,SpeciesC,300
Plains,SpeciesD,280
Plains,SpeciesE,260"""

data = pd.read_csv(pd.compat.StringIO(data_csv))

plt.figure(figsize=(16, 10))
scatter_plot = sns.scatterplot(
    data=data,
    x='Region', 
    y='Observations', 
    hue='Species', 
    palette=['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a'],  # New color scheme
    s=150  # Adjusted marker size
)

scatter_plot.set_title('Species Observations Across Different Regions', fontsize=22, pad=25)
scatter_plot.set_xlabel('Region', fontsize=15)
scatter_plot.set_ylabel('Number of Observations', fontsize=15)

# Show the plot
plt.show()