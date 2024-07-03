
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"],
    "Visitors": [1200, 1500, 1800, 2200, 2600, 3000, 3500, 3400, 3200, 2900, 2500, 2100]
}
df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the area chart
plt.figure(figsize=(18, 12))
area_chart = sns.lineplot(data=df, x='Month', y='Visitors', color="#1f77b4")

# Filling the area under the line
plt.fill_between(data['Month'], df['Visitors'], color="#aec7e8")

# Customize the axes and title
area_chart.set_title('Monthly Visitors to a National Park in 2023', fontsize=24, pad=30)
area_chart.set_xlabel('Month', fontsize=16)
area_chart.set_ylabel('Number of Visitors', fontsize=16)

# Adding annotations
for i, visitors in enumerate(df['Visitors']):
    plt.text(df['Month'][i], visitors, str(visitors), horizontalalignment='center')

# Show the plot
plt.tight_layout()
plt.show()