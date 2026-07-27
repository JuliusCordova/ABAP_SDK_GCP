# ABAP_SDK_GCP — Source Registry

**Propósito:** inventario único de fuentes utilizadas por el GPT, los manuales, runbooks, catálogos y políticas canónicas.

## Estados

- `REFERENCE_ONLY`: fuente registrada sin cambios documentales.
- `PROPOSED_UPDATE`: se identificó una mejora documental.
- `PENDING_VALIDATION`: cambio aplicado en rama o PR, pendiente de aprobación.
- `APPROVED_CANON`: fuente aprobada como sustento de una regla canónica.
- `REJECTED`: fuente descartada para el proyecto.
- `SUPERSEDED`: fuente histórica reemplazada por otra más reciente.

## Registro

| ID | Autoridad | Título | Producto / componente | Versión | Fecha de publicación o actualización | Fecha de consulta | URL o referencia | Estado | Ficha | Observaciones |
|---|---|---|---|---|---|---|---|---|---|---|
| SRC-GOOG-001 | OFICIAL GOOGLE | BigQuery Toolkit for SAP overview | BigQuery Toolkit for SAP | latest / confirmar versión instalada | No confirmada | 2026-07-27 | https://cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview | REFERENCE_ONLY | Pendiente | Referencia base del canon. |
| SRC-GOOG-002 | OFICIAL GOOGLE | BigQuery Toolkit for SAP replication | BigQuery Toolkit for SAP | latest / confirmar versión instalada | No confirmada | 2026-07-27 | https://cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-replication | REFERENCE_ONLY | Pendiente | Referencia base del canon. |
| SRC-GOOG-003 | OFICIAL GOOGLE | BigQuery Toolkit for SAP operations | BigQuery Toolkit for SAP | latest / confirmar versión instalada | No confirmada | 2026-07-27 | https://cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations | REFERENCE_ONLY | Pendiente | Referencia base del canon. |
| SRC-GOOG-004 | OFICIAL GOOGLE | ABAP SDK for Google Cloud documentation | ABAP SDK for Google Cloud | latest / confirmar versión instalada | No confirmada | 2026-07-27 | https://cloud.google.com/sap/docs/abap-sdk | REFERENCE_ONLY | Pendiente | Portal oficial de documentación. |

## Reglas de mantenimiento

1. No eliminar filas históricas; usar `SUPERSEDED`.
2. Toda ficha debe incluir metadatos, resumen, alcance, dependencias de versión e impacto.
3. Una fuente registrada no se convierte automáticamente en política canónica.
4. No registrar URLs con tokens, parámetros sensibles o accesos temporales.
5. Para documentos internos, utilizar una referencia anonimizada y no publicar el archivo completo sin autorización.
6. La fecha de consulta debe registrarse en formato `YYYY-MM-DD`.
7. Cada cambio documental debe enlazar al menos una fuente del registro o una evidencia aprobada del piloto.
