class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    


class BinaryGate(LogicGate):
      def __init__(self,n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

      def getPinA(self):
          return int(input(f"Enter Pin A for gate {self.label} :"))
      
      def getPinB(self):
          return int(input(f"Enter Pin B for gate {self.label} :"))
      
class UnaryGate(LogicGate):
    def __init__(self,n):
        super.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
    

class AndGate(BinaryGate):

    def __init__(self,n):
        super(AndGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0