Using matplotlib:
```shell
# upgrade six to the latest version
python3.12 -m pip install six -U

# fix issue: FigureCanvasAgg is non-interactive, and thus cannot be shown
python3.12 -m pip install --user PyQt5

python3.12 -m pip install --user matplotlib
```

Using plotly:
```shell
python3.12 -m pip install --user plotly

# plotly depends on pandas
python3.12 -m pip install --user pandas
```