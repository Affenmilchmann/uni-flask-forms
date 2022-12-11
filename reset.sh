CONT_NAME=homework
IMG_NAME=hw5
V=0.1

docker stop $CONT_NAME
docker rm $CONT_NAME
docker rmi $IMG_NAME:$V
docker build -t $IMG_NAME:$V .
docker run -d -p 8080:5000 --name $CONT_NAME $IMG_NAME:$V