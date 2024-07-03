
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for visualization
data = {
    'Department': ['Mathematics', 'Mathematics', 'English', 'English', 'Science', 'Science', 'Engineering', 'Engineering', 'Arts', 'Arts', 'Law', 'Law', 'Business', 'Business', 'Medical', 'Medical'],
    'Course': ['Calculus', 'Algebra', 'Literature', 'Writing', 'Physics', 'Chemistry', 'Mechanics', 'Thermodynamics', 'Painting', 'Music', 'Contracts', 'Torts', 'Economics', 'Finance', 'Anatomy', 'Pharmacology'],
    'AverageScore': [78, 85, 83, 78, 90, 82, 88, 85, 80, 92, 86, 89, 81, 87, 84, 91],
    'HoursStudy': [12, 7, 9, 10, 15, 11, 13, 14, 5, 8, 10, 9, 12, 14, 13, 12]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a Bubble Chart with Seaborn
plt.figure(figsize=(14, 8)) # Modified width and height
bubble = sns.scatterplot(data=df, x="Department", y="Course", size="HoursStudy", 
                         legend=False, sizes=(100, 1000), 
                         hue="AverageScore", palette=["#FF9999", "#66B2FF", "#99FF99", "#FFFF66", "#FF66FF"])

# Customizing the axes and title (with changed topic and headline)
plt.title("College Course Average Scores and Study Hours", fontsize=20)
plt.xlabel("Department", fontsize=15)
plt.ylabel("Course", fontsize=15)

plt.show()