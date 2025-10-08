pregunta= input("Introduce el correo electrónico: ")
usuario= pregunta.split("@")[0]
nuevocorreo= usuario  + "@ceu.es"
print(f"El correo nuevo es: {nuevocorreo}")