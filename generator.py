from random import choice, shuffle

letras = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
numeros = ["1","2","3","4","5","6","7","8","9","0"]
caracteres_especiais = ["!","@","#","$","%","&","*","_","+"]

def gerar_sequencia(Size_letter = 4, Size_numbers = 3, Size_special = 1, letter_mode = "mx"):
    gen_completo = []
    for l in range(Size_letter): # PARA GERAR AS LETRAS
        gen_letra = choice(letras)
        if letter_mode == "mx": # MODO MIXER
            
            if choice([True, False]):
                maiscula = gen_letra.upper()
                gen_completo.append(maiscula)
            else:
                gen_completo.append(gen_letra)
        
        elif letter_mode == "+": # MODO MAIÚSCULA
            maiscula = gen_letra.upper()
            gen_completo.append(maiscula)
        
        elif letter_mode == "-": # MODO MINÚSCULA
            gen_completo.append(gen_letra)


    for n in range(Size_numbers): # PARA GERAR OS NÚMEROS
        gen_numero = choice(numeros)
        gen_completo.append(gen_numero)


    for c in range(Size_special): # PARA GERAR OS CARACTERES ESPECIAIS
        gen_caracter = choice(caracteres_especiais)
        gen_completo.append(gen_caracter)

    shuffle(gen_completo)
    return "".join(gen_completo)
    
print(gerar_sequencia(5,3,1,"mx")) 