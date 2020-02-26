import re

automovel = {}

def readFile(file):
    data = file.readlines()
    

    if re.search("Categoria", data [0]):
        automovel['name'] = data[3]
    else:
        automovel['name'] = data[0]

    index = 0
    for row in data:

        if re.search("ANO\n", row.upper()):
            automovel['ano'] = data[index+1]
        elif re.search("COR\n", row.upper()):
            automovel['cor'] = data[index+1]
        elif re.search("KM", row.upper()):
            automovel['km'] = data[index+1]
        elif re.search("QUILOMETRAGEM", row.upper()):
            automovel['km'] = data[index+1]
        elif re.search("MOTOR\n", row.upper()):
            automovel['motor'] = data[index+1]
        elif re.search("MOTOR: ", row.upper()):
            result = re.split("\s",row)
            automovel['motor'] = result[9]
        index += 1
     
    return automovel