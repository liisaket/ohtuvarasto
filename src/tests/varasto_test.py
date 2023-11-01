import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.toinen_varasto = Varasto(-1, -1)
        self.kolmas_varasto = Varasto(5, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_virheellinen_alustus(self):
        # toinen varasto määrät alle 0
        self.assertAlmostEqual(self.toinen_varasto.tilavuus, 0.0)
        self.assertAlmostEqual(self.toinen_varasto.saldo, 0.0)

        # kolmas varasto alku_saldo ylittää tilavuuden
        self.assertAlmostEqual(self.kolmas_varasto.tilavuus, 5)
        # self.saldo = tilavuus
        self.assertAlmostEqual(self.kolmas_varasto.saldo, 5)
    
    def test_virheellinen_lisaa_varastoon(self):
        # saldo ei muutu jos lisää alle 0 määrän saldoa
        self.assertAlmostEqual(self.toinen_varasto.saldo, 0.0)
        self.toinen_varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.toinen_varasto.saldo, 0.0)
    
    def test_lisaa_liikaa_varastoon(self):
        # jos lisätään liikaa saldoa, niin saldon pitäisi olla = tilavuus
        self.assertAlmostEqual(self.kolmas_varasto.saldo, 5)
        self.kolmas_varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.kolmas_varasto.saldo, self.kolmas_varasto.tilavuus)

    def test_virheellinen_ota_varastosta(self):
        # jos määrä on alle 0 niin tulee 0.0
        saatu_maara = self.toinen_varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0.0)
    
    def test_ota_liikaa_varastosta(self):
        # jos määrä on yli saldon, otetaan kaikki mitä voidaan
        self.assertAlmostEqual(self.kolmas_varasto.saldo, 5)
        kaikki_mita_voidaan = self.kolmas_varasto.ota_varastosta(10)
        # saldo nollautuu ja otettiin saldon verran pois
        self.assertAlmostEqual(self.kolmas_varasto.saldo, 0.0)
        self.assertAlmostEqual(kaikki_mita_voidaan, 5)

    def test_str(self):
        str_lause = testi rikki
        self.assertEqual(str_lause, "saldo = 0, vielä tilaa 10")