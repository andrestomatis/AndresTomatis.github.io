import requests
import json

# URL del endpoint de la API
url = 'https://eightroom.voonix.net/api/?report=advertiserearnings&list&key=c2fb5fb9293a5ebe1c83ae8d53b1ca5773456fd9&start=2023-06-28&end=2023-06-28'

# TENGO QUE ESCRIBIR LA FECHA DE MANERA DINAMICA PARA QUE CADA VEZ QUE HAGA EL REQUEST, LA FECHA SEA LA ACTUAL

# Realizar la solicitud GET
response = requests.get(url)

# Verificar el código de estado de la respuesta
if response.status_code == 200:  # 200 significa éxito
    # Acceder a los datos de respuesta (en formato JSON en este caso)
    data = response.json()
    json_result = json.dumps(data)

else:
    # La solicitud no tuvo éxito, mostrar el código de estado
    print('La solicitud no tuvo éxito. Código de estado:', response.status_code)

primer_caracter = json_result[0]
resto = json_result[119:]

json_result_ok = primer_caracter + resto

import json

def modify_json(json_data):
    # Cargar los datos JSON desde la variable
    data = json.loads(json_data)

    modified_data = []
    for month, month_data in data['data'].items():
        for advertiser_id, advertiser_data in month_data.items():
            for login_id, login_data in advertiser_data.items():
                for campaign_id, campaign_data in login_data.items():
                    for date, date_data in campaign_data.items():
                        item = {
                            "month": month,
                            "advertiser_id": advertiser_id,
                            "login_id": login_id,
                            "campaign_id": campaign_id,
                            "date": date,
                            **date_data
                        }
                        modified_data.append(item)

    return modified_data

# Cadena JSON previamente definida


# Modificar el JSON
modified_data = modify_json(json_result_ok)