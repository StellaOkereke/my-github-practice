def reverse_text(text):
    """
    Reverse the input string.
    Prameters:
        text (str): The text to be reversed.and
    Returns:
        str: The reversed string.
    """
    return text[:: -1]

def add_num(a, b):
    """Adds two numbers and returns the result.

    Args:
        a (int or float): first number
        b (int or float): second number
    Returns: int or float - the sum of a and b
    """
    return a + b

if __name__ == "__main__":
    sample_text = "hello"
    num1, num2 = 5, 7
    
    print(f"Original text:{sample_text}")
    print(f"Reversed text: {reverse_text(sample_text)}")
    print(f"Sum of {num1} and {num2} : {add_num(num1, num2)}")