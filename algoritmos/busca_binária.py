def busca_binaria(arr, elem):
    less = 0 
    more = len(arr) - 1

    while less <= more:
        mid = (more + less) // 2
        sup = arr[mid] 
        
        if sup == elem:
            return mid
        if sup > elem:
            more = mid - 1  # Corrigido: move o limite superior para a esquerda
        else:
            less = mid + 1  # Corrigido: move o limite inferior para a direita
            
    return None

array = [
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
