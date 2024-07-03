
import matplotlib.pyplot as plt

categories = ['Pop', 'Rock', 'Jazz', 'Classical', 'Hip-Hop', 'Country', 'Reggae', 'Blues']
values = [180, 140, 70, 90, 110, 85, 60, 95]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6347', '#ADFF2F', '#9370DB']

plt.figure(figsize=(10, 7))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.title('Popular Music Genres in 2023', pad=40)
plt.show()