
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data_points = {
    'value': [75, 85, 95, 70, 90, 100, 80, 105, 115, 120, 130, 
              125, 135, 110, 140, 145, 150, 160, 170, 180, 190, 200]
}

# Convert to DataFrame
df = pd.DataFrame(data_points)

# Set the style
sns.set(style="whitegrid")

# Size of the figure
plt.figure(figsize=(12, 6))

# Create the histogram
sns.histplot(data=df, x="value", color="#e74c3c", binwidth=15, orientation="vertical")

# Set the title and labels
plt.title('Distribution of Monthly Sales Revenue', fontsize=16)
plt.xlabel('Sales Revenue')
plt.ylabel('Frequency')

# Show the plot
plt.show()