#!/usr/bin/env python3
"""
JWT Decoder (Header & Payload Only)
Author: Anton Lepari dan ChatGPT

Decode Base64URL JWT header & payload WITHOUT verifying signature.
Useful for debugging or inspecting JWT structure.
"""

import base64
import json
import sys


def b64url_decode(x: str) -> dict:
    """Decode Base64URL string into JSON."""
    padded = x + "=" * (-len(x) % 4)
    return json.loads(base64.urlsafe_b64decode(padded).decode())


def decode_jwt(token: str):
    """Split JWT & decode header and payload."""
    parts = token.split(".")
    if len(parts) < 2:
        print("Invalid JWT format.")
        return

    header, payload = parts[0], parts[1]

    print("=== HEADER ===")
    print(json.dumps(b64url_decode(header), indent=4))

    print("\n=== PAYLOAD ===")
    print(json.dumps(b64url_decode(payload), indent=4))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 decode_jwt.py <jwt_token>")
        sys.exit(1)

    decode_jwt(sys.argv[1])
