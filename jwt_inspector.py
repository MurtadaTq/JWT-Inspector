import base64
import json
from datetime import datetime, timezone


def base64url_decode(data):
    data += "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data)


def format_timestamp(timestamp):
    try:
        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    except Exception:
        return "Unknown"


def inspect_jwt(token):
    parts = token.strip().split(".")

    if len(parts) != 3:
        print("\n[!] Invalid JWT Token\n")
        return

    try:
        header = json.loads(base64url_decode(parts[0]))
        payload = json.loads(base64url_decode(parts[1]))
    except Exception:
        print("\n[!] Failed to decode JWT\n")
        return

    print("\n========== HEADER ==========\n")
    print(json.dumps(header, indent=4))

    print("\n========== PAYLOAD ==========\n")
    print(json.dumps(payload, indent=4))

    print("\n========== INFORMATION ==========\n")

    print(f"Algorithm : {header.get('alg', 'Unknown')}")
    print(f"Type      : {header.get('typ', 'Unknown')}")

    if "iat" in payload:
        print(f"Issued At : {format_timestamp(payload['iat'])}")

    if "exp" in payload:
        print(f"Expires   : {format_timestamp(payload['exp'])}")

        if payload["exp"] < datetime.now(timezone.utc).timestamp():
            print("Status    : Expired")
        else:
            print("Status    : Valid")

    if "iss" in payload:
        print(f"Issuer    : {payload['iss']}")

    if "sub" in payload:
        print(f"Subject   : {payload['sub']}")

    if "aud" in payload:
        print(f"Audience  : {payload['aud']}")


def main():
    print("=" * 45)
    print(" JWT Inspector")
    print(" By Murtada Tariq")
    print("=" * 45)

    token = input("\nEnter JWT Token:\n\n> ")

    inspect_jwt(token)


if __name__ == "__main__":
    main()
