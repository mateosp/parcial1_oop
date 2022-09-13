from curses.ascii import isupper
from email.headerregistry import ContentDispositionHeader
from msilib.schema import Class
from signal import strsignal
from typing_extensions import Self


class Password():
    def __init__(self, password: str):
        self.password = password
    

class Verification(Password):
    def __init__(self, lowerC: str, upperC: str, minimum: int, maximum: int) -> None:
        self.lowerC = lowerC
        self.upperC = upperC
        self.minimum = minimum
        self.maximum = maximum

    def Minimum(self):
        self.minimum = 5
        if (len(self.password) < self.minimum):
            print ("El minimo numero de caracteres es de 5")
    
    def Maximum(self): 
        self.maximum = 15
        if (len(self.maximum) > self.maximum):
            print ("El maximo numero de caracteres es de 15")
    
    def UpperLowerC(self):
        self.password 
        self.caracteres_presente = False
        for caracter in self.password:
            if (caracter.isupper() and caracter.islower()):
                self.caracteres_presente = True
            else: 
                print("La contraseña debe contener mayusculas y minusculas")

    


    



