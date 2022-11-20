import time
from lab5 import rabin_karp_algorithm
import unittest

class Testing(unittest.TestCase): 

    def test_first(self):
        test_pat_first = "sit"
        test_txt_first = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        result = [18] 
        time_start = time.time()
        position = rabin_karp_algorithm(test_pat_first, test_txt_first)
        time_end = time.time()
        print(time_end - time_start, "\n")
        self.assertEqual(position, result)
    
    def test_second(self):
        test_pat_first = "Vlad"
        test_txt_first = "Vlad"
        result = [0] 
        time_start = time.time()
        position = rabin_karp_algorithm(test_pat_first, test_txt_first)
        time_end = time.time()
        print(time_end - time_start)
        self.assertEqual(position, result)


if __name__ == "__main__":
    unittest.main()





