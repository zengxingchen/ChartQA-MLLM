
import matplotlib.pyplot as plt

# Data
activities = ["Lectures", "Self-study", "Group Study", "Online Courses", "Assignments", 
              "Projects", "Exams Preparation", "Extracurricular", "Others"]
time_spent = [30, 25, 15, 10, 8, 5, 4, 3, 2]

# Colors
colors = [
    "#1f77b4",  # Lectures
    "#ff7f0e",  # Self-study
    "#2ca02c",  # Group Study
    "#d62728",  # Online Courses
    "#9467bd",  # Assignments
    "#8c564b",  # Projects
    "#e377c2",  # Exams Preparation
    "#7f7f7f",  # Extracurricular
    "#bcbd22"   # Others
]

# Create pie chart
plt.figure(figsize=(10, 6))  # width and height in inches
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=90)

# Chart title
plt.title('Distribution of Time Spent on Different Study Activities During a Week', pad=30)

# Show plot
plt.show()