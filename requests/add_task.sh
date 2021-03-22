curl -w "\n%{time_total}\n" -X POST -d '{"num": 0, "timeout": 1.5}' http://localhost:5000/tasks
curl -w "\n%{time_total}\n" -X POST -d '{"num": 5, "timeout": 0.5}' http://localhost:5000/tasks