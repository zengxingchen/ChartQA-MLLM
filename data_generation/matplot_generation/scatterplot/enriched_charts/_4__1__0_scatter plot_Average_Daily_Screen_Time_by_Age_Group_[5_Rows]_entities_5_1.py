
import matplotlib.pyplot as plt

days = list(range(1, 32))
calories_burned = [
    230, 250, 220, 300, 320, 310, 275, 290, 310, 400, 
    375, 380, 330, 360, 370, 360, 320, 310, 315, 380, 
    390, 410, 420, 430, 400, 380, 370, 360, 370, 380, 390
]

colors = [
    '#4A90E2', '#50E3C2', '#9013FE', '#F5A623', '#F8E71C',
    '#8B572A', '#B8E986', '#417505', '#D0021B', '#F68D2E',
    '#BD10E0', '#9B9B9B', '#7ED321', '#D00131', '#901A65',
    '#F790AB', '#8D80E1', '#5ABAFC', '#80234A', '#BFA123',
    '#29CFEC', '#5B9274', '#E3787D', '#2EC4B6', '#FF6F61',
    '#FC974F', '#6D83F3', '#13C8AD', '#C772B0', '#33ACFF',
    '#876F8B'
]

plt.figure(figsize=(15, 8))

plt.scatter(days, calories_burned, c=colors)

plt.title('Daily Calories Burned in January 2024', pad=25)
plt.xlabel('Day')
plt.ylabel('Calories Burned')
plt.xticks(days)

plt.show()