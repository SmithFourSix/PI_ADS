import os #importação da biblioteca OS para dar o comando Clear no s.o linux ou cls no Windows(limpar a tela para nao ficar poluido)
import time #Importação da biblioteca time para colocar um temporizador para simular Ex: computação de votos,etc.
import heapq # importação da blibioteca heapq para mostrar tres vereadores com maiores votos 

#Declaração de variaveis
#Lugares: Yoda(0), Darth(1), Luke(2), Branco(3), Nulo(4) --- meramente demonstrav
prefeito = [['13 - Yoda','13',0,'Republica'], ['18 - Darth Vader','18',0,'Imperio'], ['15 - Luke','15',0,'Republica'], ['Branco','br',0], ['Nulo','nu',0]]
#Lugares: Sylvana(0), Mannoroth(1),Garrosh(2),Han Solo(3),Jaina(4),Turalyon(5),Darth Sidious(6),Boba Fett(7),Varok Saurfang(8),Orgrim(9)
vereadores = [['15897  - Sylvana','15897',0,'Horda'], ['12438 - Mannoroth','12438',0,'Horda'], ['14488 - Garrosh','14488',0,'Horda'], ['24638 - Han Solo ','24638',0,'Republica'], ['22874 - Jaina','22874',0,'Aliança'], ['24515 - Turalyon','24515',0,'Aliança'], ['36458 - Darth Sidious ','36458',0,'Imperio'], ['36157 - Boba Fett','36157',0,'Imperio'], ['45698 - Varok Saurfang','45698',0,'Horda'], ['48796 - Orgrim','48796',0,'Horda']]

# função principal do sistema que chama todas outras funções
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------------------------")
    print("----Bem Vindo --- Urna eletronica --- Registro-SP ----")
    print("---                                               ----")
    print("--- (1)Imprimir Zerésima                          ----")
    print("--- (2)Iniciar votação                            ----")
    print("------------------------------------------------------")
    start =  input()
    if start == '1':
        zeresima() #chamando função zeresima
        time.sleep(5) #utilização do temporizador
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
    elif start =='2':
        os.system('cls' if os.name == 'nt' else 'clear')
        votacao() #chamando função votação
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção Invalida!!!")
        print("Voltando ao menu.")
        time.sleep(5) #utilização do temporizador



def zeresima():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---------------------------Prefeitos----------------------------")
    print("- Digito: 13 - Nome: Yoda - Partido: Republica - Votos: 0      -")
    print("- Digito: 18 - Nome: Darth Vader - Partido: Imperio - Votos: 0 -")
    print("- Digito: 15 - Nome: Luke - Partido: Republica - Votos: 0      -")
    print("----------------------------------------------------------------")
    print("Aguarde...")
    time.sleep(5) #utilização do temporizador
    print("---------------------------Vereadores------------------------------")
    print("- Digito: 15897 - Nome: Sylvana - Partido: Horda Votos: 0         -")
    print("- Digito: 12438 - Nome: Mannoroth - Partido: Horda Votos: 0       -")
    print("- Digito: 14488 - Nome: Garrosh - Partido: Horda Votos: 0         -")
    print("- Digito: 24638 - Nome: Han Solo - Partido: Republica Votos: 0    -")
    print("- Digito: 22874 - Nome: Jaina - Partido: Aliança Votos: 0         -")
    print("- Digito: 24515 - Nome: Turalyon - Partido: Aliança Votos: 0      -")
    print("- Digito: 36458 - Nome: Darth Sidious - Partido: Imperio Votos: 0 -")
    print("- Digito: 36157 - Nome: Boba Fett - Partido: Imperio Votos: 0     -")
    print("- Digito: 45698 - Nome: Varok - Partido: Horda Votos: 0           -")
    print("- Digito: 48796 - Nome: Orgrim - Partido: Horda Votos: 0          -")
    print("-------------------------------------------------------------------")


