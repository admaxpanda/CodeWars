'''
To give credit where credit is due: This problem was taken from the
ACMICPC-Northwest Regional Programming Contest. Thank you problem writers.

You are helping an archaeologist decipher some runes. He knows that 
this ancient society used a Base 10 system, and that 
they never start a number with a leading zero. He's figured out most of the digits 
as well as a few operators, but he needs your help to figure out the rest.

The professor will give you a simple math expression, of the form

[number][op][number]=[number]

He has converted all of the runes he knows into digits.
The only operators he knows are addition (+),subtraction(-), and multiplication (*),
so those are the only ones that will appear. 
Each number will be in the range from -1000000 to 1000000,
and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s.
If there are ?s in an expression, they represent a digit rune that the professor doesn't know 
(never an operator, and never a leading -).
All of the ?s in an expression will represent the same digit (0-9), 
and it won't be one of the other given digits in the expression. 
No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented by the question mark.
If more than one digit works, give the lowest one. 
If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. 
The method takes a string as a paramater repressenting 
the expression and will return an int value representing the unknown rune or -1 if no such rune exists.
'''
def solve_runes(runes):
    numUsed=set()
    for i in runes:
        if i.isdigit():
            numUsed.add(int(i))
    anser=runes.split('=')[1]
    former=""
    latter=""
    operator=""
    formerint=""
    latterint=""
    anserint=""
    if '+' in runes:
        former=runes.split('=')[0].split('+')[0]
        latter=runes.split('=')[0].split('+')[1]
        operator='+'
    elif '*'in runes:
        former=runes.split('=')[0].split('*')[0]
        latter=runes.split('=')[0].split('*')[1]
        operator='*'
    elif runes.split('=')[0].count('-')==1:
        former=runes.split('=')[0].split('-')[0]
        latter=runes.split('=')[0].split('-')[1]
        operator='-'
    elif runes.split('=')[0].count('-')==3:
        former='-'+ runes.split('=')[0].split('-')[1]
        latter='-'+ runes.split('=')[0].split('-')[3]
        operator='-'
    elif len(runes.split('=')[0].split('-')[0])==0:
        former='-'+ runes.split('=')[0].split('-')[1]
        latter=runes.split('=')[0].split('-')[2]
        operator='-'
    else:
        former=runes.split('=')[0].split('-')[0]
        latter='-'+ runes.split('=')[0].split('-')[2]
        operator='-'
    #print(former,operator,latter,'=',anser)
    for i in range(10):
        if i in numUsed:
            continue
        former=former.replace('?',str(i))
        latter=latter.replace('?',str(i))
        anser=anser.replace('?',str(i))
        print(former,operator,latter,'=',anser)
        if (former[0]=='0' and len(former)!=1 
        or latter[0]=='0' and len(latter)!=1 
        or anser[0]=='0' and len(anser)!=1
        or former[0]=='-' and former[1]=='0' and len(former)!=2
        or latter[0]=='-' and latter[1]=='0' and len(former)!=2
        or anser[0]=='-' and anser[1]=='0' and len(anser)!=2
        ):
            former=former.replace(str(i),'?')
            latter=latter.replace(str(i),'?')
            anser=anser.replace(str(i),'?')
            continue
        if operator=='+' and int(former)+int(latter)==int(anser):
            return i
        if operator=='-' and int(former)-int(latter)==int(anser):
            return i
        if operator=='*' and int(former)*int(latter)==int(anser):
            return i
        former=former.replace(str(i),'?')
        latter=latter.replace(str(i),'?')
        anser=anser.replace(str(i),'?')
    return -1
    # Your code here
    pass
if __name__ =="__main__":
    print(solve_runes("-??+8=8"))
