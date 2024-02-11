import cv2
import numpy as np
from zipfile import ZipFile
import os

os.chdir("M0rsearchive")

morse_code_dict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}


def getPassword(path):

    image = cv2.imread(path)

    height, width, _ = image.shape

    background_color = image[0][0]

    password = ""

    for i in range(1, height, 2):
        morse_caracter = ""
        j = 0
        while j < width:

            if not np.array_equal(image[i][j], background_color):
                s = 0
                for l in range(j, width, 1):
                    if  np.array_equal(image[i][l], background_color):
                        break
                    s += 1
                if s == 1:
                    morse_caracter += "."
                else:
                    morse_caracter += "-"
                j = l

            j += 1
        password += morse_code_dict[morse_caracter]

    return password

def extractZip(pathZip, password):
    with ZipFile(pathZip, 'r') as zipFile:
        zipFile.extractall(pwd=bytes(password, 'utf-8'))
        zipFile.close()


def main():

    for archiveNumber in range(999, 0, -1):
        zipName = "flag_" + str(archiveNumber)
        password = getPassword("pwd.png")
        try:
            extractZip(zipName + ".zip", password)
            os.chdir("flag")
        except:
            try:
                extractZip(zipName + ".zip", password.upper())
                os.chdir("flag")
            except:
                print("ERROR"+ " " + str(archiveNumber))
                break



#main()
