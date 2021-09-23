from fsmaths import *
import math

def solve_trig(minvalue,maxvalue,trig_func,intersect):
    flist = []
    for i in range(minvalue, maxvalue):
        if abs(trig_func(i/1000)-intersect)<0.001:
            flist.append(i/1000)
    return flist

def average_func(lvalues):
    k, value_list, cvalue_list, fitem = 0, [], [], lvalues[0]
    for i in lvalues:
        if i - fitem <= 0.5:
            cvalue_list.append(i)
        else:
            value_list.append(cvalue_list[:])
            cvalue_list, fitem = [i], i
    value_list.append(cvalue_list[:])
    plist = [sum(x)/len(x) for x in value_list]
    for y in plist:
        if abs(round(y)-y) < 0.00001:
            plist[k] = round(y)
        k+=1
    return plist
            
def main():
    lowerlimit = int(input('Lower limit:   '))*1000
    upperlimit = int(input('Upper limit:   '))*1000
    func_string = input('Trig function:   ').lower()[0]
    intersection = eval(input('Point of intersection:   '))

    if func_string == 's':
        func = sin
    elif func_string == 'c':
        func = cos
    elif func_string == 't':
        func = tan

    print(average_func(solve_trig(lowerlimit,upperlimit,func,intersection)))

if __name__ == '__main__':
    main()

    


