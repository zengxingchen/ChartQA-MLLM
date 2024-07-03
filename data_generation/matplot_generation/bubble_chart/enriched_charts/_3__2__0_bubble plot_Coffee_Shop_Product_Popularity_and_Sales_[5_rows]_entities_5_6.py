
import matplotlib.pyplot as plt

countries = ['USA', 'Germany', 'UK', 'France', 'Japan', 'Canada', 'Australia', 'Switzerland', 'Netherlands', 
             'Sweden', 'Norway', 'Denmark', 'Finland', 'Ireland', 'Singapore', 'New Zealand', 'South Korea', 
             'Spain', 'Italy', 'Belgium', 'Austria', 'Portugal', 'Greece']
average_salary = [62000, 58000, 55000, 53000, 60000, 57000, 59000, 62000, 54000, 56000, 61000, 58000, 55000, 
                  60000, 63000, 55000, 52000, 49000, 50000, 54000, 57000, 47000, 46000]
employment_rate = [65.0, 74.5, 76.0, 70.3, 71.2, 73.1, 72.5, 78.0, 76.4, 74.2, 77.3, 75.1, 73.9, 74.8, 78.5, 
                   70.7, 66.2, 64.8, 60.5, 72.3, 71.9, 67.4, 58.2]
population = [331000000, 83000000, 68000000, 67000000, 126000000, 38000000, 25700000, 8600000, 17400000, 
              10300000, 5400000, 5800000, 5500000, 5000000, 5700000, 5000000, 52000000, 47300000, 59600000, 
              11400000, 8900000, 10200000, 10400000]

bubble_size = [pop / 1000000 for pop in population]

plt.figure(figsize=(14, 8))

plt.scatter(average_salary, employment_rate, s=bubble_size,
            color=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF4500', '#DA70D6', '#2E8B57', 
                   '#6A5ACD', '#00BFFF', '#FF1493', '#ADFF2F', '#DC143C', '#7B68EE', '#00FA9A', '#D2691E', 
                   '#FF69B4', '#B22222', '#8B4513', '#5F9EA0', '#DDA0DD', '#4B0082', '#FF8C00'],
            alpha=0.7, edgecolors='w', linewidth=2)

plt.title('Average Salary vs. Employment Rate in Various Countries', pad=20)
plt.xlabel('Average Salary (USD)', labelpad=15)
plt.ylabel('Employment Rate (%)', labelpad=15)

for i, country in enumerate(countries):
    plt.text(average_salary[i], employment_rate[i], country, ha='center', va='center', fontsize=8)

plt.show()