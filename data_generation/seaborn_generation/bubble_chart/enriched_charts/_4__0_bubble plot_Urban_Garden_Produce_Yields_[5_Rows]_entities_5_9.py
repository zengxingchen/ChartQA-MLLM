
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for visualization
data = {
    'Department': ['Business', 'Business', 'Music', 'Music', 'Science', 'Science', 'Education', 'Education', 'Economics', 'Economics', 'Food', 'Food', 'Technology', 'Technology', 'Health', 'Health'],
    'Course': ['Marketing', 'Management', 'Theory', 'Performance', 'Physics', 'Biology', 'Pedagogy', 'Assessment', 'Microeconomics', 'Macroeconomics', 'Nutrition', 'Culinary Arts', 'AI', 'Robotics', 'Psychology', 'Medicine'],
    'AverageScore': [82, 85, 88, 90, 91, 84, 80, 86, 89, 87, 92, 94, 95, 93, 88, 90],
    'HoursStudy': [10, 12, 8, 11, 14, 12, 9, 11, 13, 15, 10, 12, 14, 13, 11, 15]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a Bubble Chart with Seaborn
plt.figure(figsize=(16, 10)) # Modified width and height
bubble = sns.scatterplot(data=df, x="Department", y="Course", size="HoursStudy", 
                         legend=False, sizes=(100, 1000), 
                         hue="AverageScore", palette=["#FFA07A", "#20B2AA", "#778899", "#B0C4DE", "#CD5C5C", "#8FBC8F", "#FFD700", "#DDA0DD"])

# Customizing the axes and title (with changed topic and headline)
plt.title("Study Hours and Average Scores across Various Courses", fontsize=20)
plt.xlabel("Department", fontsize=15)
plt.ylabel("Course", fontsize=15)

plt.show()