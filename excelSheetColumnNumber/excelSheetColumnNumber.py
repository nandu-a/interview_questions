

def titleToNumber(columnTitle: str) -> int:
    columnNumber = 0
    power = len(columnTitle) - 1
        
    for c in columnTitle:
        columnNumber += (ord(c) - ord("A") + 1)*(26**power)
        power -= 1
            
    return columnNumber

print(titleToNumber("FXSHRXW"))

