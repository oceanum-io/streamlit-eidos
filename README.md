# streamlit-eidos

Streamlit component for EIDOS visualisation with bi-directional transport for events.

## Installation instructions

```sh
pip install streamlit-eidos
```

## Usage

There is one component function `st_eidos` with function signature:

```
component_value=st_eidos(eidos, height=500, events=['click'])
```

### Parameters

    eidos : oceanum.eidos.Eidos instance
        The EIDOS scene to render.
    height : int, default 500
        The height of the map in pixels.
    events : list, default None
        A dict of events to listen for. Can be one or more of:
        - 'click'
        - 'hover'
        - 'drag'
    

### Returns

    component_value : dict
        A dictionary containing the dictionary of the last message from the scene.

## Example
See examples/test.py for simple interactive example
