# Method 1
# f = open("E:/New folder (2)/repo/27__01_23/text", "w")  # 'r' for reading and 'w' for writing
# f.write("Hello World ")  # Write inside file
# f.close()  # Close file

# Method 2
with open("E:/New folder (2)/repo/27__01_23/text", "w") as file:     # Opens file and casts as file
    file.write("hello world ")      # Writing


