#To anonymize the users this class is used. 
class UserKey:
    configFileName = "../config/user-config.json"
    keyFileName = "../key/userKeys.txt"
    minUserCode=None
    maxUserCode=None

    dictionary = {}

#reads the json file and sets minuser code and maxuser code based on the values defined in the json file
    def loadConfig(self):
        userConfigFile = open(self.configFileName)
        userConfigData = json.load(userConfigFile)
        self.minUserCode = userConfigData['min_key']
        self.maxUserCode = userConfigData['max_key']
        userConfigFile.close()

#Loads the userskey.txt by reading the file line by line and storing it into a dictionary as key value pairs
    def load(self):
        # print("Grabbing User Keys!")
        file = open(self.keyFileName)
        lines = file.readlines()
        for line in lines:
            elements = line.split(' ')
            self.dictionary[(elements[0])] = int(elements[1])
        file.close()

#The file read above is saved by sorting the keys and then combining keys and values to a single item back to the userkeys.txt
    def save(self):
        file = open(self.keyFileName, "w")
        for keyName in sorted(self.dictionary.keys()):
            file.write(str(keyName) + " " + str(self.dictionary[keyName]) + "\n")
        file.close()

#If it has a userskey.txt file, it executes the load function
    def __init__(self):
        self.loadConfig()
        if os.path.isfile(self.keyFileName):
            self.load()

#To generate an id, it first checks if the section is already present, if it is present the same id has been returned. 
#If not a new value is generated by capturing a random integer value betweeen the min and max user codes. It checks if that random value is present in the dictionary, the value is set  to be new code if it is present. 
    def get(self, id):
        # check if section already used in sectionDict
        if id in self.dictionary.keys():
            return self.dictionary[id]
        # define new code              
        while True:
            code = random.randint(self.minUserCode, self.maxUserCode)
            if not code in self.dictionary.values():
                break
        self.dictionary[str(id)] = code
        return code

#The new abonymized values of ids are then printed in the userkey.txt file
    def print(self):
        print("*****")
        print("*** USER KEY")
        print("*** User Key Config ***")
        print("Min User Code: "+str(self.minUserCode))
        print("Max User Code: "+str(self.maxUserCode))
