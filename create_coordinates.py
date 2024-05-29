import numpy as np
import pandas as pd

# Rastgele koordinatlar üretin
np.random.seed(0)
x = np.random.randint(0, 1001, size=1000)
y = np.random.randint(0, 1001, size=1000)

# Verileri bir DataFrame'e dönüştürün
df = pd.DataFrame({'X': x, 'Y': y})

# Excel dosyasına kaydedin
df.to_excel('koordinatlar.xlsx', index=False)
print("Koordinatlar 'koordinatlar.xlsx' dosyasına kaydedildi.")
