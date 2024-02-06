class Calculadora:
    primer_num,segundo_num,resultado=None,None,None

    def __init__(self,p,s):
        self.primer_num=p
        self.segundo_num=s
    def sumar(self):
        self.resultado=self.primer_num+self.segundo_num
    def restar(self):
        self.resultado=self.primer_num-self.segundo_num
    def multiplicar(self):
        self.resultado=self.primer_num*self.segundo_num
    def dividir(self):
        if self.segundo_num !=0:
            self.resultado=self.primer_num/self.segundo_num
        else:
            self.resultado="División por cero"
    def get_resultado(self):
        return self.resultado
    
casio=Calculadora(30.8,15.1)
casio.sumar()
print(casio.get_resultado())
casio.restar()
print(casio.get_resultado())
casio.multiplicar()
print(casio.get_resultado())
casio.dividir()
print(casio.get_resultado())
