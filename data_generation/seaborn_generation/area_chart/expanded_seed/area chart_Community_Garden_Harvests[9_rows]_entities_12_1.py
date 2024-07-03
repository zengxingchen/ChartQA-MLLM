
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Provided chart table data
data = [
    {'Month': 'January', 'Produce Weight (in kg)': 150},
    {'Month': 'February', 'Produce Weight (in kg)': 120},
    {'Month': 'March', 'Produce Weight (in kg)': 180},
    {'Month': 'April', 'Produce Weight (in kg)': 240},
    {'Month': 'May', 'Produce Weight (in kg)': 300},
    {'Month': 'June', 'Produce Weight (in kg)': 360},
    {'Month': 'July', 'Produce Weight (in kg)': 420},
    {'Month': 'August', 'Produce Weight (in kg)': 480},
    {'Month': 'September', 'Produce Weight (in kg)': 450},
    {'Month': 'October', 'Produce Weight (in kg)': 380},
    {'Month': 'November', 'Produce Weight (in kg)': 320},
    {'Month': 'December', 'Produce Weight (in kg)': 200}
]

# Convert the table data to a pandas DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the lineplot
lineplot = sns.lineplot(x='Month', y='Produce Weight (in kg)', data=df, sort=False, marker='o')

# Use fill_between from Matplotlib to fill the area under the line
plt.fill_between(x=df['Month'], y1=df['Produce Weight (in kg)'], alpha=0.3)

# Customize the plot with diversified visual encoding
plt.title('Monthly Produce Weight')
plt.xticks(rotation=45, ha='right')  # Rotate the x-axis labels for better readability
plt.xlabel('Month')  # X-axis Label
plt.ylabel('Weight (kg)')  # Y-axis Label
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping

# Show the plot
plt.show()