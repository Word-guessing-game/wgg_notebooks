#!/usr/bin/env bash

cd ./model_inference_api
poetry run uvicorn app.api:app
