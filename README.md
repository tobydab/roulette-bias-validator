# roulette-bias-validator
# Roulette Bias Validator

Herramienta básica en Python para detectar desviaciones estadísticas en ruletas usando el test Chi-cuadrado.

## Requisitos
Necesitas tener instalado Python y las librerías `pandas` y `scipy`:
```bash
pip install pandas scipy
```

## Uso
1. Prepara un archivo CSV llamado `spins.csv` con una columna encabezada como `result` que contenga los números ganadores (ej. 0, 1, 2... 36).
2. Ejecuta el script:
```bash
   python validator.py
```
3. El script imprimirá el P-value. Si es menor a 0.05, indica una posible anomalía estructural vs. ruido aleatorio.

*Nota: Esto es solo una herramienta de filtrado inicial. No garantiza un edge rentable sin análisis adicional de varianza y gestión de bankroll.*
