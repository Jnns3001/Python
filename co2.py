class  journey:

    def __init__(self, way, kind, passengers):
        self.passengers = passengers
        self.way = way
        self.kind = kind

    def co2(self):
        if self.kind == 1:
            print(str(self.way*self.passengers*0.042) + "kg")
            return
        if self.kind == 2:
            print(str(self.way*self.passengers*0.042) + "kg")
            return
        if self.kind == 3:
            print(str(self.way*self.passengers*0.042) + "kg")
            return
        if self.kind == 4:
            print(str(self.way*self.passengers*0.042) + "kg")
            return
    
way = int(input("Länge des Trips:(in km)"))
kind = int(input("Reiseart:(Auto/Bus/Zug/FLugzeug)"))
passengers = int(input("Menschen die mitkommen:"))
london = journey(way,kind, passengers)
london.co2()