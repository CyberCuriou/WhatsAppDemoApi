# WhatsApp Chat API Demo

A small **Flask/Python API** that returns fictional chat records from a
local text file. This is a demo project for explaining how an API can
retrieve chat records by phone number.

> **Important:** This project uses dummy conversations stored in
> `chats.txt`. It does not connect to WhatsApp, access real WhatsApp
> accounts, or retrieve real messages.

## 1. Project files

Keep these two files in the same project directory:

``` text
whatsapp-chat-api/
├── api.py
└── chats.txt
```

-   `api.py` --- Flask API application.
-   `chats.txt` --- sample/dummy chat records read by the API.

Do not rename `chats.txt` unless you also update the filename/path used
inside `api.py`.

## 2. Open the project directory

Open a terminal and move into the directory where `api.py` and
`chats.txt` are saved.

``` bash
cd /path/to/whatsapp-chat-api
```

For example, if the folder is inside Downloads:

``` bash
cd ~/Downloads/whatsapp-chat-api
```

Check that both files are present:

``` bash
ls
```

You should see:

``` text
api.py  chats.txt
```

## 3. Create a Python virtual environment

On Ubuntu/Linux:

``` bash
python3 -m venv venv
```

If the command reports that `venv` is unavailable, install the package:

``` bash
sudo apt update
sudo apt install python3-venv
```

Then create the environment again:

``` bash
python3 -m venv venv
```

## 4. Activate the environment

``` bash
source venv/bin/activate
```

Your terminal prompt should now show `(venv)`.

## 5. Install Flask

``` bash
python -m pip install --upgrade pip
python -m pip install Flask
```

Optional: save the installed dependencies so they can be installed again
later:

``` bash
python -m pip freeze > requirements.txt
```

On a later setup, if `requirements.txt` exists, install from it with:

``` bash
python -m pip install -r requirements.txt
```

## 6. Start the API

Make sure you are in the project directory and the virtual environment
is active.

``` bash
python api.py
```

Leave this terminal running. The API should be available at:

``` text
http://127.0.0.1:5000
```

If your `api.py` is configured to use Flask's CLI rather than starting
the server itself, use:

``` bash
flask --app api run
```

Use the run method that matches the existing `api.py`; do not start both
servers at the same time.

## 7. Test the API

The demo endpoint looks up chats for the sample phone number
`9000000001`.

Open this URL in your browser:

``` text
http://127.0.0.1:5000/api/chats?phone=9000000001
```

Or test it from a second terminal:

``` bash
curl "http://127.0.0.1:5000/api/chats?phone=9000000001"
```

The API should return matching dummy chat records as JSON. The returned
records depend on the sample data currently present in `chats.txt`.

Try another phone number by changing the `phone` query parameter:

``` bash
curl "http://127.0.0.1:5000/api/chats?phone=9000000002"
```

If there are no matching records, the API may return an empty result.

## 8. Stop the API

Go back to the terminal running the server and press:

``` text
Ctrl + C
```

To leave the Python virtual environment:

``` bash
deactivate
```

## 9. Start it again later

Whenever you want to run the demo again:

``` bash
cd /path/to/whatsapp-chat-api
source venv/bin/activate
python api.py
```

Then open:

``` text
http://127.0.0.1:5000/api/chats?phone=9000000001
```

## 10. Troubleshooting

### Flask module not found

Make sure the virtual environment is active, then run:

``` bash
source venv/bin/activate
python -m pip install Flask
```

### Port 5000 is already in use

Check which process is listening on port 5000:

``` bash
ss -tlnp | grep :5000
```

Stop only the process you have identified as the old demo server:

``` bash
kill <PID>
```

Replace `<PID>` with the process ID shown by the previous command.
Alternatively, if the application supports Flask CLI, run it on another
port:

``` bash
flask --app api run --port 5001
```

Then use port `5001` in the test URL:

``` bash
curl "http://127.0.0.1:5001/api/chats?phone=9000000001"
```

### API returns no chats

-   Confirm `chats.txt` is in the same location expected by `api.py`.
-   Confirm the phone number exists in the sample data.
-   Check the server terminal for Python errors.
-   Keep the existing `chats.txt` record format; the API parser expects
    the format implemented in `api.py`.

### `api.py` cannot find `chats.txt`

Run the server from the project directory:

``` bash
cd /path/to/whatsapp-chat-api
source venv/bin/activate
python api.py
```

If the code uses a relative file path, its working directory can affect
where Python looks for `chats.txt`.

------------------------------------------------------------------------

## Quick-start commands (Ubuntu/Linux)

After the first-time setup is complete:

``` bash
cd /path/to/whatsapp-chat-api
source venv/bin/activate
python api.py
```

In another terminal:

``` bash
curl "http://127.0.0.1:5000/api/chats?phone=9000000001"
```

## Demo scope

This is a local educational API backed by fictional data. It
demonstrates an HTTP request and a JSON response; it is **not a WhatsApp
integration** and does not demonstrate access to real WhatsApp messages.

For Flask's official setup and run instructions, see the [Flask
installation
guide](https://flask.palletsprojects.com/en/stable/installation/) and
[Flask
quickstart](https://flask.palletsprojects.com/en/stable/quickstart/).
