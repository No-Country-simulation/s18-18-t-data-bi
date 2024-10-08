# Dataset de Detección de Incendios DEFINICION DE CADA COLUMNA


### Columnas del Dataset

- **latitude**: Latitud geográfica de la detección del incendio, medida en grados.
- **longitude**: Longitud geográfica de la detección del incendio, medida en grados.
- **brightness**: Brillo o temperatura de radiancia en la banda infrarroja media (en kelvin), captada por el sensor. Un valor alto generalmente indica una mayor intensidad del incendio.
- **scan**: El ancho del campo de visión del escaneo en kilómetros. Es un parámetro relacionado con la resolución espacial de la detección.
- **track**: El largo del campo de visión del escaneo en kilómetros, complementando el valor de `scan` para definir la resolución espacial.
- **acq_date**: Fecha de adquisición de los datos del incendio por el satélite. Indica cuándo se detectó el incendio.
- **acq_time**: Hora de adquisición de los datos (hora UTC), expresada en formato de 24 horas (HHMM). Es el momento preciso en que el satélite captó la detección del incendio.
- **satellite**: Nombre del satélite que capturó la detección. Puede ser Terra, Aqua o Suomi NPP.
- **instrument**: Instrumento o sensor que realizó la detección, por ejemplo, MODIS (Moderate Resolution Imaging Spectroradiometer) o VIIRS (Visible Infrared Imaging Radiometer Suite).
- **confidence**: Confianza o probabilidad de que la detección sea un incendio real, expresada en un porcentaje o categoría. En MODIS, por ejemplo, puede variar entre "low", "nominal" y "high". En VIIRS, los valores suelen ser numéricos.
- **version**: Versión del producto de detección de incendios utilizada, que refleja posibles actualizaciones en los algoritmos o procesos de detección.
- **bright_t31**: Brillo o temperatura en la banda de 31 micrones del espectro infrarrojo térmico (en kelvin). Proporciona información adicional sobre la temperatura de los objetos observados.
- **frp**: Potencia radiante del fuego (*Fire Radiative Power*) medida en megavatios (MW). Es una estimación de la cantidad de energía emitida por el incendio, que se relaciona con la intensidad del mismo.
- **daynight**: Indica si la detección fue realizada durante el día (D) o la noche (N).
- **type**: Tipo de detección. Puede ser 0 (detección "normal" de fuego) o 2 (un fuego procedente de una fuente no estándar, como la quema controlada).
