
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
page_views = [350, 345, 360, 355, 340, 365, 370, 360, 355, 380, 
              390, 385, 395, 370, 360, 375, 380, 385, 390, 370, 
              360, 365, 375, 380, 390, 395, 400, 385, 380, 370]

plt.figure(figsize=(12, 6))  # Changing width and height of the chart
plt.plot(days, page_views, marker='o', color='#1ABC9C', linewidth=2)  # Modified color scheme

# Adding annotations for the highest and lowest page views
plt.annotate('Lowest Page Views', xy=(5, 340), xytext=(6, 320),
             arrowprops=dict(facecolor='#E74C3C', shrink=0.05))
plt.annotate('Highest Page Views', xy=(27, 400), xytext=(26, 410),
             arrowprops=dict(facecolor='#F39C12', shrink=0.05))

plt.title('Daily Page Views in June', pad=20)  # New headline which fits the topic
plt.xlabel('Day')  # Changing labels to fit the new data type
plt.ylabel('Page Views')
plt.grid(True)

plt.show()