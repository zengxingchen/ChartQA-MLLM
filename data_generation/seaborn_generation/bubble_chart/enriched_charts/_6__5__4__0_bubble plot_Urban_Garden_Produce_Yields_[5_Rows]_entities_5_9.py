
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for visualization
data = {
    'Category': ['Mental Health', 'Mental Health', 'Physical Health', 'Physical Health', 'Emotional Wellbeing', 'Emotional Wellbeing', 'Social Health', 'Social Health', 'Sleep Health', 'Sleep Health', 'Work-Life Balance', 'Work-Life Balance', 'Substance Abuse Prevention', 'Substance Abuse Prevention', 'Child and Adolescent Health', 'Child and Adolescent Health'],
    'Subcategory': ['Stress Management', 'Anxiety Reduction', 'Exercise', 'Nutrition', 'Meditation', 'Gratitude Journaling', 'Community Engagement', 'Volunteering', 'Good Sleep Hygiene', 'Regular Sleep Schedule', 'Time Management', 'Workplace Flexibility', 'Awareness Programs', 'Counseling', 'Prenatal Care', 'School Health Programs'],
    'ImpactScore': [80, 85, 88, 90, 92, 89, 84, 91, 86, 88, 90, 87, 93, 89, 91, 92],
    'EffortHours': [12, 14, 10, 11, 13, 15, 12, 13, 14, 10, 11, 12, 14, 10, 12, 13]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a Bubble Chart with Seaborn
plt.figure(figsize=(16, 10))  # Modified width and height
bubble = sns.scatterplot(data=df, x="Category", y="Subcategory", size="EffortHours", 
                         legend=False, sizes=(100, 1000), 
                         hue="ImpactScore", palette=["#3498db", "#2ecc71", "#e74c3c", "#f1c40f", "#9b59b6", "#34495e", "#e67e22", "#1abc9c"])

# Customizing the axes and title
plt.title("Impact and Effort in Health & Psychology Projects", fontsize=20, pad=20)
plt.xlabel("Category", fontsize=15)
plt.ylabel("Subcategory", fontsize=15)

# Adding legend
plt.legend(title="Impact Score", fontsize=12, title_fontsize=14, loc='upper right')

plt.show()