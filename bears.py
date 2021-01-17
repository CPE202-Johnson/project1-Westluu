def bears(n: int):
    """ A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears.
    
    Args:
        n(int): Any postive number of bears.
    
    Returns:
        True(bool): Returns True if its possible to get exactly 42 bears.
        False(bool): Returns False if it's not possible to get exactly 42 bears.
    """
    if n == 42: # Base Case 1
        return True
    
    # Base Case 2
    if n % 5 != 0 and n % 3 != 0 and n % 4 != 0 and n % 2 != 0:
        return False
    
    else: 
        # If any are true, thus the case is case
        a = False
        b = False
        c = False
        
        # Reduction Case
        if n < 42:
            return False
        
        if n % 2 == 0:
            a = bears(n/2)
        
        if n % 3 == 0 or n % 4 == 0:
            last_two = n % 100
            first = last_two // 10
            last = last_two % 10
            mult = first * last
            if mult != 0:
                b = bears(n - mult)
        
        if n % 5 == 0:
            c = bears(n - 42)

        # At the end of the possiblities, if any of the branches are true, the case is true
        if a == True or b == True or c == True:
            return True