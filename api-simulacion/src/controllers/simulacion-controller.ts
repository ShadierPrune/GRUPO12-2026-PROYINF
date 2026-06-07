import type { Request, Response } from 'express';
import { SimulacionService } from '../services/simulacion-service';

export class SimulacionController {
    private service = new SimulacionService();

    crearSimulacion = async (req: Request, res: Response): Promise<any> => {
        const { monto, plazo, taza } = req.body; // Mantenemos "taza" para no romper el contrato del frontend actual

        // Validación de tipos (Sanitización rápida de entrada)
        if (typeof monto !== 'number' || typeof plazo !== 'number' || typeof taza !== 'number') {
             return res.status(400).json({ error: 'Monto, plazo y taza deben ser números.' });
        }

        try {
            // Orquestación hacia la capa de negocio determinista
            const resultado = await this.service.procesarSimulacionDeterminista(monto, plazo, taza);
            
            return res.json({
                mensaje: "Simulación guardada con éxito",
                ...resultado
            });
        } catch (error) {
            console.error('[SimulacionController Error]:', error);
            return res.status(500).json({ error: 'Error interno al procesar la simulación' });
        }
    };
}