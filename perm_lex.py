def perm_gen_lex(a: str):
    """ This function takes a string of lower-case letters in order
    and returns a list of permutations in lexicographic order.

    Args:
        a(str): A string of unique lower case letters in abc order. 
    
    Returns:
        abc_list(list): Returns a permutation of a in lexicographic order.
    """
    if len(a) == 0:
        return []
    
    if len(a) == 1:
        return [a]
    
    else:
        perm_list = []
        
        # Goes through every letter and removing it once
        for char in range(len(a)):
            first_char = a[char]  
            remove_list = list(a)
            remove_list.remove(first_char)
            remove_char = "".join(remove_list)
            
            # Once string is reduce, we recrusivly call it, for each removed letter
            # Then store each permutation in the list of the smaller string
            for perm in perm_gen_lex(remove_char):
                perm_list.append(first_char + perm)
        
        return perm_list
