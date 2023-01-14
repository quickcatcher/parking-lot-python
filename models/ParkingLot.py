class ParkingLot:
    def __init__(self, totalCapacity):
        self.totalCapacity = totalCapacity
        self.currentCapacity = 0
        self.vehiclesParked = []
    
    def parkVehicle(self, vehicle):
        if(self.currentCapacity>=self.totalCapacity):
            return "Sorry the Parking lot is full"
        
        self.currentCapacity+=1
        self.vehiclesParked.append(vehicle)
        return "Vehicle parked successfully"
    
    def unparkVehicle(self, vehicle):
        regno = vehicle.getRegistrationNumber()
        vehicleToUnpark = None
        for i in self.vehiclesParked:
            if(i.getRegistrationNumber() == regno):
                vehicleToUnpark = i
                break
        
        if(vehicleToUnpark == None):
            return "This vehicle is not parked here"
        else:
            self.vehiclesParked.remove(vehicleToUnpark)
            self.currentCapacity-=1
            return "Vehicle unParked successfully"
    
    def showParkingLot(self):
        displayList = []
        for i in self.vehiclesParked:
            displayList.appand(i.getRegistrationNumber)
        return displayList