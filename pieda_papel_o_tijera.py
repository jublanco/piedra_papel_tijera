# importamos la libreria random
import random

#Definimos las variables
game_list = ["Piedra", "Papel", "Tijera"]
computer = c = 0
nombre = input("Ingrese tu nombre: ")
player = p = 0

# Le decimos que vaya imprimiendo el puntaje de cada uno
print("Puntaje: Computer: " + str(c))
print("Puntaje: " + nombre + ": " + str(p))

#El loop
run = True
while run:
    computer_choice = random.choice(game_list)
    player = input("Piedra, Papel, Tijera o Quit para salir: ")
    if player == computer_choice:
        print("Empate")
    elif player == "Piedra":
        if computer_choice == "Tijera":
                print("Gana " + nombre)
                p += 1
        else:
            print("Gana computer")
            c += 1
    elif player == 'Papel':
        if computer_choice == 'Piedra':
                print("Gana "+ nombre)
                p += 1
        else:
            print("Gana computer")
            c += 1
    elif player == "Tijera":
        if computer_choice == "Papel":
                print("Gana "+ nombre)
                p += 1
        else:
            print("Gana computer")
            c += 1
    elif player == "Quit":
        break
    else:
        print("Comando equivocado!!")

    print(nombre +": " + player)
    print("Computer: " + computer_choice)
    print("")
    print("Puntaje: Computer: " + str(c))
    print("Puntaje: " + nombre + ": " + str(p))
    print("")