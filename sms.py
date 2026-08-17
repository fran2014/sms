import requests

# URL base de la API de TextBelt
url = 'https://textbelt.com/text'

# Ingresa el número de teléfono al que deseas enviar el mensaje
print('Ingrese el número telefonico al que desea enviar el mensaje.')
receiver = input()

# Ingresa el mensaje que deseas enviar
print('Escriba el mensaje que desea enviar')
message = input()

# Parámetros de la solicitud POST
payload = {
    'phone': receiver,
    'message': message,
    'key': 'textbelt',  # La clave 'textbelt' se utiliza para el plan gratuito de TextBelt
}

# Realiza la solicitud POST a la API de TextBelt
response = requests.post(url, data=payload)

# Verifica el estado del envío
if response.json().get('success'):
    print("Mensaje enviado con éxito.")
else:
    print("Error al enviar el mensaje.")
