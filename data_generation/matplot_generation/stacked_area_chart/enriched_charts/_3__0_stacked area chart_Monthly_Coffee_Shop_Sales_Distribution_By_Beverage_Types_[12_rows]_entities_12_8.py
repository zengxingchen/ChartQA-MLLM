
import matplotlib.pyplot as plt
import pandas as pd

# Generate data points
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Individual A': [12000, 14000, 13000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000],
    'Individual B': [15000, 13000, 14000, 15000, 16000, 17000, 16000, 17000, 18000, 19000, 20000, 21000],
    'Individual C': [8000, 10000, 12000, 11000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]
}

df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(14, 8))

# Plotting the stacked area chart
plt.stackplot(df['Month'],
              df['Individual A'], df['Individual B'], df['Individual C'],
              labels=['Individual A', 'Individual B', 'Individual C'],
              colors=['#FF5733', '#33FF57', '#3357FF'])

# Add title and labels
plt.title('Monthly Steps Count of Three Individuals')
plt.xlabel('Month')
plt.ylabel('Steps Count')

# Add legend
plt.legend(loc='upper left')

# Annotate specific data points
for i, (mon, a, b, c) in enumerate(zip(df['Month'], df['Individual A'], df['Individual B'], df['Individual C'])):
    if mon == 'December':
        plt.text(i, a+b+c, f'{a+b+c}', ha='center', va='bottom')

# Show the plot
plt.show()