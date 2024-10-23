def calcular_percentual(dados):
    total  = sum(dados.values())
    
    percentual = {estado: round((faturamento / total) * 100, 2) for estado, faturamento in dados.items()}
    
    return percentual

if __name__ == "__main__":
    faturamento_menal = {
        "sp": 67836.43,
        "rj": 36678.66,
        "mg": 29229.88,
        "es": 27165.48,
        "outros": 19849.53
    }
    
    resultado = calcular_percentual(faturamento_menal)
    print (resultado)