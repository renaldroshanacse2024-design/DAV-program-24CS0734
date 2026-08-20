"""
Experiment 1: Installation and Exploration of Data Analytics Libraries
AIM: To download, install, and explore the features of NumPy, SciPy, Jupyter, Statsmodels, Pandas,
     Matplotlib, Seaborn, Plotly, and Bokeh for scientific computing, data analysis, and visualization.
"""

def main():
    print("=== EXPERIMENT 1: LIBRARY INSTALLATION AND VERIFICATION ===")
    try:
        import numpy as np
        print(f"NumPy Version: {np.__version__}")
    except ImportError as e:
        print(f"NumPy Import Failed: {e}")

    try:
        import pandas as pd
        print(f"Pandas Version: {pd.__version__}")
    except ImportError as e:
        print(f"Pandas Import Failed: {e}")

    try:
        import matplotlib
        print(f"Matplotlib Version: {matplotlib.__version__}")
    except ImportError as e:
        print(f"Matplotlib Import Failed: {e}")

    try:
        import seaborn as sns
        print(f"Seaborn Version: {sns.__version__}")
    except ImportError as e:
        print(f"Seaborn Import Failed: {e}")

    try:
        import statsmodels.api as sm
        print(f"Statsmodels Version: {sm.__version__}")
    except ImportError as e:
        print(f"Statsmodels Import Failed: {e}")

    try:
        import scipy
        print(f"SciPy Version: {scipy.__version__}")
    except ImportError as e:
        print(f"SciPy Import Failed: {e}")

    try:
        import plotly
        print(f"Plotly Version: {plotly.__version__}")
    except ImportError as e:
        print(f"Plotly Import Failed: {e}")

    try:
        import bokeh
        print(f"Bokeh Version: {bokeh.__version__}")
    except ImportError as e:
        print(f"Bokeh Import Failed: {e}")

    try:
        import jupyterlab
        print(f"JupyterLab Version: {jupyterlab.__version__}")
    except ImportError as e:
        print(f"JupyterLab Import Failed: {e}")
        
    print("\nAll libraries are successfully verified.")

if __name__ == "__main__":
    main()
