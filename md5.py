'''Finds the md5 and sha1 values of the input .txt file'''
import hashlib

filename = input("Enter the file name: ")
with open(filename, "rb") as f:
    text_file = f.read()  # read file as text_file
    md5_hash = hashlib.md5(text_file).hexdigest()
    print(md5_hash)
    sha_hash = hashlib.sha1(text_file).hexdigest()
    print(sha_hash)
