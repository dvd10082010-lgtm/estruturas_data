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
