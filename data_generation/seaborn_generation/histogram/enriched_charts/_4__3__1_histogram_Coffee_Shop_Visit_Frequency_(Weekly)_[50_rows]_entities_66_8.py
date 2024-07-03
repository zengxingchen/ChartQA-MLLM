
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points for the new topic "Height Distribution of Athletes"
height_data = [165, 170, 175, 160, 180, 185, 150, 155, 190, 195, 200, 210, 155, 160, 165, 
               175, 185, 190, 195, 155, 160, 165, 170, 175, 180, 185, 190, 195, 160, 165, 
               170, 175, 180, 185, 190, 195, 155, 160, 165, 170, 175, 180, 185, 190, 195, 
               160, 165, 170, 175, 180, 185, 190, 195]

# Create the DataFrame
df = pd.DataFrame(height_data, columns=['Height'])

# Set the style
sns.set_style('whitegrid')

# Create the histogram
plt.figure(figsize=(16, 10))
sns.histplot(df['Height'], bins=10, color="#4682B4", binwidth=5, kde=True, element="bars", orientation="horizontal")

# Customize the plot with title and labels
plt.title('Height Distribution of Athletes', fontsize=20, pad=20)
plt.xlabel('Frequency', fontsize=15)
plt.ylabel('Height (cm)', fontsize=15)

# Show the plot
plt.show()