
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data points provided
data = {
    'Hobby': ["Reading", "Writing", "Painting", "Dancing", "Cycling", "Hiking", "Gaming", "Gardening", 
              "Cooking", "Swimming", "Photography", "Knitting", "Yoga", "Fishing", "Running", 
              "Meditation", "Traveling", "Bird Watching", "Stargazing", "Woodworking"],
    'Average Hours per Week': [5, 3, 4, 6, 7, 8, 10, 2, 5, 4, 3, 2, 6, 4, 7, 3, 9, 2, 3, 4]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the bar plot and modify it according to the given options
plt.figure(figsize=(14, 10))  # Change width and height of chart
barplot = sns.barplot(y='Hobby', x='Average Hours per Week', data=df, color="#FF6347", ci=None)  # Horizontal and specific color

# Modify the height of bars
for bar in barplot.patches:
    bar.set_height(0.6)  # Adjust the height of the bars

# Adjust the appearance of the plot
plt.title('Average Hours Spent on Hobbies per Week', fontsize=18, pad=20)
plt.xlabel('Average Hours per Week', fontsize=14)
plt.ylabel('Hobby', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Remove the top and right spines
sns.despine(left=True, bottom=True)

# Show the barplot
plt.show()