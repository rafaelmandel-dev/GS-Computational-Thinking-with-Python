# Guardian - Avaliação de Geração de Energia Sustentável

Este repositório contém o código fonte do Guardian, um software que utiliza dados climáticos e geográficos para recomendar o melhor tipo de energia sustentável para uma região específica.

## Objetivo do Projeto

O Guardian busca maximizar a eficiência energética, promovendo o uso de fontes renováveis como energia solar, eólica e hidrelétrica, além de contribuir para a sustentabilidade ambiental e autonomia regional.

## Desenvolvedores

- Rafael Mandel, 560333

- Luigi Thinego, 560755

- Felipe Silva, 559848

## Link para video explicativo

[Clique aqui e acesse o video no Youtube](https://youtu.be/T60BqlcKrpY)

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal.

- **Funções Dinâmicas**: Estruturas modulares e reutilizáveis.

## Funcionalidades

### Entradas do Usuário

O software coleta os seguintes dados:

1. **Temperatura Média Anual (em °C)**: Indica o clima predominante na região.

2. **Média de Horas de Sol por Dia**: Essencial para avaliar o potencial de energia solar.

3. **Velocidade Média do Vento (em km/h)**: Determina a viabilidade de energia eólica.

4. **Média de Chuvas Anuais (em mm)**: Importante para a avaliação da energia hidrelétrica.

5. **Tipo de Relevo**: Identifica se é planície, montanha ou planalto, ajudando na escolha da fonte de energia.

### Avaliação

O software analisa os dados fornecidos e determina a melhor fonte de energia para a região:

- Energia Solar: Alta incidência de sol e poucas chuvas.

- Energia Eólica: Ventos fortes em regiões de planície ou planalto.

- Energia Hidrelétrica: Alternativa para regiões sem recursos ideais para solar ou eólica.

### Saída do Sistema

- Tipo de Energia Recomendado: Baseado nos dados inseridos.

- Justificativa: Uma explicação clara para a recomendação realizada.

## Como Executar o Projeto

1. **Requisitos:**

- Python 3.6 ou superior.

2. **Clonar o Repositório:**

git clone <[URL do repositório](https://github.com/rafaelmandel-dev/GS-Computational-Thinking-with-Python)>

3. **Executar o Código:**

- Navegue até o diretório onde o repositório foi clonado.

- Execute o seguinte comando:

``python GS.py``

4. **Insira os Dados:**

- Siga as instruções no terminal para fornecer os dados climáticos e geográficos.

5. **Resultado:**

- O sistema exibirá o tipo de energia ideal e a justificativa da escolha.

## Exemplo de Uso

    Informe a temperatura média anual (em °C): 25
    Informe a média de horas de sol por dia: 7
    Informe a velocidade média do vento (em km/h): 10
    Informe a média de mm de chuva por ano: 300
    Informe o tipo de relevo (planície, montanha, planalto): planície

    A melhor geração de energia para a sua região é: Solar
    Justificativa: Alta incidência solar e poucas chuvas são ideais para energia solar.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.