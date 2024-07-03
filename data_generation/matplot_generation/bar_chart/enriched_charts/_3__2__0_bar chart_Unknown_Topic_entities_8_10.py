
import matplotlib.pyplot as plt

# Data
topics = [
    'Ethics', 'Sustainability', 'Technology', 'Innovation', 'AI Ethics', 
    'Fashion Trends', 'Luxury Brands', 'Personal Finance', 'Investing', 
    'Market Analysis', 'Classical Literature', 'Modern Fiction', 
    'Ancient History', 'Archaeological Discoveries', 'Fitness Regimes', 
    'Nutritional Science', 'Future Tech', 'Digital Society', 
    'Space Exploration', 'Travel Destinations', 'Wildlife Conservation', 
    'Climate Change', 'Mental Health', 'Cultural Studies'
]
interest_level = [
    55, 65, 90, 75, 85, 70, 60, 80, 95, 75, 50, 65, 85, 70, 80, 90, 
    100, 85, 95, 70, 80, 90, 85, 75
]

# Plotting the bar chart
plt.figure(figsize=(10, 14))
plt.barh(topics, interest_level, height=0.5, color=[
    '#ff5733', '#33ff57', '#3357ff', '#ff33a6', '#a633ff', '#ffb833', 
    '#33fff6', '#ff3333', '#33ff33', '#3333ff', '#ffa833', '#33a6ff', 
    '#a633a6', '#33ffa8', '#a6a633', '#ffa633', '#33a6a6', '#a6ff33', 
    '#ff33ff', '#33a8ff', '#a8a633', '#ff3377', '#77ff33', '#3377ff'
])

# Customizing the plot
plt.xlabel('Interest Level')
plt.title('Interest Levels in Various Topics')
plt.xlim(0, 110)

# Show the plot
plt.show()