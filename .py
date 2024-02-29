peso = float (input ('Qual o seu peso em KG ? '))
altura = float ( input ('Qual a sua altura em M ? '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print ('Esta pessoa está abaixo do peso ideal e seu IMC é de {:.1f} '.format (imc))
elif imc < 25:
    print ('Esta pessoa está com o peso ideal e seu IMC é de {:.1f} '.format(imc))
elif imc < 30:
    print ('Esta pessoa está com sobrepeso e seu IMC é de {:.1f} '.format (imc))
elif imc < 40:
    print ('Esta pessoa está em obesidade e seu IMC é de {:.1f} '.format (imc))
else: 
    print ('Esta pessoa está em obesidad morbida, cuidado! O seu IMC é de {:.1f} '.format(imc))