from settings.config import Config

ORM = {
    'connections': {
        'default': Config.DB_CONNECTION
    },
    'apps': {
        'models': {
            'models': ['aerich', *Config.DB_MODELS]
        }
    }
}
