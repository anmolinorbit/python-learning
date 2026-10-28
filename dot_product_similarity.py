vector_a = [1,2,3]
vector_b = [4,5,6]

if len(vector_a) != len(vector_b):
    print("Error: Vectors must be of the same length.")
else:
    dot_product = 0
    for i in range(len(vector_a)):
        product = vector_a[i] * vector_b[i]
        dot_product += product

    print(dot_product)