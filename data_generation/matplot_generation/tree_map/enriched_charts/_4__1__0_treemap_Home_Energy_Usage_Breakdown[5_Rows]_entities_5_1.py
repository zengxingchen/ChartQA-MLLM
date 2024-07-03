
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Health Topic': ['Mental Health', 'Physical Fitness', 'Nutrition', 'Sleep', 'Stress Management', 
                     'Hydration', 'Healthy Aging', 'Preventive Care', 'Vaccinations', 
                     'Sexual Health', 'Chronic Diseases', 'Substance Abuse', 
                     'Occupational Health', 'Infectious Diseases', 'Environmental Health'],
    'Percentage': [25.2, 20.1, 18.3, 15.5, 10.7, 5.8, 4.4, 3.0, 2.6, 1.4, 1.0, 0.7, 0.5, 0.4, 0.3]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#9edae5', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2']

# Create the figure with specified figure size
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Percentage'], label=df['Health Topic'], color=colors, alpha=0.8)

# Set the title of the plot
plt.title('Distribution of Health Topics', fontsize=22, pad=20)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()