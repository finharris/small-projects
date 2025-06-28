def findSequenceIdentifier(data):
    if len(set(data)) <= 1: return data
    
    output = []
    
    for i in range(len(data)):
        if i == len(data)-1: return findSequenceIdentifier(output)
        
        difference = max(data[i], data[i+1]) - min(data[i], data[i+1])
        
        output.append(difference)
        
        
def main():
    
    data = [1,4,9,16,25]
    data2 = [1,8,27,64,125, 216]
    print(findSequenceIdentifier(data2))    

    return

if __name__ == "__main__":
    main()