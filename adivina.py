import random  # Traemos la herramienta para generar números aleatorios

def juego_adivinanza():
    print("=======================================")
    print("   ¡BIENVENIDO A ADIVINA EL NÚMERO!    ")
    print("=======================================")
    print("Estoy pensando en un número del 1 al 100...")

    # 1. La computadora elige un número al azar
    numero_secreto = random.randint(1, 100)
    intentos = 0

    # 2. Iniciamos un bucle infinito (se repite hasta que ganemos)
    while True:
        # Pedimos el número al usuario
        usuario_dice = input("¿Cuál crees que es?: ")

        # Convertimos el texto a número entero
        try:
            numero_usuario = int(usuario_dice)
        except ValueError:
            print("❌ Error: ¡Por favor ingresa solo números!")
            continue # Vuelve al inicio del bucle

        intentos = intentos + 1  # Sumamos un intento

        # 3. Lógica de decisión (Comparaciones)
        if numero_usuario < numero_secreto:
            print("🔼 ¡Más alto! Busca un número mayor.")
        
        elif numero_usuario > numero_secreto:
            print("🔽 ¡Más bajo! Te pasaste.")
        
        else:
            # Si no es mayor ni menor, ¡es igual! (Ganaste)
            print(f"🎉 ¡FELICIDADES! Adivinaste el número {numero_secreto}.")
            print(f"🏆 Te tomó {intentos} intentos.")
            break  # Rompemos el bucle para terminar el juego

# Ejecutamos la función
juego_adivinanza()