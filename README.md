# ABAP_SDK_GCP

Repositorio gobernado para las políticas, prompts, referencias y documentación del GPT personalizado `ABAP SDK GCP Copilot`.

## Archivos principales

- `ABAP_SDK_GCP_CANON.md`: políticas canónicas.
- `ABAP_SDK_GCP_KNOWLEDGE_GOVERNANCE.md`: ingestión y actualización documental.
- `GPT_MASTER_PROMPT.md`: instrucciones maestras del GPT.
- `CUSTOM_GPT_BUILDER_CONFIG.md`: configuración para desplegar el GPT personalizado.
- `references/SOURCE_REGISTRY.md`: inventario de fuentes.

## Regla de gobierno

`main` contiene conocimiento aprobado. Las ramas y Pull Requests contienen propuestas pendientes de revisión.

## Respuestas del GPT

Las respuestas técnicas deben incluir procedimientos completos, validación end-to-end, criterios GO/NO-GO, rollback y enlaces a la documentación gobernada y oficial.

## Integración GitHub

La consulta en tiempo real requiere una App conectada o una Acción personalizada. Los archivos cargados como Knowledge son copias estáticas y no se sincronizan automáticamente con el repositorio.

## Documentación oficial base

- ABAP SDK for Google Cloud.
- BigQuery Toolkit for SAP overview.
- BigQuery Toolkit for SAP replication.
- BigQuery Toolkit for SAP operations.
