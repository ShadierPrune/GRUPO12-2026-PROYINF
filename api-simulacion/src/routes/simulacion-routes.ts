import { Router } from 'express';
import { SimulacionController } from '../controllers/simulacion-controller';

const router = Router();
const controller = new SimulacionController();

router.post('/simulacion', controller.crearSimulacion);

export default router;