CONT_NAME=db
IMG_NAME=dbimg:dev

docker stop $CONT_NAME
docker rm   $CONT_NAME
docker rmi  $IMG_NAME

docker build -t $IMG_NAME .
docker run -d --name $CONT_NAME -p 1123:1123 $IMG_NAME
