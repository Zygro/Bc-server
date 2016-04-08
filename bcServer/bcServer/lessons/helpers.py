import difflib

def compare_files(file1, file2):
    print(type(file2) is str)
    print(file2)
    text1 = file1.read()
    text2 = file2.read()


    return (' '.join(str(text1)) == ' '.join(str(text2)))
