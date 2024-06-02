.PHONY: generate-client

clean:
	poetry run black .
	poetry run flake8

generate:
	docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
        -i /local/openapi.yaml \
        -g python \
        -o /local