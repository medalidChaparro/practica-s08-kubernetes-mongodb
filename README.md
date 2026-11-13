# PRACTICA S08 - DESPLIEGUE DE BACKEND CON KUBERNETES

## 1. Descripcion del proyecto

Implementacion y despliegue de una API Backend desarrollada
con Flask y Python, conectada a una base de datos MongoDB,
utilizando Kubernetes.

## 2. Tecnologias utilizadas

- Kubernetes
- Docker
- Python 3.12
- Flask
- MongoDB 7.0
- YAML
- Killercoda

## 3. Arquitectura del proyecto

- Namespace: practica-s08
- Backend: Flask
- Base de datos: MongoDB
- Puerto Backend: 5000
- Puerto MongoDB: 27017
- NodePort: 30080

## 4. Configuraciones implementadas

- Creacion del Namespace.
- Configuracion de variables mediante ConfigMap.
- Gestion de credenciales mediante Secret.
- Despliegue de MongoDB mediante Deployment.
- Creacion del servicio interno ClusterIP.
- Despliegue del Backend Flask.
- Exposicion del Backend mediante NodePort.

## 5. Endpoints disponibles

### Inicio
GET /

Devuelve informacion general de la aplicacion.

### Health Check
GET /health

Verifica el estado del Backend.

### Conexion con MongoDB
GET /db

Comprueba la conexion entre Flask y MongoDB.

## 6. Despliegue en Kubernetes

Ejecutar los siguientes comandos:

```bash
kubectl apply -f k8s/00-namespace.yaml
kubectl apply -f k8s/01-app-configmap.yaml
kubectl apply -f k8s/02-db-secret.yaml
kubectl apply -f k8s/03-mongo-stack.yaml
kubectl apply -f k8s/04-backend-stack.yaml
```

## 7. Verificacion

Consultar los Pods y servicios:

```bash
kubectl get pods,services -n practica-s08
```

Consultar los nodos:

```bash
kubectl get nodes -o wide
```

Probar el Backend:

```bash
curl http://172.30.1.2:30080/
curl http://172.30.1.2:30080/health
curl http://172.30.1.2:30080/db
```

## 8. Resultados obtenidos

- Backend desplegado correctamente.
- MongoDB en estado Running.
- Conexion entre Backend y MongoDB exitosa.
- Endpoint Health funcionando.
- Servicio NodePort funcionando en el puerto 30080.

## 9. Conclusion

Se logro desplegar una API Backend con Flask y MongoDB
dentro de un entorno Kubernetes, verificando la comunicacion
entre los servicios y el acceso externo mediante NodePort.

