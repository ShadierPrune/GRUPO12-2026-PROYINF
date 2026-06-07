import { pool } from '../config/database';

export interface ISimulacionDB {
    id_simulacion: string;
    monto: number;
    plazo: number;
    tasa: number;
    cuota_mensual: number;
    total_pagado: number;
    fecha_creacion: Date;
}

export class SimulacionRepository {
    async guardar(datos: ISimulacionDB): Promise<void> {
        const query = `
            INSERT INTO simulaciones (id_simulacion, monto, plazo, tasa, cuota_mensual, total_pagado, fecha_creacion)
            VALUES ($1, $2, $3, $4, $5, $6, $7);
        `;
        
        const values = [
            datos.id_simulacion, 
            datos.monto, 
            datos.plazo, 
            datos.tasa, 
            datos.cuota_mensual, 
            datos.total_pagado, 
            datos.fecha_creacion
        ];

        await pool.query(query, values);
    }
}