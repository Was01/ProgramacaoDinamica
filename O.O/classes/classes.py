class Fracao:
    def __init__(self,num,dem):
        if dem < 0:
            num = -num
            dem = -dem
        self.numerador = num
        self.denominador = dem
      
    
    def inverter(self):
       return Fracao(self.denominador,self.numerador)
    
    def negar(self):
        return Fracao(-self.numerador,self.denominador)
    
    def mdc(self):
        a=self.numerador
        b=self.denominador
        if a<b:
            a,b=b,a
        r=a%b
        while r!=0:
            a=b
            b=r
            r=a%b
        return b
    
    def simplificar(self):
        r=self.numerador%self.denominador
        if r==0:
            self.numerador=int(self.numerador/self.denominador)
            self.denominador=1
        else:
            mdc=self.mdc()
            self.numerador=int(self.numerador/mdc)
            self.denominador=int(self.denominador/mdc)
        return Fracao(self.numerador,self.denominador)
    
    def somar(self,outra):
        self.numerador=self.numerador*outra.denominador+self.denominador*outra.numerador
        self.denominador=self.denominador*outra.denominador
        return Fracao(self.numerador,self.denominador).simplificar()
    
    def __add__(self,outra):
        return self.somar(outra)
    
    def subtrair(self,outra):
        self.numerador=self.numerador*outra.denominador-self.denominador*outra.numerador
        self.denominador=self.denominador*outra.denominador
        return Fracao(self.numerador,self.denominador).simplificar()
    
    def __sub__(self,outra):
        return self.subtrair(outra)
      
    
    def multiplicar(self,outra):
        self.numerador=self.numerador*outra.numerador
        self.denominador=self.denominador*outra.denominador
        return Fracao(self.numerador,self.denominador).simplificar()
    
    def __mul__(self,outra):
        return self.multiplicar(outra)
    
    def dividir(self,outra):
        return Fracao(self.numerador,self.denominador).multiplicar(outra.inverter()).simplificar()
    
    def __str__(self):
        representation = "{}/{}".format(self.numerador, self.denominador)
        return representation
    
    def __repr__(self):
        representation="Fracao({},{})".format(self.numerador,self.denominador)
        return representation
    

    
a = Fracao(8,16)
b= Fracao(16,8)
d=a.negar()


print(d)
    