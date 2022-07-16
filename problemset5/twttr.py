def shorten(x):
    for letter in x:
        if letter in ("A","a","E","e","I","i","O","o","U","u"):
            x=x.replace(letter,"")
    return x


