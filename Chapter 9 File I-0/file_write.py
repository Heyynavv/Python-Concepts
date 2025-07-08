str = "Written using write operations in files"
str1 = "Using with keyword to write a string in a new file"

f = open("myfile.text" , "w")
f.write(str)
f.close

f = open("random.txt" , "w")
f.write(str1)
f.close

