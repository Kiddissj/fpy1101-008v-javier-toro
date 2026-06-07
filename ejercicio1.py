senior = 0
junior = 0
while True:
    try:
        print("¿Cuantos medicos desea ingresar?")
        c_med=int(input())
        
        if c_med <=0:
            print("¡Registro medico invalido! Ingresa un entero positivo para continuar")
        else:
            break
    except:
        print("¡Registro medico invalido! Ingresa un entero positivo para continuar")

for e in range(c_med):
    print(f"MEDICO NUMERO {e+1}")
    while True:
        print("ingrese el nombre del medico (min. 6 caracteres y sin espacios)")
        n_med = input()
        if len(n_med) < 6 or (" " in n_med):
            print("El nombre no debe contener mas de 6 caracteres ni tampoco espacios")
        else:
            break
    while True:
        try:
            print("Ingrese los años de experiencia del profesional")
            a_exp = int(input(""))
            if a_exp < 0:
                print("¡Error clinico! Ingresa un numero entero positivo para continuar")
            else:
                break
        except:
             print("¡Error clinico! Ingresa un numero entero positivo para continuar")

    if a_exp <= 5:
        junior = junior + 1
    if a_exp > 5:
        senior = senior + 1 

print(f"¡El hospital cuenta con {senior} Especialistas Senior y {junior} Residentes Junior! ¡Sistema listo para operar!")
