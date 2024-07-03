
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for visualization
data = {
    'Department': ['Fashion', 'Fashion', 'Beauty', 'Beauty', 'Science', 'Science', 'Art', 'Art', 'History', 'History', 'Travel', 'Travel', 'Music', 'Music', 'Health', 'Health'],
    'Course': ['Design', 'Textiles', 'Makeup', 'Skincare', 'Physics', 'Chemistry', 'Painting', 'Sculpture', 'Medieval', 'Modern', 'Adventure', 'Guides', 'Composition', 'Performance', 'Wellness', 'Medicine'],
    'AverageScore': [88, 82, 90, 85, 92, 84, 78, 80, 87, 91, 86, 88, 83, 85, 89, 92],
    'HoursStudy': [12, 10, 14, 13, 15, 11, 9, 8, 10, 13, 14, 12, 11, 13, 14, 12]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a Bubble Chart with Seaborn
plt.figure(figsize=(16, 9))
bubble = sns.scatterplot(data=df, x="Department", y="Course", size="HoursStudy", 
                         legend=True, sizes=(100, 1000), 
                         hue="AverageScore", palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#33FFF6"])

# Customizing the axes and title
plt.title("Average Scores and Study Hours in Fashion & Beauty", fontsize=20)
plt.xlabel("Department", fontsize=15)
plt.ylabel("Course", fontsize=15)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Average Score")

plt.show()