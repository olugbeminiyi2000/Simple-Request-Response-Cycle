# RapidLiteHTTP Server and Browser

## Overview

RapidLiteHTTP is a simple HTTP server written in Python that can serve text files based on user requests. This README provides instructions on how to set up and run the server, as well as launch a web browser to interact with the server.

## Requirements

- Python 3.8 or above installed on your pc
- Git (for cloning the repository) also installed on your pc

## Clone the repository to your local machine:
1. Open a terminal window on your favourite text editor e.g VisualStudiocode

```terminal
git clone https://github.com/olugbeminiyi2000/Simple-Request-Response-Cycle.git
```

## Navigate to the project directory:
1. Navigate to the directory containing the server script and your text files.

```terminal
cd Simple-Request-Response-Cycle
```
## Setup and Execution

### For Windows Users:


#### Run the following commands:
   1. Split your terminal screen into 2.
   
   2. On one side, run the server script with the root path as an argument:
   ```terminal
   python simpleserver.py "C:\path\to\gitrepo"
   ```
   3. on the other side i.e second terminal run web-browser script
   ```terminal
   python simplewebrowser.y
   ```
### For Linux/Unix Users:

#### Run the following commands:
   1. Split your terminal screen into 2.
   
   2. On one side, Make this script executable (if necessary):
    ```terminal
    chmod +x request-response.sh
    ```
   3. on the other side i.e second terminal run web-browser script
   ```terminal
   python simplewebrowser.y
   ```
## Server Details

- The server listens on `localhost` at port `9000`.
- It handles requests for text files in the specified root path.

## Note

- If an invalid location is provided, the server will serve a default location ("/python.txt").

## Additional Information

- The server supports both Windows and Linux/Unix environments.
- Ensure you have the necessary permissions to run scripts.

Feel free to modify the script and instructions based on your specific use case.


