import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
from tests.maksukortti_test import TestMaksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_oikeat_maarat(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')

    def test_oikeat_edulliset(self):
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_oikeat_maukkaat(self):
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_kateis_maksu_lisaa_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")

    def test_kateis_maukas_maksu_lisaa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")

    def test_kateis_maksu_lisaa_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.edulliset), "1")
 
    def test_kateis_maksu_lisaa_maaraa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_liian_vahan_rahaa_ei_muuta_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(220)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_liian_vahan_rahaa_ei_muuta_saldoa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_korttiosto_veloittaa_kortilta(self):
        kortti = Maksukortti(240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)

    def test_korttiosto_maukas_veloittaa_kortilta(self):
        kortti = Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)

    def test_korttiost_lisaa_myytyjen_lounaide_maaraa(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_korttiost_lisaa_myytyjen_lounaide_maaraa_maukas(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_korttiosto_ei_lapi_liian_vahalla_rahalla(self):
        kortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate.edulliset), '0')

    def test_korttiosto_maukas_ei_lapi_liian_vahalla_rahalla(self):
        kortti = Maksukortti(230)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_kortilla_ei_rahaa_ei_muuta_saldoa(self):
        kortti = Maksukortti(220)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti.saldo), '220')
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_maukkaasti_kortilla_ei_rahaa_ei_muuta_saldoa(self):
        kortti = Maksukortti(220)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti.saldo), '220')

    def test_korttiosto_palauttaa_false_jos_ei_rahaa(self):
        kortti = Maksukortti(220)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
    
    def test_korttiosto_palauttaa_false_jos_ei_rahaa_maukas(self):
        kortti = Maksukortti(220)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_kassassa_olevaa_raha_ei_muutu(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")   

    def test_kortille_lataus_toimii(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 400)
        self.assertEqual(str(kortti.saldo),"400")
       
    def test_kortille_lataus_toimii_kassassa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 400)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100400')

    def test_ladataan_miinusta_kortille(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -20)
        self.assertEqual(kortti.saldo, 0)