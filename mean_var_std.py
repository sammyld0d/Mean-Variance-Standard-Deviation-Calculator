import numpy as np

def calculate(num_list): #example input [0,1,2,3,4,5,6,7,8]
    dc = {'mean':[],
          'variance':[],
          'standard deviation':[],
          'max':[],
          'min':[],
          'sum':[]}
    
    if len(num_list) != 9 or any(type(item) != int for item in num_list):
        raise ValueError('List must contain nine numbers.')
    else:
        i_list = [0, 1, None]
        array = np.array([num_list[0:3],num_list[3:6],num_list[6:9]])

        for i in i_list:
            if type(i) == int:
                dc['mean'].append(list(np.mean(array, axis = i)))
                dc['variance'].append(list(np.var(array, axis = i)))
                dc['standard deviation'].append(list(np.std(array, axis = i)))
                dc['max'].append(list(np.max(array, axis = i)))
                dc['min'].append(list(np.min(array, axis = i)))
                dc['sum'].append(list(np.sum(array, axis = i)))
            else:
                dc['mean'].append(np.mean(array))
                dc['variance'].append(np.var(array))
                dc['standard deviation'].append(np.std(array))
                dc['max'].append(np.max(array))
                dc['min'].append(np.min(array))
                dc['sum'].append(np.sum(array))

    calculations = dc

    return calculations