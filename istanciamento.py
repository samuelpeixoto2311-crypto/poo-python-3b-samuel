from app1 import Filme, Serie, Documentario, Podcast
from app2 import Pix, Cartao, Boleto, ValePresente

catalogo = [
    Filme("Jumanji", "Aventura", 367), Filme("King Kong", "Ação", 812),
    Serie("One pice", "Anime", 99 ), Serie("Tung Tung Sahur", "Ação", 67),
    Documentario("Animal PLanet", "Natureza", "Vida Selvagem"), Documentario("Caos total", "Ação", "Documentário"),
    Podcast("Podpa", "Resenha", 67), Podcast("Café com leite", "Conversa", 82)
]

for item in catalogo:
    item.exibir_info()

print("__"*50)
print("\n")



pagamentos = [
Pix(),
Cartao(),
Boleto(),
ValePresente()
]
for pagamento in pagamentos:
    pagamento.processar()