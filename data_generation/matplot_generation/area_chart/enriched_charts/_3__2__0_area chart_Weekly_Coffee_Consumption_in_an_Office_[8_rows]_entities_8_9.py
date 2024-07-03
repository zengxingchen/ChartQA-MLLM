
import matplotlib.pyplot as plt

days = list(range(1, 31))
number_of_visitors = [
    150, 180, 210, 250, 240, 220, 260, 290, 310, 280, 300, 330, 340, 360,
    380, 400, 420, 450, 470, 440, 460, 490, 510, 530, 550, 580, 600, 620,
    650, 670
]

plt.figure(figsize=(16, 9))
plt.fill_between(days, number_of_visitors, color="#1E90FF")

plt.title("Daily Visitor Count in June", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Number of Visitors")
plt.xticks(range(1, 31, 2))
plt.yticks(range(100, 701, 50))

plt.text(15, 500, "Visitor peak period", fontsize=12, color='red')

plt.show()