# Workshop FastAPI - APIC 📸
_Eng. David Pinchao_ <br>
_Universidad de Nariño_ <br>
_Ipiales_ <br>
_2024_

### Introduction

This repository is a workshop focused on learning FastAPI and building robust, high-performance, and fully documented web APIs. ⚡️

You'll learn to integrate a multimodal model (vision-to-text) seamlessly with other applications through the API while diving into the full development lifecycle. This includes working with databases 📊, writing unit tests 🧪, highlighting the best practices 🙌, and creating thorough documentation to ensure well-structured and scalable APIs 📄.

Join us and start building powerful, real-world APIs!

### Setup 👷

**Requirements**

- Python3.10 🐍
- Docker & Compose 🐳
- Editor 📝

In case you need to install these requirements follow [this guide](https://splashy-watercress-0c3.notion.site/Instalaci-n-requerimientos-FastAPI-cf3740a8ecbe4a9586c8bda6cf90b6b2).

**Installation** 
  
The Makefile is a file that contains the commands that you need to run by simply running `make <action>`. If you run into some problems copy and paste the command present within the file.

1. Build the docker image:
   
  ```bash
  make build
  ```

2. Run the application:

  ```bash
  make up
  ```

3. Stop the application:
   
  ```bash
  make down
  ```

4. Run tests:

  ```bash
  make test
  ```

(Optional) Set up the editor with the packages so this can read the access to different packages used by the app:

```bash
make env
make install
```

### Play around with the API ⏯️

The app should be served through the uvicorn server running on `localhost:8000`, you may not know the API endpoints so take a look at the documentation in the following endpoints:

```
/docs
/redoc
```

Now you can discover and play with this amazing API, congratulations 🎉.
