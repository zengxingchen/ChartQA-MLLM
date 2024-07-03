
import matplotlib.pyplot as plt
import squarify

categories = [
    'Painting', 'Sculpture', 'Photography', 'Architecture', 'Ceramics',
    'Graphic Design', 'Fashion Design', 'Interior Design', 'Film', 'Printmaking',
    'Drawing', 'Illustration', 'Industrial Design', 'Digital Art', 'Textile Art',
    'Metalwork', 'Glass Art', 'Woodworking', 'Animation', 'Mixed Media',
    'Performance Art', 'Calligraphy', 'Tattoo Art'
]
counts = [
    1800, 1500, 1300, 1100, 950, 850, 750, 700, 650, 600,
    550, 500, 450, 400, 350, 300, 250, 200, 180, 160,
    140, 120, 100
]

color_palette = [
    '#FF7F50', '#6495ED', '#FFD700', '#ADFF2F', '#FF69B4',
    '#CD5C5C', '#4B0082', '#00FFFF', '#FF6347', '#8A2BE2',
    '#00FF00', '#4682B4', '#D2691E', '#DC143C', '#FF00FF',
    '#800000', '#00FF7F', '#DDA0DD', '#1E90FF', '#B0C4DE',
    '#FF4500', '#2E8B57', '#6A5ACD'
]

plt.figure(figsize=(20, 12))
squarify.plot(sizes=counts, label=categories, color=color_palette, alpha=0.8)

plt.title('Diverse Fields of Art & Design', fontsize=24, fontweight='bold', pad=30)
plt.axis('off')

plt.show()