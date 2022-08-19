docker build -t iris:0.1.0 .
<!-- docker run -i -d -p 8001:8001 iris:0.1.0 -->
kind load docker-image iris:0.1.0

kubectl apply -f iris_service.yaml

kubectl port-forward service/flask-service 1080:1080
