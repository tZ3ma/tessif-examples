import numpy as np
import pandas as pd
import tessif.frused.namedtuples as nts

# flow_gradients
mapping = {
    "sources": {
        "s1": {
            "name": "source_1",
            "outputs": ("electricity",),
            "latitude": 42,
            "longitude": 42,
            "region": "Here",
            "sector": "Power",
            "carrier": "Electricity",
            "component": "source",
            "node_type": "source",
            "accumulated_amounts": {
                "electricity": nts.MinMax(min=0, max=float("+inf"))
            },
            "flow_rates": {"electricity": nts.MinMax(min=0, max=10)},
            "flow_costs": {"electricity": 1},
            "flow_emissions": {"electricity": 0},
            "flow_gradients": {
                "electricity": nts.PositiveNegative(positive=5, negative=5)
            },
            "gradient_costs": {
                "electricity": nts.PositiveNegative(positive=0, negative=0)
            },
            "timeseries": None,
        },
        "s2": {
            "name": "source_2",
            "outputs": ("electricity",),
            "latitude": 42,
            "longitude": 42,
            "region": "Here",
            "sector": "Power",
            "carrier": "Electricity",
            "component": "source",
            "node_type": "source",
            "accumulated_amounts": {
                "electricity": nts.MinMax(min=0, max=float("+inf"))
            },
            "flow_rates": {"electricity": nts.MinMax(min=0, max=10)},
            "flow_costs": {"electricity": 1},
            "flow_emissions": {"electricity": 5},
            "flow_gradients": {
                "electricity": nts.PositiveNegative(positive=5, negative=5)
            },
            "gradient_costs": {
                "electricity": nts.PositiveNegative(positive=0, negative=0)
            },
            "timeseries": None,
        },
    },
    "transformers": {},
    "sinks": {
        "sink": {
            "name": "sink",
            "inputs": ("electricity",),
            "latitude": 42,
            "longitude": 42,
            "region": "Here",
            "sector": "Power",
            "carrier": "Electricity",
            "node_type": "sink",
            "component": "sink",
            "accumulated_amounts": {
                "electricity": nts.MinMax(min=0, max=float("+inf"))
            },
            "flow_rates": {"electricity": nts.MinMax(min=10, max=10)},
        },
    },
    "storages": {},
    "busses": {
        "bus": {
            "name": "central_bus",
            "inputs": (
                "source_1.electricity",
                "source_2.electricity",
            ),
            "outputs": ("sink.electricity",),
            "latitude": 42,
            "longitude": 42,
            "region": "Here",
            "sector": "Power",
            "carrier": "Electricity",
            "node_type": "central_bus",
            "component": "bus",
        },
    },
    "timeframe": {
        "primary": pd.date_range("01/01/2015", periods=4, freq="H"),
        "secondary": pd.date_range("10/03/2019", periods=3, freq="H"),
    },
    "global_constraints": {
        "primary": {
            "name": "default",
            "emissions": float("+inf"),
            "material": float("+inf"),
        },
        "secondary": {
            "name": "80% Reduction",
            "emissions": 30,
            "material": float("+inf"),
        },
        "tertiary": {
            "name": "100% Reduction",
            "emissions": 0,
            "material": float("+inf"),
        },
        "quartiary": {
            "name": "100% Reduction - 50% Material",
            "emissions": 0,
            "resources": 20,
        },
    },
}
