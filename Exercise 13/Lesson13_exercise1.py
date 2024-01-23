# Write a Python program to square and cube every number in a given list of integers using Lambda.
answer_1=[1,2,3,4]
answer_2=[1,2,3,4]

kar=map(lambda x: pow(x,2), answer_1)
khor=map(lambda y: y**3, answer_2)

print(list(kar), list(khor))