# python_grpc_example

## Overview
An example Python gRPC project implementing unary and bidirectional services

## Dependencies

`pip install grpcio grpcio-tools`

## Unary

```
cd unary
python -m grpc_tools.protoc --proto_path=. ./unary.proto --python_out=. --grpc_python_out=.
```

## Bidirectional

```
cd bidirectional
python -m grpc_tools.protoc --proto_path=.  ./bidirectional.proto --python_out=. --grpc_python_out=.
```

<hr />

[Reference](https://www.velotio.com/engineering-blog/grpc-implementation-using-python)