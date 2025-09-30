def split(species):
    vowals = "aeiouAEIOU"
    prefix = ""

    for char in species:
        if char not in vowals:
            prefix += char
        else:
            break
    suffix = species[len(prefix):]
    return prefix,suffix

def hybridize(species1, species2):
    prefix1, suffix1 = split(species1)
    prefix2, suffix2 = split(species2)
    hybrid1 = prefix1 + suffix2
    hybrid2 = prefix2 + suffix1
    return hybrid1, hybrid2
