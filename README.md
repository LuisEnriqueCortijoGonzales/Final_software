# Final_software

Este es el examen final de software.

## Solo requiere de Flask

## Pregunta 1

En los archivos clases.py, BD.py y app.py.

## Pregunta 2

Para ejecutar las pruebas, utiliza el siguiente comando en la terminal: 
```
python -m unittest -v test_app.py
```

## Pregunta 3

Asumiendo que broadcast en este contexto se refiere a enviar un mensaje o notificación a todos los contactos.
1. Primero a la clase Usuario le añadiria un atributo con el cual pueda almacenar y manejar el numero de mensajes enviados y el costo total de los mensajes asociados al usuario.
2. En la clase Mensaje añadiria un atributo asociado al costo del mensaje.
3. En el metodo de envio de mensajes realizaria la mayoria de cambios, como el sistema de notificación a contactos apoyado del metodo ya implementado que retorna los contactos de un usuario, la asociación de costos del mensaje y adicional a esto implementaria un nuevo metodo para obtener el costo_total de cada cliente.
4. A su ves esto supondria realizar nuevos y mayores casos de prueba nuevos a la aplicación como lo son la notificación y que los costos de los mensajes esten correctos al numero de mensajes enviados por los usuarios.

No existe mucho riesgo de romper lo ya implementado porque el app esta en un estado muy simple y a su vez esta se encuentra correctamente organizada en varios archivos que manejan cada aspecto del app, como funcionalidad, clases y datos. Sumado a la implementación de pruebas para monitorerar como va el app diria que es casi nulo "romper" el app. 