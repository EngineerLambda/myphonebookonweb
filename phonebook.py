phonebook = {"A":92965079  , "B" :929650798, "C":819876545,  "D":234567897, "E":907873, "F":907873,"G" :907873, "H":907873, "I":907873}
    


def Create(name, number):
    if name not in phonebook:
        phonebook[name] = {number}
        print(f"saved,  {name}:{number}" )
    else:
        print("you might have make a mistake")



def Delate(name):
     if name in phonebook:
        phonebook.pop(name)
        print(f"deleted,{'name'}:{'number'}")
     else:
        print("No deleted item found")



def update(name = phonebook.keys, number = phonebook.values):
    if name in phonebook:
        phonebook[name]
        print(f'UPDATED SUCCESSFUL {name},{number}')
    else:
        print('FAILED TO UPDATE')


def search(name):
    if name in phonebook:
        phonebook[name]
        print(f'SEEN  , {name}:{phonebook[name]}')
    else:
        print('NOT FOUND')


def blocked(name = dict.keys in phonebook):
 if name in phonebook:
    phonebook, dict.keys
    print(f"BLOCKED, {name} ")
 else:
    print("Not Found")

def all_contact():
    print(phonebook)


Create("mummy",  78929)
Delate("A")
update('B', 200000000)
search('D')
blocked('C')
all_contact()
    













#print(phonebook)