## Creación de clases avanzando el proyecto en las US

Para la la creación del sistema, es necesario definir unas estructuras que sirvan de base para la operación de la aplicación del plaroyecto. Estas son las estructuras que se han definido: 

- UserProfile: Gestiona la información del perfil del usuario, incluyendo habilidades y experiencia. Permite añadir o eliminar servicios ofrecidos. Esta tiene un método receive_rating para permitir que los usuarios reciban calificaciones de otros usuarios, cumpliendo con la []().

- Service: Representa un servicio o habilidad ofrecida en la plataforma, con detalles como nombre, descripción y precio. Posee un método add_rating para agregar calificaciones a un servicio, lo que permite implementar el sistema de calificaciones mencionado en la []().

- Rating: Permite calificar servicios o usuarios, con un sistema de puntuación y comentarios y un sistema de referencia al servicio calificado para vincular las entidades.

- Transaction: Gestiona las transacciones entre compradores y vendedores, incluyendo el seguimiento del estado de la transacción.
La existencia de esta clase permite las transacciones, cumpliendo la []().

- Chat: Facilita la comunicación entre usuarios con un sistema de mensajería. La existencia de esta clase permite la comunicación interna, cumpliendo la []().

- ServiceMarketplace: Es la clase principal que gestiona la plataforma, permitiendo registrar usuarios, añadir servicios o buscar servicios con filtros específicos. Esta clase tiene métodos como _search_services_ con una subfunción _matches_filter (para implementar la búsqueda de servicios usando filtros específicos), _create_transaction_ para manejar la creación de transacciones o start_chat para iniciar una conversación entre usuarios.

Todos estas clases y sus respectivos métodos se pueden encontrar [aquí](/././src/SvcMkp.py).
