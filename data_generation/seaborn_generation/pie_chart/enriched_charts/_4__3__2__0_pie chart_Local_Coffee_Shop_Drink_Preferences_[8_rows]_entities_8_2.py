
import matplotlib.pyplot as plt

labels = 'Streaming', 'Gaming', 'Social Media', 'Reading', 'Fitness', 'Cooking', 'Traveling', 'Photography'
sizes = [120, 90, 80, 70, 60, 50, 40, 30]
colors = ['#FF5733', '#33FFBD', '#3380FF', '#FFC300', '#FF33A8', '#A833FF', '#33FF57', '#FF3380']

plt.figure(figsize=(12, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Leisure Activities Among Adults', pad=20)
plt.axis('equal')
plt.show()