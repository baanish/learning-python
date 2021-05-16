import csv

csvReader = csv.reader(open("improvedCreatorInput.csv"))
jsonFile = open("improvedCreatorJSON.json", "w")
jsonFields = []
for inputData in csvReader:
    #use the first line to get the names of the fields
    if(csvReader.line_num != 1):
        #check if first line of value
        if(csvReader.line_num == 2):
            jsonFile.write("{")
        else:
        #add a comma and new line if not first line
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
            #store the names in a list
            jsonFields.append(field)
        jsonFile.write("{ \"data\": [\n")
jsonFile.write("\n]\n}")
