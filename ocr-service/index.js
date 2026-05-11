const express = require('express');
const multer = require('multer');
const { DocumentProcessorServiceClient } = require('@google-cloud/documentai').v1;
const path = require('path');
const app = express();
const port = 4000;

// Configuración de Multer (Memoria)
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

// Configuración de Google Cloud (desde variables de entorno o defaults)
const projectId = process.env.GOOGLE_PROJECT_ID || 'grand-landing-491820-m8';
const location = process.env.GOOGLE_LOCATION || 'us';
const processorId = process.env.GOOGLE_PROCESSOR_ID || '8f3bd26ee64c7e9a';

const client = new DocumentProcessorServiceClient({
  keyFilename: path.resolve(__dirname, '../key.json')
});

async function procesarImagen(encodedImage, mimeType) {
  const name = `projects/${projectId}/locations/${location}/processors/${processorId}`;

  const request = {
    name,
    rawDocument: {
      content: encodedImage,
      mimeType: mimeType,
    },
  };

  const [result] = await client.processDocument(request);
  const { document } = result;

  const datosExtraidos = {};

  if (document.entities && document.entities.length > 0) {
    for (const entity of document.entities) {
      const tipo = entity.type;
      const texto = entity.mentionText;
      datosExtraidos[tipo] = texto.replace(/\n/g, ' ').trim();
    }
  } else if (document.text) {
    // Si usaron un procesador genérico (Document OCR) en lugar de Identity Parser,
    // extraemos todo el texto crudo como plan B.
    datosExtraidos['texto_completo'] = document.text.trim();
  }
  return datosExtraidos;
}

// Interfaz web simple para probar el OCR desde el navegador
app.get('/', (req, res) => {
  res.send(`
    <html>
      <body style="font-family: Arial, sans-serif; padding: 40px;">
        <h2>Prueba rápida de OCR</h2>
        <form action="/process" method="POST" enctype="multipart/form-data">
          <input type="file" name="imagenCedula" accept="image/*" required /><br><br>
          <button type="submit" style="padding: 10px 20px; font-size: 16px; cursor: pointer;">Extraer Datos</button>
        </form>
      </body>
    </html>
  `);
});

// Endpoint interno para procesar
app.post('/process', upload.single('imagenCedula'), async (req, res) => {
  try {
    console.log('Procesando solicitud de OCR...');
    if (!req.file) {
      return res.status(400).json({ error: 'No se recibió ninguna imagen.' });
    }

    const fileBuffer = req.file.buffer;
    const mimeType = req.file.mimetype;
    const encodedImage = fileBuffer.toString('base64');

    const resultado = await procesarImagen(encodedImage, mimeType);

    console.log('OCR completado con éxito.');
    res.json({ resultado });

  } catch (error) {
    console.error('Error en el servicio de OCR:', error);
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Servicio OCR corriendo en http://localhost:${port}`);
});
