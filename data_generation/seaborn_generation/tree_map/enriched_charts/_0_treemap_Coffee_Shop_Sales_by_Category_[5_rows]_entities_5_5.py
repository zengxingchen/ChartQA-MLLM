
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a DataFrame with the data
data = {
    'Language': ['JavaScript', 'Python', 'Java', 'C#', 'PHP', 'C++', 'TypeScript', 'Swift', 'Ruby', 'Kotlin', 'Go', 'Rust', 'Dart', 'Scala', 'Elixir'],
    'Usage': [265, 230, 200, 150, 150, 130, 115, 95, 75, 60, 55, 40, 30, 25, 20],
    'Paradigm': ['Event-driven', 'Object-Oriented', 'Object-Oriented', 'Object-Oriented', 'Scripting', 'Object-Oriented', 'Event-driven', 'Object-Oriented', 'Scripting', 'Functional',
                 'Concurrent', 'Concurrent', 'Event-driven', 'Functional', 'Functional']
}
df = pd.DataFrame(data)

# Plot parameters
plt.figure(figsize=(12, 8))
cmap = [ '#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
         '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
         '#809900', '#E6B3B3', '#6680B3', '#66991A', '#FF99E6']

# Create a treemap
squarify.plot(sizes=df['Usage'], label=df['Language'], color=cmap, alpha=0.8)

plt.title('Popular Programming Languages by Global Usage')
plt.axis('off')

plt.show()