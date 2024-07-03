
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature_C': [-2, -1, 4, 10, 16, 20, 23, 22, 17, 10, 4, -1]
}

df = pd.DataFrame(data)

# Converting 'Month' to a categorical type for proper ordering
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Initialize the figure
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")

# Create an area chart
sns.lineplot(data=df, x='Month', y='Average_Temperature_C', color="#1f77b4")
plt.fill_between(data=df, x='Month', y1='Average_Temperature_C', alpha=0.3, color="#1f77b4")

# Annotating the maximum temperature
max_temp = df['Average_Temperature_C'].max()
max_temp_month = df.loc[df['Average_Temperature_C'] == max_temp, 'Month'].iloc[0]
plt.text(x=max_temp_month, y=max_temp, s='Peak\n{}°C'.format(max_temp), color="black",
         horizontalalignment='left', size='medium', style='italic')

# Customize the axes and the title
plt.title("Average Monthly Temperatures in City XYZ")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")

# Show the plot
plt.show()