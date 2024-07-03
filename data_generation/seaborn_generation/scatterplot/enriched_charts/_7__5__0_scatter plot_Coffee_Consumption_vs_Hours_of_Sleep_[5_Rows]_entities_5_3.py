
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Activity': ['Exercise', 'Meditation', 'Reading', 'Socializing', 'Sleeping', 'Cooking', 'Gardening', 
                 'Traveling', 'Hiking', 'Painting', 'Music', 'Volunteering', 'Yoga', 'Writing', 'Photography', 'Crafting'],
    'HoursPerWeek': [5, 2, 4, 7, 8, 3, 2, 1, 3, 2, 4, 3, 3, 2, 2, 1],
    'HappinessScore': [80, 85, 75, 90, 95, 70, 78, 82, 88, 76, 81, 87, 84, 79, 77, 73]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 7))

# Create scatterplot
scatter = sns.scatterplot(
    x='HoursPerWeek', 
    y='HappinessScore', 
    data=df, 
    s=100,  # size of points
    color='#FF6347'  # tomato color
)

# Setting the title
plt.title('Hours Spent on Wellness Activities vs Happiness Score', pad=20)

# Add labels to the axes
plt.xlabel('Hours Spent on Activities per Week')
plt.ylabel('Happiness Score')

# Show the plot
plt.show()