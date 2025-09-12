# Data persistence with containers

> If you want to persist data even after a container is deleted, you can use a volume. A volume is a location in your local filesystem, managed by Docker.


**Adding volumes for a database**
```yml
todo-database:
    # ...
    volumes:
      - database:/data/db
```

- The volumes element that is nested in todo-database tells Compose to mount the volume named database to /data/db in the container for the todo-database service.

- The top-level volumes element defines and configures a volume named database that can be used by any of the services in the Compose file.


**Adding a bind mount to compose**
```bash
todo-app:
    # ...
    volumes:
      - ./app:/usr/src/app
      - /usr/src/app/node_modules
```
