

# Graph - Romeo, Julia, Paris, Laurenty
V={
    "J":["R","P","L"],
    "R":["J","P", "L"],
    "L":["J","R"],
    "P":["J","R"],
}

def graph_degree(V):
    return max([node_degree(V, n) for n in V.keys()  ])

def node_degree(V, node):
    if node in V.keys():
        return len(V[node])
    else:
        return -1

for n in V.keys():
    print(f'Degree of {n}: {node_degree(V, n)}')

print(f'graph degree {graph_degree(V)}')
















# { 
# 	Smartphone: { Web Browser: 30, Book: 22 } ,
# 	Web Browser: {Book: 32, MP3: 25},
# 	MP3: {Book: 44},
# 	Book:[]
# }

# V={}

# def add_node(V, node):

#     if node in V.keys():
#         return
#     else:
#         V[node] = {}

# def add_edge(V, source, dest, weight):
#     if not source in V.keys() or not dest in V.keys():
#         return
#     else:
#         if not dest in V[source].keys():
#             V[source][dest]  = weight
# V={}
# add_node(V, "Smartphone" )
# add_node(V, "Web Browser" )
# add_node(V, "Book" )
# add_node(V, "MP3" )

# add_edge(V, 'Smartphone', 'Web Browser', 30)
# add_edge(V, 'Smartphone', 'Book', 22)
# add_edge(V, 'Web Browser', 'Book', 32)
# add_edge(V, 'Web Browser', 'MP3', 25)
# add_edge(V, 'MP3', 'Book', 44)



# print(V)
# print(f'Koszt czasu Web Browser->Book {V["Web Browser"]["Book"]}')














# def add_node(V, node):

#     if node in V.keys():
#         return
#     else:
#         V[node] = []

# def add_edge(V, source, dest):
#     if not source in V.keys() or not dest in V.keys():
#         return
#     else:
#         if not dest in V[source]:
#             V[source].append(dest)
# V={}
# add_node(V, "ZP" )
# add_node(V, "PE" )
# add_node(V, "ZE" )
# add_node(V, "Zprez" )
# add_node(V, "RW" )

# add_edge(V, 'RW', 'Zprez')
# add_edge(V, 'RW', 'ZP')


# add_edge(V, 'ZP', 'PE')
# add_edge(V, 'ZP', 'RW')

# add_edge(V, 'PE', 'ZE')
# print(V)

# V = ["a", "b", "c", "d", "f"]
# E=[ (0,2), (1,2), (2,3), (2,4)]


# def create_matrix(V, E):
#     matrix=[]
    
#     for i in range(len(V)):
#         row=[0 for _ in range(len(V))]
       
#         for first, second in E:
#             if i == first:
#                 row[second] = 1
        
#         matrix.append(row)
    
#     return matrix

# def create_matrix2(V,E):
#     matrix = []
#     for val1 in range(len(V)):
#         matrix.append([1 if (val1, val2) in E else 0 for val2 in range(len(V))])

#     return matrix

# m = create_matrix2(V, E)
# for i in m:
#     print(i)



# V = [1,2,3,4] # indeksy w macierzy 1->index 0, 2->index 1 ...
# E = [ 
#     (1,2),
#     (2,4),
#     (1,3),
#     (3,4)
# ]

# matrix = [ 
#     [0,1,1,0],
#     [0,0,0,1],
#     [0,0,0,1],
#     [0,0,0,0],
# ]

# start = 2
# idx = V.index(start)
# for i in range(len(V)):
#     if matrix[idx][i] == 1:
#         print(V[i])
# print('-'*5)
# print([V[i] for i in range(len(V)) if matrix[V.index(start)][i] == 1 ])



# V = ['Julia', 'Romeo', 'Parys', 'Laurenty']
# E = [
#      ['Julia', 'Romeo'], ['Julia', 'Parys'], ['Julia', 'Laurenty'],
#      ['Romeo', 'Parys'], ['Romeo', 'Laurenty'],
# ]
# # Julia - 0, Romeo - 1, Parys - 2, Laurenty -3
# matrix = [
    
#     [0,1,1,1],
#     [1,0,1,1],
#     [1,1,0,0],
#     [1,1,0,0]
# ]

# def who_knows_person(person, V, matrix):
#     friends = []
#     idx = V.index(person)

#     for i in range(len(V)):
        
#         if matrix[idx][i] == 1:
            
#             friends.append(V[i])
        
#     return friends

# print(who_knows_person("Romeo", V, matrix))


    # przekształcenie nazwy potaci do numery wiersza w matrix, bo
    # pierwszy wiersz to Julia
    # drugi to Romeo ...






# wycieczka Olsztyn w jeden dzień

# V = ['Dworzec PKP', "Rozkopy przy Victorze", "Aura", "Stare Miasto", "MacDonalds", "Galeria Warmińska"]
# E = [('Dworzec PKP' , "Rozkopy przy Victorze"),
#      ('Dworzec PKP' , "Stare Miasto"), 
#      ("Stare Miasto", "Galeria Warmińska" ), 
#      ("Rozkopy przy Victorze", "Aura"),
#      ("Aura", "MacDonalds"),
#      ("MacDonalds", "Galeria Warmińska"),
#     ]

# # jaki następny przystanek, następny przystanek, od przystanku start
# start = 'Dworzec PKP'
# for f,s in E:
#     if f == start:
#         print(s)
# print([s for (f,s) in E if f == start])

# # Aby dojechać do przystanku koniec
# end="Aura"
# for f,s in E:
#     if s == end:
#         print(f)
# print([f for (f,s) in E if s==end])
