class Pagamento:
    def processar(self):
        print("Processando pagamento")

class Pix(Pagamento):
    def processar(self):
        print("Pagamento via PIX")

class Cartao(Pagamento):
    def processar(self):
        print("Pagamento via cartao")

class Boleto(Pagamento):
    def processar(self):
        print("Pagamento via boleto")

class ValePresente(Pagamento):
    def processar(self):
        print("Pagamento via ValePresente")