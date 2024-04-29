def inverse(entry):
    if isinstance(entry, int):
        raise ValueError('Vous devez saisir une chaîne de caractères')

    for itm in entry:
        if not isinstance(itm, str):
            raise ValueError('Vous devez saisir une chaîne de caractères')
    
    if isinstance(entry, list) and len(entry) == 4:
        entry.pop()

    entry = "".join(entry)

    return entry[::-1]

if __name__ == "__main__":
    print(inverse('hello'))