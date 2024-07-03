
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Expenditure on Education': [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410],
    'Expenditure on Healthcare': [250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360],
    'Expenditure on Infrastructure': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data preparation for stacked area chart
df_melted = df.melt('Month', var_name='Category', value_name='Value')

# Transformation of 'Month' to categorical type for proper ordering
df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

# Plotting
plt.figure(figsize=(14, 8))

# Expenditure on Education: #FFA07A (Light Salmon), Expenditure on Healthcare: #20B2AA (Light Sea Green), Expenditure on Infrastructure: #9370DB (Medium Purple)
colors = ["#FFA07A", "#20B2AA", "#9370DB"]

# Stackplot
plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Monthly Government Expenditures for 2023', fontsize=20, pad=20)
plt.ylabel('Expenditure (in millions)', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Category', loc='upper left')

# Annotation
for i, row in df.iterrows():
    total_value = row['Expenditure on Education'] + row['Expenditure on Healthcare'] + row['Expenditure on Infrastructure']
    plt.text(row['Month'], total_value, f'{total_value}', ha='center', va='bottom')

sns.despine()

# Show the plot
plt.tight_layout()
plt.show()