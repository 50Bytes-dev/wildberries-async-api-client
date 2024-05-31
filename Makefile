.PHONY: generate
generate: ## generate wb api
	openapi-generator generate -i ./schemas/openapi.yaml -g python -o . --library asyncio --package-name wildberries_async_api_client --additional-properties=projectName=wildberries-async-api-client,library=asyncio
