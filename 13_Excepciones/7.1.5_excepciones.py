dic = {
    "alumnoA": "luis",

    "alumnoB": "tomi",

    "alumnoC": "lucas",

}


print(dic)


try:
    print(dic['alumnoa'])
    if not dic['alumno']:
        raise KeyError ("clave erronea")

except KeyError:
    print(KeyError)
