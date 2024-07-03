
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Data in CSV format
data = """Month,Average High (°C),Average Low (°C)
January,7,1
February,8,1
March,12,4
April,16,7
May,20,11
June,24,15
July,27,17
August,27,16
September,23,14
October,18,10
November,12,5
December,8,2"""

# Read the data into a pandas DataFrame
df = pd.read_csv(StringIO(data))

# Set figure size
plt.figure(figsize=(12, 6))

# Plotting the area chart
plt.fill_between(df['Month'], df['Average High (°C)'], color="#FF5733", alpha=0.5)
plt.fill_between(df['Month'], df['Average Low (°C)'], color="#33D1FF", alpha=0.5)

# Creating labels for the axes and the headline
plt.title("Monthly Average Temperatures of City X", fontsize=14, fontweight='bold')
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")

# Customizing the x-axis to display all months
plt.xticks(rotation=45)
plt.tight_layout()

# Displaying the chart
plt.show()