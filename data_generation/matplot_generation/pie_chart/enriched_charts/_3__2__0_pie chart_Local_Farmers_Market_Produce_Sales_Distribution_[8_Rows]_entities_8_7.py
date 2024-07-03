
import matplotlib.pyplot as plt

# Data
activities = ["Lectures", "Self-study", "Group Study", "Online Courses", "Assignments", 
              "Projects", "Exams Preparation", "Extracurricular", "Others"]
time_spent = [28, 22, 12, 15, 10, 7, 5, 3, 8]

# Colors
colors = [
    "#4B0082",  # Lectures
    "#FF4500",  # Self-study
    "#32CD32",  # Group Study
    "#FFD700",  # Online Courses
    "#8A2BE2",  # Assignments
    "#A52A2A",  # Projects
    "#DC143C",  # Exams Preparation
    "#808080",  # Extracurricular
    "#DAA520"   # Others
]

# Create pie chart
plt.figure(figsize=(12, 7))  # width and height in inches
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=90)

# Chart title
plt.title('Distribution of Time Spent on Different Study Activities During a Week', pad=30)

# Show plot
plt.show()