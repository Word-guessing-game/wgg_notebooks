#!/usr/bin/env bash

set -x
set -e

docker-compose run --rm api bash -l -c "poetry run pytest -v"
