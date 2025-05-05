# Tsunami

## instructions

* install connecpy protoc
    > `go install github.com/i2y/connecpy/protoc-gen-connecpy@latest`
* add go to path
    > `export PATH=$PATH:~/go/bin`
* generate proto classes
    > `protoc --python_out=./generated --pyi_out=./generated --connecpy_out=./generated ./proto/aloha.proto`

### running

### adding new endpoint
