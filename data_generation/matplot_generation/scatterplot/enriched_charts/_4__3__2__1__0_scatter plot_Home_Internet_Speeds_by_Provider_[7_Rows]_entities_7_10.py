
import matplotlib.pyplot as plt

country = ["USA", "Canada", "Germany", "UK", "France", "Japan", "Australia", "South Korea", "China", "India",
           "Brazil", "South Africa", "Russia", "Mexico", "Italy", "Spain", "Netherlands", "Sweden", "Switzerland",
           "Austria", "Norway", "Denmark", "Finland", "Ireland", "Belgium", "Singapore", "New Zealand", "Argentina",
           "Chile", "Colombia"]
revenue = [85000, 79000, 77000, 82000, 78000, 83000, 80000, 75000, 72000, 65000, 70000, 68000, 74000, 67000, 73000,
           71000, 76000, 79000, 88000, 74000, 82000, 80000, 75000, 78000, 76000, 85000, 74000, 69000, 72000, 66000]
marketing_expenditure = [18000, 16500, 17000, 17500, 16000, 19000, 18500, 15000, 14000, 11000, 13000, 12000, 15500, 12500,
                         14500, 13500, 16000, 17000, 19500, 15500, 18000, 17500, 15000, 16500, 16000, 20000, 15500, 12500,
                         14000, 11500]
colors = ['#1E90FF', '#FF4500', '#32CD32', '#FFD700', '#8A2BE2', '#DC143C', '#00CED1', '#FF1493', '#7FFF00', '#FF69B4',
          '#B22222', '#6A5ACD', '#FF8C00', '#7CFC00', '#D2691E', '#6495ED', '#DB7093', '#00BFFF', '#FFDAB9', '#98FB98',
          '#FF00FF', '#BA55D3', '#CD5C5C', '#20B2AA', '#87CEEB', '#00FA9A', '#9370DB', '#3CB371', '#FF6347', '#4682B4']

plt.figure(figsize=(24, 18))

for i in range(len(country)):
    plt.scatter(revenue[i], marketing_expenditure[i], color=colors[i], label=country[i])

plt.title('Company Revenue vs Marketing Expenditure in Various Countries', pad=40)
plt.xlabel('Revenue (USD Million)')
plt.ylabel('Marketing Expenditure (USD Million)')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

plt.show()