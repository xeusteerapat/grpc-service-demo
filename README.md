# Example Python gRPC

create virtual env

```shell
python3 -m venv .grpc_demo_env

source .grpc_demo_env/bin/activate.fish
```

upgrade `pip`

```shell
python3 -m pip install --upgrade pip
```

install packages

```shell
python3 -m pip install grpcio

python3 -m pip install grpcio-tools
```

Generating `gRPC` files, run

```shell
python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ item.proto
```

**ALWAYS USE `python3`**
