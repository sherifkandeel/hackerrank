D = {}
D[1] = "one"
D[2] = "two"
D[3] = "three"
D[4] = "four"
D[5] = "five"
D[6] = "six"
D[7] = "seven"
D[8] = "eight"
D[9] = "nine"
D[10] = "ten"
D[11] = "eleven"
D[12] = "twelve"
D[13] = "thirteen"
D[14] = "fourteen"
D[16] = "sixteen"
D[17] = "seventeen"
D[18] = "eighteen"
D[19] = "nineteen"
D[20] = "twenty"
D[30] = "thirty"
to = "to"
half = "half"
past = "past"
minute = "minute"
minutes = "minutes"
quarter = "quarter"
oclock = "o' clock"
s = " "

def write(h,m):
    if m == 0:
        return D[h]+s+oclock
    if m == 1:
        return D[m]+s+minute+s+past+s+D[h]
    elif m == 15:
        return quarter+s+past+s+D[h]
    elif m == 30:
        return half+s+past+s+D[h]
    elif m < 30:
        if m <= 20:
            return D[m]+s+past+s+D[h]
        else:
            return D[m-m%10]+s+D[m%10]+s+minutes+s+past+s+D[h]
    elif m>30:
        m = 60-m
        h = h+1
        if m==1:
            return D[m]+s+minute+s+to+s+D[h]
        elif m==15:
            return quarter+s+to+s+D[h]
        elif m <=20:
            return D[m]+s+minutes+s+to+s+D[h]
        elif m>20:
            return D[m-m%10]+s+D[m%10]+s+minutes+s+to+s+D[h]
            




h = int(raw_input())
m = int(raw_input())

print write(h,m)
