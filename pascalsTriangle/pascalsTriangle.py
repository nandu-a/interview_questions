
#function
def generate(numRows: int):
    answer = [[1]]
        
    for i in range(1, numRows):
        lastRow = [0] + answer[-1] + [0]
        newRow = []
        
        for j in range(0, len(lastRow) - 1):
            newRow.append(lastRow[j] + lastRow[j+1])
            
        answer.append(newRow)
        
    return answer

print(generate(3))

