# Compiled by Mihai Boicu based on code created by:
# 2021 July-August
# - David Liu (a1.py, a2.py gc processing)
# - Anish Malik (a3.py - qr processing) 
# 2022 March-
# - Anushree Manoharrao (session-key.py - documentation,comments)s 

"""
Understanding of the class Session Key - By Anushree Manoharrao
If the sessionskey.txt file exists, then the function “load” is executed. It reads the file line by line, splitting them based on space and 
storing each line to a dictionary where the former part is the key to the latter part.
Else, generate and save functions are executed in that order. 
The “generate” function uses the session-config.json file to generate the sessionkey.txt file. 
It opens and loads the json file. Generates the sessionkeys for the duration mentioned in the start_year and end_year of json file, e.g., from 2000 to 2030. 
It generates two values and is stored as a dictionary using the below technique. The first value which is the anonymizing the year is generated by performing (year*100) +sem. 
Second value which is a key to each year is generated by adding the previous key to a randomly generated integer between the defined range of minstep and maxstep,
incrementing it for every year in that order. 
The generated dictionary is saved by executing the “save” function. It creates a new file by writing to sessionkeys.txt file by reading from the dictionary generated. 
It appends the key and values using a space to the txt file. 

"""

# Session Anonymization Key

class SessionKey:
    keyFileName = "../key/sessionKeys.txt"
    configFileName = "../config/session-config.json"

    dictionary = {}

    def load(self):
        file = open(self.keyFileName)
        lines = file.readlines()
        for line in lines:
            sessions = line.split(" ")
            self.dictionary[int(sessions[0])] = int(sessions[1])
        file.close()

    def save(self):
        # print("No session keys file found, creating new file!")
        file = open(self.keyFileName, "w")
        for keyName in sorted(self.dictionary.keys()):
            file.write(str(keyName) + " " + str(self.dictionary[keyName]) + "\n")
        file.close()

    def generate(self):
        configFile = open(self.configFileName,)
        configData = json.load(configFile)

        startYear = configData['start_year']
        endYear = configData['end_year']
        lastKey = configData['start_key']
        minStep = configData['min_step']
        maxStep = configData['max_step']
        semesters = configData['semesters_list']

        for i in range(startYear,endYear+1):
            for sem in semesters:
                self.dictionary[(i*100+sem)] = lastKey
                lastKey += random.randint(minStep, maxStep)

        # print("lastKey: ",lastKey)
        # print("sessionDict: ", sessionDict)

    def __init__(self):
        if os.path.isfile(self.keyFileName):
            self.load()
        else:
            self.generate()
            self.save()

            
