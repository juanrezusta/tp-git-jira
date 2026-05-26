import os
import pandas as pd
import matplotlib.pyplot as plt

# Definición de rutas fijas
DATA_DIR = "datos"
RESULTS_DIR = "resultados"

# Levantamos el archivo directamente desde la carpeta local datos
df = pd.read_csv(os.path.join(DATA_DIR, "monthly_climate_raw.csv"))

# Filtrado por la fuente GISTEMP
df_filtered = df[df['Source'] == 'GISTEMP'].copy()
df_filtered['Date'] = pd.to_datetime(df_filtered['Date'])
df_filtered['Year'] = df_filtered['Date'].dt.year

# Cálculos estadísticos básicos
mean_temp = df_filtered['Mean'].mean()
max_temp = df_filtered['Mean'].max()
min_temp = df_filtered['Mean'].min()
annual_evolution = df_filtered.groupby('Year')['Mean'].mean().reset_index()

# Escritura del archivo de texto final con indicadores
with open(os.path.join(RESULTS_DIR, "indicadores_climaticos.txt"), "w") as f:
    f.write("==================================================\n")
    f.write("   REPORTE DE INDICADORES CLIMÁTICOS GLOBALES     \n")
    f.write("==================================================\n")
    f.write(f"Temperatura Promedio Historica: {mean_temp:.4f} °C\n")
    f.write(f"Temperatura Maxima Registrada: {max_temp:.4f} °C\n")
    f.write(f"Temperatura Minima Registrada: {min_temp:.4f} °C\n")

# Diseño y exportación del gráfico
plt.figure(figsize=(10, 5))
plt.plot(annual_evolution['Year'], annual_evolution['Mean'], color='crimson', linewidth=2, label='Anomalía Media Anual')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.title("Evolución Histórica de la Anomalía de Temperatura Global", fontsize=12, fontweight='bold')
plt.xlabel("Año")
plt.ylabel("Anomalía de Temperatura (°C)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.savefig(os.path.join(RESULTS_DIR, "evolucion_temperatura.png"), dpi=300, bbox_inches='tight')
plt.close()
