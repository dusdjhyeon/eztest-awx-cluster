DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "dVdsWGs4SmhKN1YtNUMscFNsa2hpSS5ZQkQwOVhtR2dUaWQwV1VuVlZxSlI4dXZ4UUlCclA3Tm84M1l6VEpEaUJraG8yaV9PUm5FRUQsUFM1cWVLS1docywtYVREdzR3dFF6ZEdwREI1VktoU3lWcDE6LEZVZ2M1NG1yWG1KZzI="
