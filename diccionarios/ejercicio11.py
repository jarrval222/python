datos = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

lineas = datos.split('\n')
claves = lineas[0].split(';')
directorio = {}

for linea in lineas[1:]:
    valores = linea.split(';')
    nif = valores[0]
    info = {
        claves[1]: valores[1],
        claves[2]: valores[2],
        claves[3]: valores[3],
        claves[4]: float(valores[4])
    }
    directorio[nif] = info

print(directorio)