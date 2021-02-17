## 함수 선언부
def printPoly(p_x):
    term = len(p_x) -1 # largest power
    polyStr = "P(x)= "

    for i in range(len(p_x)):
        coef = p_x[i]
        if coef >= 0:
            polyStr += '+'
        polyStr += str(coef) + 'x^' + str(term) + " "
        term -= 1
    
    return polyStr

def calcPoly(xValue, p_x):
    term = len(p_x) -1 # largest power
    answer = 0

    for i in range(len(p_x)):
        coef = p_x[i]
        answer += coef * xValue ** term
        term -= 1
    
    return answer


## 전역 변수부
px = [4, -3, 0, 2] # 4x^3 + 3x^2 + 0x^1 + 2x^0


if __name__ == '__main__':
    print(calcPoly(5, px))