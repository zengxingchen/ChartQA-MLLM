
import matplotlib.pyplot as plt

data = {
    'Category': ['Mystery', 'Science Fiction', 'Fantasy', 'Thriller', 'Romance', 
                 'Drama', 'Comedy', 'Action', 'Adventure', 'Horror', 
                 'Documentary', 'Biography', 'Animated', 'Musical', 
                 'Western', 'Historical'],
    'Rating': [8.1, 7.5, 9.2, 8.8, 6.5, 7.8, 8.3, 7.0, 8.6, 6.8, 9.0, 7.7, 8.9, 7.4, 6.9, 8.4],
    'Popularity (Millions)': [220, 185, 300, 240, 150, 190, 210, 170, 260, 140, 280, 160, 230, 175, 130, 195],
    'User Engagement (1-10)': [9.2, 8.8, 9.5, 8.9, 7.4, 8.3, 8.7, 7.9, 9.0, 7.1, 9.6, 8.2, 9.3, 8.4, 7.0, 8.6]
}

fig, ax = plt.subplots(figsize=(16, 10))

for i in range(len(data['Category'])):
    ax.scatter(data['Rating'][i], data['Popularity (Millions)'][i], 
               s=(data['User Engagement (1-10)'][i] ** 3) * 10, 
               alpha=0.6,
               color=['#FF6347', '#4682B4', '#8A2BE2', '#3CB371', '#FF4500', 
                      '#6A5ACD', '#FFD700', '#D2691E', '#FF1493', '#7FFF00', 
                      '#DDA0DD', '#8B4513', '#20B2AA', '#FF69B4', '#CD853F', 
                      '#4169E1'][i])

ax.set_title('Popular Book Categories: Rating vs Popularity with User Engagement as Bubble Size', fontsize=18, pad=25)
ax.set_xlabel('Rating', fontsize=14)
ax.set_ylabel('Popularity (Millions)', fontsize=14)
ax.grid(True)

plt.show()