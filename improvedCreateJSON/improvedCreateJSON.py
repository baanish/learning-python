import csv

csvReader = csv.reader(open("improvedCreatorInput.csv"))
jsonFile = open("improvedCreatorJSON.json", "w")
jsonFields = []
readFirstLine = False
for inputData in csvReader:
    if(readFirstLine) :
        if(csvReader.line_num == 2):
            jsonFile.write("{")
        else:
            jsonFile.write(" ,\n{")
        i = 0
        for value in inputData:
            if(i != len(inputData) - 1) :
                jsonFile.write("\"" + jsonFields[i] + "\":\"" + value + "\" ,")
            else :
                jsonFile.write("\"" + jsonFields[i] + "\":\"" + value + "\" }")
            i = i + 1
    else :
        for field in inputData:
            jsonFields.append(field)
            readFirstLine = True
        jsonFile.write("{ \"data\": [\n")
jsonFile.write("\n]\n}")

