
import matplotlib.pyplot as plt

# Data
topic = ['Art & Design', 'Music & Performing Arts', 'Health & Psychology', 
         'Food & Nutrition', 'Education & Learning', 'Business & Entrepreneurship', 
         'Travel & Adventure', 'Sports & Fitness', 'Entertainment & Leisure']
average_interest_hours = [8.2, 7.9, 7.5, 7.3, 7.0, 6.8, 6.5, 6.3, 6.0]

# Create vertical bar chart
plt.figure(figsize=(12, 7))
colors = ['#ff7f50', '#6a5acd', '#ff6347', '#3cb371', '#ffa07a', '#20b2aa', '#ff69b4', '#dda0dd', '#ff1493']

plt.bar(topic, average_interest_hours, color=colors, width=0.6)

# Customizing the plot
plt.ylabel('Average Interest Hours per Week')
plt.title('Average Interest Hours per Week by Topic (2024)', pad=20)
plt.ylim(5.5, 8.5)  # Truncate y-axis to start from 5.5

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()