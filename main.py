import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('fichero_csv.csv')

# Guardar como archivo Excel
df.to_excel('fichero_excel.xlsx', index=False)