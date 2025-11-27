#!/usr/bin/env python3
"""
Fake / Dummy JWT Generator (Unsigned JWT)
Author: Anton Lepari dan ChatGPT

This script generates a **non-signed JWT** using the "alg": "none" header.
Useful for:
- Testing
- Debugging payloads
- Prototyping authentication flows
- Demonstrating JWT structure

NOT for production use.
"""

import base64
import json
import sys


def b64url_encode(data: dict) -> str:
    """Encode dict to Base64URL without padding (=)."""
    raw = json.dumps(data, separators=(",", ":")).encode()
    encoded = base64.urlsafe_b64encode(raw).rstrip(b"=")
    return encoded.decode()


def generate_jwt(payload: dict) -> str:
    """Generate unsigned JWT with alg=none."""
    header = {"alg": "none", "typ": "JWT"}
    h = b64url_encode(header)
    p = b64url_encode(payload)
    return f"{h}.{p}."


if __name__ == "__main__":
    # If payload provided as CLI argument
    if len(sys.argv) > 1:
        try:
            payload = json.loads(sys.argv[1])
        except Exception:
            print("Invalid JSON payload. Example:\npython3 fake_jwt.py '{\"user\":\"minsx\"}'")
            sys.exit(1)
    else:
        payload = {"user": "minsx"}

    token = generate_jwt(payload)
    print(token)
