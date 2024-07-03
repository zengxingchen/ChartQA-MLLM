
import matplotlib.pyplot as plt

# Subject scores data
subjects = [
    "Mathematics", "Physics", "Chemistry", "Biology", "History", 
    "Geography", "English", "Spanish", "Computer Science", "Physical Education", 
    "Art", "Music", "Economics", "Psychology", "Philosophy", 
    "Sociology", "Political Science", "Business Studies", "Environmental Science", 
    "Literature", "Statistics", "Astronomy", "Geology", "Anthropology", 
    "Engineering", "Medicine", "Law", "Nursing", "Education", 
    "Architecture", "Journalism", "Public Health", "Social Work"
]
scores = [
    88, 92, 85, 90, 82, 
    87, 91, 78, 95, 80, 
    89, 84, 86, 88, 90, 
    81, 83, 89, 85, 92, 
    93, 94, 84, 87, 91, 
    90, 88, 85, 86, 92, 
    87, 89, 88
]

# New color scheme using specific color codes for each subject
colors = [
    '#ff6347', '#4682b4', '#32cd32', '#ffd700', '#dda0dd', 
    '#6a5acd', '#ff4500', '#2e8b57', '#1e90ff', '#8a2be2', 
    '#dc143c', '#00ced1', '#ff8c00', '#7b68ee', '#ff00ff', 
    '#3cb371', '#0000cd', '#adff2f', '#7fff00', '#ff1493', 
    '#ff69b4', '#ba55d3', '#9370db', '#87ceeb', '#dda0dd', 
    '#db7093', '#6495ed', '#b0e0e6', '#5f9ea0', '#ff6347', 
    '#4682b4', '#32cd32', '#ffd700'
]

# Create vertical bar chart
plt.figure(figsize=(18, 8))  # Width and height of the chart
plt.bar(subjects, scores, color=colors, width=0.6)  # Bar color and bar width

# Set the title and labels
plt.title('Scores of Students in Different Subjects', fontsize=18, pad=20)
plt.ylabel('Score', fontsize=16)
plt.xlabel('Subject', fontsize=16)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Display the bar chart
plt.show()