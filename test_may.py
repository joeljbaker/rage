import unittest
from may import family_scenarios

class FamilyScenariosTest(unittest.TestCase):
    def test_max_age(self):
        kids = family_scenarios(max_age=5, max_kids=3)
        max_age = 0
        for fam in kids:
            self.assertTrue(max(fam)<=5)
            if(max(fam))>max_age:
                max_age=max(fam)
        self.assertEqual(max_age, 5)

    def test_max_kids(self):
        kids = family_scenarios(max_age=5, max_kids=3)
        max_len = 0
        for fam in kids:
            self.assertTrue(len(fam)<=3)
            if(len(fam))>max_len:
                max_len=len(fam)
        self.assertEqual(max_len, 3)

    def test_uniqueness1(self):
        kids = family_scenarios(max_age=3, max_kids=1)
        self.assertEqual(len(kids), 3)
        self.assertEqual([len(fam) for fam in kids], [1,1,1])

    def test_uniquenesss2(self):
        kids = [fam for fam in family_scenarios(max_age=2, max_kids=2) if len(fam)==2]
        self.assertEqual(3, len(kids)) # make sure the (2,1) option has been filtered out

if __name__ == '__main__':
    unittest.main()
