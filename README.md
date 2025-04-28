# POO_Encapsulamiento-Polimorfismo
# Ejercicio 1: Registro de Notas 
--------------------------------------------------
- Clase Estudiante con atributos privados: _nombre, _codigo y _notas.
- Propiedades:
    - nombre: getter y setter que valida que no esté vacío.
    - codigo: getter y setter que valida que sea alfanumérico.
- Métodos:
    - agregar_nota(nota): Añade una nota si está entre 0.0 y 5.0.
    - calcular_promedio(): Retorna el promedio de notas.
    - es_aprobado(): Retorna True si el promedio es mayor o igual a 3.0.

# Ejercicio 2: Gestión de Cartera de Criptomonedas 
-----------------------------------------------------------------------
- Clase CarteraCripto con atributos privados: _usuario y __saldo_btc.
- Métodos:
    - consultar_saldo(): Retorna el saldo actual en BTC.
    - comprar_btc(monto_usd, precio_actual_btc): Convierte USD a BTC y lo añade al saldo.
    - vender_btc(monto_btc, precio_actual_btc): Vende BTC y retorna el equivalente en USD.
    - No se puede vender más BTC de los que se tienen disponibles.
- El saldo BTC se mantiene encapsulado y solo es accesible mediante métodos.

# Ejercicio 3: Sistema de Seguridad 
---------------------------------------------------
- Clase Empleado con atributos privados: __nombre, __rol, __clave_acceso.
- Propiedades:
    - nombre y rol: solo lectura.
- Métodos:
    - verificar_clave(clave_ingresada): Verifica si la clave ingresada es correcta (comparación con la clave cifrada).
    - cambiar_clave(clave_antigua, nueva_clave): Cambia la clave solo si la antigua es válida.
- La clave se almacena cifrada invirtiendo el string.

# Ejercicio 4: Sistema de Personas en Hospital
-------------------------------------------------------------------------
- Clase base Persona:
    - Atributos privados: __nombre, __edad, __documento.
    - Propiedades y setters para acceder a los datos (validar edad >= 0).

- Clase Paciente (hereda de Persona):
    - Atributos privados: __diagnostico, __historial (lista).
    - Métodos:
        - agregar_historial(entrada)
        - ver_historial()
        - ver_diagnostico()

- Clase Doctor (hereda de Persona):
    - Atributo privado: __especialidad.
    - Métodos:
        - ver_especialidad()
        - modificar_diagnostico(paciente, nuevo_diagnostico): Solo si paciente es instancia de Paciente.
        - 
# Ejercicio 5: Tipos de Transporte 
-----------------------------------------------------------
- Clase base Transporte con método tipo_transporte().
- Clases hijas:
    - Coche: tipo_transporte() imprime "Transporte terrestre."
    - Avion: tipo_transporte() imprime "Transporte aéreo."
    - Barco: tipo_transporte() imprime "Transporte marítimo."

# Ejercicio 6: Sistema de Empleados 
-----------------------------------------------------------------------------
- Clase base Empleado:
    - Atributos privados: __nombre, __sueldo_base.
    - Getters y setters para sueldo_base.
    - Método calcular_salario() básico.
- Clases hijas:
    - EmpleadoFijo: Usa el sueldo base.
    - EmpleadoPorHoras: Multiplica sueldo_base por horas_trabajadas.
    - EmpleadoTemporal: Calcula sueldo proporcional a días trabajados.
- Uso de polimorfismo: llamar calcular_salario() en una lista de empleados.

