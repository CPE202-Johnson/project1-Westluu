
def convert(num: int, b: int):
    """Recursive function that returns a string representing num in the base b
    
    Args:
        num(int): A base 10 integer.
        b(int): An integer from 2 - 16.
     
    Returns:
        string(str): Returns a sttring of the base. 
    """
    # A list of Variables if base >= 10
    big_base = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    remain =  num % b
    
    # If base >= 10, change base according to its value
    if remain >= 10:
        remain = big_base[remain % 10]
    string = str(remain)
    quo = num // b

    if quo == 0:
       return string
    
    else:
        # Recursively calling the quotient and reducing it
        # Until it becomes zero
        return convert(quo, b) + string