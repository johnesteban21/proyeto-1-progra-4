from sodapy import Socrata
import pandas as pd


def conexion_da():
    client = Socrata("www.datos.gov.co", None)
    return client


def consultar(departamento, municipio, cultivo, limit):
    client = conexion_da()
    results = client.get("ch4u-f3i5", limit=limit,
                         where=f"departamento='{departamento}' AND municipio='{municipio}' AND cultivo='{cultivo}'")

    if not results:
        print("No se encontraron datos para los criterios seleccionados.")
        return None

    results_df = pd.DataFrame.from_records(results)

    for columna in ['ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']:
        if columna in results_df.columns:
            results_df[columna] = pd.to_numeric(results_df[columna], errors='coerce')

    return results_df


def calcular_mediana(df, columnas_edaficas):
    medianas = {}
    for columnas in columnas_edaficas:
        # Convertir los datos a numéricos, ya que son de tipo texto
        df[columnas] = pd.to_numeric(df[columnas], errors='coerce')
        medianas[columnas] = df[columnas].median()

    # Mapear nombres de columnas a nombres más legibles
    mapeo_nombres = {
        'ph_agua_suelo_2_5_1_0': 'PH',
        'f_sforo_p_bray_ii_mg_kg': 'Fosforo',
        'potasio_k_intercambiable_cmol_kg': 'Potasio'
    }

    medianas_legibles = {mapeo_nombres.get(nombre_columna, nombre_columna): valor_mediana for nombre_columna, valor_mediana in medianas.items()}

    return medianas_legibles
