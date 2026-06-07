l_disponibles = 120
h_libros      = 0

while True:
    print(" ")
    print("=== MENU PRINCIPAL===")
    print("1. Libros disponibles")
    print("2. Reservar libros")
    print("3. Devolver Prestamo")
    print("4. Historial de prestamo")
    print("5. Salir")
    print(" ")
    
    try: 
        print(" ")
        print("Ingresa una opcion")
        opcion = int(input())
        
        if opcion >5 or opcion <0:
            print(" ")
            print("Porfavor ingresa una de las opciones indicadas")

        elif opcion == 1:
            print(" ")
            print(f"La cantidad de libros disponibles es {l_disponibles}")

        elif opcion == 2:
            while True:
                try:
                    print(" ")
                    print("¿Cuantos libros desea reservar?")
                    reserva = int(input())
                    if reserva <= 0:
                        print(" ")
                        print("Debes ingresar un numero entero positivo para continuar")
                    elif reserva > l_disponibles:
                        print(" ")
                        print(f"la cantidad de libros no puede ser mayor a {l_disponibles}")
                    else:
                        print(" ")
                        print("Reserva hecha con exito")
                        l_disponibles = l_disponibles - reserva 
                        h_libros = h_libros + reserva
                        break
                except:
                    print(" ")
                    print("Debes ingresar un numero entero positivo para continuar")
        elif opcion == 3:
            while True:
                try:
                    print(" ")
                    print("¿Cuantos libros desea devolver?")
                    dev = int(input())
                    if dev <0:
                        print(" ")
                        print("Debes ingresar un numero entero positivo para continuar")
                    elif dev > 120:
                        print(" ")
                        print("La cantidad a devolver no puede superar la cantidad maxima de la biblioteca (120)")
                    elif l_disponibles + dev > 120:
                        l_disponibles = 120
                        print(" ")
                        print("Devolucion hecha con exito")
                        break
                    else:
                        print(" ")
                        print("Devolucion hecha con exito")
                        l_disponibles = l_disponibles + dev
                        h_libros = h_libros - dev
                        break
                except:
                    print(" ")
                    print("Debes ingresar un numero entero positivo para continuar")
        elif opcion == 4:
            print(" ")
            print(f"La cantidad de reservas activas son {h_libros}")
        elif opcion == 5:
            print(" ")
            print("Gracias por utilizar el software, hasta la proxima")
            break
    except:
        print(" ")
        print("Debes ingresar un numero entero positivo para continuar")
