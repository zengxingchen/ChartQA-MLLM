
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for visualization
data = {
    'Topic': ['Cinema', 'Cinema', 'Music', 'Music', 'Sports', 'Sports', 'Art', 'Art', 'Tech', 'Tech', 'History', 'History', 'Travel', 'Travel', 'Food', 'Food'],
    'SubTopic': ['Movies', 'Directing', 'Composition', 'Performance', 'Soccer', 'Basketball', 'Painting', 'Sculpture', 'AI', 'Robotics', 'Medieval', 'Modern', 'Adventure', 'Guides', 'Cuisine', 'Nutrition'],
    'InterestLevel': [90, 85, 88, 92, 86, 89, 87, 84, 91, 93, 88, 90, 89, 87, 85, 92],
    'HoursSpent': [12, 15, 14, 13, 16, 11, 10, 9, 13, 12, 14, 13, 15, 12, 14, 11]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a Bubble Chart with Seaborn
plt.figure(figsize=(18, 10))
bubble = sns.scatterplot(data=df, x="Topic", y="SubTopic", size="HoursSpent", 
                         legend=True, sizes=(100, 1000), 
                         hue="InterestLevel", palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#33FFF6", "#FFC300", "#DAF7A6", "#581845"])

# Customizing the axes and title
plt.title("Interest Levels and Hours Spent in Various Leisure Activities", fontsize=20)
plt.xlabel("Topic", fontsize=15)
plt.ylabel("SubTopic", fontsize=15)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1), title="Interest Level")

plt.show()