import re
automovel = {}

def readFile(file):
    data = file.readlines()
    

    if re.search("Categoria", data [0]):
        automovel['nome'] = data[3]
    else:
        automovel['nome'] = data[0]

    index = 0
    for row in data:
        if re.search("ANO\n", row.upper()):
            automovel['ano'] = re.sub('\s','',data[index+1])
        elif re.search("COR\n", row.upper()):
            automovel['cor'] = re.sub('\n','',data[index+1])
        elif re.search("KM", row.upper()):
            automovel['km'] = re.sub('\n','',data[index+1])
        elif re.search("QUILOMETRAGEM", row.upper()):
            automovel['km'] = re.sub('\n','',data[index+1])
        elif re.search("MOTOR\n", row.upper()):
            automovel['motor'] = re.sub('\n','',data[index+1])
        elif re.search("MOTOR: ", row.upper()):
            result = re.split("\s",row)
            automovel['motor'] = result[9]
        index += 1


    return automovel