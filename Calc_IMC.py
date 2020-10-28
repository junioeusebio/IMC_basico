peso = float(input('Digite seu peso em kilos: '))
altura = float(input('Digite sua altura em metros: '))
 
imc = peso / (altura * altura)

def mensagem_imc():


    if imc < 18.5:
        print ('Seu IMC é de: {:.2f} e esta classificado como magreza e o Grau é 0'.format(imc))

    elif imc < 24.9:
        print ('Seu IMC é de: {:.2f} e esta classificado como normal e o Grau é 0'.format(imc))

    elif imc < 29.9:
        print ('Seu IMC é de: {:.2f} e esta classificado como sobrepeso e o Grau é I'.format(imc))

    elif imc < 39.9:
        print ('Seu IMC é de: {:.2f} e esta classificado como obesidade e o Grau é II'.format(imc))

    elif imc < 40:
        print ('Seu IMC é de: {:.2f} e esta classificado como obesidade grave e o Grau é III'.format(imc))

