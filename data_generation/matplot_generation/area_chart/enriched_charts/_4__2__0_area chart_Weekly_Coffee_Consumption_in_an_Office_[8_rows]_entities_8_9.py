
import matplotlib.pyplot as plt

days = list(range(1, 31))
number_of_new_users = [
    5, 7, 10, 12, 15, 18, 21, 19, 23, 25, 22, 28, 30, 32, 35, 37, 40, 38, 42, 45,
    43, 47, 50, 53, 55, 58, 60, 62, 65, 68
]

plt.figure(figsize=(16, 9))
plt.fill_between(days, number_of_new_users, color="#3498DB")

plt.title("User Growth Over a Month in June")
plt.xlabel("Day of the Month")
plt.ylabel("Number of New Users")
plt.xticks(range(1, 31, 2))
plt.yticks(range(0, 71, 5))

plt.text(20, 50, "Significant growth period", fontsize=12, color='green')

plt.show()