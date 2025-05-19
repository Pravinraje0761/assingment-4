a=str(input("Enter the lines you want to Add to the file :"))
file1=open("sample.txt","w")
file1.write(a)
print("the data is succesfully added to the sample file")
file1.close()


b=str(input("Enter the lines you want to Appened to the file :"))
file1=open("sample.txt","a")
file1.write(b)
print("the data is succesfully added to the sample file")
file1.close()


print("the final content of the file is:")
file1=open("sample.txt","r")
reading_file=file1.read()
print(reading_file)
file1.close()