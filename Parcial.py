#importar las librerias necesariass
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


#Cargar el archivo csv

df = pd.read_csv('phone_search.csv')

#mostrar las primeras filas y columnas
print(df.head())
print( df.columns)

print("------------------------\n")
# Agrupar por calificación de estrellas y contar
print("Calificacion/Cantidad de productos con esa calificacion")
ratings_count = df.groupby('product_star_rating')['asin'].count()
print(ratings_count)

print("-----------------------------")
# Convertir 'product_price' a tipo numérico
df['product_price'] = df['product_price'].replace({r'\$': '', r',': ''}, regex=True).astype(float)

# Gráfico de barras de productos por calificación
ratings_count.plot(kind='bar')
plt.title('Número de Productos por Calificación de Estrellas')
plt.xlabel('Calificación de Estrellas')
plt.ylabel('Número de Productos')
plt.show()

# Histograma de precios
plt.figure(figsize=(8, 6))
sns.histplot(df['product_price'], bins=20, kde=True)
plt.title('Distribución de Precios de Productos')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.show()

print("-----------------------")
# Producto con mayor número de calificaciones
producto_mas_calificado = df.loc[df['product_num_ratings'].idxmax()]
print(f"Producto más calificado: {producto_mas_calificado['product_title']} con {producto_mas_calificado['product_num_ratings']} calificaciones.")
print("--------------------------")
# Crear una columna de descuento
df['discount'] = ((df['product_original_price'].replace({r'\$': '', r',': ''}, regex=True).astype(float) - df['product_price']) / 
                   df['product_original_price'].replace({r'\$': '', r',': ''}, regex=True).astype(float)) * 100
print(df[['product_title', 'product_price', 'product_original_price', 'discount']].head(10))
