class Config:
    # Configurazioni comuni
    pass

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # Altre configurazioni specifiche per il testing