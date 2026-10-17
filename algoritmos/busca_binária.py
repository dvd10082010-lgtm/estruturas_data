def busca_binaria(arr,elem):
    less = 0 
    more = len(arr) - 1

    while less <= more:
        # o looping fica responsável por atualidade os valores de more e less, já que aqui nenhum valor é constante
        mid = (more + less) // 2
        sup = arr[mid]  

        if sup == elem:
            return mid
        elif  sup < elem:
            less = mid + 1
        else:
            more = mid - 1
    return None 

array =  [1,5,6,7,9,10]

print(busca_binaria(array,10))