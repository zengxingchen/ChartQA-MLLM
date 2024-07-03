import matplotlib.pyplot as plt

categories = ['Travel', 'Adventure', 'Governance', 'Politics', 'Health', 'Psychology',
              'Design', 'Art', 'Future Technologies', 'Society', 'Science', 
              'Nature', 'Fitness', 'Sports', 'Fashion', 'Beauty', 
              'Literature', 'Writing', 'Business', 'Entrepreneurship']
counts = [75, 120, 40, 90, 110, 95, 130, 85, 150, 60, 105, 115, 140, 130, 80, 
          70, 125, 135, 55, 45]

colors = [
    '#800080', '#FF1493', '#8A2BE2', '#4B0082', '#FF6347',
    '#4169E1', '#4682B4', '#7FFFD4', '#20B2AA', '#FF4500',
    '#228B22', '#2E8B57', '#ADFF2F', '#3CB371', '#6A5ACD',
    '#7B68EE', '#00FF7F', '#32CD32', '#FF69B4', '#00BFFF',
]

plt.figure(figsize=(16, 10))

plt.scatter(categories, counts, c=colors, s=100)

plt.title('Interest in Lifestyle Topics for 2024', pad=30)
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')

plt.show()