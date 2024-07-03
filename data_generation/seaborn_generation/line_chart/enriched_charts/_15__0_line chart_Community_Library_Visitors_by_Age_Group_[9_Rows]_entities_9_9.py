
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Number_of_Tourists': [3000, 3200, 5000, 8000, 12000, 18000, 25000, 24000, 17000, 11000, 6000, 3500]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(14, 7))

# Plotting the line chart
line_plot = sns.lineplot(x='Month', y='Number_of_Tourists', data=df, color='#1f77b4', marker='o')

# Annotating specific data points
plt.annotate('Peak Season', xy=('July', 25000), xytext=('August', 26000),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)
plt.annotate('Low Season', xy=('January', 3000), xytext=('February', 4000),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=12)

# Setting the title and labels
plt.title('Monthly Tourist Visits to Landmark XYZ', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Tourists', fontsize=12)

# Adjusting the x-axis to show all the months clearly
plt.xticks(rotation=45)

# Show the plot with the customizations
plt.show()