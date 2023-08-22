while True: 

    "   "" Inicia um laço de repetição infinito """ 

    """ Inicia as variáveis, incluindo o calculo do IMC """ 

    peso=float(input('Quanto você pesa em Kg?')) 

    altura=float(input('Qual a sua altura em metros?')) 

    IMC = peso/(altura**2) 


    """ Verificação do IMC e saida do resultado """ 

    if IMC < 18.5: 

        print('Diagnóstico: Abaixo do peso normal 🟨') 

    elif IMC >=18.5 and IMC <25: 

        print('Diagnóstico: peso normal 🟩') 

    elif IMC >=25 and IMC <30: 

        print('Diagnóstico: Acima do peso ideal 🟨') 

    elif IMC >=30 and IMC <35: 

        print('Diagnóstico: Obsidade grau 1 🟧') 

    elif IMC >=35 and IMC <40: 

        print('Diagnóstico: obeso 2 (Obsidade severa)🟫') 

    elif IMC >=40: 

        print('Diagnóstico: obesidade 3 (mórbida)🟥') 

        print('O seu IMC é de {:.2f}'.format(IMC)) 

    else: 
        print('Dado inválido')
 

        """ Resposta do usuario ao sistema """ 

    resposta=input("Deseja refazer?[S/ N]") 

    """ verificação da resposta, transfomação para maiusculo """ 

    if resposta.upper() != "S" : 

        """ Encerramento do programa, caso a resposta seja negativa """ 

        print("até mais") 

        break 