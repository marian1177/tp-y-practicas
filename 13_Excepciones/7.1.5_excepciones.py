dic = {
    "alumnoA": "luis",

    "alumnoB": "tomi",

    "alumnoC": "lucas",

}


print(dic)


try:
    print(dic['alumnoa'])
except KeyError:
    print("error de clave")
