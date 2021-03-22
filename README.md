# Elastoo task
## Run (With Docker)
### Local
```
cd docker/
docker-compose up --build
```

### Production
```
cd docker/
docker-compose -f docker-compose.prod.yml up --build
```

## Run (Without Docker)
1. Set environment
```
pip install -r requirements.txt
```

2. Entry point: ` run.sh `