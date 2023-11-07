Documentación de la API de Datos Meteorológicos - Prueba Técnica
Estimado equipo de evaluación,

Me complace presentar la documentación y los detalles de la API de Datos Meteorológicos que he desarrollado como parte de la prueba técnica propuesta. A continuación, se detallan los pasos necesarios para poner en funcionamiento la API, así como las decisiones técnicas y las justificaciones detrás de mi enfoque, pido disculpas por responder tarde a este email, lo habia recibido en la carpeta de spam, y solo hoy pude notarlo, 4 dias tarde pero espero tener la oportunidad de trabajar en su equipo o que me tengan en cuenta para futuras vacantes.

Puesta en Marcha
Requisitos Previos
Para ejecutar la API, se necesita tener Docker y Docker Compose instalados. Estas herramientas permiten la contenerización de la aplicación y aseguran un despliegue consistente.

Instrucciones de Ejecución
Clonar el repositorio del proyecto.
Navegar al directorio del proyecto a través de la terminal.
Ejecutar docker-compose up para iniciar los servicios de la API y la base de datos MySQL.
Utilizar Postman o cualquier cliente HTTP para interactuar con los endpoints de la API.
Estructura de la API
La API cuenta con tres endpoints principales:

GET /api/data: Recupera datos actuales de condiciones meteorológicas de un servicio externo.
POST /api/data: Almacena los datos recuperados en una base de datos MySQL.
GET /api/data/{id}: Obtiene un registro específico por ID de la base de datos.
Tecnologías y Decisiones Técnicas
Para el desarrollo de esta API, tomé la decisión de utilizar FastAPI. A pesar de tener más experiencia con Flask, opté por FastAPI para demostrar mi versatilidad y capacidad de adaptación a nuevas tecnologías. FastAPI ofrece un rendimiento superior y capacidades modernas de asincronía que me permitieron aprender y aplicar mejores prácticas en el desarrollo de APIs modernas.

El proceso de desarrollo tomó aproximadamente 6 horas, con recesos estratégicos de 15 minutos cada dos horas, para mantener un alto nivel de concentración y eficiencia.

Comentarios y Documentación del Código:
He puesto especial cuidado en la claridad y estructura del código. Cada función y clase cuenta con comentarios explicativos que facilitan la comprensión y mantenibilidad del código.

Además, he incluido un conjunto de pruebas Postman que evidencian el correcto funcionamiento de la API, las cuales estaré encantado de demostrar y explicar durante una presentación técnica o entrevista.

API utilizada:
Obtuve la API de manera gratuida en la web de RapidApi aunque tiene solicitudes limitadas me fue de mucha utilidad para presentar la prueba tecnica, la API usada para esta prueba fue: AI Weather by Meteosource. Aunque al enviar esta prueba tecnica ocultare la API al igual que usuario y contraseñas de MySQL.

Conclusión
Espero que esta documentación proporcione una visión clara de mi enfoque y ejecución en esta prueba técnica. Estoy abierto a cualquier pregunta y agradecería la oportunidad de discutir mi trabajo en detalle.

Atentamente,

Javier Perez