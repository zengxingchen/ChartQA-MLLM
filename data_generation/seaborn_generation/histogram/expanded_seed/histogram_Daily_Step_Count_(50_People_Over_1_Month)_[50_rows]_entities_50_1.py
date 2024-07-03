
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = [
    {'Person': 'Person 1', 'Steps': 3245},
    {'Person': 'Person 2', 'Steps': 5678},
    {'Person': 'Person 3', 'Steps': 8392},
    {'Person': 'Person 4', 'Steps': 11234},
    {'Person': 'Person 5', 'Steps': 9483},
    {'Person': 'Person 6', 'Steps': 7492},
    {'Person': 'Person 7', 'Steps': 5047},
    {'Person': 'Person 8', 'Steps': 6861},
    {'Person': 'Person 9', 'Steps': 7023},
    {'Person': 'Person 10', 'Steps': 11542},
    {'Person': 'Person 11', 'Steps': 9437},
    {'Person': 'Person 12', 'Steps': 8327},
    {'Person': 'Person 13', 'Steps': 4879},
    {'Person': 'Person 14', 'Steps': 2975},
    {'Person': 'Person 15', 'Steps': 10489}
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Set the style of seaborn
sns.set_style('whitegrid')

# Create a histogram plot
plt.figure(figsize=(10, 6)) # Customize the size of the plot
sns.histplot(data=df, x='Steps', bins=8, kde=True, color='skyblue', edgecolor='black')

# Additional customizations for a better looking plot
plt.title('Histogram of Steps Taken by Persons')
plt.xlabel('Number of Steps')
plt.ylabel('Frequency')
plt.xticks(rotation=45) # Rotate the x-axis labels for better visibility
plt.tight_layout() # Fit the plot nicely within the figure area

# Show the plot
plt.show()