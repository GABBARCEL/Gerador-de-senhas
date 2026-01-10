from random import choice, shuffle


letras = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
numeros = ["1","2","3","4","5","6","7","8","9","0"]
caracteres_especiais = ["!","@","#","$","%","&","*","_","+",",",".","/","?"]
### ↑↑↑↑↑  LETRAS ESCOBO GLOBAL, VOCÊ PODE DESCONSIDERALAS CHAMANDO A FUNÇÃO new_filtered_password COM OS PARÂMETROS COMUNS E A LETRA A SER IGNORADA ↑↑↑↑↑


def new_password(size_letter = 4, size_numbers = 3, size_special = 1, letter_mode = "mixer"):
    gen_completo = []
    for l in range(size_letter): 
        gen_letra = choice(letras)
        if letter_mode == "mixer": # MODO MIXER
                    
            if choice([True, False]):
                maiscula = gen_letra.upper()
                gen_completo.append(maiscula)
            else:
                gen_completo.append(gen_letra)
                
        elif letter_mode == "upper": # MODO MAIÚSCULA
            maiscula = gen_letra.upper()
            gen_completo.append(maiscula)
                
        elif letter_mode == "lower": # MODO MINÚSCULA
            gen_completo.append(gen_letra)
        
        else:
                raise ValueError("Invalid letter_mode")


    for n in range(size_numbers): 
        gen_numero = choice(numeros)
        gen_completo.append(gen_numero)


    for c in range(size_special): # PARA GERAR OS CARACTERES ESPECIAIS
        gen_caracter = choice(caracteres_especiais)
        gen_completo.append(gen_caracter)

    shuffle(gen_completo)
    return "".join(gen_completo)

def new_filtered_password(size_letter = 4, size_numbers = 3, size_special = 1, letter_mode = "mixer", filter = None):
    gen_completo = []
    if filter is None:
        filter = []

    # FILTRADOS
    filterLetters = []
    filterNumbers = []
    filterSpecials = []

    # FILTRO LETRAS
    for c in letras:
        if c not in filter:
            filterLetters.append(c)

    # FILTRO NÚMEROS
    for c in numeros:
        if c not in filter:
            filterNumbers.append(c)

    # FILTRO CARACTERES ESPECIAIS
    for c in caracteres_especiais:
        if c not in filter:
            filterSpecials.append(c)

    ###   GERAÇÃO

    # GERAÇÃO DAS LETRAS
    if size_letter > 0 and not filterLetters:
        raise ValueError("Impossible to create a password with the current filter!\nAll letters have been removed")
    
    else:
        for l in range(size_letter):
            gen_letra = choice(filterLetters)
            if letter_mode == "mixer": # MODO MIXER
                        
                if choice([True, False]):
                    maiscula = gen_letra.upper()
                    gen_completo.append(maiscula)
                else:
                    gen_completo.append(gen_letra)
                    
            elif letter_mode == "upper": # MODO MAIÚSCULA
                maiscula = gen_letra.upper()
                gen_completo.append(maiscula)
                    
            elif letter_mode == "lower": # MODO MINÚSCULA
                gen_completo.append(gen_letra)

            else:
                raise ValueError("Invalid letter_mode")

    # GERAÇÃO DE NÚMEROS
    if size_numbers > 0 and not filterNumbers:
        raise ValueError("Impossible to create a password with the current filter!\nAll numbers have been removed")
    
    else:
        for l in range(size_numbers):
            gen_numero = choice(filterNumbers)
            gen_completo.append(gen_numero)

    
    # GERAÇÃO DE CARACTERES ESPECIAIS
    if size_special > 0 and not filterSpecials:
        raise ValueError("Impossible to create a password with the current filter!\nAll special characters have been removed")
    
    else:
        for l in range(size_special):
            gen_especial = choice(filterSpecials)
            gen_completo.append(gen_especial)

    shuffle(gen_completo)
    return "".join(gen_completo)