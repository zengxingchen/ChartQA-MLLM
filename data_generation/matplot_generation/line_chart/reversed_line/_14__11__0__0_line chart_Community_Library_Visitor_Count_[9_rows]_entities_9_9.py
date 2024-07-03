
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
steps = [12000, 13000, 12500, 14000, 15000, 14500, 16000, 15500, 17000, 16500, 18000, 17500]

plt.figure(figsize=(12, 6))

plt.plot(months, steps, marker='o', linestyle='-', color='#FF6347')  # Tomato color

for i, step in enumerate(steps):
    plt.annotate(str(step), xy=(months[i], step), xytext=(5, -10), textcoords='offset points')

plt.gca().invert_yaxis()
plt.title('Monthly Step Count', pad=20)
plt.xlabel('Month')
plt.ylabel('Steps')

plt.show()