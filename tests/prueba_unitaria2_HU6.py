import unittest
import requests

class TestCrearSimulacion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.URL = "http://localhost:4000/api/v1/simulacion"
        print("Iniciando las pruebas")
    
    def test_tc02_simular_sin_guardar_progreso(self):
        
        """
        Caso de prueba 2: Verifica que al enviar guardar: false, el sistema calcule pero NO guarde.
        *Se espera que este test falle con el código actual del backend.*
        """
        
        payload = {
            "monto": 500000,
            "plazo": 24,
            "taza": 1.2,
            "guardar": False
        }
        
        response = requests.post(self.URL, json=payload)
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
        print("Se terminaron de revisar las pruebas")