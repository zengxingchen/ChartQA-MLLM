
import matplotlib.pyplot as plt

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 
          'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 
          'Fort Worth', 'Columbus', 'Charlotte', 'Indianapolis', 'San Francisco', 
          'Seattle', 'Denver', 'Washington', 'Boston', 'Detroit', 'Nashville', 
          'Memphis', 'Portland', 'Oklahoma City', 'Las Vegas', 'Baltimore', 
          'Louisville', 'Milwaukee']
bookstores = [45, 35, 40, 50, 42, 38, 47, 36, 49, 41, 48, 34, 46, 37, 43, 39, 44, 33, 
              32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', '#A1D6E2', '#1995AD', 
          '#BCBABE', '#766F64', '#8BB8B8', '#3B9C9C', '#5D4C46', '#778C85', '#D1B499', 
          '#A2885F', '#FF7F50', '#6A5ACD', '#20B2AA', '#DB7093', '#FF1493', '#00CED1', 
          '#FF6347', '#4682B4', '#ADFF2F', '#00FA9A', '#DAA520', '#B22222', '#FF4500', 
          '#1E90FF', '#3CB371']

plt.figure(figsize=(14, 10))
plt.bar(cities, bookstores, color=colors, width=0.7)

plt.ylabel('Number of Bookstores')
plt.title('Number of Bookstores in Various U.S. Cities')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()