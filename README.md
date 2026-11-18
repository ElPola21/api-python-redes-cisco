# El script automatiza la generación de un inventario de red exportable a partir de los datos devueltos por la API de Cisco.
# Utiliza la lógica de autenticación y consulta de dispositivos/hosts de los scripts previos, procesa la respuesta JSON y escribe los atributos relevantes (hostname, dirección IP, plataforma, versión o estado) en un archivo .csv mediante el módulo nativo csv de Python.
