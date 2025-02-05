def find_duplicates_nested_loop(l: list) -> list:
    duplicates = []
    
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j] and l[i] not in duplicates:
                duplicates.append(l[i])
                break 
            
    return duplicates

def find_duplicates_dict(l: list) -> list:
    count_dict = {}
    duplicates = []

    for num in l:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count > 1:
            duplicates.append(num)

    return duplicates

if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]
    
    print("Sample 1:", find_duplicates_nested_loop(sample1)) 
    print("Sample 2:", find_duplicates_nested_loop(sample2))  
    print("Sample 3:", find_duplicates_nested_loop(sample3))  
    print("Sample 4:", find_duplicates_nested_loop(sample4))  
    print("Sample 1:", find_duplicates_dict(sample1))  
    print("Sample 2:", find_duplicates_dict(sample2))  
    print("Sample 3:", find_duplicates_dict(sample3))  
    print("Sample 4:", find_duplicates_dict(sample4))  
