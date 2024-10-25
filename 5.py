f = open("demofile3.txt", "w")
f.write("Now the file has more content!")
f.close()


f = open("demofile3.txt", "r")
print(f.read())
f.close()

