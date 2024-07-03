
import matplotlib.pyplot as plt

# Data
topics = [
    'Philosophy & Ethics', 'Music & Performing Arts', 'Food & Nutrition', 'Politics & Governance',
    'Science & Nature', 'Culture & Society', 'Business & Entrepreneurship', 'Economics & Finance',
    'History & Archaeology', 'Fashion & Beauty', 'Future Technologies & Society', 'Literature & Writing',
    'Education & Learning', 'Environment & Climate Change', 'Health & Psychology', 'Entertainment & Leisure',
    'Art & Design', 'Travel & Adventure', 'Sports & Fitness', 'Astronomy & Space Exploration'
]
subscribers = [
    350, 300, 280, 260, 240, 220, 210, 200, 180, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60
]
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF5', '#FFBD33', '#8B33FF', '#33FF85', 
    '#FF3380', '#FFA533', '#3385FF', '#FF3333', '#85FF33', '#FF9933', '#33BBFF', '#FF3366', '#33CC99', 
    '#33B2FF', '#FFCC33'
]

# Create a pie chart
plt.figure(figsize=(14, 12))  # Adjusting the size of the pie chart
plt.pie(subscribers, labels=topics, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Podcast Subscribers by Topic', pad=20)

plt.show()