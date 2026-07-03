
# JWT Inspector

A lightweight Python tool for inspecting and decoding **JSON Web Tokens (JWT)** locally.

JWT Inspector allows you to safely decode JWT headers and payloads without sending any data to external servers.

> **Disclaimer:** This tool is intended for educational and defensive security purposes only. It does **not** verify signatures, modify tokens, or perform any offensive actions.

---

## ✨ Features

- Decode JWT Header
- Decode JWT Payload
- Display Algorithm
- Display Token Type
- Show Issued At (`iat`)
- Show Expiration Time (`exp`)
- Check if the token has expired
- Display Issuer (`iss`)
- Display Subject (`sub`)
- Display Audience (`aud`)
- Works completely offline
- No external dependencies

---

## 📦 Requirements

- Python 3.8+

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/DevDebo/JWT-Inspector.git
```

Enter the project directory:

```bash
cd JWT-Inspector
```

---

## ▶️ Usage

Run the script:

```bash
python jwt_inspector.py
```

Paste your JWT token when prompted.

---

## 📸 Example

### Input

```text
> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Output

```text
=============================================
 JWT Inspector
 By Murtada Tariq
=============================================

========== HEADER ==========

{
    "alg": "HS256",
    "typ": "JWT"
}

========== PAYLOAD ==========

{
    "sub": "123456789",
    "name": "John",
    "iat": 1710000000,
    "exp": 1910000000
}

========== INFORMATION ==========

Algorithm : HS256
Type      : JWT
Issued At : 2024-03-09 16:00:00 UTC
Expires   : 2030-07-18 00:53:20 UTC
Status    : Valid
Subject   : 123456789
```

---

## 📁 Project Structure

```text
JWT-Inspector/
│
├── jwt_inspector.py
├── README.md
└── LICENSE
```

---

## 🗺️ Roadmap

- [ ] Colored terminal output
- [ ] Export decoded data as JSON
- [ ] Save analysis reports
- [ ] Read JWT from files
- [ ] Interactive menu
- [ ] Improved error handling

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed with ❤️ by **Murtada Tariq**

If you found this project useful, consider giving it a ⭐ on GitHub.

