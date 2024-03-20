class InMemoryStorage:
    def __init__(self):
        self.data = []

    def save(self, ip, path):
        self.data.append({'ip': ip, 'path': path})

    def get_all(self):
        return self.data

class SimpleLimiter:
    def is_allowed(self, ip):
        # Logica di rate limiting fittizia: permette sempre
        return True
