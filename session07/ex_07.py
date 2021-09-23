#1.1 (1) failed
# def check_fermat(a,b,c,n):
#     if type(a and b and c) == int():
#         if n > 2:
#             if a**n + b**n == c**n:
#                 print("Holy smokes, Fermat was wrong!")
#             else:
#                 print("No, that doesn’t work.")
#         else: 
#             print("n is not right")
#     else:
#         print('a,b,c is not correct')
#     return (a,b,c,n)
# check_fermat(1,1,1,3)

#1.2 failed:  Professor, could you please help me with the code in column 36? It is showing an error but I don't know why since I have already changed it into a float
def calculate_bmi(weight, height):
    weight = float(weight)
    height = float(height)
    bmi = weight/height/height
    print(bmi)
    return(bmi)

def get_bmi_catagory(bmi):
    bmi = float(bmi)
    if bmi <= 18.5:
        print('Underweight')
    elif bmi in range[18.5,24.9]:
        print('Normal weight')
    elif bmi in range[25, 29.9]:
        print('Overweight')
    else:
        print('Obesity')

calculate_bmi(70,1.8)
get_bmi_catagory(21.6)