# Marvel's Avengers Server Emulator


Client and Server emulator for Marvel's Avengers.
The client is responsible to downgrade the connection encryption enforcement and redirecting it to the localhost(127.0.0.1).
The server responds with pre-recorded JSON from Square Enix Servers, they're tied to my game progress at the moment.

You can read the blogpost about this project at: https://krystalgamer.github.io/avengers-emulator/

Video of the emulator in action: https://www.youtube.com/watch?v=MLn475soq1M 

## Installation

### Client 
Download the latest [release](https://github.com/krystalgamer/MarvelAvengers/releases). Rename the original `osdk.dll` to `osdk_orig.dll` and drop the one from the release.

When the game starts you should now have a console which logs `curl_easy_setopt` calls and hooks/patches.

### Server

Install Python 3.

Go the server folder and run `python -m pip install -r requirements.txt`. It only needs to be ran once per python installation.

Run the server with `python server.py`.



### Notes

If `python` does not work try `python3`.

Currently the server listens on `localhost` so it must be on ther same server as the client.

If you already have python installation and don't want to polute the package namespace, you can create a virtual environment. This [tutorial](https://docs.python.org/3/tutorial/venv.html) covers it in-depth.

## Client

Forwards all DLL calls to the original `osdk_orig.dll`.

Hooks(IAT) `getaddrinfo` forcing it to return `localhost` information.

Hooks(trampoline) `curl_easy_setopt` to control the network flow.

Drops the encryption enforcement by injecting `CURLOPT_SSL_VERIFYHOST` and `CURLOPT_SSL_VERIFYPEER`.

Dumping capabilities are disabled - uncomment and fix the paths to re-enable them.

## Server

Flask server with `adhoc` ssl_context, which allows for on the fly certificate generation.

Answers with JSONs from `jsons` folder.

Defined most critical endpoints to allow gameplay.

405 handler exists due to the client prefixing the HTTP method with a token.

`merge_slashes` is disabled to the client having double-slashes URL and Flask not liking it.


## TODO

- [ ] Have an actual Database
- [ ] Fix the market
- [ ] Improve the 405 handler
- [ ] Custom server address configuration


