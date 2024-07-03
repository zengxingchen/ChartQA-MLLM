
import matplotlib.pyplot as plt

# Data to plot
topics = [
    'Philosophy', 'Ethics', 'Logic', 'Metaphysics', 'Epistemology', 
    'Aesthetics', 'Political Philosophy', 'Philosophy of Science', 
    'Ethics in AI', 'Ancient Philosophy'
]
amounts = [50000, 38000, 30000, 21000, 27000, 19000, 24000, 23000, 28000, 26000]

# Define colors for each topic
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF9E33', 
    '#33FFD7', '#FF3333', '#57FF33', '#33A8FF', '#F333FF'
]

# Creating the pie chart
plt.figure(figsize=(14,12))
plt.pie(amounts, labels=topics, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Philosophy & Ethics Revenue Distribution', pad=20)

plt.show()