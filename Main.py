from lista_encadeada import LinkedList 

Llist = LinkedList()

lista_esquesita = [
    "Aceitação", "Afeto", "Alegria", "Altruísmo", "Amizade", 
    "Amor", "Aprendizado", "Autenticidade", "Autonomia", "Bondade", 
    "Calma", "Capacidade", "Caridade", "Companheirismo", "Compaixão", 
    "Compreensão", "Confiança", "Conhecimento", "Cooperação", "Coragem", 
    "Criatividade", "Cuidado", "Determinação", "Disciplina", "Empatia", 
    "Equilíbrio", "Espiritualidade", "Ética", "Família", "Foco", 
    "Generosidade", "Gratidão", "Honestidade", "Honra", "Humildade", 
    "Integridade", "Justiça", "Lealdade", "Liberdade", "Otimismo", 
    "Paciência", "Perseverança", "Respeito", "Responsabilidade", "Segurança", 
    "Sinceridade", "Solidariedade", "Tolerância", "Transparência", "União"
]

Llist.transform(lista_esquesita)  
Llist.append_node("Unção")
x = Llist.get(50)

from algoritmos.busca_binária import busca_binaria

print(busca_binaria(lista_esquesita, "Amor"))