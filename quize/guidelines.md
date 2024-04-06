# create virtual env

`
python -m venv openai-env
`

## activate vnv

for this my os is windows , in vs code i set/open terminal as `git-bash` options and then

`
source openai-env/Scripts/activate
`

## .env file

i also created a `.env` file where i put open-api key

`OPENAI_API_KEY=####################`

## app.py

`pip install dot-env`

then put the code int `app.py` or you can see in the `app.py` file

``` from openai import OpenAI
    import os 
    from dotenv import load_dotenv
    import os

    # Load environment variables from .env file

    load_dotenv()

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )
```
