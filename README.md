# Real Estate Website Clone

A clone website for property listings using Django. 

## Running application using local Python environment 

1. Create a virtual environment using venv
```bash 
  python -m venv venv
```
2. Activate the virtual environment in powershell, for MacOS or Linux follow [this link](https://docs.python.org/3/library/venv.html)
```bash 
  venv/Scripts/Activate.ps1
```
3. To install run necessary packages
```bash 
  pip install -r requirements.txt
```
4. Once installed run following command to start server
```bash 
  python manage.py runserver
```

## Running using Docker

1. Use following commands to run
```bash 
  docker build -t your_custom_container_name .
  docker run -d --restart=unless-stopped -p 8000:8000 --name=your_custom_container_name your_custom_container_name
  docker logs -f your_custom_container_name
```

1. Else for MacOS or Linux users use:
```bash 
  sudo bash build-image.sh
```