import os

test_filelist = os.listdir("./dataset")
test_filelist = [os.path.join("./dataset/", file) for file in test_filelist if file.endswith('.wav')]
print(test_filelist)