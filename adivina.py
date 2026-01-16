# Juego de Adivina el Número
# Creado por: Samuel Martinez 
# Versión: 2.0 (Con dificultad añadida)

import random

def juego_adivinanza():
    print("=======================================")
    print("   ¡BIENVENIDO A ADIVINA EL NÚMERO!    ")
    print("=======================================")
    print("Tienes 7 VIDAS para adivinar el número del 1 al 100.")
    print("=======================================")

    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 7  # 💀 Definimos el límite de vidas

    while True:
        # Mostramos cuántas vidas le quedan
        vidas_restantes = max_intentos - intentos
        print(f"\n❤️ Vidas restantes: {vidas_restantes}")

        usuario_dice = input("¿Cuál es el número?: ")

        try:
            numero_usuario = int(usuario_dice)
        except ValueError:
            print("❌ Error: ¡Solo números por favor!")
            continue

        intentos = intentos + 1

        # 1. Revisamos si GANÓ
        if numero_usuario == numero_secreto:
            print(f"\n🎉 ¡GANASTE! El número era {numero_secreto}.")
            print(f"🏆 Te sobraron {max_intentos - intentos} vidas.")
            break
        
        # 2. 💀 Revisamos si PERDIÓ (Game Over)
        if intentos >= max_intentos:
            print(f"\n💀 GAME OVER. Se te acabaron las vidas.")
            print(f"El número secreto era: {numero_secreto}")
            break

        # 3. Si no ganó ni perdió, damos pistas
        if numero_usuario < numero_secreto:
            print("🔼 ¡Más alto!")
        elif numero_usuario > numero_secreto:
            print("🔽 ¡Más bajo!")

juego_adivinanza()