"""
Random Password Generator Module.

This module provides functions to generate secure random passwords
using letters, numbers, and special characters. It also supports
filtering specific characters that should be excluded from the
generated password.

Main functions:
- new_password: Generates a password using all available characters.
- new_filtered_password: Generates a password excluding user-defined characters.
"""

from random import choice, shuffle


# ========================
# CHARACTER SETS
# ========================

letras = [
    "q","w","e","r","t","y","u","i","o","p",
    "a","s","d","f","g","h","j","k","l",
    "z","x","c","v","b","n","m"
]
"""
Global list containing all lowercase letters used for password generation.
"""

numeros = ["1","2","3","4","5","6","7","8","9","0"]
"""
Global list containing numeric characters used for password generation.
"""

caracteres_especiais = ["!","@","#","$","%","&","*","_","+",",",".","/","?"]
"""
Global list containing special characters used for password generation.
"""


# ========================
# FUNCTIONS
# ========================

def new_password(size_letter=4, size_numbers=3, size_special=1, letter_mode="mixer"):
    """
    Generate a random password using letters, numbers, and special characters.

    Args:
        size_letter (int, optional): Number of letters in the password.
            Default is 4.
        size_numbers (int, optional): Number of numeric characters in the password.
            Default is 3.
        size_special (int, optional): Number of special characters in the password.
            Default is 1.
        letter_mode (str, optional): Defines how letters are generated.
            Options:
            - "mixer": mix of uppercase and lowercase letters
            - "upper": all letters in uppercase
            - "lower": all letters in lowercase
            Default is "mixer".

    Returns:
        str: Randomly generated password.

    Raises:
        ValueError: If an invalid letter_mode is provided.
    """
    gen_completo = []

    # LETTER GENERATION
    for _ in range(size_letter):
        gen_letra = choice(letras)

        if letter_mode == "mixer":
            gen_completo.append(
                gen_letra.upper() if choice([True, False]) else gen_letra
            )
        elif letter_mode == "upper":
            gen_completo.append(gen_letra.upper())
        elif letter_mode == "lower":
            gen_completo.append(gen_letra)
        else:
            raise ValueError("Invalid letter_mode")

    # NUMBER GENERATION
    for _ in range(size_numbers):
        gen_completo.append(choice(numeros))

    # SPECIAL CHARACTER GENERATION
    for _ in range(size_special):
        gen_completo.append(choice(caracteres_especiais))

    shuffle(gen_completo)
    return "".join(gen_completo)


def new_filtered_password(
    size_letter=4,
    size_numbers=3,
    size_special=1,
    letter_mode="mixer",
    filter=None
):
    """
    Generate a random password while excluding specified characters.

    This function allows the user to filter out letters, numbers, or
    special characters that should not appear in the generated password.

    Args:
        size_letter (int, optional): Number of letters in the password.
            Default is 4.
        size_numbers (int, optional): Number of numeric characters in the password.
            Default is 3.
        size_special (int, optional): Number of special characters in the password.
            Default is 1.
        letter_mode (str, optional): Defines how letters are generated.
            Options:
            - "mixer": mix of uppercase and lowercase letters
            - "upper": all letters in uppercase
            - "lower": all letters in lowercase
            Default is "mixer".
        filter (list[str], optional): List of characters to be excluded
            from password generation. Default is None.

    Returns:
        str: Randomly generated password with filters applied.

    Raises:
        ValueError:
            - If an invalid letter_mode is provided.
            - If all characters of a required type are removed by the filter,
              making password generation impossible.
    """
    gen_completo = []

    if filter is None:
        filter = []

    # APPLY FILTERS
    filterLetters = [c for c in letras if c not in filter]
    filterNumbers = [c for c in numeros if c not in filter]
    filterSpecials = [c for c in caracteres_especiais if c not in filter]

    # LETTER GENERATION
    if size_letter > 0 and not filterLetters:
        raise ValueError(
            "Impossible to create a password with the current filter!\n"
            "All letters have been removed"
        )

    for _ in range(size_letter):
        gen_letra = choice(filterLetters)

        if letter_mode == "mixer":
            gen_completo.append(
                gen_letra.upper() if choice([True, False]) else gen_letra
            )
        elif letter_mode == "upper":
            gen_completo.append(gen_letra.upper())
        elif letter_mode == "lower":
            gen_completo.append(gen_letra)
        else:
            raise ValueError("Invalid letter_mode")

    # NUMBER GENERATION
    if size_numbers > 0 and not filterNumbers:
        raise ValueError(
            "Impossible to create a password with the current filter!\n"
            "All numbers have been removed"
        )

    for _ in range(size_numbers):
        gen_completo.append(choice(filterNumbers))

    # SPECIAL CHARACTER GENERATION
    if size_special > 0 and not filterSpecials:
        raise ValueError(
            "Impossible to create a password with the current filter!\n"
            "All special characters have been removed"
        )

    for _ in range(size_special):
        gen_completo.append(choice(filterSpecials))

    shuffle(gen_completo)
    return "".join(gen_completo)