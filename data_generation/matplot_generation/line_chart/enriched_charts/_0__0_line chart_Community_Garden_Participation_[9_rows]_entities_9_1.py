
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
steps = [3456, 5678, 2345, 7890, 6543, 3452, 8765, 4321, 9100, 12123, 
         7654, 8760, 10987, 5674, 7890, 2345, 6543, 9876, 3456, 6789, 
         1234, 8901, 4567, 7654, 9876, 3456, 7890, 5432, 6789, 4321]

plt.figure(figsize=(14, 7))  # Changing width and height of the chart
plt.plot(days, steps, marker='o', color='#4CAF50', linewidth=2)  # Modified color scheme

# Adding annotations for the highest and lowest steps
plt.annotate('Lowest Steps', xy=(20, 1234), xytext=(21, 2000),
             arrowprops=dict(facecolor='#E74C3C', shrink=0.05))
plt.annotate('Highest Steps', xy=(10, 12123), xytext=(9, 13000),
             arrowprops=dict(facecolor='#2980B9', shrink=0.05))

plt.title('Daily Step Count in June', pad=20)  # New headline which fits the topic
plt.xlabel('Day')  # Changing labels to fit the new data type
plt.ylabel('Number of Steps')
plt.grid(True)

plt.show()