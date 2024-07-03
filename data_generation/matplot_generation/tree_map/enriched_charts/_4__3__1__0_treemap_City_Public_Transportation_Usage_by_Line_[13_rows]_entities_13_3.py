
import matplotlib.pyplot as plt
import squarify

labels = [
    'Reading Fiction', 'Writing Essays', 'Poetry', 'Drama', 
    'Screenwriting', 'Short Stories', 'Non-Fiction', 'Fantasy', 
    'Science Fiction', 'Mystery', 'Biography', 'Memoir', 
    'Playwriting', 'Journalism', 'Editing', 'Literary Criticism'
]
sizes = [20, 15, 12, 18, 10, 17, 8, 9, 14, 7, 6, 11, 5, 13, 4, 3]
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 
    '#ffb3e6', '#c4e17f', '#76d7c4', '#c6a8d6', '#f7b7a3', 
    '#ff7f50', '#87ceeb', '#32cd32', '#ffa07a', '#8a2be2', 
    '#d2691e'
]

plt.figure(figsize=(16, 14))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

plt.title('Distribution of Time Spent on Various Literary Activities', fontsize=22, pad=20)
plt.axis('off')

plt.show()