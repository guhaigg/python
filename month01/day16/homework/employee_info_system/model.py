class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __str__(self):
        return str(self.__dict__)

    def __gt__(self, other):
        return self.money > other.money

    def __eq__(self, other):
        return self.eid == other.eid
