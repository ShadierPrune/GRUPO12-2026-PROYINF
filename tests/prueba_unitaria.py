import unittest
import requests
####
class TestProyecto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.URL = "http://localhost:4000"
        cls.URL_simulacion = f"{cls.URL}/api/v1/simulacion"
    # Test de la HU01: Simulación de préstamo
    def test_simulacion_prestamo(self):
        print("\nCaso de prueba HU01: Simulación de préstamo", end=" ")
        datos = {
            "monto": 0,
            "plazo": 6, # cualquier plazo
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
        #print(body)
        self.assertEqual(body["cuota_mensual"],cuota_esperada)
        self.assertEqual(body["intereses_totales"],intereses_esperado)
        self.assertEqual(body["total_pagado"],total_pagado)
        
    def test_simular_y_guardar_progreso(self):
        # Caso de prueba 1: Verifica que al enviar guardar: true, el sistema retorne un ID de simulación.
        print("\nCaso de prueba HU06: simular y guardar progreso: ", end=" ")
        payload = {
            "monto": 500000,
            "plazo": 24,
            "taza": 1.2,
            "guardar": True
        }
        
        response = requests.post(self.URL_simulacion, json=payload)
        data = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("id_simulacion", data, "El sistema no retornó un id_simulacion al guardar.")
        print("Caso de prueba 1 pasado correctamente.")
    
    def test_tc02_simular_sin_guardar_progreso(self):
        
        """
        Caso de prueba 2: Verifica que al enviar guardar: false, el sistema calcule pero NO guarde.
        *Se espera que este test falle con el código actual del backend.*
        """
        
        print("\nCaso de prueba HU06: simular sin guardar progreso: ", end=" ")
        
        payload = {
            "monto": 500000,
            "plazo": 24,
            "taza": 1.2,
            "guardar": False
        }
        
        response = requests.post(self.URL_simulacion, json=payload)
        data = response.json()
        
        self.assertEqual(response.status_code, 200)
        
        # Según el CA 2, si no quiere guardar (algo que no pregunta la página), no debería generarse ni devolverse un ID.
        self.assertNotIn(
            "id_simulacion", 
            data, 
            "Fallo detectado: El sistema generó y guardó un ID a pesar de que guardar era False."
        )
    
    @classmethod
    def tearDownClass(cls):
        print("\nSe terminaron de revisar las pruebas")
