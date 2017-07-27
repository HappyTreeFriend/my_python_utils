#!/usr/bin/env python
#-*-coding:utf-8-*-
#Created by happytree on 28/3/17.
#Description : File operation, including Read

class MyFile(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def _open(self, mode="r"):
        self.fp = open(self.file_path, mode)
        self.file_name = self.fp.name

    def read(self):
        self._open("r")
        file_content = self.fp.read()
        self.fp.close()
        return file_content

    def write(self, content):
        self._open("w")
        self.fp.write(content)
        self.fp.close()

    def close(self):
        self.fp.close()

if __name__ == "__main__":
    my_file = MyFile("__init__.py")
    print my_file.read()