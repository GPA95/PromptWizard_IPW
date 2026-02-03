def analyze_bookkeeper(word):
    word = word.lower()
    
    # 1. Count consecutive double letter pairs
    double_pairs = 0
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            double_pairs += 1
            
    # 2. Count the total number of the letter 'e'
    e_count = word.count('e')
    
    # 3. Multiply and return result
    return double_pairs * e_count

# Execution
word = "Bookkeeper"
result = analyze_bookkeeper(word)
print(f"Result for '{word}': {result}")
