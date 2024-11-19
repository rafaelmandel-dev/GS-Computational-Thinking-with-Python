def numero_valido(valor):
    return all(c in '0123456789.-' for c in valor) and valor.count('.') <= 1 and valor.count('-') <= 1

def obter_dados_usuario():
    while True:
        temperatura = input("Informe a temperatura média anual (em °C): ")
        if numero_valido(temperatura):
            try:
                temperatura = float(temperatura)
                break
            except ValueError:
                pass
        print("Entrada inválida. Por favor, insira um número válido para a temperatura.")

    while True:
        sol = input("Informe a média de horas de sol por dia: ")
        if numero_valido(sol):
            try:
                sol = float(sol)
                break
            except ValueError:
                pass
        print("Entrada inválida. Por favor, insira um número válido para as horas de sol.")

    while True:
        vento = input("Informe a velocidade média do vento (em km/h): ")
        if numero_valido(vento):
            try:
                vento = float(vento)
                break
            except ValueError:
                pass
        print("Entrada inválida. Por favor, insira um número válido para a velocidade do vento.")

    while True:
        chuva = input("Informe a média de mm de chuva por ano: ")
        if numero_valido(chuva):
            try:
                chuva = float(chuva)
                break
            except ValueError:
                pass
        print("Entrada inválida. Por favor, insira um número válido para mm de chuva.")

    while True:
        relevo = input("Informe o tipo de relevo (planície, montanha, planalto): ").lower()
        if relevo in ["planície", "montanha", "planalto"]:
            break
        else:
            print("Entrada inválida. Por favor, insira um tipo de relevo válido (planície, montanha, planalto).")

    return temperatura, sol, vento, chuva, relevo

def avaliar_geracao_energia(temp, sol, vento, chuva, relevo):
    if sol > 6 and chuva < 500:
        return "solar", "Alta incidência solar e poucas chuvas são ideais para energia solar."
    elif vento > 20 and relevo in ["planície", "planalto"]:
        return "eólica", "Velocidade média do vento adequada para geração de energia eólica."
    else:
        return "hidrelétrica", "Nenhum recurso ideal identificado, recomendada análise local detalhada."

def principal():
    temperatura, sol, vento, chuva, relevo = obter_dados_usuario()
    tipo_energia, justificativa = avaliar_geracao_energia(temperatura, sol, vento, chuva, relevo)
    
    print(f"\nA melhor geração de energia para a sua região é: {tipo_energia.capitalize()}")
    print(f"Justificativa: {justificativa}")

# Chamando a função principal diretamente
principal()
