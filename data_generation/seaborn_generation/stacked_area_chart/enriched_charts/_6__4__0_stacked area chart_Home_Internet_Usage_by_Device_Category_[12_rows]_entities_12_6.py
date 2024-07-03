
import pandas as pd
import matplotlib.pyplot as plt

# Define the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'New York': [32, 35, 45, 55, 65, 75, 85, 83, 75, 65, 55, 38],
    'Los Angeles': [58, 60, 65, 68, 70, 75, 80, 79, 77, 70, 65, 60],
    'Chicago': [28, 30, 40, 50, 60, 70, 75, 73, 70, 60, 50, 35]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data preparation for stacked area chart
df_melted = df.melt('Month', var_name='City', value_name='Temperature')

# Transformation of 'Month' to categorical type for proper ordering
df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

# Plotting
plt.figure(figsize=(16, 10))

# New York: #4682B4 (Steel Blue), Los Angeles: #FFD700 (Gold), Chicago: #DC143C (Crimson)
colors = ["#4682B4", "#FFD700", "#DC143C"]

# Stackplot
plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Annual Temperature Data for Different Cities', fontsize=20, pad=20)
plt.ylabel('Temperature (°F)', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(title='City', loc='upper right')

# Annotation
for i, row in df.iterrows():
    total_temp = row['New York'] + row['Los Angeles'] + row['Chicago']
    plt.text(row['Month'], total_temp, f'{total_temp}', ha='center', va='bottom')

# Remove top and right borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Show the plot
plt.tight_layout()
plt.show()