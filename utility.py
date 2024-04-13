from os import path

def getpath():
    '''get path of current directory'''
    return path.dirname(path.abspath(__file__))

