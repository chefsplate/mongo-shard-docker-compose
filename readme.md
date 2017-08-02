Mongo Sharded Cluster with Docker Compose
=========================================
A simple sharded Mongo Cluster with a replication factor of 2 running in `docker` using `docker-compose`.

Designed to be quick and simple to get a local or test environment up and running. Needless to say... DON'T USE THIS IN PRODUCTION!

Heavily inspired by [https://github.com/jfollenfant/mongodb-sharding-docker-compose](https://github.com/jfollenfant/mongodb-sharding-docker-compose)

### Mongo Components

* Config Server (3 member replica set): `config01`,`config02`,`config03`
* 3 Shards (each a 2 member replica set):
	* `shard01a`,`shard01b`
	* `shard02a`,`shard02b`
	* `shard03a`,`shard03b`
* 1 Router (mongos): `router`
* (TODO): DB data persistence using docker data volumes

### First Run (initial setup)
**Start all of the containers** (daemonized)

```
docker-compose up -d
```

**Initialize the replica sets (config server and shards) and router**

```
sh init.sh
```

This script has a `sleep 20` to wait for the config server and shards to elect their primaries before initializing the router

**Verify the status of the sharded cluster**

```
docker-compose exec router mongo
mongos> sh.status()
--- Sharding Status ---
  sharding version: {
	"_id" : 1,
	"minCompatibleVersion" : 5,
	"currentVersion" : 6,
	"clusterId" : ObjectId("5981df064c97b126d0e5aa0e")
}
  shards:
	{  "_id" : "shard01",  "host" : "shard01/shard01a:27018,shard01b:27018",  "state" : 1 }
	{  "_id" : "shard02",  "host" : "shard02/shard02a:27019,shard02b:27019",  "state" : 1 }
	{  "_id" : "shard03",  "host" : "shard03/shard03a:27020,shard03b:27020",  "state" : 1 }
  active mongoses:
	"3.4.6" : 1
 autosplit:
	Currently enabled: yes
  balancer:
	Currently enabled:  yes
	Currently running:  no
		Balancer lock taken at Wed Aug 02 2017 14:17:42 GMT+0000 (UTC) by ConfigServer:Balancer
	Failed balancer rounds in last 5 attempts:  0
	Migration Results for the last 24 hours:
		No recent migrations
  databases:
```

### Normal Startup
The cluster only has to be initialized on the first run. Subsequent startup can be achieved simply with `docker-compose up` or `docker-compose up -d`

### Accessing the Mongo Shell
Its as simple as:

```
docker-compose exec router mongo
```

### Resetting the Cluster
To remove all data and re-initialize the cluster, make sure the containers are stopped and then:

```
docker-compose rm
```

Execute the **First Run** instructions again.