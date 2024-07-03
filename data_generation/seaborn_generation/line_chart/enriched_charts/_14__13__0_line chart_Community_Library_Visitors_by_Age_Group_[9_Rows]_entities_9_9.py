
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Enrolled_Students': [350, 370, 400, 390, 410, 420, 415, 430, 440, 445, 455, 470]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(12, 6))

# Plotting the line chart
line_plot = sns.lineplot(x='Month', y='Enrolled_Students', data=df, color='#2E8B57', marker='o')

# Annotating specific data points
plt.annotate('Mid-year dip', xy=('July', 415), xytext=('August', 410),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=12)
plt.annotate('End of year peak', xy=('December', 470), xytext=('November', 465),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=12)

# Setting the title and labels
plt.title('Monthly Enrollment in 2024 for XYZ School', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Enrolled Students', fontsize=12)

# Adjusting the x-axis to show all the months clearly
plt.xticks(rotation=45)

# Show the plot with the customizations
plt.show()