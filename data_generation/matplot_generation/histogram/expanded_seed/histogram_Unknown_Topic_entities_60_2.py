
import matplotlib.pyplot as plt

# Provided data
data = [
    {'User': 'User 1', 'Daily Steps': 7523},
    {'User': 'User 2', 'Daily Steps': 11120},
    {'User': 'User 3', 'Daily Steps': 9456},
    {'User': 'User 4', 'Daily Steps': 7210},
    {'User': 'User 5', 'Daily Steps': 6882},
    {'User': 'User 6', 'Daily Steps': 15432},
    {'User': 'User 7', 'Daily Steps': 3109},
    {'User': 'User 8', 'Daily Steps': 14250},
    {'User': 'User 9', 'Daily Steps': 4780},
    {'User': 'User 10', 'Daily Steps': 10222},
    {'User': 'User 11', 'Daily Steps': 6599},
    {'User': 'User 12', 'Daily Steps': 8733},
    {'User': 'User 13', 'Daily Steps': 11869},
    {'User': 'User 14', 'Daily Steps': 12422},
    {'User': 'User 15', 'Daily Steps': 5124}
]

# Extracting the "Daily Steps" values for histogram plotting
steps = [user['Daily Steps'] for user in data]

# Creating the histogram
plt.figure(figsize=(10, 6))

# Customizing the histogram with colors and edge color
n, bins, patches = plt.hist(steps, bins=8, color='skyblue', edgecolor='black')

# Adding a grid for better readability
plt.grid(axis='y', alpha=0.75)

# Adding a title and labels
plt.title('Distribution of Daily Steps Among Users')
plt.xlabel('Daily Steps')
plt.ylabel('Number of Users')

# Annotating the histogram bars with the number of users in each bin
for i in range(len(patches)):
    plt.text(patches[i].xy[0] + patches[i]._width / 2, 
             patches[i]._height + 0.1, 
             str(int(patches[i]._height)), 
             ha='center')

# Show mean line
mean_steps = sum(steps) / len(steps)
plt.axvline(mean_steps, color='r', linestyle='dashed', linewidth=2)
plt.text(mean_steps + 200, plt.ylim()[1] * 0.75, 'Mean: {:.2f}'.format(mean_steps), color='r')

# Increase x, y axis limits if needed
plt.xlim(0, max(steps) + 5000)
plt.ylim(0, max(n)+1)

# Display the histogram
plt.show()