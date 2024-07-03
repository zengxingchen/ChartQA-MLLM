
import matplotlib.pyplot as plt
import squarify

# Data
book_title = [
    'Harry Potter and the Philosopher\'s Stone', 'The Hobbit', 'And Then There Were None', 'The Da Vinci Code',
    'The Catcher in the Rye', 'The Alchemist', 'To Kill a Mockingbird', 'The Great Gatsby', 
    'The Lord of the Rings', 'Fifty Shades of Grey', 'Lolita', 'The Chronicles of Narnia', 
    'Catcher in the Rye', 'The Da Vinci Code', 'The Kite Runner', 'One Hundred Years of Solitude', 
    'Twilight', 'Pride and Prejudice', 'Wuthering Heights'
]
copies_sold = [
    120, 100, 100, 80, 65, 65, 60, 55, 150, 100, 60, 85, 65, 80, 55, 47, 120, 20, 30
]
color_code = [
    '#FF9FAB', '#FFD700', '#FF851B', '#00AFFF', '#B10DC9', '#2ECC40', '#FF851B', '#FFDC00',
    '#85144b', '#0074D9', '#001f3f', '#39CCCC', '#FF4136', '#3D9970', '#2ECC40', '#39CCCC',
    '#B10DC9', '#85144b', '#FF4136'
]

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=copies_sold, label=book_title, color=color_code, alpha=0.7)
plt.title('Best-Selling Fiction Books of All Time', fontsize=20, pad=30)
plt.axis('off')
plt.show()