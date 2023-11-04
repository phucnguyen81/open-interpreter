Set up .env file:
```sh
INTERPRETER_CLI_USE_AZURE=True
AZURE_API_TYPE=azure
AZURE_API_KEY=<api-key-here>
AZURE_API_BASE=https://phuc-openai.openai.azure.com/
AZURE_API_VERSION=2023-08-01-preview
AZURE_DEPLOYMENT_NAME=gpt-4
```

Install virtual environment with poetry:
```sh
poetry install
```

Add dotenv plugin to load .env file:
```sh
poetry self add poetry-plugin-dotenv
```

Run the interpreter:
```sh
poetry run python main.py
```

Run the interpreter outside open-interpreter directory:
```powershell
$env:POETRY_DOTENV_LOCATION="/path/to/.env"
poetry run -C /path/to/open-interpreter python /path/to/main.py
```
