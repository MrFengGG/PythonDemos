try:
    with open("e:/1.txt","w") as out:
        print("你好啊,python",file=out)
except IOError as err:
    print("File error:"+str(err))
