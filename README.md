# MAS Pronombres 🇪🇸

Helper ligero para **Monika After Story (MAS)** que facilita el uso de pronombres, artículos y concordancia de género en submods en español.

---

## 📦 Instalación

1. Descarga la versión más reciente desde [Releases](../../releases).
2. Descomprime el zip `mas_pronombres_es` dentro del directorio del juego

## 💡 ¿Cómo funciona?

El script añade dos funciones idénticas (`gen` y `w`) que devuelven texto dinámico según la configuración del usuario (`persistent.gender`):
- **`f`**: Femenino (por defecto `"a"`)
- **`m`**: Masculino (por defecto `"o"`)
- **`x`**: Neutro / Otro (por defecto `"e"`)

---

## 🛠️ Ejemplos de uso en los diálogos

### 1. Para cambiar terminaciones o letras sueltas (`gen`)
Puedes intercalar la función directamente dentro de los corchetes del texto:

```renpy
m "¡Qué bueno verte, bienvenid[gen('a', 'o', 'e')]!"
m "Sabía que eras un[gen('a', 'o', 'e')] chic[gen('a', 'o', 'e')] genial."
```
### 2. Para cambiar palabras completas (w)
También puedes usar w() para devolver palabras enteras según el género:

```renpy
m "Eres mi mejor [w('amiga', 'amigo', 'amigue')] del mundo."
m "Ten cuidado, [w('muchacha', 'muchacho', 'chique')]."
```

_Creado por CofKaf para la comunidad hispanohablante de Monika After Story._
