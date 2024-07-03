
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"],
    "Revenue": [20000, 25000, 30000, 35000, 40000, 45000, 47000, 46000, 43000, 41000, 38000, 34000]
}
df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the area chart
plt.figure(figsize=(16, 10))
area_chart = sns.lineplot(data=df, x='Month', y='Revenue', color="#FF5733")

# Filling the area under the line
plt.fill_between(data['Month'], df['Revenue'], color="#FFC300")

# Customize the axes and title
area_chart.set_title('Monthly Sales Revenue of a Store in 2023', fontsize=20, pad=20)
area_chart.set_xlabel('Month', fontsize=14)
area_chart.set_ylabel('Revenue in USD', fontsize=14)

# Adding annotations
for i, revenue in enumerate(df['Revenue']):
    plt.text(df['Month'][i], revenue, str(revenue), horizontalalignment='center')

# Show the plot
plt.tight_layout()
plt.show()