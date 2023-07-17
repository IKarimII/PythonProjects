name1 = input("Enter your name: ")
name2 =input("Enter the name of your partner")

combined_names = (name1 + name2).upper()

T = combined_names.count("T")
R = combined_names.count("R")
U = combined_names.count("U")
E = combined_names.count('E')

L = combined_names.count('L')
O = combined_names.count('O')
V = combined_names.count('V')
E = combined_names.count('E')

love_score  = str(T+R+U+E) + str(L+O+V+E)
print(love_score)