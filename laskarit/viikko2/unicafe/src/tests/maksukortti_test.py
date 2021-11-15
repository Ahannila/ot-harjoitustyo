import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti.saldo), "10")

    def test_lataus_kasvattaa_oikein(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(str(self.maksukortti.saldo), "15")

    def test_raha_vahentyy(self):
        self.maksukortti.ota_rahaa(4)
        self.assertEqual(str(self.maksukortti.saldo), "6")

    def test_ei_voi_menna_miinukselle(self):
        self.maksukortti.ota_rahaa(4)
        self.maksukortti.ota_rahaa(4)
        self.maksukortti.ota_rahaa(4)
        self.maksukortti.ota_rahaa(4)
        self.maksukortti.ota_rahaa(4)
        self.assertEqual(str(self.maksukortti.saldo), "2")
        
    def test_palautuu_true_jos_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(4), True)

    def test_palautuu_false_jos_ei_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(12), False)

    def test_tulostus_toimii(self):
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")

        
    
