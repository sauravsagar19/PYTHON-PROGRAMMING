def CI(P,R,T):

    print("Principal:",P)
    print("Rate:",R)
    print("Time:",T)
    A=P* (pow((1+R/100),T))
    C= A-P
    print("compound_interest:",C)
CI(1000,10,2)


"""
