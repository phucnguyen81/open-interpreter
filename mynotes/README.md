Set up .env file:
```sh
INTERPRETER_CLI_USE_AZURE=True
AZURE_API_TYPE=azure
AZURE_API_KEY=<api-key-here>
AZURE_API_BASE=https://phuc-openai.openai.azure.com/
AZURE_API_VERSION=2023-08-01-preview
AZURE_DEPLOYMENT_NAME=gpt-4
```

Run the interpreter:
```
set-dotenv.ps1
poetry run python main.py
```

Run the interpreter outside open-interpreter directory:
```
?? some how load .env
poetry run -C /path/to/open-interpreter python /path/to/main.py
```

