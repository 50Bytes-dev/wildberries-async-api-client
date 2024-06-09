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
python schemas/repair_schema.py
```

### Step 4
```shell
openapi-python-generator --library aiohttp ./schemas/openapi.yaml wildberries_async_api_client
```