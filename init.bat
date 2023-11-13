
docker-compose exec config01 sh -c "mongosh --port 27017 < /scripts/init-configserver.js"


docker-compose exec shard01a sh -c "mongosh --port 27017 < /scripts/init-shard01.js"


docker-compose exec shard02a sh -c "mongosh --port 27017 < /scripts/init-shard02.js"


docker-compose exec shard03a sh -c "mongosh --port 27017 < /scripts/init-shard03.js"


@echo off
echo WAIT 20s : CONFIGURATION OF THE REPLICATS 
timeout /t 20 /nobreak
echo Fin de la pause


docker-compose exec router sh -c "mongod"


docker-compose exec router sh -c "mongosh < /scripts/init-router.js"


docker-compose exec router sh -c "mongosh < /scripts/users.js"


docker-compose exec router-replica sh -c "mongod"


docker-compose exec router-replica sh -c "mongosh < /scripts/init-router.js"


docker-compose exec router-replica sh -c "mongosh < /scripts/users.js"