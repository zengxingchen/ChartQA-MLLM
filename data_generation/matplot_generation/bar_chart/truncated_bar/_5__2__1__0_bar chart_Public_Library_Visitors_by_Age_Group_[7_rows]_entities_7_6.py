
import matplotlib.pyplot as plt

# Data
genres = [
    "Education", "Health", "Psychology", "Culture", "Society",
    "Technology", "Politics", "Finance", "Art", "Design", 
    "Science", "Nature", "Entertainment", "Leisure", 
    "Astronomy", "Space", "Fashion", "Beauty", "Travel", 
    "Adventure", "Sports", "Fitness", "Music", 
    "Performing Arts", "History", "Archaeology", "Food", 
    "Nutrition", "Philosophy", "Ethics", "Literature", 
    "Writing", "Environment", "Climate", "Business", "Entrepreneurship"
]
participants = [
    85, 95, 90, 100, 80, 110, 75, 120, 130, 125, 105, 115, 
    140, 135, 145, 150, 125, 115, 160, 155, 170, 165, 175, 
    180, 190, 185, 195, 200, 210, 205, 220, 215, 230, 225, 
    240, 235
]

# Creating vertical bar chart
fig, ax = plt.subplots(figsize=(14, 10))

ax.bar(genres, participants, color=[
    '#0073e6', '#00e673', '#e6007a', '#e67300', '#33e600', 
    '#00e6e6', '#e63300', '#7300e6', '#e6e600', '#0099e6', 
    '#e600e6', '#33e6e6', '#e6e633', '#e63333', '#33e6b3', 
    '#b3e633', '#3373e6', '#e60000', '#33e6e6', '#e63300', 
    '#33e633', '#e633e6', '#33b3e6', '#e600b3', '#33e600', 
    '#e60033', '#00e633', '#e6e600', '#00e6b3', '#e600e6', 
    '#e6b300', '#e60000', '#b3e633', '#33e6b3', '#e60000', 
    '#00e6e6'
], width=0.6)

# Set y-axis limit to start from 70
ax.set_ylim(70, 250)

# Adding labels and title
ax.set_ylabel('Participants (in thousands)')
ax.set_title('Participation in Various Activities in 2023', pad=20)

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.show()