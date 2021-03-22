# Elastoo task
## Documentation
[https://elastoo.kosyachniy.com:9443/docs](https://elastoo.kosyachniy.com:9443/docs)

## Usage
Use scripts for check API methods:
* [Create task](requests/add_task.sh)
* [Get processed results](requests/get_results.sh)
* [Get current task queue](requests/get_tasks.sh)

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