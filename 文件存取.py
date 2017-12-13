import pickle
try:
    with open("f:/1.txt","wb") as out:
        names = ["jack","london",["son","children"],"help"]
        pickle.dump(names,out)
except IOError as err:
    print("file error:"+str(err))
except pickle.PicklkleError as perr:
    print("PickleError:"+str(perr))

try:
    with open("f:/1.txt","rb") as reader:
        renames = pickle.load(reader)
        print(renames)
except IOError as erri:
    print("file error:"+str(erri))
except pickle.PickleError as errp:
    print("pickle error:"+str(errp))

