
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [50, 55, 65, 70, 80, 95, 100, 90, 85, 80, 75, 60]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure with modified size
plt.figure(figsize=(14, 7))

# Plotting the line chart with a different color scheme
line_plot = sns.lineplot(x='Month', y='Revenue', data=df, color='#3498DB', marker='o')

# Annotating specific data points
plt.annotate('Peak Revenue', xy=('July', 100), xytext=('August', 105),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=12)
plt.annotate('Post-Summer Drop', xy=('August', 90), xytext=('September', 95),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=12)

# Setting the title and labels with a new topic
plt.title('Monthly Revenue Trends for XYZ Corp', fontsize=18, loc='center')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($K)', fontsize=12)

# Adjusting the x-axis to show all the months clearly
plt.xticks(rotation=45)

# Show the plot with the customizations
plt.show()