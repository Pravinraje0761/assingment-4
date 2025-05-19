
try:
    file1 = open("sample.txt", "r")
    print("reading file")
    reading_file = file1.readline()
    print("reading line one: ", reading_file)
    reading_file2 = file1.readline()
    print("reading line two: ", reading_file2)
    file1.close()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")



