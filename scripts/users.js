
db.createUser({user: "MYUSERNAME",pwd: "MYPASSWORD",roles: [{ role: "readWrite", db: "admin" },{ role: "readWrite", db: "dbtests" }]});