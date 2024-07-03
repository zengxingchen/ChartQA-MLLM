
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for visualization
data = {
    'Department': ['Economics', 'Economics', 'Finance', 'Finance', 'Accounting', 'Accounting', 'Statistics', 'Statistics', 'Banking', 'Banking', 'Insurance', 'Insurance', 'Taxation', 'Taxation', 'Auditing', 'Auditing'],
    'Course': ['Microeconomics', 'Macroeconomics', 'Investment Analysis', 'Corporate Finance', 'Financial Accounting', 'Managerial Accounting', 'Probability Theory', 'Statistical Inference', 'Banking Operations', 'Risk Management', 'Life Insurance', 'Property Insurance', 'Tax Law', 'Tax Planning', 'Internal Auditing', 'External Auditing'],
    'AverageScore': [89, 87, 93, 90, 88, 85, 92, 90, 87, 91, 89, 90, 88, 87, 92, 94],
    'HoursStudy': [13, 15, 12, 14, 10, 12, 11, 13, 14, 12, 10, 12, 11, 13, 14, 15]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a Bubble Chart with Seaborn
plt.figure(figsize=(18, 12)) # Modified width and height
bubble = sns.scatterplot(data=df, x="Department", y="Course", size="HoursStudy", 
                         legend=True, sizes=(100, 1000), 
                         hue="AverageScore", palette=["#FF6347", "#4682B4", "#32CD32", "#FFD700", "#8A2BE2", "#D2691E", "#FF4500", "#DA70D6"])

# Customizing the axes and title
plt.title("Study Hours and Average Scores in Economics & Finance Courses", fontsize=22, pad=20)
plt.xlabel("Department", fontsize=16)
plt.ylabel("Course", fontsize=16)
plt.legend(title="Average Score", bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()