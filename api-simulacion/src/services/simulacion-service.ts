import { SimulacionRepository, ISimulacionDB } from '../repositories/simulacion-repository';

export class SimulacionService {
    private repository = new SimulacionRepository();

    // MODALIDAD DETERMINISTA
    async procesarSimulacionDeterminista(monto: number, plazo: number, tasa: number) {
        // Ejecutar el cálculo matemático financiero
        const tasaInteresEfectiva = tasa / 100;
        const cuota = tasaInteresEfectiva > 0
            ? (monto * (tasaInteresEfectiva * Math.pow(1 + tasaInteresEfectiva, plazo))) / (Math.pow(1 + tasaInteresEfectiva, plazo) - 1) : monto / plazo;

        const totalPagado = cuota * plazo;
        const intereses = totalPagado - monto;

        const resultados = {
            cuota_mensual: Math.round(cuota),
            total_pagado: Math.round(totalPagado),
            intereses_totales: Math.round(intereses)
        };

        // Preparar los datos para la persistencia
        const id_simulacion = `SIM-${Date.now()}-${Math.random().toString(36).substring(2, 9).toUpperCase()}`;
        const dataDB: ISimulacionDB = {
            id_simulacion,
            monto,
            plazo,
            tasa,
            cuota_mensual: resultados.cuota_mensual,
            total_pagado: resultados.total_pagado,
            fecha_creacion: new Date()
        };

        // Guardar en BD usando el repositorio
        await this.repository.guardar(dataDB);

        return {
            id_simulacion,
            ...resultados
        };
    }

    // MODALIDAD PREDICTIVA (Placeholder porque no sé si está en algún lado o hay que hacerla)
    async procesarSimulacionPredictiva(datosCliente: any) {
        // implementar lógica de cálculo de probabilidad si es que la pillo,
        // consulta de antecedentes históricos y recomendación de condiciones.
        throw new Error("Modalidad predictiva no implementada aún.");
    }
}