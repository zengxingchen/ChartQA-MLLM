
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Books_Published': [150, 180, 220, 240, 230, 260, 290, 300, 280, 320, 350, 370]
}
df = pd.DataFrame(data)

# Ensure that the Year column is treated as categorical with the correct order
df['Year'] = pd.Categorical(df['Year'], categories=data['Year'], ordered=True)

# Set the aesthetic style of the plots
sns.set_theme()

# Create the area chart
plt.figure(figsize=(16, 8))
area_chart = sns.lineplot(data=df, x='Year', y='Books_Published', sort=False, color='#4682B4')
area_chart.fill_between(df['Year'], df['Books_Published'], alpha=0.4, color='#4682B4')

# Assign an annotation/text label on the chart for the highest number of books published
plt.text(x=2021, y=370, s='Peak Books Published (370)', color='darkred', va='bottom', ha='center')

# Set chart title and labels
plt.title('Annual Book Publications Over the Years', loc='center', pad=20)
plt.xlabel('Year')
plt.ylabel('Number of Books Published')

# Finalize and show the plot
plt.tight_layout()
plt.show()