import pandas as pd
from scipy.stats import chisquare

def check_bias(file_path):
    try:
        # Lee el CSV. Asumimos una columna llamada 'result' con los números ganadores.
        df = pd.read_csv(file_path)
        
        if 'result' not in df.columns:
            print("Error: La columna 'result' no existe en el CSV.")
            return

        counts = df['result'].value_counts().sort_index()
        total_spins = len(df)
        
        # Ruleta europea (37 casillas: 0-36). Si es americana, cambia a 38.
        num_slots = 37 
        
        # Frecuencia esperada si fuera perfecta
        expected_freq = [total_spins / num_slots] * num_slots
        
        # Ordenamos las frecuencias observadas para que coincidan con el índice 0-36
        observed_freq = []
        for i in range(num_slots):
            if i in counts.index:
                observed_freq.append(counts[i])
            else:
                observed_freq.append(0)
                
        # Test Chi-cuadrado
        stat, p_value = chisquare(observed_freq, f_exp=expected_freq)
        
        print(f"Total Spins: {total_spins}")
        print(f"Chi-Square Statistic: {stat:.2f}")
        print(f"P-Value: {p_value:.5f}")
        
        if p_value < 0.05:
            print("RESULTADO: Desviación estadísticamente significativa detectada (posible bias).")
        else:
            print("RESULTADO: Sin desviación significativa (comportamiento aleatorio esperado).")
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    # Cambia 'spins.csv' por el nombre de tu archivo real si es diferente
    check_bias('spins.csv')
