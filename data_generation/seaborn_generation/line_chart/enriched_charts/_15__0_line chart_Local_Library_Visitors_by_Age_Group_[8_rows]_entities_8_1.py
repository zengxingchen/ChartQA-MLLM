
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Caloric_Intake': [2200, 2100, 2300, 2500, 2700, 2800, 3000, 2900, 2600, 2400, 2300, 2200]
}

# Create DataFrame
df = pd.DataFrame(data)

# Adjusting the aesthetics
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(14, 7))
lineplot = sns.lineplot(x='Month', y='Average_Caloric_Intake', data=df, marker='o', linewidth=2.5,
                        color='#2ca02c')

# Customize the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Caloric Intake', fontsize=14)
plt.title('Monthly Average Caloric Intake', fontsize=18)

# Annotating the data points
for x, y in zip(df['Month'], df['Average_Caloric_Intake']):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()