def votacao():
    print("-------------------Votação------------------")
    print("- Digite a opção escolhida:                -")
    print("- (1) - Prefeito                           -")
    print("- (2) - Vereador                           -")
    print("- (3) - Branco                             -")
    print("--------------------------------------------")
    res = int(input())

    if res == 1:                                                                                                                #PREFEITO VOTAÇÃO
        print("-----Digite o numero do candidato-----")
        cand = int(input())
        os.system('cls' if os.name == 'nt' else 'clear')
        if cand == 13:
            print(" Nome: Yoda - Partido: Republica -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '13' == prefeito[0][1]:
                    prefeito[0][2] = prefeito[0][2]+1
                print('-----Computando voto-----')
                
                
                time.sleep(5)
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()
            

        elif cand == 18:
            print(" Nome: Darth Vader - Partido: Imperio -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '18' in prefeito[1][1]:
                    prefeito[1][2] = prefeito[1][2]+1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()
        
        elif cand == 15:
            print(" Nome: Luke - Partido: Republica -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '15' == prefeito[2][1]:
                    prefeito[2][2] = prefeito[2][2]+1
                print('-----Computando voto-----')                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()    
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida")
            print("Voto será computado com nulo.")
            cand = input("Deseja Continuar?(sim ou não)\n")
            if cand == 'sim':
                os.system('cls' if os.name == 'nt' else 'clear')
                if 'nu' == prefeito[4][1]:
                     prefeito[4][2] =  prefeito[4][2] +1
                print('-----Computando voto-----')

                time.sleep(5) #utilização do temporizador
                print("“Finalizar a votação ou continuar? (finalizar ou continuar)\n”")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()
            elif cand == 'não' or cand == 'nao':
                menu()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu() 



        

        
    




#VEREADOR VOTAÇÃO    
    elif res == 2:
        print("-----Digite o numero do candidato-----")
        cand = int(input())
        os.system('cls' if os.name == 'nt' else 'clear')
        if cand == 15897:
            print("Nome: Sylvana - Partido: Horda -")
            cand = input("Deseja continuar?(sim ou não)")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '15897' == vereadores[0][1]:
                    vereadores[0][2] = vereadores[0][2] +1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu() 
            

        elif cand == 12438:
            print("- Nome Mannoroth - Partido: Horda -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '12438' == vereadores[1][1]:
                    vereadores[1][2] = vereadores[1][2] +1
                print('-----Computando voto-----')
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()
        
        elif cand == 14488:
            print(" Nome: Garrosh - Partido: Horda -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '14488' == vereadores[2][1]:
                    vereadores[2][2] = vereadores[2][2] +1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()

        elif cand == 24638:
            print("Nome: Han Solo - Partido: Republica")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '24638' == vereadores[3][1]:
                    vereadores[3][2] = vereadores[3][2] +1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()       

        elif cand == 22874:
            print(" Nome: Jaina - Partido: Aliança -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '22874' == vereadores[4][1]:
                    vereadores[4][2] = vereadores[4][2] +1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()       

        elif cand == 24515:
            print(" Nome: Turalyon - Partido: Aliança -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '24515' == vereadores[5][1]:
                    vereadores[5][2] = vereadores[5][2] +1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()  

        elif cand == 36458:
            print("Nome: Darth Sidious - Partido: Imperio -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '36458' == vereadores[6][1]:
                    vereadores[6][2] = vereadores[6][2] +1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()                           
        
        elif cand == 36157:
            print(" Nome: Boba Fett - Partido: Imperio -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '36157' == vereadores[7][1]:
                    vereadores[7][2] = vereadores[7][2] +1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()                           
        
        elif cand == 45698:
            print(" Nome: Varok - Partido: Horda -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '45698' == vereadores[8][1]:
                    vereadores[8][2] = vereadores[8][2] +1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()                           
        
        elif cand == 48796:
            print(" Nome: Orgrim - Partido: Horda -")
            cand = input("Deseja continuar?(sim ou não)\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            if cand == 'sim' or cand == 'Sim' or cand =='SIM':
                if '48796' == vereadores[9][1]:
                    vereadores[9][2] = vereadores[9][2] +1
                print('-----Computando voto-----')
                
                
                time.sleep(5) #utilização do temporizador
                print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()     

            elif cand == 'não' or cand == 'nao':
                menu()
                
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()                           
                                  
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida")
            print("Voto será computado com nulo.")
            cand = input("Deseja Continuar?(sim ou não)\n")
            if cand == 'sim':
                os.system('cls' if os.name == 'nt' else 'clear')
                if 'nu' == prefeito[4][1]:
                     prefeito[4][2] =  prefeito[4][2] +1
                print('-----Computando voto-----')

                time.sleep(5) #utilização do temporizador
                print("“Finalizar a votação ou continuar? (finalizar ou continuar)\n”")
                cand = input()
                if cand == 'finalizar' or cand == 'FINALIZAR':          #MOSTRAR RESULTADOS 
                    total()
                elif cand == 'continuar' or cand == 'CONTINUAR:':
                    votacao()
            elif cand == 'não' or cand == 'nao':
                menu()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção invalida")
                print("Voltando ao menu principal.")
                time.sleep(5) #utilização do temporizador
                menu()
       

    # Votação branco
    elif res == 3:
        print("Voto será computado com Branco.")
        cand = input("Deseja Continuar?(sim ou não)\n")
        if cand == 'sim':
            os.system('cls' if os.name == 'nt' else 'clear')
            if 'br' == prefeito[3][1]:
                     prefeito[3][2] =  prefeito[3][2] +1
            print('-----Computando voto-----')                
            time.sleep(5) #utilização do temporizador
            print("Finalizar a votação ou continuar? (finalizar ou continuar)\n")
            cand = input()
            if cand == 'finalizar' or cand == 'FINALIZAR':
                total()
                exit()
            elif cand == 'continuar' or cand == 'CONTINUAR:':
                votacao()     

        elif cand == 'não' or cand == 'nao':
            menu()
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção invalida.")
        print("Voltando ao menu inicial em 5 segundos...")
        print("Aguarde...")
        time.sleep(5) #utilização do temporizador
        menu()

def total():
    print('--------------------Prefeito--------------------------')
    print('-----------------Votos Computados---------------------')
    print('Prefeito:',prefeito[0][0],' Partido:',prefeito[0][3],'votos:', prefeito[0][2])
    print('Prefeito:',prefeito[1][0],' Partido:',prefeito[1][3],'votos:', prefeito[1][2])
    print('Prefeito:',prefeito[2][0] ,' Partido:',prefeito[2][3],'votos:', prefeito[2][2])
    print(prefeito[3][0] ,'votos:', prefeito[3][2])
    print(prefeito[4][0] ,'votos:', prefeito[4][2])
    print('------------------------------------------------------')
    time.sleep(5) #utilização do temporizador
    total_ver()
    

def total_ver():
    print('--------------------Vereadores------------------------')
    print('-----------------Votos Computados---------------------')
    print('Vereador:', vereadores[0][0] ,' Partido:',vereadores[0][3],'votos:', vereadores[0][2])
    print('Vereador:', vereadores[1][0] ,' Partido:',vereadores[1][3],'votos:', vereadores[1][2])
    print('Vereador:', vereadores[2][0] ,' Partido:',vereadores[2][3],'votos:', vereadores[2][2])
    print('Vereador:', vereadores[3][0] ,' Partido:',vereadores[3][3],'votos:', vereadores[3][2])
    print('Vereador:', vereadores[4][0] ,' Partido:',vereadores[4][3],'votos:', vereadores[4][2])
    print('Vereador:', vereadores[5][0] ,' Partido:',vereadores[5][3],'votos:', vereadores[5][2])
    print('Vereador:', vereadores[6][0] ,' Partido:',vereadores[6][3],'votos:', vereadores[6][2])
    print('Vereador:', vereadores[7][0] ,' Partido:',vereadores[7][3],'votos:', vereadores[7][2])
    print('Vereador:', vereadores[8][0] ,' Partido:',vereadores[8][3],'votos:', vereadores[8][2])
    print('Vereador:', vereadores[9][0] ,' Partido:',vereadores[9][3],'votos:', vereadores[9][2])
    print(prefeito[3][0] ,'votos:', prefeito[3][2])
    print(prefeito[4][0] ,'votos:', prefeito[4][2])
    print('------------------------------------------------------')
    time.sleep(5) #utilização do temporizador
    os.system('cls' if os.name == 'nt' else 'clear')
    totalizacao()
    #função para achar vencedor dos candidatos para prefeito 
def totalizacao():
    second_turn = [prefeito[0][2],prefeito[1][2],prefeito[2][2]]
    x = len(second_turn) == len(set(second_turn))
    max = prefeito[0][2]
    if x == False:
        print('--------------------Novo Prefeito-----------------------')
        print('Empate na votação...')
        print("Haverá um Segundo turno ...")
        print('------------------------------------------------------')
        time.sleep(3) #utilização do temporizador
        totalizacao_ver()
    else:
        if prefeito[1][2] > max:
            max = prefeito[1][2]
            print('--------------------Novo Prefeito-----------------------')
            print('- Novo prefeito:', prefeito[1][0], ' Votos:', max,' Partido:',prefeito[1][3])
            print('------------------------------------------------------')
            time.sleep(5) #utilização do temporizador
            totalizacao_ver()

        elif prefeito[2][2] > max:
            max = prefeito[2][2]
            print('--------------------Novo Prefeito-----------------------')
            print('- Novo prefeito:', prefeito[2][0], ' Votos:', max,' Partido:',prefeito[2][3])
            print('------------------------------------------------------')
            time.sleep(5) #utilização do temporizador
            totalizacao_ver()

        elif max == 0:
            print('--------------------Novo Prefeito-----------------------')
            print('Não houve Votos em nenhum prefeito....')
            print('--------------------------------------------------------')
            time.sleep(5) #utilização do temporizador
            totalizacao_ver()
        
        elif prefeito[0][2] >= max:
            max = prefeito[0][2]
            print('--------------------Novo Prefeito-----------------------')
            print('- Novo prefeito:', prefeito[0][0], ' Votos:', max,' Partido:',prefeito[0][3])
            print('------------------------------------------------------')
            time.sleep(5) #utilização do temporizador
            totalizacao_ver()
    
        else:
            
            totalizacao_ver()
            

    
        

    

    
  #função para achar vencedor ou vencedores dos candidatos vereadores  
def totalizacao_ver():
    top = [[vereadores[0][2],'- Votos', 'Vereador:',vereadores[0][0]],[vereadores[1][2],'- Votos', 'Vereador:',vereadores[1][0]],[vereadores[2][2],'- Votos', 'Vereador:',vereadores[2][0]],[vereadores[3][2],'- Votos', 'Vereador:',vereadores[3][0]],[vereadores[4][2],'- Votos', 'Vereador:',vereadores[4][0]],[vereadores[5][2],'- Votos', 'Vereador:',vereadores[5][0]],[vereadores[6][2],'- Votos', 'Vereador:',vereadores[6][0]],[vereadores[7][2],'- Votos', 'Vereador:',vereadores[7][0]],[vereadores[8][2],'- Votos', 'Vereador:',vereadores[8][0]],[vereadores[9][2],'- Votos', 'Vereador:',vereadores[9][0]]]
    top = heapq.nlargest(3, top)
    print('--------------------Novos Vereadores-----------------------')
    if top[0][0] >= 1: 
        print(top[0])
        if top[1][0] >= 1:
            print(top[1])
            if top[2][0] >= 1:
                print(top[2])
        else:
            if top[2][0] >= 1:
                print(top[2])
        

    else:
        print('Não houve Votos em nenhum vereador....')
        print('--------------------------------------------------------')
        
    
    print('-----------------------------------------------------------')
    time.sleep(5) #utilização do temporizador
    exit()


while True:
    menu()