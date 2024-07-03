
import matplotlib.pyplot as plt

# Table data represented as lists
books = ['Harry Potter', 'The Hobbit', 'Pride and Prejudice', 'To Kill a Mockingbird', 'The Great Gatsby',
         'Moby Dick', 'War and Peace', '1984', 'Ulysses', 'The Catcher in the Rye', 'The Odyssey', 'Jane Eyre']
sales = [120, 95, 80, 130, 105, 75, 65, 140, 55, 115, 85, 90]

# Custom color codes for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', 
          '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33',
          '#FF8C33', '#A6FF33']

# Setting the size of the plot
plt.figure(figsize=(12, 6))

# Creating a vertical bar chart
plt.bar(books, sales, color=colors, width=0.4)

# Customizing the plot
plt.ylabel('Sales (thousands)')
plt.title('Book Sales')
plt.ylim(0, max(sales) + 20)  # Adjusting y-axis limits for better clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adding a grid for the y-axis

# Display the plot
plt.xticks(rotation=45, ha='right')  # Rotating x-axis labels for better readability

# Display the plot
plt.show()