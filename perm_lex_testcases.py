import unittest
import perm_lex

class TestAssign1(unittest.TestCase):
    """ This test if the function is able to take a spring and
        output all the possiable peermutation of that spring in
        lexicographic order.
    """

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

        self.assertEqual(perm_lex.perm_gen_lex('bc'), ['bc', 'cb'])
        
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

        self.assertEqual(perm_lex.perm_gen_lex('def'), ['def', 'dfe', 'edf', 'efd', 'fde', 'fed'])

        self.assertEqual(perm_lex.perm_gen_lex('ghi'), ['ghi', 'gih', 'hgi', 'hig', 'igh', 'ihg'])
        
        self.assertEqual(perm_lex.perm_gen_lex('abcd'), ['abcd', 'abdc', 'acbd', 'acdb', 'adbc',
                                                         'adcb', 'bacd', 'badc', 'bcad', 'bcda', 
                                                         'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 
                                                         'cbda', 'cdab', 'cdba', 'dabc', 'dacb',
                                                         'dbac', 'dbca', 'dcab', 'dcba'])
        
        
                             
if __name__ == "__main__":
        unittest.main()
