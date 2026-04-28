# Proyecto 8 - HAProxy + Datadog
--------------------------------------------------------------------
# Ejecucion
```
git clone https://github.com/Katar012/proyecto8-haproxy-datadog/
cd proyecto8-haproxy-datadog
vagrant up
vagrant ssh lab
cd /vagrant
docker-compose up --build
```
### Luego verificamos en otra ventana de la misma maquina virtual "lab"
```
for i in {1..10}; do curl -s localhost:8081; done
```
--------------------------------------------------------------------
# Integrantes

### Juan David Cuero Reina.
### Juan Esteban Vila Marin.
### Alejandro Rodriguez.
### Diego Alejandro Ramirez.
