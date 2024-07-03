
import matplotlib.pyplot as plt

data = {
    'Topic': ['Poetry', 'Short Stories', 'Novel Writing', 'Screenwriting', 'Essay Writing', 
              'Memoir', 'Journalism', 'Research Papers', 'Blogs', 'Technical Writing', 
              'Playwriting', 'Creative Nonfiction', 'Songwriting', 'Travel Writing', 
              'Biographies', 'Speechwriting', 'Reviews', 'Letters', 'Scripts', 'Comics'],
    'Pages Written': [50, 80, 120, 90, 70, 60, 100, 150, 40, 110, 65, 95, 30, 85, 75, 55, 45, 20, 70, 35],
    'Time Spent (hours)': [5, 8, 12, 10, 7, 6, 9, 14, 4, 11, 7, 9, 3, 8, 7, 5, 4, 2, 6, 3],
    'Enjoyment Level (1-10)': [9, 8.5, 9.5, 8, 7.5, 8.2, 7.8, 8.4, 7.9, 8.1, 8.7, 8.9, 9.3, 8.6, 8.2, 8.4, 7.9, 7.3, 8.3, 7.7]
}

fig, ax = plt.subplots(figsize=(16, 12))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#FF5733', 
          '#FFB533', '#5733FF', '#A1FF33', '#A133FF', '#FF33A1', '#33FFA1', 
          '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#FF5733', 
          '#FFB533', '#5733FF']

for i in range(len(data['Topic'])):
    ax.scatter(data['Pages Written'][i], data['Time Spent (hours)'][i], 
               s=(data['Enjoyment Level (1-10)'][i] ** 3) * 10,  
               alpha=0.6,
               color=colors[i]) 

ax.set_title('Literature & Writing: Pages Written vs Time Spent with Enjoyment Level as Bubble Size', fontsize=18)
ax.set_xlabel('Pages Written', fontsize=14)
ax.set_ylabel('Time Spent (hours)', fontsize=14)
ax.grid(True)

plt.show()