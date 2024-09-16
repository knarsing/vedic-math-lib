
import unittest
from vedic_math_lib import sutras

class TestVedicMathSutras(unittest.TestCase):

    def test_ekadhikena_purvena(self):
        self.assertEqual(sutras.ekadhikena_purvena(25), 625)
        self.assertEqual(sutras.ekadhikena_purvena(35), 1225)

    def test_nikhilam_navatascaramam_dasatah(self):
        self.assertEqual(sutras.nikhilam_navatascaramam_dasatah(7), 3)

    def test_urdhva_tiryagbhyam(self):
        self.assertEqual(sutras.urdhva_tiryagbhyam(12, 13), 156)

    def test_paravartya_yojayet(self):
        self.assertEqual(sutras.paravartya_yojayet(10, 2), 5.0)

if __name__ == "__main__":
    unittest.main()
