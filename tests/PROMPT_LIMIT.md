# Validación del límite del prompt maestro

`GPT_MASTER_PROMPT.md` debe tener como máximo **8,000 caracteres**, incluyendo:

- letras y números;
- espacios;
- saltos de línea;
- símbolos Markdown;
- URLs y bloques de código.

El contenido adicional debe mantenerse en `GPT_COMPLEMENTARY_INSTRUCTIONS.md`, `ABAP_SDK_GCP_CANON.md`, manuales, runbooks y referencias.

## Ejecución

```bash
python tests/check_prompt_length.py
```

La validación falla con código distinto de cero cuando el archivo supera el límite.

## Regla de diseño

No utilizar los 8,000 caracteres completos. Mantener margen para correcciones menores sin invalidar la configuración del GPT Builder.
