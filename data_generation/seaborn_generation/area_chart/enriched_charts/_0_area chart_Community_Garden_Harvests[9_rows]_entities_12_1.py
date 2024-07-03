
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"],
    "AverageTemperature": [0, 1.3, 3.5, 8.6, 13.4, 17.5, 19.0, 18.6, 14.9, 10.5, 4.8, 1.2]
}
df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the area chart
plt.figure(figsize=(12, 6))
area_chart = sns.lineplot(data=df, x='Month', y='AverageTemperature', color="#FF5733")

# Filling the area under the line
plt.fill_between(data['Month'], data['AverageTemperature'], color="#FFC300")

# Customize the axes and title
area_chart.set_title('Average Monthly Temperatures for 2023', fontsize=18)
area_chart.set_xlabel('Month', fontsize=12)
area_chart.set_ylabel('Temperature (°C)', fontsize=12)

# Adding annotations
for i, temp in enumerate(df['AverageTemperature']):
    plt.text(df['Month'][i], temp, str(temp), horizontalalignment='center')

# Show the plot
plt.tight_layout()
plt.show()