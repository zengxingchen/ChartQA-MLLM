
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Data
subjects = ['Mathematics', 'Science', 'History', 'Language Arts', 'Physical Education', 'Music', 'Art', 'Technology', 'Social Studies']
hours = [25, 20, 15, 18, 10, 8, 12, 14, 16]

# Color Scheme in HEX
colors = ['#FF6347', '#4682B4', '#9ACD32', '#FFD700', '#6A5ACD', '#FF69B4', '#8FBC8F', '#20B2AA', '#FFA07A']

# Creating a figure to accommodate a larger treemap
fig, ax = plt.subplots(1, figsize=(14, 8))

# Creating the treemap
squarify.plot(sizes=hours, label=subjects, color=colors, alpha=0.8, ax=ax)

# Title of the treemap
plt.title('Distribution of Study Hours Across Subjects', fontsize=16)

# Removing the axes for better aesthetics
plt.axis('off')

# Display the plot
plt.show()