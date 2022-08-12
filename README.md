# **Organize Data From a API Request**
A small project that gets data from an api, filters it and stores it into a 'csv' file.

# Modules
**Used pandas for data handling and httpx for server side procedures.**

- httpx - <a href="https://www.python-httpx.org/" target="_blank">[check the official documentation](https://www.python-httpx.org/)</a>
- pandas - <a href="https://pandas.pydata.org/" target="_blank">[check the official documentation](https://pandas.pydata.org/)</a>

## Usage of HTTPX
@ this project i chose to use **HTTPX** intead of the standard *requests* library just to make something different.

```python
import httpx

def request(api: str) -> dict:
    # open a request session
    with httpx.Client() as client:
        try:
            # makes a GET request to the server
            r = client.get(api)   
        # error handling     
        except httpx.ConnectError:
            print('unable to connect!')
    return r.json() # returns data in json format
```
  
# **Contact**
**email:** lonelyrl@protonmail.com
