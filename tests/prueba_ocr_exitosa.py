# Evalúa que el OCR procese exitosamente una imagen adjunta y devuelva un código 200 OK
# con el texto extraído, cumpliendo la meta de que el usuario no escriba a mano.
import unittest
import requests

class TestOCRExitosa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Servidor local del OCR
        cls.URL = "http://localhost:4500"
        
        # Imagen PNG transparente de 1x1 pixel simulada en bytes
        cls.imagen_dummy = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'

    def test_ocr_subida_exitosa(self):
        # Prueba: Camino Feliz (Subiendo un archivo)
        URL_ocr = f"{self.URL}/process"
        
        archivos = {
            'imagenCedula': ('carnet_prueba.png', self.imagen_dummy, 'image/png')
        }
        
        respuesta = requests.post(URL_ocr, files=archivos)

        # El servidor debe responder con éxito (200 OK)
        self.assertEqual(respuesta.status_code, 200)
        
        # Debe devolver el JSON con el resultado del texto extraído
        self.assertIn("resultado", respuesta.json())

if __name__ == '__main__':
    unittest.main()
