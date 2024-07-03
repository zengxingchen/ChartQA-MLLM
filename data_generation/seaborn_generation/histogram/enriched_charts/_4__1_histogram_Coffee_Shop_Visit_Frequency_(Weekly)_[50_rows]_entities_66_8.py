
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Height data points
height_data = [150, 152, 154, 155, 157, 160, 161, 162, 165, 168, 170, 172, 
               173, 175, 177, 180, 182, 184, 185, 188, 190, 192, 193, 195, 
               197, 200, 202, 204, 205, 207, 210]

# Create the DataFrame
df = pd.DataFrame(height_data, columns=['Height'])

# Set the style
sns.set_style('whitegrid')

# Create the histogram
plt.figure(figsize=(12, 8))
sns.histplot(df['Height'], bins=15, color="#2ecc71", binwidth=3, orientation='horizontal')

# Customize the plot with title and labels
plt.title('Height Distribution in Sports Players', fontsize=15, pad=20)
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Height (cm)', fontsize=12)

# Show the plot
plt.show()