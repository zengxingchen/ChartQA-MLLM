import matplotlib.pyplot as plt

country = ["USA", "Canada", "Mexico", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Brazil", "Argentina", "China", "Japan", "South Korea", "India", "Russia", "South Africa", "Egypt", "Saudi Arabia", "Nigeria"]
obesity_rate = [36, 29, 28, 27, 25, 24, 21, 23, 30, 22, 26, 16, 4, 5, 20, 24, 28, 31, 35, 14]
exercise_frequency = [45, 50, 30, 55, 60, 65, 70, 62, 48, 35, 33, 75, 82, 80, 25, 38, 40, 20, 15, 12]
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', '#AEC7E8', '#FFBB78', '#98DF8A', '#FF9896', '#C5B0D5', '#C49C94', '#F7B6D2', '#C7C7C7', '#DBDB8D', '#9EDAE5']

plt.figure(figsize=(14, 8))

for i in range(len(country)):
    plt.scatter(obesity_rate[i], exercise_frequency[i], color=colors[i], label=country[i])

plt.title('Obesity Rate vs Exercise Frequency in Various Countries', pad=20)
plt.xlabel('Obesity Rate (%)')
plt.ylabel('Exercise Frequency (%)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()