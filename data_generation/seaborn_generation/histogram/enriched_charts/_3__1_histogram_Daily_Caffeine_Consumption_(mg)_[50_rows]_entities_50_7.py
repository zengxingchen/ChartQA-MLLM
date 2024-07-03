
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame with generated data
data = {
    'Speed': [12.4, 14.8, 11.2, 13.5, 15.6, 12.7, 14.2, 10.8, 13.9, 16.1, 11.5, 
              14.5, 13.1, 15.2, 12.3, 14.0, 13.4, 11.8, 15.0, 12.9, 13.7, 14.6, 
              12.1, 15.3, 13.6, 12.0, 14.9, 15.4, 11.9, 13.8, 14.3, 13.2, 12.5, 
              14.4, 13.3, 12.6, 15.1, 11.7, 13.0, 15.5]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Set the size of the figure
plt.figure(figsize=(10, 8))

# Plot the histogram chart
sns.histplot(df['Speed'], bins=10, kde=False, color='#ff5733', binwidth=0.5, orientation='horizontal')

# Adding title and labels
plt.title('Distribution of Running Speeds of Athletes', pad=20)
plt.xlabel('Frequency')
plt.ylabel('Speed (mph)')

# Show plot
plt.show()