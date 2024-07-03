
import matplotlib.pyplot as plt
import squarify

# Data
books = ['The Great Gatsby', 'Moby Dick', 'War and Peace', 'Ulysses', 'To Kill a Mockingbird', '1984', 'The Catcher in the Rye', 'Pride and Prejudice', 'Lord of the Flies', 'The Odyssey', 'Crime and Punishment', 'The Brothers Karamazov', 'Brave New World', 'Wuthering Heights', 'Jane Eyre', 'Anna Karenina', 'The Divine Comedy', 'Hamlet', 'Othello', 'King Lear']
pages = [218, 635, 1225, 730, 281, 328, 277, 432, 182, 543, 671, 824, 268, 416, 507, 964, 798, 242, 213, 210]

# Colors
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#7FFF00', '#FF4500', '#6495ED', '#FF69B4', '#1E90FF', '#DC143C', '#00CED1', '#FF1493', '#7B68EE', '#D2691E', '#00FA9A', '#9400D3', '#FFB6C1', '#9370DB', '#48D1CC', '#ADFF2F', '#FF7F50']

plt.figure(figsize=(15, 12))

# Treemap
squarify.plot(sizes=pages, label=books, color=colors, alpha=0.85)

plt.title('Page Distribution of Classic Literature', fontsize=24, pad=20)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()