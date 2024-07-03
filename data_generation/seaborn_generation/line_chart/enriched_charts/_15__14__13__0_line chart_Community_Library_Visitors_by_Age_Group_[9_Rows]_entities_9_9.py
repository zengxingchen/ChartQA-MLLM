
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature': [30, 32, 40, 55, 65, 75, 80, 78, 70, 60, 45, 35]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(10, 5))

# Plotting the line chart
line_plot = sns.lineplot(x='Month', y='Average_Temperature', data=df, color='#1E90FF', marker='o')

# Annotating specific data points
plt.annotate('Summer peak', xy=('July', 80), xytext=('June', 78),
             arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=12)
plt.annotate('Winter low', xy=('January', 30), xytext=('February', 32),
             arrowprops=dict(facecolor='purple', shrink=0.05), fontsize=12)

# Setting the title and labels
plt.title('Average Monthly Temperatures in 2024', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Temperature (°F)', fontsize=12)

# Adjusting the x-axis to show all the months clearly
plt.xticks(rotation=45)

# Show the plot with the customizations
plt.show()