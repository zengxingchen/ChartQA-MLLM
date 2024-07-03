
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Calories': [2000, 2200, 2100, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100]
}

df = pd.DataFrame(data)

# Converting 'Month' to a categorical type for proper ordering
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Initialize the figure
plt.figure(figsize=(16, 8))
plt.style.use('seaborn-whitegrid')

# Create an area chart
plt.plot(df['Month'], df['Calories'], color="#3498db")
plt.fill_between(df['Month'], df['Calories'], alpha=0.3, color="#3498db")

# Annotating the maximum calories
max_calories = df['Calories'].max()
max_calories_month = df.loc[df['Calories'] == max_calories, 'Month'].iloc[0]
plt.text(x=max_calories_month, y=max_calories, s='Peak\n{:,} cal'.format(max_calories), color="black",
         horizontalalignment='left', size='medium', style='italic')

# Customize the axes and the title
plt.title("Monthly Caloric Intake for an Average Individual", pad=20)
plt.xlabel("Month")
plt.ylabel("Calories")

# Show the plot
plt.show()