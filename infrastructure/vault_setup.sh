#!/bin/bash
docker run -d --name=hashicorp-vault --cap-add=IPC_LOCK -e 'VAULT_DEV_ROOT_TOKEN_ID=myroot' -p 8200:8200 vault
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='myroot'
vault kv put secret/api_keys binance_api='your_binance_api_key' openai_api='your_openai_key'