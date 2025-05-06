# Tsunami

## instructions

* install connecpy protoc
    > `go install github.com/i2y/connecpy/protoc-gen-connecpy@latest`
* add go to path
    > `export PATH=$PATH:~/go/bin`
* generate proto classes (files expect generated files to be in `./proto`)
    > `protoc --python_out=./ --pyi_out=./ --connecpy_out=./ ./proto/aloha.proto`
* run server
    > `uv run hypercorn --bind :8001 server:app`

### running

* run hypercorn serve
    > `uv run hypercorn --bind :3000 server:app`
* test aloha
    >```sh
    >   curl -X POST \
    >   http://0.0.0.0:3000/aloha.v1.AlohaEthereumService/ChecksumAddress \
    >   -H "Content-Type: application/json" \
    >   -d '{"address": "0x0fc59C9C998537c940a9Dfc7DacDe533a9c496Fe"}'
    > ```

### adding new endpoint
