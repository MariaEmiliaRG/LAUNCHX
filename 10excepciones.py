def main(): 
    #try:
    #    open("/path/to/mars.jpg")
    #except FileNotFoundError:
    #    print("No se encontró el archivo")

    
    #try:
    #    configuration = open('config.txt')
    # Puedes acceder al error asociado
    #except FileNotFoundError as err:
    #     print("got a problem trying to read the file:", err)
    #except IsADirectoryError:
    #    print("Found config.txt but it is a directory, couldn't read it")
    # Se pueden agrupar excepciones
    #except (BlockingIOError, TimeoutError): 
    #        print("Filesystem under heavy load, can't complete reading configuration file")

    #Partir de un error más genérico y diferenciarlo con el atributo errno 
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")


if __name__ == "__main__": 
    main()