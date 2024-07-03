
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Time of Day (24h)': '08:00', 'Latte Sales (Units)': 25, 'Espresso Sales (Units)': 30, 'Iced Coffee Sales (Units)': 10},
    {'Time of Day (24h)': '11:00', 'Latte Sales (Units)': 45, 'Espresso Sales (Units)': 35, 'Iced Coffee Sales (Units)': 40},
    {'Time of Day (24h)': '14:00', 'Latte Sales (Units)': 20, 'Espresso Sales (Units)': 25, 'Iced Coffee Sales (Units)': 35},
    {'Time of Day (24h)': '17:00', 'Latte Sales (Units)': 15, 'Espresso Sales (Units)': 20, 'Iced Coffee Sales (Units)': 50},
    {'Time of Day (24h)': '20:00', 'Latte Sales (Units)': 5, 'Espresso Sales (Units)': 10, 'Iced Coffee Sales (Units)': 30}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# We need to convert the time into a numerical value for plotting
# For simplicity, let's convert the hour part only
df['Time (Hours)'] = pd.to_datetime(df['Time of Day (24h)']).dt.hour

# Now we melt the DataFrame to have coffee types as a separate categorical variable
df_melted = df.melt(id_vars=['Time of Day (24h)', 'Time (Hours)'], 
                    value_vars=['Latte Sales (Units)', 'Espresso Sales (Units)', 'Iced Coffee Sales (Units)'],
                    var_name='Coffee Type', value_name='Sales (Units)')

# Create a scatterplot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(data=df_melted, x='Time (Hours)', y='Sales (Units)',
                               hue='Coffee Type', style='Coffee Type', size='Sales (Units)',
                               sizes=(50, 200))

# Customize the axes and legends
scatter_plot.set_title('Coffee Sales Scatterplot')
scatter_plot.set_ylabel('Sales (Units)')
scatter_plot.set_xlabel('Time of Day (24h)')
scatter_plot.legend(title='Coffee Type', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()