def num_to_words(n):
    """
    A simple function to convert integers 0-999 to English words
    to avoid external dependencies like 'num2words'.
    """
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 0: return "zero"
    
    words = ""
    
    # Handle Hundreds
    if n >= 100:
        words += ones[n // 100] + " hundred"
        n %= 100
        if n > 0: words += " and "
    
    # Handle Tens and Ones
    if n >= 20:
        words += tens[n // 10]
        if n % 10 > 0:
            words += "-" + ones[n % 10]
    elif n >= 10:
        words += teens[n - 10]
    elif n > 0:
        words += ones[n]
        
    return words

def find_odd_numbers_without_e(limit):
    found_numbers = []
    
    print(f"Scanning the first {limit} numbers...")
    
    for i in range(limit):
        # Check if the number is Odd
        if i % 2 != 0:
            word = num_to_words(i)
            # Check if 'e' is NOT in the word
            if 'e' not in word:
                found_numbers.append(f"{i} ({word})")

    if not found_numbers:
        print("\nResult: No odd numbers found without the letter 'e'.")
        print("Theory confirmed: It's impossible in standard English!")
    else:
        print("\nResult: Found them!", found_numbers)

# Let's run the search for the first 1,000 numbers
find_odd_numbers_without_e(1000)