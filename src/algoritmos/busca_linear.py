def busca_linear(list,elem):
    for i in range(len(list)):
        if list[i] == elem:
            return i 

    return None

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

elem_esc = "Perseverança"



indice =(busca_linear(lista_esquesita,elem_esc))

if indice is not None:
    print(f"achamos o elemento {elem_esc} no indice {indice}!")
else:
    print(f"não encontramos o elemento '{elem_esc}' em nenhum elemento")