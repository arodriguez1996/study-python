"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que 
sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""



nums = [4, 5, 6, 2]
goal = 7

# def find_first_sum(nums, goal):
#     acc = []
#     i = 0
#     while i < len(nums):
#         j = i + 1
#         if len(acc) == 2: break
#         while j < len(nums):
#             if len(acc) == 2: break
#             if nums[i] + nums[j] == goal:
#                 acc = [i, j]            
#             j += 1
#         i += 1

#     return acc if len(acc) == 2 else None

# def find_first_sum(nums, goal):
#     if len(nums) == 0: return None

#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == goal:
#                 return [i, j]
#     return None        
    


# def find_first_sum(nums, goal):
    # seen = {} # diccionario para guardar el numero y su índice
    # for index, value in enumerate(nums):
    #     missing = goal - value
    #     if missing in seen: return [seen[missing], index]
    #     seen[value] = index # guardar el número actual a los vistos, porque no hemos encontrado la combinación
    # return None


def find_first_sum(nums, goal):
    acc = {}
    for i, value in enumerate(nums):
        diff = goal - value
        if diff in acc: return [acc[diff], i]
        acc[value] = i
    return None

print(f'returned --> {find_first_sum(nums, goal)}')