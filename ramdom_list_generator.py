def random_list_maker(n,initial,final):
    import random

    random_list = [random.randint(initial, final) for i in range(n)]
    print(random_list)

i=int(input("Enter how many elements should be in the list : "))
initial=int(input("starting range of list integer: "))
final=int(input("ending range of list integer: "))
random_list_maker(i,initial,final)

