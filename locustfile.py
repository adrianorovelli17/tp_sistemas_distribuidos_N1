from locust import HttpUser, task, between

class UsuarioHotSale(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def comprar(self):
        self.client.post("/orders?producto_id=1&cantidad=1")

    @task(7)
    def ver_catalogo(self):
        self.client.get("/products")