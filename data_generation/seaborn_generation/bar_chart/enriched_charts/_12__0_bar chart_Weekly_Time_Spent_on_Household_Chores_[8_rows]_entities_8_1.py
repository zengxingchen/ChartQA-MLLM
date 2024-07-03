
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Book': ["To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "Moby-Dick",
             "War and Peace", "Ulysses", "The Catcher in the Rye", "Jane Eyre", "Wuthering Heights",
             "Brave New World", "The Odyssey", "Crime and Punishment", "Great Expectations",
             "Les Misérables", "The Brothers Karamazov", "One Hundred Years of Solitude",
             "Catch-22", "The Divine Comedy", "Anna Karenina"],
    'AverageRating': [4.27, 4.17, 4.25, 3.91, 3.49, 4.11, 3.75, 3.80, 4.12, 3.85, 3.98, 3.75, 4.20,
                      3.77, 4.20, 4.32, 4.07, 3.98, 4.11, 4.05]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 10))  # Width and height modification
sns.barplot(y="AverageRating", x="Book", data=df,
            palette=['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1',
                     '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC',
                     '#EFC050', '#5B5EA6', '#9B2335', '#DFCFBE', '#55B4B0',
                     '#E15D44', '#7FCDCD', '#BC243C', '#C3447A', '#98B4D4'],
            dodge=False)  # Color modification using specific color codes

# Set the bars' width
for bar in plt.gca().patches:
    bar.set_width(0.6)  # Width of bars when vertical (actually controls the width of vertical bars)

plt.ylabel('Average Rating')
plt.xlabel('Book')
plt.title('Average Ratings of Classic Literature Books', pad=20)
plt.xticks(rotation=90)
sns.despine(left=True, bottom=True)  # Cleaning up the plot
plt.show()