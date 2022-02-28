from operaciones import * 
def validacion(hora):
    horas = 0
    minutos = 0
    tamaño = len(hora)
    if tamaño == 5:
        if hora[0].isalpha()  or hora[1].isalpha()  or hora[3].isalpha() or hora[4].isalpha():
            print("Contiene letras por ende  termino")
        else:
            horas = hora[0:2]
            minutos = hora[3:5]
    elif  tamaño == 4:
        if hora[1] == ":":
            if hora[0].isalpha()  or hora[2].isalpha() or hora[3].isalpha():
                print("Contiene letras por ende  termino")
            else:
                horas = hora[0]
                minutos = hora[2:4]
        else:
            if hora[0].isalpha()  or hora[1].isalpha() or hora[3].isalpha():
                print("Contiene letras por ende  termino")
            else:
                horas = hora[0:2]
                minutos = hora[3]
    else:
        print("Utilizamos el estandar de 24 horas: HH:MM")
    print(horas, minutos)
    positivos(horas,minutos)
def positivos(horas,minutos):
    phoras = int(horas)
    pminutos = int(minutos)
    if phoras < 0:
        print("No pueden haber horas negativas")
    elif pminutos < 0:
        print("No pueden haber minutos negativos")
    elif phoras == 0 and pminutos == 0:
        print("x")
    else:
        ingresarDatos(phoras, pminutos)