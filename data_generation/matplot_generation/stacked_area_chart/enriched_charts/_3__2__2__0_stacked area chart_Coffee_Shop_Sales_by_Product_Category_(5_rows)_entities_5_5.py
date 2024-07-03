
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Sports': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85],
    'Technology': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    'Entertainment': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
}

# Create a dataframe
df = pd.DataFrame(data)

# Define x-axis based on 'Month'
x = df['Month']

# Plot using specific color codes
plt.figure(figsize=(18, 12))
plt.stackplot(x, df['Sports'], df['Technology'], df['Entertainment'], 
              colors=['#ff5733', '#33ff57', '#3357ff'], labels=['Sports', 'Technology', 'Entertainment'])

# Adding title and labels
plt.title('Monthly Engagement in Sports, Technology, and Entertainment Over a Year', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Engagement Hours', fontsize=14)

# Add annotations
plt.annotate('Sports in January', xy=(0, df['Sports'][0]), 
             xytext=(0, 180), arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.annotate('Entertainment in December', xy=(11, df['Sports'][11] + df['Technology'][11] + df['Entertainment'][11]), 
             xytext=(11, 400), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Adding legend
plt.legend(loc='upper left')

# Display the figure
plt.show()