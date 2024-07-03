
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Art_Exhibitions': [10, 15, 20, 25, 30, 35, 40, 38, 35, 28, 22, 15]
}
df = pd.DataFrame(data)

# Ensure that the Month column is treated as categorical with the correct order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_theme()

# Create the area chart
plt.figure(figsize=(16, 8))
area_chart = sns.lineplot(data=df, x='Month', y='Art_Exhibitions', sort=False, color='#1f77b4')
area_chart.fill_between(df['Month'], df['Art_Exhibitions'], alpha=0.4, color='#1f77b4')

# Assign an annotation/text label on the chart for the highest number of art exhibitions
plt.text(x='July', y=40, s='Peak Exhibitions (40)', color='red', va='bottom', ha='center')

# Set chart title and labels
plt.title('Monthly Number of Art Exhibitions in the City')
plt.xlabel('Month')
plt.ylabel('Number of Art Exhibitions')

# Finalize and show the plot
plt.tight_layout()
plt.show()