import os

def getStudentNames():
    folder = './photo/train'

    names = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

    textfile  = open("names.txt", "w")
    for element in names:
        textfile.write(element + "\n")
    textfile.close()

    return names
