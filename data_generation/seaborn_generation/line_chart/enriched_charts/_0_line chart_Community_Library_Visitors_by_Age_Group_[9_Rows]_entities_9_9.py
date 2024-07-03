
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature': [5, 6, 10, 14, 18, 22, 25, 24, 20, 15, 10, 7]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(12, 6))

# Plotting the line chart
line_plot = sns.lineplot(x='Month', y='Average_Temperature', data=df, color='#FF5733', marker='o')

# Annotating specific data points
plt.annotate('Peak summer', xy=('July', 25), xytext=('August', 26),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)
plt.annotate('Start of fall', xy=('September', 20), xytext=('October', 21),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=12)

# Setting the title and labels
plt.title('Average Monthly Temperature in City XYZ', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)

# Adjusting the x-axis to show all the months clearly
plt.xticks(rotation=45)

# Show the plot with the customizations
plt.show()