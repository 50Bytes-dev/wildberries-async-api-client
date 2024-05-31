# Wieldberries Async API Client

### Steps for regenerate client

### Step 1
```shell
npm install -g https://github.com/50Bytes-dev/openapi-merger.git
```

### Step 2
```shell
openapi-merger -i ./schemas/input.yaml -o ./schemas/openapi.yaml
```

### Step 3
```shell
brew install openapi-generator
```

```shell
make generate
```