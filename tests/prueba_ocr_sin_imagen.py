"""
1. Simula a un cliente que, por accidente, apretó "Enviar" sin adjuntar la foto del carnet.
2. Garantiza que el sistema NO se caiga ni colapse al intentar procesar un archivo nulo 
   (lo que de otra forma causaría un error crítico 500 en el servidor).
3. Evalúa que el backend sea capaz de atajar el problema a tiempo, rechazando la 
   solicitud ordenadamente con un código 400 (Bad Request).
4. Verifica que se devuelva el mensaje exacto "No se recibió ninguna imagen.", permitiendo 
   así que el Frontend de la aplicación pueda mostrar una alerta amigable al cliente.
"""
import unittest
import requests

class TestOCRError(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Servidor local del OCR
        cls.URL = "http://localhost:4500"

    def test_ocr_sin_imagen(self):
        # Prueba: fallida (No se sube nada)
        URL_ocr = f"{self.URL}/process"
        
        # No enviamos ningún archivo adjunto en la petición
        respuesta = requests.post(URL_ocr)

        # El servidor debe rechazar la petición con error 400 (Bad Request)
        self.assertEqual(respuesta.status_code, 400)
        
        body = respuesta.json()
        
        # Comprobamos que devuelva el mensaje exacto de error programado
        self.assertIn("error", body)
        self.assertEqual(body["error"], "No se recibió ninguna imagen.")

if __name__ == '__main__':
    unittest.main()
