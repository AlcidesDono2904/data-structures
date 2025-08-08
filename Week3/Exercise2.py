import pickle #library for binary files.
from typing import Any

# Path of the file
FILE = "dictionary.dat"
#TODO: change dict to list of dicts
def saveBinaryDictionary(dictionary: list[dict[Any,Any]]) -> None:
    with open (file = FILE, mode = "wb") as file :
        pickle.dump(dictionary, file)
    print ("Data saved to binary file.")
    
def loadBinaryDictionary() -> list[dict[Any,Any]]:
    try:
        with open (file = FILE, mode = "rb") as file:
            dictionary = pickle.load(file)
            return dictionary
    except FileNotFoundError:
        print("No file found.")
        return [{}]
  
if __name__ == "__main__":
    list_of_dicts = [ 
     {"a":"10", "b":"20"}, 
     {"c":"30", "d":"40"}, 
     {"e":"50", "f":"60"} 
    ]
    
    print ("Saving the list of dicts...")
    saveBinaryDictionary(list_of_dicts)
    
    loaded_list = loadBinaryDictionary()
    print (loaded_list)