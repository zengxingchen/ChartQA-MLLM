
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
philosophy_articles = [12, 15, 20, 25, 30, 35, 33, 28, 22, 18, 15, 10]

# Changes to data to enrich visualization (slightly more articles in March and fewer in October for example)
philosophy_articles[2] += 2  # March
philosophy_articles[9] -= 2  # October

# Modify color scheme with color codes, change figure size, change trend by inverting the y-axis
plt.figure(figsize=(12, 8))
plt.plot(months, philosophy_articles, color='#FF5733', marker='o')

# Adding labels with annotations
for i, (month, articles) in enumerate(zip(months, philosophy_articles)):
    plt.annotate(f'{articles} articles', (month, articles), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Published Articles in Philosophy & Ethics')
plt.xlabel('Month')
plt.ylabel('Number of Articles')
plt.gca().invert_yaxis()

# Display chart
plt.show()