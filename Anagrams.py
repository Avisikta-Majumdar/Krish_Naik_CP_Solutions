def anagrams(a,b):
    a.lower()
    s1= a.split(" ")

    b.lower()
    s2= b.split(" ")

    s1_list = [i for i in s1]
    s2_list = [i for i in s2]

    return s1_list.sort()==s2_list.sort()


S1 , S2 =(input("ENTER S{}  :-  ".format(i)) for i in range(1,3))

print("S1 & S2 are anagrams") if anagrams(S1,S2) else print("S1 & S2 are not anagrams")
