class Vehicle:
    __registrationNumber = None
    __model = None
    __color = None

    def __init__(self, registrationNumber, model, color):
        self.__registrationNumber = registrationNumber
        self.__model = model
        self.__color = color
    
    def getRegistrationNumber(self):
        return self.__registrationNumber 