import csv
def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    dict1=dict()
    lista1=[]
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                for item in row:
                    cantidad=item.count(";")
                    ultpos=0
                    cont=0
                    while cont<cantidad:
                        lista1=[]
                        posición=ultpos+item[ultpos::].find(";")
                        producto=item[ultpos:posición]
                        division=producto.find(":")
                        lista1.append(int(producto[division+1:]))
                        if producto[0:division] not in dict1:
                            dict1[producto[0:division]]=lista1
                        else:
                            dict1[producto[0:division]]+=lista1
                        ultpos=posición+1
                        cont+=1
            return dict1
    except FileNotFoundError:
        print("Error: The file does not exist.")
        raise

productos=read_file_to_dict("datos.csv")

def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto in data:
        total=0.00
        cont=0
        for valores in data[producto]:
            total+=valores
            cont+=1
        promedio=total/cont
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
        
process_dict(productos)
