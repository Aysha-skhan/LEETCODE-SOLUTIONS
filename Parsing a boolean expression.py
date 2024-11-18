def parseBoolExpr( expression: str):
    eval = []
    arth = []
    for z in range(len(expression)):
        if expression[z]!=')' and expression[z]!=',':
            if expression[z]=='f':
                eval.append(0)
            elif expression[z]=='t':
                eval.append(1)
            else:
                eval.append(expression[z])
        elif expression[z]==')':
            v=')'
            while v!='(':
                v=eval.pop()
                if v!='(':
                    arth.append(v)
            op=eval.pop()
            if op=='!':
                result=not arth.pop()
                if result==False:
                    result=0
                else:
                    result=True
                eval.append(result)
            elif op=='|':
                temp = arth.pop()
                for k in range(len(arth)):
                    t = arth.pop()
                    temp = t or temp
                eval.append(temp)
                # print(arth)
            elif op=='&':
                temp=arth.pop()
                for k in range(len(arth)):
                    t=arth.pop()
                    temp= t and temp
                    # print(temp, 'temp&')
                # print(arth,'aftr')
                eval.append(temp)
    if eval[0]==0:
        return False
    else:
        return True





print(parseBoolExpr('|(&(t,f,t),!(t))'))

