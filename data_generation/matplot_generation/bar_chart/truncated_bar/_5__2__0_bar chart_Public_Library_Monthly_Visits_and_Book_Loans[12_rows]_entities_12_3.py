import matplotlib.pyplot as plt

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 
          'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 
          'Fort Worth', 'Columbus', 'Charlotte', 'Indianapolis', 'San Francisco', 
          'Seattle', 'Denver', 'Washington', 'Boston', 'Detroit', 'Nashville', 
          'Memphis', 'Portland', 'Oklahoma City', 'Las Vegas', 'Baltimore', 
          'Louisville', 'Milwaukee']

average_temperatures = [60, 65, 55, 70, 75, 62, 72, 67, 68, 66, 69, 71, 67, 58, 64, 
                        56, 63, 57, 61, 59, 58, 54, 63, 66, 60, 64, 73, 61, 62, 53]

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', '#A1D6E2', '#1995AD', 
          '#BCBABE', '#766F64', '#8BB8B8', '#3B9C9C', '#5D4C46', '#778C85', '#D1B499', 
          '#A2885F', '#FF7F50', '#6A5ACD', '#20B2AA', '#DB7093', '#FF1493', '#00CED1', 
          '#FF6347', '#4682B4', '#ADFF2F', '#00FA9A', '#DAA520', '#B22222', '#FF4500', 
          '#1E90FF', '#3CB371']

plt.figure(figsize=(16, 12))
plt.barh(cities, average_temperatures, color=colors, height=0.6)

plt.xlabel('Average Temperature (°F)')
plt.title('Average Temperatures in Various U.S. Cities', pad=20)
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)

plt.xlim(50, 80)
plt.tight_layout()

plt.show()