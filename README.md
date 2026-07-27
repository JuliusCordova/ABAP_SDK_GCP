# ABAP_SDK_GCP

Repositorio gobernado para las políticas, prompts, referencias y documentación del GPT personalizado `ABAP SDK GCP Copilot`.

## Archivos principales

- `ABAP_SDK_GCP_CANON.md`: políticas canónicas.
- `GPT_MASTER_PROMPT.md`: instrucciones esenciales del GPT; máximo 8,000 palabras.
- `GPT_COMPLEMENTARY_INSTRUCTIONS.md`: reglas ampliadas, plantillas y flujos operativos.
- `ABAP_SDK_GCP_KNOWLEDGE_GOVERNANCE.md`: ingestión y actualización documental.
- `CUSTOM_GPT_BUILDER_CONFIG.md`: configuración para desplegar el GPT personalizado.
- `references/SOURCE_REGISTRY.md`: inventario de fuentes oficiales, internas y experimentales.

## Regla de gobierno

`main` contiene conocimiento aprobado. Las ramas y Pull Requests contienen propuestas pendientes de revisión.

El prompt maestro debe mantenerse dentro del límite de 8,000 palabras. El detalle adicional se conserva en documentos complementarios de GitHub que el prompt referencia explícitamente.

## Respuestas del GPT

Las respuestas técnicas deben incluir procedimientos completos, validación end-to-end, criterios GO/NO-GO, rollback y enlaces a la documentación gobernada y oficial.

## Integración GitHub

La consulta en tiempo real requiere una App conectada o una Acción personalizada. Los archivos cargados como Knowledge son copias estáticas y no se sincronizan automáticamente con el repositorio.
