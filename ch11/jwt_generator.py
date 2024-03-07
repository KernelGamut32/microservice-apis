from datetime import datetime, timedelta
from pathlib import Path
import uuid

import jwt
from cryptography.hazmat.primitives import serialization


def generate_jwt():
    now = datetime.utcnow()
    payload = {
        "iss": "https://auth.mycompany.io/",
        "sub": str(uuid.uuid4()),
        "aud": "http://127.0.0.1:8000/orders",
        "iat": (now + timedelta(hours=-5)).timestamp(),
        "exp": (now + timedelta(hours=24)).timestamp(),
        "scope": "openid",
    }

    private_key_text = Path("new_key.pem").read_text()
    private_key = serialization.load_pem_private_key(
        private_key_text.encode(),
        password=None,
    )
    return jwt.encode(payload=payload, key=private_key, algorithm="RS256")


print(generate_jwt())
