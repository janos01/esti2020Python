import szamev
import unittest

class TesztSzamev(unittest.TestCase):
    
    def testVizsgalSzamIgaz(self):
        res = szamev.vizsgalSzam('34')
        self.assertEqual(res, True, 'Elvárt eredmény True')
        
    def testVizsgalSzamIgaz2(self):
        res = szamev.vizsgalSzam('767')
        self.assertEqual(res, True, 'Elvárt eredmény True')
        
    def testVizsgalSzamHamis(self):
        res = szamev.vizsgalSzam('34aa')
        self.assertEqual(res, False, 'Elvárt eredmény False')


if __name__ == "__main__":
    unittest.main()
