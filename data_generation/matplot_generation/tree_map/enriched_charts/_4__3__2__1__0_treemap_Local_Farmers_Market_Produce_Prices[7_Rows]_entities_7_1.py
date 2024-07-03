
import matplotlib.pyplot as plt
import squarify

topics = ['Governance', 'Fashion', 'Art', 'Climate Change', 'Music', 'History', 
          'Space Exploration', 'Culture', 'Literature', 'Business', 'Travel', 
          'Science', 'Psychology', 'Sports', 'Entertainment', 'Education']
values = [10.5, 14.2, 13.9, 11.8, 9.6, 8.7, 12.4, 15.1, 7.3, 6.9, 5.1, 3.8, 2.7, 1.9, 0.8, 0.4]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff6347', '#2ca02c', 
          '#ff7f0e', '#d62728', '#8c564b', '#bcbd22']

plt.figure(figsize=(16, 12))
squarify.plot(sizes=values, label=topics, color=colors, alpha=0.8)

plt.title('Popularity of Various Topics in 2023', fontsize=18, pad=20)
plt.axis('off')

plt.show()