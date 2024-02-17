DATABASES = {
        'default': {
            'ATOMIC_REQUESTS': true,
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': "awx",
            'USER': "awx",
            'PASSWORD': "awxpass",
            'HOST': "10.0.116.93",
            'PORT': "5432",
        }
}

BROADCAST_WEBSOCKET_SECRET = "Qzg4OUw1U0dXWFZVeElPV3k4eUhXekdyX1R2MGowUzExcjAyd2ppWnJwOlosRVJPeDowaW9IMzNndGdyS2s2ellxM2luWlU5ckpfZ0E0ZEdrcjFfTWpQSHRmYTd5dVY5UmtxLFVPSjFIZnZYR25FeWp2TWx5WDBEQVBvYTNzV1E="