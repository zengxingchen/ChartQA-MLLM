
import matplotlib.pyplot as plt

# Data
years = [
    2010, 2011, 2012, 2013, 2014, 
    2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023
]
books_published = [
    20, 25, 30, 35, 40, 
    45, 50, 55, 60, 65, 
    70, 75, 80, 85
]

# Plot configuration
plt.figure(figsize=(14, 8))
bars = plt.barh(years, books_published, height=0.5, color=[
    '#1E90FF', '#32CD32', '#FFD700', '#FF4500',
    '#6A5ACD', '#FF69B4', '#2E8B57', '#8A2BE2',
    '#A52A2A', '#7FFF00', '#FF6347', '#4682B4',
    '#00CED1', '#DAA520'
])

# Axes labels and title
plt.xlabel('Number of Books Published')
plt.ylabel('Year')
plt.title('Annual Book Publications (2010-2023)')

# Show the plot
plt.show()