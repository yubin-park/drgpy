# drgpy 

`drgpy` is a Python library for assigning a combination of diagnosis and procedure codes to Diagnosis Related Groups (MS-DRG) that is used in Medicare inpatient reimbursement today.

NOTE the current default version is configured as MSDRG v40. However, the latest version is not thoroughly tested yet.
Rawfiles: https://www.cms.gov/files/zip/icd-10-ms-drg-definitions-manual-files-v372.zip

## Installing

Installing from the source:
```
$ git clone git@github.com:yubin-park/drgpy.git
$ cd drgpy
$ python setup.py develop
```

Or, simply using `pip`:
```
$ pip install drgpy
```

## File Structure
- `drgpy/`: The package source code is located here.
  - `data/`: The raw data files downloaded from [the CMS website](https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/MS-DRG-Classifications-and-Software.html). 
  - `msdrg.py`: The main file for the MS-DRG logic.
  - `_mdcsrdr.py`: A script that reads/parses `mdcs_xx_xx.txt` data files.
  - `_appndxrdr.py`: A script that reads/parses `appendix_xx.txt` data files.
  - `_mdcs0007.py`: logics for MDC00 - MDC07
  - `_mdcs0811.py`: logics for MDC08 - MDC11
  - `_mdcs1221.py`: logics for MDC12 - MDC21
  - `_mdcs2225.py`: logics for MDC22 - MDC25
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
>>> from drgpy.msdrg import DRGEngine
>>> de = DRGEngine(version="v40")
>>> print(de.get_drg.__doc__)

        Return the corresponding DRG code for the diagnoses and procedures

        Parameters
        ----------
        dx_lst : list
                A list of ICD-10 diagnosis codes
        pr_lst : list
                A list of ICD-10 procedure codes
>>>
>>> de.get_drg(["B20"],[])
'977'
>>> de.get_drg([], ["02HA0RS"])
'983'
>>> de.get_drg([], ["02HA0RS", "02PA0RZ"])
'002'
>>>
```

Please refer to the test scripts under the `tests/` folder if you want to see other example use cases.

## License
Apache 2.0

## Authors
Yubin Park, PhD

## References
- https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/MS-DRG-Classifications-and-Software.html
- https://www.cms.gov/files/zip/icd-10-ms-drg-definitions-manual-files-v372.zip



