
import matplotlib.pyplot as plt

countries = [
    'Canada', 'Russia', 'Germany', 'United Kingdom', 'France', 'Spain', 
    'Italy', 'Greece', 'Turkey', 'Australia', 'Brazil', 'India', 
    'China', 'Japan', 'South Korea', 'Mexico', 'South Africa', 
    'Argentina', 'Nigeria', 'Egypt'
]

book_sales = [
    15.4, 20.1, 25.3, 22.8, 18.5, 14.3, 16.7, 12.9, 21.4, 19.7, 23.6, 29.0, 
    35.2, 24.6, 17.3, 13.8, 11.5, 13.4, 9.7, 10.2
]

colors = [
    '#2E8B57', '#4682B4', '#D2691E', '#8A2BE2', '#5F9EA0', '#D2B48C', 
    '#FF6347', '#FF4500', '#DAA520', '#9ACD32', '#32CD32', '#00CED1', 
    '#BA55D3', '#FF69B4', '#CD5C5C', '#F4A460', '#FFD700', '#8B008B', 
    '#9932CC', '#7FFF00'
]

plt.figure(figsize=(12, 14))
plt.barh(countries, book_sales, color=colors, height=0.7)
plt.xlabel('Book Sales (millions)')
plt.title('Book Sales by Country', pad=20)
plt.show()