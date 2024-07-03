
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Calorie_Intake': [2000, 2100, 2200, 2150, 2250, 2300, 2400, 2350, 2300, 2250, 2200, 2150]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the order of the months
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 'September',
    'October', 'November', 'December'], ordered=True)

# Plot the data
plt.figure(figsize=(12, 6))
ax = sns.lineplot(x='Month', y='Calorie_Intake', data=df, 
                  marker='o', color='#FF5733')

# Annotations and labels
for x, y in zip(df['Month'], df['Calorie_Intake']):
    ax.text(x, y, f'{y} cal', color='black', ha='center', va='bottom')

# Customize appearance
ax.set_title('Monthly Average Calorie Intake', fontsize=16, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Calorie Intake (cal)', fontsize=14)
sns.set_style('whitegrid')

plt.show()