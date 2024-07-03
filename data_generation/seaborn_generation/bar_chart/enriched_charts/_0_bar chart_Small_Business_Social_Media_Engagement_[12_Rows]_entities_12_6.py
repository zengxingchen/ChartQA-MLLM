
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate the data
data = {
    'Country': ['Canada', 'United States', 'Mexico', 'Brazil', 'United Kingdom', 'Germany', 
                'France', 'Italy', 'Russia', 'China', 'India', 'Australia', 'Japan', 
                'South Korea', 'Nigeria', 'Egypt'],
    'Population_Density': [4, 36, 66, 25, 275, 233, 119, 206, 9, 153, 464, 3, 347, 527, 226, 103]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the bar chart
plt.figure(figsize=(14, 8))  # Change width and height of the chart
ax = sns.barplot(x='Population_Density', y='Country', data=df, palette=['#003f5c', '#58508d', '#bc5090', 
                                                                        '#ff6361', '#ffa600', '#a05195',
                                                                        '#f95d6a', '#d45087', '#2f4b7c',
                                                                        '#665191', '#a05195', '#f95d6a',
                                                                        '#ff7c43', '#ffa600', '#003f5c',
                                                                        '#488f31'],
                 dodge=False)

# Modify the width of bars
for bar in ax.patches:
    bar.set_height(0.4)

# Set the title
ax.set_title('Population Density by Country (inhabitants per square kilometer)', fontsize=16)

# Show the plot
plt.show()