def countwords(s):
    if s.strip()==" ":
        return 0
    words=s.split()
    return len(words)
if _name=="main_":
    s=input("enter the string")
    print("no.of words:",countwords(s))
