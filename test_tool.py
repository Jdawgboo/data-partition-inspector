import unittest
from tool import overlaps
class Tests(unittest.TestCase):
 def test_overlap(self): self.assertEqual(overlaps({'train':{'a'},'test':{'a','b'}}),['test:train'])
if __name__=='__main__': unittest.main()
