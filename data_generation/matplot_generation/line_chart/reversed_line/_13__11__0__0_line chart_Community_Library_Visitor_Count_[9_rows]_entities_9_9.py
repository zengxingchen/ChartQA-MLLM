
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
number_of_tourists = [450, 470, 490, 510, 530, 550, 570, 590, 610, 630, 650, 670]

plt.figure(figsize=(18, 9))

plt.plot(months, number_of_tourists, marker='o', linestyle='-', color='#FF6347')  # Tomato color

for i, tourists in enumerate(number_of_tourists):
    plt.annotate(str(tourists), xy=(months[i], tourists), xytext=(5, -10), textcoords='offset points')

plt.title('Monthly Number of Tourists', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Tourists')

plt.gca().invert_yaxis()

plt.show()