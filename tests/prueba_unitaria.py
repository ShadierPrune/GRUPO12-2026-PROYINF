import unittest
import requests

class TestProyecto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.URL = "http://localhost:4000"

    @classmethod
    def tearDownClass(cls):
        print("Se terminaron de revisar las pruebas")
    
    def test_simulacion_prestamo(self):

        datos = {
            "monto": 100000,
            "plazo": 12,
            "taza": 1.5
        }
        URL_simulacion = f"{self.URL}/api/v1/simulacion"
        respuesta = requests.post(URL_simulacion, json=datos)

        self.assertEqual(respuesta.status_code, 200) #o sea, que llega bien

        body = respuesta.json()

        # Los valores entregados funcionan
        self.assertIn("cuota_mensual", body)
        self.assertIn("total_pagado", body)
        self.assertIn("intereses_totales", body)
        self.assertIn("id_simulacion", body)

        # Que no tenga valores negativos
        self.assertGreaterEqual(body["cuota_mensual"],0)
        self.assertGreaterEqual(body["intereses_totales"],0)
        self.assertGreaterEqual(body["total_pagado"],0)
        
        # Que calcen con su salida esperada
        
        cuota_esperada = 0
        intereses_esperado = 0
        total_pagado = 0
        # tengo que ver los casos a mano despues, revisaré
        # cuando es muy chico y cuando es muy grande, tiene
        # que ser caso BORDE
        self.assertAlmostEqual(body["cuota_mensual"],cuota_esperada, places=2)
        self.assertAlmostEqual(body["intereses_totales"],intereses_esperado, places=2)
        self.assertAlmostEqual(body["total_pagado"],total_pagado, places=2)
        
        