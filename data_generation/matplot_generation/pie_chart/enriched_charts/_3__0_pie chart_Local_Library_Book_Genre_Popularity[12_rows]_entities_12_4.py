
import matplotlib.pyplot as plt

# Data to plot
genres = [
    'Rock', 'Pop', 'Jazz', 'Classical', 'Hip Hop', 
    'Country', 'Electronic', 'Reggae', 'Blues', 'Latin'
]
revenue = [45000, 34000, 22000, 15000, 37000, 25000, 20000, 18000, 13000, 21000]

# Define colors for each genre
colors = [
    '#FF4500', '#FFD700', '#1E90FF', '#32CD32', '#8A2BE2',
    '#FF6347', '#40E0D0', '#DAA520', '#ADFF2F', '#FF69B4'
]

# Creating the pie chart
plt.figure(figsize=(12,10))
plt.pie(revenue, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Music Genre Revenue Distribution', pad=20)

plt.show()