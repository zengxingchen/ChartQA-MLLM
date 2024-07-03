
import matplotlib.pyplot as plt
import pandas as pd

# Generate data points
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Product A': [200, 220, 250, 275, 300, 310, 330, 340, 350, 370, 360, 390],
    'Product B': [120, 130, 140, 160, 175, 180, 190, 200, 210, 220, 210, 230],
    'Product C': [80, 90, 100, 110, 120, 130, 140, 160, 180, 200, 190, 220]
}

df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 6))

# Plotting the stacked area chart
plt.stackplot(df['Month'],
              df['Product A'], df['Product B'], df['Product C'],
              labels=['Product A', 'Product B', 'Product C'],
              colors=['#FF6F61', '#6B5B95', '#88B04B'])

# Add title and labels
plt.title('Monthly Sales Data of Products A, B, and C')
plt.xlabel('Month')
plt.ylabel('Sales (in units)')

# Add legend
plt.legend(loc='upper left')

# Annotate specific data points
for i, (mon, a, b, c) in enumerate(zip(df['Month'], df['Product A'], df['Product B'], df['Product C'])):
    if mon == 'December':
        plt.text(i, a+b+c, f'{a+b+c}', ha='center', va='bottom')

# Show the plot
plt.show()