# Print N mobile numbers on separate lines in the required format.

def wrapper(f):
    def fun(l):
        
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
        
        """
        newL = list()
    
        for i in l:
            if len(i) == 12 and i[2] == "9" and i[1] == "1":
                newL.append("+91 " + i[2:7] + " " + i[7:12])
            elif i[0] == "0":
                newL.append("+91 " + i[1:6] + " " + i[6:11])
            elif i[0] == "+":
                newL.append("+91 " + i[3:8] + " " + i[8:13])
            elif len(i) == 10:
                newL.append("+91 " + i[0:5] + " " + i[5:10])
                
        newL.sort()
        
        for i in newL:
            print(i)
        """
            
    return fun

