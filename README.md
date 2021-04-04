# First Homework

## What package should do

`methods_importer` has to check if any of `modules` contains `callable` object with name `method_name` and return list of such objects

## Usage
```
from hw1.import_monster import methods_importer


array_methods = methods_importer("array", ["numpy", "pandas"])
```

## Install for development
`make install-all`

`pre-commit install`

## Run tests
`make pytest`
