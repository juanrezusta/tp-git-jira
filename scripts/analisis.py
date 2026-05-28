import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = "datos"
RESULTS_DIR = "resultados"

df = pd.read_csv(os.path.join(DATA_DIR, "monthly_climate_raw.csv"))

# Filtrado por la fuente GISTEMP
# LOGICA: Aislamiento de registros correspondientes a la serie 'GISTEMP' (NASA) mediante indexación booleana y normalización temporal de tipos de datos.
# POR QUÉ: Se selecciona GISTEMP por su consistencia metodológica global. La conversión a datetime y la extracción del atributo '.dt.year' son críticas para poder agrupar y segmentar métricas por períodos anuales exactos más adelante.
df_filtered = df[df['Source'] == 'GISTEMP'].copy()
df_filtered['Date'] = pd.to_datetime(df_filtered['Date'])
df_filtered['Year'] = df_filtered['Date'].dt.year

# Cálculos estadísticos básicos
# LOGICA: Computación de estadísticos descriptivos agregados (promedio, máximos y mínimos absolutos) sobre las anomalías y agrupación estructurada (.groupby) por año.
# POR QUÉ: Permite sintetizar millones de observaciones mensuales en indicadores clave de tendencia central y dispersión. La agrupación anual ('annual_evolution') prepara la estructura requerida para evaluar el comportamiento histórico.
mean_temp = df_filtered['Mean'].mean()
max_temp = df_filtered['Mean'].max()
min_temp = df_filtered['Mean'].min()
annual_evolution = df_filtered.groupby('Year')['Mean'].mean().reset_index()

# Escritura del archivo de texto final con indicadores
# LOGICA: Apertura de canal de escritura en modo 'w' para exportar un reporte limpio en texto plano intercalando strings formateados con interpolación de variables (: .4f).
# POR QUÉ: Automatiza la entrega de un entregable legible para stakeholders que no leen código, aislando los resultados estadísticos críticos en un archivo independiente ('indicadores_climaticos.txt').
with open(os.path.join(RESULTS_DIR, "indicadores_climaticos.txt"), "w") as out_f:
    out_f.write("==================================================
")
    out_f.write("    REPORTE DE INDICADORES CLIMÁTICOS GLOBALES    
")
    out_f.write("==================================================
")
    out_f.write(f"Temperatura Promedio Historica: {mean_temp:.4f} °C
")
    out_f.write(f"Temperatura Maxima Registrada: {max_temp:.4f} °C
")
    out_f.write(f"Temperatura Minima Registrada: {min_temp:.4f} °C
")

# Diseño y exportación del gráfico
# LOGICA: Renderizado de un gráfico de líneas temporal utilizando la interfaz orientada a objetos de Matplotlib, configurando grillas, leyendas explicativas y una línea de referencia en el origen (y=0).
# POR QUÉ: La visualización es indispensable para identificar visualmente la tendencia ascendente de la anomalía térmica. La línea gris discontinua en cero funciona como umbral crítico para evidenciar a partir de qué año el calentamiento global se volvió constante. Se exporta a alta resolución (300 DPI) para su incorporación en el informe final.
plt.figure(figsize=(10, 5))
plt.plot(annual_evolution['Year'], annual_evolution['Mean'], color='crimson', linewidth=2, label='Anomalía Media Anual')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.title('Evolución Histórica de la Anomalía de Temperatura Global', fontsize=12, fontweight='bold')
plt.xlabel('Año')
plt.ylabel('Anomalía de Temperatura (°C)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.savefig(os.path.join(RESULTS_DIR, "evolucion_temperatura.png"), dpi=300, bbox_inches='tight')
plt.close()