from random import randrange

continua = "S"
while continua == "S" or continua == "s":
    lista = [1, 2, 3, 4, "X", 6, 7, 8, 9, 10]
    numero = [1, 2, 3, 4, "X", 6, 7, 8, 9, 10]
    
    def msgd():
        print("Você perdeu!")
        
    def msgv():
        print("Você ganhou!")
    
    def tabuleiro():
        
        print(" +-------+-------+-------+ \n \
|       |       |       | \n \
|   ",lista[0],"   |   ",lista[1],"   |   ",lista[2],"   | \n \
|       |       |       | \n \
+-------+-------+-------+ \n \
|       |       |       | \n \
|   ",lista[3],"   |   ",lista[4],"   |   ",lista[5],"   | \n \
|       |       |       | \n \
+-------+-------+-------+ \n \
|       |       |       | \n \
|   ",lista[6],"   |   ",lista[7],"   |   ",lista[8],"   | \n \
|       |       |       | \n \
+-------+-------+-------+", sep="")
    
    def jogada():
        x = False
        while x == False:
            try:
                a = int(input("Digite o número de sua jogada: "))
                if lista[a-1] == "O" or lista[a-1] == "X":
                    print("-Número já jogado")
                    raise
                else:
                    lista[a-1] = "O"
                    numero[a-1] = "J"
                x = True
            except:
                print("-Digite um número válido")
            
    
    def bot():
        for i in range(300):
            random = randrange(10)
            if random in numero:
                lista[random-1] = "X"
                numero[random-1] = "J"
                break
            else:
                continue
            
    def venceu():
        vit = ['O', 'O', 'O']
        if lista[0:3] == vit or lista[6:9] == vit:
            msgv()
            return True
        elif lista[0] == 'O' and lista[3] == 'O' and lista[6] == 'O':
            msgv()
            return True
        elif lista[2] == 'O' and lista[5] == 'O' and lista[8] == 'O':
            msgv()
            return True
        else:
            der = ['X', 'X', 'X']
            if lista[0:3] == der or lista[6:9] == der or lista[3:6] == der:
                msgd()
                return True
            elif lista[0] == 'X' and lista[3] == 'X' and lista[6] == 'X':
                msgd()
                return True
            elif lista[2] == 'X' and lista[5] == 'X' and lista[8] == 'X':
                msgd()
                return True
            elif lista[0] == 'X' and lista[4] == 'X' and lista[8] == 'X':
                msgd()
                return True
            elif lista[2] == 'X' and lista[4] == 'X' and lista[6] == 'X':
                msgd()
                return True
            else:
                for i in range(1,10):
                    if i in lista:
                        return False
                else:
                    print("Empatou!")
                    return True
            
    tabuleiro()
    while venceu() == False:
        venceu()
        if venceu() == True:
            break
        jogada()
        tabuleiro()
        venceu()
        if venceu() == True:
            break
        bot()
        tabuleiro() 
    
        
    continua = input("Deseja continuar?(S/N) ")
    continua = continua.upper
    
    while continua != "S" and continua != "N":
        continua = input("Deseja continuar?(S/N) ")
        continua = continua.upper()



