import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Excel dosyasını okuyun
df = pd.read_excel('koordinatlar.xlsx')

# Grafik boyutunu ve ızgara boyutunu ayarlayın
fig, ax = plt.subplots(figsize=(10, 10))
grid_size = 100  # 50, 100 veya 200 olarak değiştirebilirsiniz

# Her ızgara için farklı renkler belirleyin
num_colors = (1000 // grid_size) ** 2
colors = np.random.rand(num_colors, 3)

# Noktaları ızgaralara göre renklendirin
for i in range(0, 1000, grid_size):
    for j in range(0, 1000, grid_size):
        # Her bir ızgaradaki noktaları seçin
        mask = (df['X'] >= i) & (df['X'] < i + grid_size) & (df['Y'] >= j) & (df['Y'] < j + grid_size)
        color_index = (i // grid_size) * (1000 // grid_size) + (j // grid_size)
        ax.scatter(df[mask]['X'], df[mask]['Y'], color=colors[color_index], s=10)

# Grafik ayarları
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
ax.set_title('Rastgele Noktaların Görselleştirilmesi')
ax.set_xlabel('X Koordinatları')
ax.set_ylabel('Y Koordinatları')
ax.grid(True)

# Grafiği kaydedin
plt.savefig('koordinatlar_grafik.jpeg')
plt.show()
print("Grafik 'koordinatlar_grafik.jpeg' dosyasına kaydedildi.")