
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for visualization
data = {
    'Category': ['Physical Health', 'Physical Health', 'Mental Health', 'Mental Health', 'Emotional Health', 'Emotional Health', 'Cognitive Health', 'Cognitive Health', 'Social Health', 'Social Health', 'Spiritual Health', 'Spiritual Health', 'Occupational Health', 'Occupational Health', 'Environmental Health', 'Environmental Health'],
    'SubCategory': ['Fitness', 'Nutrition', 'Stress Management', 'Meditation', 'Self-Care', 'Relationships', 'Memory', 'Learning', 'Community', 'Volunteering', 'Mindfulness', 'Gratitude', 'Work-Life Balance', 'Career Development', 'Sustainability', 'Outdoor Activities'],
    'AverageRating': [85, 90, 88, 95, 80, 82, 89, 92, 87, 91, 93, 88, 84, 86, 90, 85],
    'WeeklySessions': [10, 8, 12, 6, 7, 9, 11, 10, 5, 4, 6, 8, 10, 7, 8, 9]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a Bubble Chart with Seaborn
plt.figure(figsize=(16, 9)) # Modified width and height
bubble = sns.scatterplot(data=df, x="Category", y="SubCategory", size="WeeklySessions", 
                         legend=False, sizes=(100, 1000), 
                         hue="AverageRating", palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FF8F33"])

# Customizing the axes and title
plt.title("Health & Psychology: Ratings and Weekly Sessions", fontsize=20, pad=20)
plt.xlabel("Category", fontsize=15)
plt.ylabel("SubCategory", fontsize=15)

# Adjust legend position to avoid overlapping with title
plt.legend(title='Average Rating', loc='lower right', bbox_to_anchor=(1.25, 0.5), borderaxespad=0)

plt.show()