import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = "datos"
RESULTS_DIR = "resultados"

# Leer el archivo de datos raw
df = pd.read_csv(os.path.join(DATA_DIR, "monthly_climate_raw.csv"))

# SOLICITUD DE INPUT DINÁMICO
# LOGICA: Uso de la función nativa input() para parametrizar de forma dinámica la fuente de análisis climático.
# POR QUÉ: Permite que el script sea interactivo y reutilizable, dándole al usuario la libertad de elegir la serie de datos (ej. GISTEMP) en tiempo de ejecución sin alterar el código fuente.
fuente_elegida = input("Ingrese la fuente de datos a analizar (ej. GISTEMP): ")

# Filtrado por la fuente ingresada por el usuario
# LOGICA: Aislamiento de registros mediante indexación booleana usando la variable dinámica y normalización temporal.
df_filtered = df[df['Source'] == fuente_elegida].copy()
df_filtered['Date'] = pd.to_datetime(df_filtered['Date'])
df_filtered['Year'] = df_filtered['Date'].dt.year

# Cálculos estadísticos básicos
mean_temp = df_filtered['Mean'].mean()
max_temp = df_filtered['Mean'].max()
min_temp = df_filtered['Mean'].min()
annual_evolution = df_filtered.groupby('Year')['Mean'].mean().reset_index()

# Escritura del archivo de texto final con indicadores
with open(os.path.join(RESULTS_DIR, "indicadores_climaticos.txt"), "w") as out_f:
    out_f.write("==================================================\n")
    out_f.write(f"    REPORTE DE INDICADORES: {fuente_elegida}    \n")
    out_f.write("==================================================\n")
    out_f.write(f"Temperatura Promedio Historica: {mean_temp:.4f} °C\n")
    out_f.write(f"Temperatura Maxima Registrada: {max_temp:.4f} °C\n")
    out_f.write(f"Temperatura Minima Registrada: {min_temp:.4f} °C\n")

# Diseño y exportación del gráfico
plt.figure(figsize=(10, 5))
plt.plot(annual_evolution['Year'], annual_evolution['Mean'], color='crimson', linewidth=2, label=f'Anomalía Media {fuente_elegida}')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.title(f'Evolución Histórica de la Anomalía de Temperatura ({fuente_elegida})', fontsize=12, fontweight='bold')
plt.xlabel('Año')
plt.ylabel('Anomalía de Temperatura (°C)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.savefig(os.path.join(RESULTS_DIR, "evolucion_temperatura.png"), dpi=300, bbox_inches='tight')
plt.close()
