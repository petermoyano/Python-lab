#Bad example of how to close a file! If the f.write fails, the file will not be closed!
def manually_calling_close_on_a_file(filename):
    f = open(filename, "w")
    f.write("This is a test\n")
    f.close()


#The with statement will close the file even if an exception occurs!
def good_example_of_how_to_close_a_file(filename):
    with open(filename, "w") as f:
        f.write("This is a test\n")
