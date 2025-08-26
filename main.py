def calculo_imc(altura,peso):
    #formula imc = Peso / Altura x 2
    imc = float(peso / (altura **2))
    return float(imc)

def classificar(resultado_imc):
    if resultado_imc < 18.5:
         return 'magro'
    elif resultado_imc >= 18.5 and resultado_imc <= 24.9:
          return 'normal'
    elif resultado_imc >= 25.0 and resultado_imc  <= 29.9:
         return 'sobrepeso'
    elif resultado_imc >= 30.0 and resultado_imc  <= 39.9:
         return 'obesidade'
    else:
         return 'obesidade grave'


altura = float(input('digite sua altura:'))
peso = float(input('Digite seu peso:'))
imc = calculo_imc(altura,peso)
classificacao = classificar(imc)
print(f'Seu imc: {float(imc)} e sua classsicar:{classificacao}')
      
