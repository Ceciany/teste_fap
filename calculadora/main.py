class Calculadora:

    def __init__(self,n1=10, n2=10):
        self.n1 = n1
        self.n2 = n2
    
    def somar (self,n1,n2):
        return n1+n2
    
    def subtrair (self,n1,n2):
        return n1-n2
    
    def multiplicar (self,n1,n2):
        return n1*n2
    
    def dividir (self,n1,n2):
        return n1/n2
    
calc = Calculadora()
print(calc.somar(5,2))
print(calc.subtrair(5,2))
print(calc.multiplicar(5,2))
print(calc.dividir(5,2))