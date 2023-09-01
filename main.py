from api import consultar, calcular_mediana
import ui

ui.mensaje_bienvenido()
departamento, municipio, cultivo, limit = ui.pantalla_pedir_datos()
resultados = consultar(departamento,municipio,  cultivo, limit)
if resultados is None:

    exit()
# Calcula las medianas
columnas_edaficas = ['ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']
medianas = calcular_mediana(resultados, columnas_edaficas)

# Muestra los resultados
ui.mostrar_resultados(resultados, medianas)
