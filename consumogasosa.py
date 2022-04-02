def calculadora(km, valor, consumo, dias, pessoas):
    valor_por_km = valor/consumo
    valor_por_dia = valor_por_km * km
    valor_mes = valor_por_dia * dias
    valor_pessoa = round((valor_mes-100)/pessoas)
    print(f'Valor por mês: {valor_mes}')
    print(f'Valor por pessoa: {valor_pessoa}')


if __name__ == '__main__':
    km = int(input('Distancia ida e volta: '))
    valor = float(input('Valor da gasolina/alcool: '))
    consumo = float(input('Consumo do carro: '))
    dias = int(input('Dias de uso: '))
    pessoas = int(input('Pessoas no carro: '))
    calculadora(km, valor, consumo, dias, pessoas)
