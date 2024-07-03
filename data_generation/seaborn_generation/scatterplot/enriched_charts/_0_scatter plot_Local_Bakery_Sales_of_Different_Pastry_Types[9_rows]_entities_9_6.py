
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Assuming the data is in a CSV file named 'climate_data.csv'
data = """
City,Average_Temperature,Average_Humidity
New York,16,63
Los Angeles,19,65
Chicago,12,77
Houston,21,78
Phoenix,25,36
Philadelphia,16,68
San Antonio,22,75
San Diego,18,69
Dallas,24,65
San Jose,21,60
Austin,22,64
Jacksonville,22,72
Fort Worth,23,67
Columbus,15,70
Charlotte,20,65
Seattle,13,78
Denver,12,52
El Paso,23,45
Detroit,12,71
Washington D.C.,17,70
Nashville,18,69
Memphis,20,68
Portland,15,73
Las Vegas,27,22
Louisville,17,72
Baltimore,16,67
Milwaukee,11,76
Albuquerque,20,50
Tucson,25,44
Fresno,24,55
Sacramento,21,68
Kansas City,16,73
Long Beach,19,70
Mesa,25,37
Atlanta,19,70
Miami,28,75
Cleveland,13,77
Tulsa,20,66
Oakland,18,73
Minneapolis,10,75
"""

# Load the dataset into a pandas DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data))

# Create the scatterplot with customized features
plt.figure(figsize=(14, 8))
scatter = sns.scatterplot(
    data=df, 
    x="Average_Temperature", 
    y="Average_Humidity", 
    palette=sns.color_palette(["#FF6347", "#4682B4"]),
    edgecolor="w", s=100
)

# Customize the plot's title and labels
scatter.set_title('Climate Patterns: Average Temperature vs. Humidity', fontsize=18)
scatter.set_xlabel('Average Temperature (°C)', fontsize=14)
scatter.set_ylabel('Average Humidity (%)', fontsize=14)

# Adjust font size for the ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Remove the top and right spines for a cleaner look
sns.despine()

# Show the plot
plt.show()