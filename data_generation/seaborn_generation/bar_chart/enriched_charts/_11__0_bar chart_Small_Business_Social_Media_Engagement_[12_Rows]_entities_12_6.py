
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate the data
data = {
    'Author': ["J.K. Rowling", "George R.R. Martin", "Agatha Christie", "William Shakespeare", 
               "Stephen King", "Isaac Asimov", "J.R.R. Tolkien", "Jane Austen", "Mark Twain", 
               "Ernest Hemingway", "Charles Dickens", "Leo Tolstoy", "F. Scott Fitzgerald", 
               "Virginia Woolf", "Harper Lee", "Gabriel Garcia Marquez"],
    'Books_Published': [7, 5, 66, 39, 63, 40, 13, 6, 28, 9, 15, 12, 5, 9, 1, 7]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the bar chart
plt.figure(figsize=(10, 12))  # Change width and height of the chart
ax = sns.barplot(y='Author', x='Books_Published', data=df, palette=['#003f5c', '#58508d', '#bc5090', 
                                                                      '#ff6361', '#ffa600', '#a05195',
                                                                      '#f95d6a', '#d45087', '#2f4b7c',
                                                                      '#665191', '#a05195', '#f95d6a',
                                                                      '#ff7c43', '#ffa600', '#003f5c',
                                                                      '#488f31'],
                 dodge=False)

# Modify the width of bars
for bar in ax.patches:
    bar.set_height(0.6)

# Set the title
ax.set_title('Number of Books Published by Authors', fontsize=16)

# Show the plot
plt.show()