# Scripts for this project

* [Generate SECRET_KEY app](#generate-secret_key-app)
* [Development Mode](#development-mode)
* [Production Mode](#production-mode)



## Generate SECRET_KEY app

This script generates a secret key for your application

### Command
```
poetry run gen_key
```

Execution result:
```
✔ Your key has been generated
+------------------------------------------------------+
| e7df7+$+fqm0%d+p*4w)$296ax2oj$d-k5gf%(&v5#tlji4-4e   |
+------------------------------------------------------+
```

### Extra options

* ``--length`` - ***The default value is 50.*** This parameter is responsible for the number of characters in your key

## Development Mode

This command is borrowed from such a package manager as ``npm``.

### Command
```
poetry run dev
```

If you take an interest in how this script works, you will see that the  command is simply called in the root of the project
 
```
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload
```

### Extra options

* ``--host`` - ***The default value is 127.0.0.1.*** This parameter is responsible for the number of characters in your key
* ``--port`` - ***The default value is 8000.*** This parameter is responsible for the number of characters in your key
* ``--reload`` - ***The default value is True.*** This parameter is responsible for the number of characters in your key