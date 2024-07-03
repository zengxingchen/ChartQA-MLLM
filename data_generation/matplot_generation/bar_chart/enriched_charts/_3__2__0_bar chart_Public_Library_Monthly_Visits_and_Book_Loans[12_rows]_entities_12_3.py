
import matplotlib.pyplot as plt

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 
          'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 
          'Fort Worth', 'Columbus', 'Charlotte', 'Indianapolis', 'San Francisco', 
          'Seattle', 'Denver', 'Washington', 'Boston', 'Detroit', 'Nashville', 
          'Memphis', 'Portland', 'Oklahoma City', 'Las Vegas', 'Baltimore', 
          'Louisville', 'Milwaukee']
museums = [120, 90, 85, 95, 70, 80, 65, 75, 88, 77, 82, 60, 67, 72, 78, 69, 115, 83, 
           76, 110, 105, 68, 73, 66, 74, 61, 79, 81, 64, 71]

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', '#A1D6E2', '#1995AD', 
          '#BCBABE', '#766F64', '#8BB8B8', '#3B9C9C', '#5D4C46', '#778C85', '#D1B499', 
          '#A2885F', '#FF7F50', '#6A5ACD', '#20B2AA', '#DB7093', '#FF1493', '#00CED1', 
          '#FF6347', '#4682B4', '#ADFF2F', '#00FA9A', '#DAA520', '#B22222', '#FF4500', 
          '#1E90FF', '#3CB371']

plt.figure(figsize=(16, 12))
plt.barh(cities, museums, color=colors, height=0.6)

plt.xlabel('Number of Museums')
plt.title('Number of Museums in Various U.S. Cities')
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)

plt.tight_layout()

plt.show()