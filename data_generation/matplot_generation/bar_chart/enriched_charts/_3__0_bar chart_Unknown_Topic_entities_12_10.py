import matplotlib.pyplot as plt

countries = ['China', 'India', 'USA', 'Indonesia', 'Brazil', 'Russia', 'Japan', 'Germany', 'France', 'UK', 'Italy', 'Canada', 'Australia', 'South Korea', 'Mexico', 'Spain']
gdp_growth = [6.1, 5.0, 2.3, 5.3, 1.1, 1.3, 0.7, 0.6, 1.5, 1.4, 0.3, 1.7, 2.2, 2.0, -0.1, 2.0]

colors = ['#4B0082', '#FFD700', '#DC143C', '#7FFF00', '#00BFFF', '#FF69B4', '#8A2BE2', '#FF4500', '#2E8B57', '#ADFF2F', '#DAA520', '#FF6347', '#4682B4', '#32CD32', '#8B0000', '#D2691E']

plt.figure(figsize=(14, 10))
plt.bar(countries, gdp_growth, color=colors, width=0.6)
plt.ylabel('GDP Growth Rate (%)')
plt.title('GDP Growth Rates of Countries')
plt.ylim(-1, max(gdp_growth) + 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

plt.show()