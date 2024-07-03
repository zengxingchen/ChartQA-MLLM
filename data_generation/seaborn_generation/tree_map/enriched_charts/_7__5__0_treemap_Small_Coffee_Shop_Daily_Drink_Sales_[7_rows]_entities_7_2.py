
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Subject': [
        'Biology', 'Chemistry', 'Physics', 'Mathematics', 'History',
        'Geography', 'English Literature', 'Computer Science', 'Economics',
        'Psychology', 'Philosophy', 'Sociology', 'Political Science', 
        'Anthropology', 'Statistics', 'Art History', 'Environmental Science', 'Linguistics'
    ],
    'Value': [
        100, 80, 120, 110, 90,
        70, 130, 95, 85, 75,
        65, 55, 105, 60, 115,
        50, 125, 100
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD',
    '#FF4500', '#7FFFD4', '#DA70D6', '#CD5C5C', '#FF69B4',
    '#8B4513', '#1E90FF', '#3CB371', '#FFA500', '#20B2AA',
    '#778899', '#BDB76B', '#8A2BE2'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(16, 12))

# Create a treemap
squarify.plot(sizes=df['Value'], label=df['Subject'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Impact Values of Various Academic Subjects', fontsize=24, y=1.05)

# Show the plot
plt.show()