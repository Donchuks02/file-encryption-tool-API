# File Encryption Tool API

## Overview
The File Encryption Tool API is a scalable and efficient solution for encrypting and decrypting files, managing encryption keys, and analyzing encryption usage. This API enables individuals and organizations to secure sensitive data through intuitive and robust endpoints, supporting web and mobile front-end applications.

---

## Features

### User Management
- **Sign Up:** Register a new user.
- **Login:** Authenticate an existing user.
- **Profile Management:** Update user profile information.

### File Encryption and Decryption
- **Encrypt Files:** Upload a file and apply encryption.
- **Decrypt Files:** Decrypt an uploaded file using the correct key or password.
- **Key Management:** Generate, view, and manage encryption keys.

### File Management
- **List Encrypted Files:** View details of all encrypted files.
- **Delete Files:** Remove encrypted files from the system.

### Analytics and Reporting
- **Encryption Statistics:** View metrics on encryption usage, such as number of encrypted files and methods used.
- **Download Reports:** Export encryption activity reports for record-keeping.

### Administrator Features
- **User Management:** Manage user accounts, reset passwords, and handle queries.
- **System Monitoring:** Monitor system performance and usage statistics.

---

## API Endpoints

### User Management
- `POST /signup`: Register a new user.
- `POST /login`: Authenticate a user.
- `GET /profile`: Retrieve profile details.
- `PUT /profile`: Update profile information.

### File Encryption and Decryption
- `POST /encrypt`: Upload a file to encrypt.
- `POST /decrypt`: Upload an encrypted file for decryption.
- `POST /keys`: Manage encryption keys.

### File Management
- `GET /files`: Retrieve a list of encrypted files.
- `DELETE /files/{id}`: Delete an encrypted file.

### Analytics and Reporting
- `GET /analytics`: Retrieve encryption usage statistics.
- `GET /reports`: Download encryption activity reports.

---

## Installation

### Prerequisites
- Python 3.10+
- Docker and Docker Compose
- PostgreSQL

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/file-encryption-tool.git
   cd file-encryption-tool
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Set up environment variables in a `.env` file:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   If using Docker, make the wait-for-it.sh script executable:

   ```bash
   chmod +x wait-for-it.sh

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Or, use Docker:
   ```bash
   docker-compose up --build
   ```

---

## Usage

### Encrypt a File
Send a `POST` request to `/encrypt` with a file and encryption method.

### Decrypt a File
Send a `POST` request to `/decrypt` with the encrypted file and the correct key.

### Manage Files
- Retrieve a list of encrypted files using `GET /files`.
- Delete a file with `DELETE /files/{id}`.

### View Analytics
Access encryption statistics via `GET /analytics`.

---

## Security
- HTTPS for encrypted data transmission.
- Input validation to prevent SQL injection and XSS.
- Secure encryption algorithms such as AES and RSA.

---

## Testing
Run the test suite using:
```bash
pytest tests/
```

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or feedback, please contact [chukwudidavid02@gmail.com](mailto:chukwudidavid02@gmail.com).

---

## Acknowledgments
Special thanks to [master_backend](https://projects.masteringbackend.com/) for providing valuable tools and resources.

