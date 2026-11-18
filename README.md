## Descripción de los scripts

* `src/01_get-ticket.py`: Envía las credenciales de acceso al controlador mediante una petición `POST` y obtiene el token de autenticación (*service ticket*) necesario para realizar las consultas posteriores.
* `src/02_get-network-device.py`: Consulta a través de la API REST el listado de dispositivos de red administrados (routers, switches) y muestra los datos obtenidos.
* `src/03_get-host.py`: Consulta a través de la API REST los hosts finales conectados a la red detectados por el controlador.
* `src/04_tabulate.py`: Consulta los dispositivos de red desde la API y los muestra en consola formateados como una tabla legible utilizando la librería `tabulate`.
* `src/05_inventario_csv.py`: Automatiza la generación de un inventario de red exportable. Utiliza la lógica de autenticación y consulta de los scripts previos, procesa la respuesta JSON y escribe los atributos relevantes (hostname, dirección IP, plataforma, versión y estado) en un archivo `.csv` mediante el módulo nativo `csv` de Python.
