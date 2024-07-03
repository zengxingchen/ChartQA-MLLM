
import matplotlib.pyplot as plt

# Subject scores data
subjects = [
    "Math", "Science", "English", "History", "Art", 
    "Physical Education", "Music", "Computer Science", 
    "Economics", "Psychology", "Sociology", "Biology"
]
scores = [85, 90, 78, 82, 88, 92, 87, 91, 80, 84, 86, 89]

# New color scheme using specific color codes for each subject
colors = [
    '#4b0082', '#ff4500', '#2e8b57', '#ff6347', '#4682b4',
    '#d2691e', '#ff69b4', '#778899', '#b0c4de', '#dda0dd',
    '#8a2be2', '#3cb371'
]

# Create vertical bar chart
plt.figure(figsize=(12, 6))  # Width and height of the chart
plt.bar(subjects, scores, color=colors, width=0.5)  # Bar color and band width

# Set the title and labels
plt.title('Student Scores by Subject', fontsize=16, pad=20)
plt.xlabel('Subject', fontsize=14)
plt.ylabel('Score', fontsize=14)

# Display the bar chart
plt.show()