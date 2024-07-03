
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [10000, 12000, 15000, 17000, 16000, 18000, 19000, 22000, 21000, 23000, 24000, 25000]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(14, 8))

# Plotting the line chart
line_plot = sns.lineplot(x='Month', y='Revenue', data=df, color='#1F77B4', marker='o')

# Annotating specific data points
plt.annotate('Mid-year boost', xy=('June', 18000), xytext=('July', 18500),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)
plt.annotate('End of year peak', xy=('December', 25000), xytext=('November', 24500),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=12)

# Setting the title and labels
plt.title('Monthly Revenue in 2024 for ABC Corp', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (USD)', fontsize=12)

# Adjusting the x-axis to show all the months clearly
plt.xticks(rotation=45)

# Show the plot with the customizations
plt.show()