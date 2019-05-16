# drgpy 

`drgpy` is a Python library for assigning a combination of diagnosis and procedure codes to Diagnosis Related Groups (MS-DRG) that is used in Medicare inpatient reimbursement today.

## Installing

Installing from the source:
```
$ git clone git@github.com:yubin-park/drgpy.git
$ cd drgpy
$ python setup.py develop
```

Or, simply using `pip`:
```
$ pip install drgmpy
```

## File Structure
- `drgpy/`: The package source code is located here.
  - `data/`: The raw data files downloaded from [the CMS website](https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/MS-DRG-Classifications-and-Software.html). 
  - `utils.py`: A module for readings data files
- `tests/`: test scripts to check the validity of the outputs.
- `LICENSE.txt`: Apache 2.0.
- `README.md`: This README file.
- `setup.py`: a set-up script.

## Code Examples
`drgpy` is really simple to use. 
Please see some examples below.
NOTE that all functions used below have docstrings. 
If you want to see the input parameter specifications,
please type `print(<instance>.<function>.__doc__)`.

```python
TBD
```

Please refer to the test scripts under the `tests/` folder if you want to see other example use cases.

## License
Apache 2.0

## Authors
Yubin Park, PhD

## References
- https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/MS-DRG-Classifications-and-Software.html




