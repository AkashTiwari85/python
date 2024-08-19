class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
       print(f"The name of employee:{self.id} is {self.name}")

       e=Employee("tiwari",5)
       e.showDetails()
