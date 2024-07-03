
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
pollution_index = [80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58]

plt.figure(figsize=(16, 8))

plt.plot(months, pollution_index, marker='o', linestyle='-', color='#1E90FF')  # DodgerBlue color

for i, index in enumerate(pollution_index):
    plt.annotate(str(index), xy=(months[i], index), xytext=(5, 5), textcoords='offset points')

plt.gca().invert_yaxis()
plt.title('Monthly Pollution Index', pad=20)
plt.xlabel('Month')
plt.ylabel('Pollution Index')

plt.show()