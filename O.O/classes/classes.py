class Fracao:
    def __init__(self,num,dem):
        self.numerador=num
        self.denominador=dem
    
    def inverter(self):
       return Fracao(self.denominador,self.numerador)
    
    def negar(self):
        return Fracao(-self.numerador,self.denominador)
    
    def mdc(self):
        if self.numerador<self.denominador:
            self.numerador,self.denominador=self.denominador,self.numerador
        r=self.numerador%self.denominador
        while r!=0:
            self.numerador=self.denominador
            self.denominador=r
            r=self.numerador%self.denominador
        return self.denominador
    
    def simplificar(self):
        r=self.numerador%self.denominador
        if r==0:
            self.numerador=int(self.numerador/self.denominador)
            self.denominador=1
        else:
            x=Fracao(self.numerador,self.denominador)
            mdc=x.mdc()
            self.numerador=int(self.numerador/mdc)
            self.denominador=int(self.denominador/mdc)
        return Fracao(self.numerador,self.denominador)



a=Fracao(45,90)

a=a.simplificar()

print(a.numerador)
print(a.denominador)

