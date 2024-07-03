
import matplotlib.pyplot as plt

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 
          'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 
          'Fort Worth', 'Columbus', 'Charlotte', 'Indianapolis', 'San Francisco', 
          'Seattle', 'Denver', 'Washington', 'Boston', 'Detroit', 'Nashville', 
          'Memphis', 'Portland', 'Oklahoma City', 'Las Vegas', 'Baltimore', 
          'Louisville', 'Milwaukee']
libraries = [95, 85, 78, 65, 68, 60, 74, 70, 72, 64, 66, 62, 59, 61, 63, 60, 85, 80, 
             67, 88, 82, 58, 64, 57, 69, 56, 75, 76, 54, 53]

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', '#A1D6E2', '#1995AD', 
          '#BCBABE', '#766F64', '#8BB8B8', '#3B9C9C', '#5D4C46', '#778C85', '#D1B499', 
          '#A2885F', '#FF7F50', '#6A5ACD', '#20B2AA', '#DB7093', '#FF1493', '#00CED1', 
          '#FF6347', '#4682B4', '#ADFF2F', '#00FA9A', '#DAA520', '#B22222', '#FF4500', 
          '#1E90FF', '#3CB371']

plt.figure(figsize=(18, 10))
plt.bar(cities, libraries, color=colors, width=0.7)

plt.ylabel('Number of Libraries')
plt.title('Number of Libraries in Various U.S. Cities', pad=20)
plt.ylim(50, 100)
plt.xticks(rotation=45)
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)

plt.tight_layout()

plt.show()