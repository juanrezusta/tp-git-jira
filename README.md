Analisis de Datos Climaticos
Integrantes
          P1 - Lider y organizador: Juan rezusta
          P2 - Desarrollador tecnico: Tomas Rebottaro
          P3 - QA y revisor: Juan rezusta

Descripcion del proyecto:

  Este proyecto consiste en un script que analiza datos climaticos a partir de un archivo CSV.
  
  El script toma un dataset con informacion de temperatura, hace calculos basicos (promedio, maximo y minimo) y arma un grafico con la evolucion de la temperatura media a lo largo del tiempo.
  
  La idea es que no quede atado a un solo dataset, sino que se pueda reutilizar con otros archivos CSV que tengan la misma estructura.

Dataset utilizado

  El script trabaja con archivos CSV ubicados en la carpeta /datos.
  
  Para este trabajo se uso un dataset de temperaturas globales, pero el codigo permite cambiar el archivo de entrada mientras respete el formato esperado.

Ejecucion del proyecto:

  Clonar el repositorio
  Ubicarse en la carpeta del proyecto
  En caso de desear otra fuente, cambiar el contenido del archivo "monthly_climate_war.csv" por formato similar de datos.
  Ejecutar el script dentro de /scripts

El script se encarga de:

  leer el archivo
  procesar los datos
  generar los resultados automaticamente

Estructura del repositorio:

  /datos
  Contiene el archivo CSV que se usa como entrada
  
  /scripts
  Contiene el script principal del analisis
  
  /resultados
  Contiene los archivos generados:
  un archivo de texto con indicadores
  un grafico de la evolucion de temperatura


El script genera:

  Un archivo de texto con:
    temperatura promedio historica
    temperatura maxima registrada
    temperatura minima registrada
  Un grafico de linea que muestra como va cambiando la temperatura media con el tiempo

En el caso analizado, se puede ver una tendencia general a la suba en los ultimos años.

Consideraciones tecnicas:

El codigo esta pensado para ejecutarse de principio a fin sin depender de pasos intermedios salvo se quiera personalizar la fuente.
