
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create DataFrame from the provided data
data = [
    {'Month': 'January', 'Rainfall(mm)': 78}, {'Month': 'February', 'Rainfall(mm)': 52},
    {'Month': 'March', 'Rainfall(mm)': 63}, {'Month': 'April', 'Rainfall(mm)': 47},
    {'Month': 'May', 'Rainfall(mm)': 58}, {'Month': 'June', 'Rainfall(mm)': 32},
    {'Month': 'July', 'Rainfall(mm)': 49}, {'Month': 'August', 'Rainfall(mm)': 62},
    {'Month': 'September', 'Rainfall(mm)': 74}, {'Month': 'October', 'Rainfall(mm)': 68},
    {'Month': 'November', 'Rainfall(mm)': 80}, {'Month': 'December', 'Rainfall(mm)': 91}
]
df = pd.DataFrame(data)

# Convert 'Month' from string to categorical to maintain proper order on x-axis
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'],
    ordered=True)

# Set up the Seaborn style
sns.set_style('whitegrid')

# Create the area chart: we will plot a line chart and fill the area under it
plt.figure(figsize=(12, 6))
plt.fill_between(df['Month'], df['Rainfall(mm)'], color="skyblue", alpha=0.4)
plt.plot(df['Month'], df['Rainfall(mm)'], color="Slateblue", alpha=0.6, linewidth=2)

# Customize the plot with diversified visual encoding
plt.title('Monthly Rainfall (in mm)', fontdict={'fontsize': 20, 'fontweight': 'bold'})
plt.xlabel('Month', fontdict={'fontsize': 14})
plt.ylabel('Rainfall (mm)', fontdict={'fontsize': 14})
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.yticks(fontsize=12)
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping

# Show the plot
plt.show()