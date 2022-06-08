from re import S, X
import PySimpleGUI as sg

#Tema
sg.theme('Dark Grey')

#Conteudo do menu
layout = [
        [sg.Push(),sg.Text('Digite o Salário Bruto'),sg.Push()],
        [sg.Push(),sg.Input(key='-wage-',justification='c'),sg.Push()],
        [sg.Push(),sg.Text('Dependentes'),sg.Push()],
        [sg.Push(),sg.Input('0',key='-dep-',justification='c'),sg.Push()],
        [sg.Push(),sg.OK(),sg.Cancel(),sg.Push()]    
]

#Configurando a janela do programa
window = sg.Window('Calculadora de Salário Líquido', layout)

while True:
    
    #Finalmente chamando o programa
    event,values = window.read()
    
    
    try:
        wage = float(values['-wage-'])
        dependentes = int(values['-dep-'])
        
        sg.Print('Seu salário bruto: R$',wage)    
        
        #INSS
        primeira_linha_desconto_inss = 1212 * 0.075
        segunda_linha_desconto_inss = (2427.35 - 1212) * 0.09
        terceira_linha_desconto_inss = (3641.03 - 2427.35) * 0.12
        quarta_linha_desconto_inss =  (wage - 3641.03) * 0.14
        
        if wage <= 1212: 
            aliquota_inss = 0.075
            aliquota_efetiva_inss = aliquota_inss

        if 1212 < wage < 2427.35:
            aliquota_inss = 0.09
            desconto_inss = ((wage - 1212) * aliquota_inss) + (primeira_linha_desconto_inss)
            aliquota_efetiva_inss = desconto_inss / wage
            
        if 2427.35 < wage < 3641.03: 
            aliquota_inss = 0.12
            desconto_inss = ((wage - 2427.35) * aliquota_inss) + (primeira_linha_desconto_inss) + (segunda_linha_desconto_inss)
            aliquota_efetiva_inss = desconto_inss / wage
        
        if 3641.03 < wage <= 7087.22:
            aliquota_inss = 0.14
            desconto_inss = ((wage - 3641.03) * aliquota_inss) + (primeira_linha_desconto_inss) + (segunda_linha_desconto_inss) + (terceira_linha_desconto_inss)
            aliquota_efetiva_inss = desconto_inss / wage
        
        if wage >= 7087.22:
            aliquota_inss = 0.14
            desconto_inss = 828.38
            aliquota_efetiva_inss = desconto_inss / wage
        
        sg.Print('\n1) Desconto (INSS): R$',round(desconto_inss,2),' Aliquota Efetiva: ',round(aliquota_efetiva_inss*100,2),'%')
        
        #IRRF
        primeira_linha_irrf = 1903.98
        segunda_linha_irrf = 2826.65
        terceira_linha_irrf = 3751.05
        quarta_linha_irrf = 4664.68
        desconto_dependentes = dependentes * 189.59
        base_irrf = wage - desconto_inss - desconto_dependentes
        
        if base_irrf < primeira_linha_irrf:
            aliquota_irrf = 0
            desconto_irrf = aliquota_irrf
        
        if primeira_linha_irrf < base_irrf < segunda_linha_irrf:
            aliquota_irrf = 0.075
            desconto_irrf = (base_irrf * aliquota_irrf) - 142.80
            aliquota_efetiva_irrf = desconto_irrf / wage
            
        if segunda_linha_irrf < base_irrf < terceira_linha_irrf:
            aliquota_irrf = 0.15
            desconto_irrf = (base_irrf * aliquota_irrf) - 354.80
            aliquota_efetiva_irrf = desconto_irrf / wage
            
        if terceira_linha_irrf < base_irrf < quarta_linha_irrf:
            aliquota_irrf = 0.225
            desconto_irrf = (base_irrf * aliquota_irrf) - 636.13
            aliquota_efetiva_irrf = desconto_irrf / wage
            
        if wage > quarta_linha_irrf:
            aliquota_irrf = 0.275  
            desconto_irrf = (base_irrf * aliquota_irrf) - 869.36
            aliquota_efetiva_irrf = desconto_irrf / wage
                    
        if desconto_irrf != 0:
            sg.Print('\n2) Desconto (IRRF): R$',round(desconto_irrf,2),' Alíquota Efetiva (IRRF): ',round(aliquota_efetiva_irrf*100,2),'%')
        else:
            sg.Print("\n2) Desconto (IRRF): Isento ")

        #VA
        desconto_va = 19.80
        sg.Print('\n3) Desconto Ticket Alimentação: R$',desconto_va)
        
        #VT
        transporte = 3.80
        numero_passes_diario = 2
        dias_uteis_mes = 22
        if wage <= 2786.667: #(7,6*22 / 0,06) total de passes do mes dividido pelo desconto max de 6%
            desconto_vt = wage * 0.06
        else:
            desconto_vt = transporte * numero_passes_diario * dias_uteis_mes
    
        sg.Print('\n4) Desconto Vale Transporte: R$',desconto_vt)

        #Salario Liquido
        net_wage = wage - desconto_inss - desconto_irrf - desconto_vt - desconto_va
        sg.Print('\n5) Salário Líquido: R$',round(net_wage,2))
        
    
    except ValueError:
        sg.Print('Utilize o Ponto para as casas decimais "." ao invés da vírgula ","')  
    
    if event in ('Cancel',sg.WIN_CLOSED):
        sg.Print("Fechando")
        break

window.close()
