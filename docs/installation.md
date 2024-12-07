# Installation

## **1**
To run this project, first create a virtual environment. I used the module `uv` for that.
Install all the modules displayed in the [Modules Section](index.md/#modules)
```Python
# Install UV
pip install uv

# Start a new virtual project
uv init flightprices

# Start a new virtual environment
uv venv --python 3.12.1

# add the Modules
uv add <module_name>

```

## **2**

Create a file `secure.py` within the folder **scripts**.

Add just this line of code with a string of your phone number.

```
phone = '+12345678901'
```

Go to the [Web WhatsApp Site](https://web.whatsapp.com/) and connect your phone to receive the messages, otherwise the script will break.

## **3**

Next open the script `CompareFares.py`. This Python script controls a loop where you should input in the `[list]` of how many days ahead of today you want to search flights.

The numbers suggested are `[10, 30, 60, 90]`. 

For the `get_flights()` function, add:

* `origin_cd`: the code of the flight origin
* `destin_cd`: the code of the flight destin.

Run the script and wait for completion.
You will see the messages on the terminal prompt of your IDE.