# eRemiza API

## Installation
```console
$ pip install eremiza-api
```

## Usage
```python
from eremiza import Client

client = Client("email@example.com", "password")

alarms = client.get_alarms(count=5)
```

## All methods
```python
def get_alarms(count=3, offset=0) # Returns list of latest alarms
```
