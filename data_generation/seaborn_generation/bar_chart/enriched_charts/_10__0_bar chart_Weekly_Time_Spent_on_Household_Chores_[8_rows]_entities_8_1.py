
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Genre': ['Pop', 'Rock', 'Hip-Hop', 'Classical', 'Jazz', 'Country', 'Electronic', 'R&B', 'Reggae', 
              'Blues', 'Metal', 'Folk', 'Latin', 'K-Pop', 'Gospel', 'Soul', 'Punk', 'Disco', 'Funk', 'Techno'],
    'Number_of_Albums': [200, 150, 120, 80, 60, 90, 110, 70, 40, 50, 65, 55, 45, 35, 25, 30, 20, 15, 10, 5]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 10))  # Width and height modification
sns.barplot(y="Number_of_Albums", x="Genre", data=df,
            palette=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4', '#f7dc6f',
                     '#6fa8dc', '#c9a0dc', '#E39191', '#a5a5a5', '#58D68D', '#D68910', '#52BE80', '#1F618D', '#2ECC71', '#E59866', '#5DADE2'],
            dodge=False)  # Color modification using specific color codes

# Set the bars' height
for bar in plt.gca().patches:
    bar.set_width(0.6)  # Width of bars when vertical

plt.ylabel('Number of Albums')
plt.xlabel('Genre')
plt.title('Number of Albums Released by Music Genre')
sns.despine(left=True, bottom=True)  # Cleaning up the plot
plt.show()