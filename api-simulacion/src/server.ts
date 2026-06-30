import express from 'express';
import cors from "cors";
import simulacionRoutes from './routes/simulacion-routes';

const app = express();
const PORT = 3000; 
app.disable("x-powered-by");

app.use(cors({
  origin: 'http://localhost:5173', 
  credentials: true,              
}));
app.use(express.json());

// Montamos las rutas bajo la misma versión de la API
app.use('/api/v1', simulacionRoutes);

app.listen(PORT, () => {
    console.log(`[API Simulación] Corriendo en puerto interno ${PORT} bajo arquitectura en capas.`);
});