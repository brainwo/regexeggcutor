default:
    just run

init:
    poetry update
    poetry run python3 create_db.py

run:
    export $(cat secrets.env) && poetry run python3 src
