
# -*- coding: utf-8 -*-

peso =  float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua altura '))
imc = peso / (altura ** 2 )
print('O IMC é de {:.1f}'.format(imc))
if imc < 16:
    print('Magressa Grave')
elif  16 <= imc < 17:
    print('Magresa Moderada')
elif 17 <= imc < 18.5:
    print('Magressa Leve')
elif 18.5 <= imc < 25:
    print('Saudavel')
elif 25 <= imc <30:
    print('Sobre Psso')
elif 30<= imc <35:
    print("Obesidade Grau I")
elif 35 <= imc <40:
    print("Obesidade Grau II (SEVERA)")
elif 40 <= imc:
    print("Obesidade Grau III(Morbida)")



