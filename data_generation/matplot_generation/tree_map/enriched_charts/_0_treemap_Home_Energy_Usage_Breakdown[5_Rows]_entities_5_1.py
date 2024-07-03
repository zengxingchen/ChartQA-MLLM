
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Language': ['JavaScript', 'Python', 'Java', 'C#', 'PHP', 'TypeScript', 
                 'C++', 'Ruby', 'Swift', 'Objective-C', 'Kotlin', 'Rust'],
    'Popularity': [29.91, 18.58, 16.05, 9.34, 6.21, 5.07, 
                   4.74, 2.76, 2.05, 1.69, 1.39, 1.21]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#63b2ee', '#76da91', '#f8cb7f', '#f89588', 
          '#7cd6cf', '#9192ab', '#7898e1', '#efa666', 
          '#eddd86', '#9987ce', '#65b2c9', '#d7ab82']

# Create the figure with specified figure size
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Popularity'], label=df['Language'], color=colors, alpha=0.6)

# Set the title of the plot
plt.title('Programming Language Popularity Treemap', fontsize=20)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()