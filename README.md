# drgpy

`drgpy` is a Python library for assigning a combination of diagnosis and procedure codes to Diagnosis Related Groups (MS-DRG) that is used in Medicare inpatient reimbursement today.

The default version is MS-DRG v43.1, effective April 1, 2026. Bundled versions range from v36 through v43.1.

## Installing

Installing from the source:

```
$ git clone git@github.com:yubin-park/drgpy.git
$ cd drgpy
$ python -m pip install --editable .
```

Or, simply using `pip`:

```
$ pip install drgpy
```

## Development

Install the standardized development dependency group and run the tests:

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install --upgrade pip
$ python -m pip install --editable . --group dev
$ python -m pytest
```

Build and validate the source and wheel distributions:

```bash
$ python -m build
$ python -m twine check dist/*
```

### Real-World Validation

Real inpatient claim data may be used to discover mismatches, but raw claim
rows, identifiers, service dates, and complete claim fingerprints should not be
committed to this repository. Convert each confirmed mismatch into the smallest
synthetic diagnosis/procedure combination that reproduces the relevant CMS rule,
then add that minimized case to the version tests.

Cases requiring unavailable inputs such as age, sex, or POA indicators should be
tracked separately rather than treated as grouper mismatches. A successful claim
sample comparison is useful regression evidence, but does not establish complete
parity with the official CMS grouper.

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
- `pyproject.toml`: package metadata, build configuration, and development dependency groups.

## Code Examples

`drgpy` is really simple to use.
Please see some examples below.
NOTE that all functions used below have docstrings.
If you want to see the input parameter specifications,
please type `print(<instance>.<function>.__doc__)`.

### Date-Based Version Selection

Use the wrapper to select the version effective on the supplied discharge date:

```python
>>> from drgpy.msdrg_allvers import DRGEngineAllVers
>>> de = DRGEngineAllVers()
>>> print(de.get_drg.__doc__)

        Return the corresponding DRG code for the diagnoses and procedures

        Parameters
        ----------
        dx_lst : list
                A list of ICD-10 diagnosis codes
        pr_lst : list
                A list of ICD-10 procedure codes
        date: str
                YYYY-MM-DD format
                Depending on the date of the claim,
                the engine will choose the appropriate version.
                For example, 2025-10-01 selects v43 and
                2026-04-01 selects v43.1.
        gender: str
                "F" or "M"
        is_alive: boolean
                if the patient is alive at discharge (True)
```

### Each Version Separately

NOTE that this usage doesn't require the date field.

```python
>>> from drgpy.msdrg import DRGEngine
>>> de = DRGEngine(version="v43.1")
>>> print(de.get_drg.__doc__)

        Return the corresponding DRG code for the diagnoses and procedures

        Parameters
        ----------
        dx_lst : list
                A list of ICD-10 diagnosis codes
        pr_lst : list
                A list of ICD-10 procedure codes
        gender: str
                "F" or "M"
        is_alive: boolean
                if the patient is alive at discharge (True)
>>>
>>> de.get_drg(["B20"],[])
'977'
>>> de.get_drg([], ["02HA0RS"])
'983'
>>> de.get_drg([], ["02HA0RS", "02PA0RZ"])
'002'
>>>
```

Calling `DRGEngine()` without a version uses the latest bundled version. POA
indicators may be supplied as a list aligned with the diagnoses or as a mapping
keyed by diagnosis code. Missing POA values default to `"Y"` for backward
compatibility.

```python
from drgpy.msdrg import DRGEngine

engine = DRGEngine()
drg = engine.get_drg(
    ["I21A1", "E0800"],
    [],
    poa=["Y", "N"],
)
```

### Outcome Simulation

Use `get_code_drg_candidates` to inspect the DRGs directly referenced by a
single diagnosis or procedure in the bundled CMS value sets. These are broad
rule candidates, not final grouped outcomes.

```python
engine.get_code_drg_candidates("A419", code_type="diagnosis")
engine.get_code_drg_candidates("0SG0071", code_type="procedure")
```

Use `simulate_drg_permutations` to group the same code set once for each
diagnosis selected as principal. All remaining diagnoses are treated as
secondary diagnoses. Procedure order and secondary-diagnosis order are not
permuted because they do not change grouping semantics.

```python
simulations = engine.simulate_drg_permutations(
    ["I469", "A021"],
    ["B2151ZZ"],
)

possible_drgs = engine.get_possible_drgs(
    ["I469", "A021"],
    ["B2151ZZ"],
)
```

Each simulation contains the selected principal diagnosis, secondary
diagnoses, procedures, selected DRG, and all matching DRGs before hierarchy
selection. These helpers support coding scenario review and audit workflows;
they do not determine documentation or billing appropriateness.

Please refer to the test scripts under the `tests/` folder if you want to see other example use cases.

## Raw Data Change Log

1. For v38+, in `mdcs_00_07.txt`, edit

```
NON-OPERATING ROOM PROCEDURES
02H63JZ*
```

to

```
NON-OPERATING ROOM PROCEDURES

  02H63JZ*
```

2. For any version, in `mdcs_08_11.txt`, remove

```
To qualify as bilateral or multiple joint procedures you must have at least one code from two different lower extremity sites as listed below.
Examples: left hip  and right hip - bilateral; left hip and left knee - multiple;  left hip and right ankle - multiple; left knee and right knee - bilateral
```

3. In `mdcs_00_07.txt`, remove

```
COMBINATION OF CODES IN THE NEXT FOUR LISTS
...
```

Alos, in v40, duplicate sections exist for this part.

4. In `mdcs_12_21.txt`, remove

```
Principal or secondary diagnosis of newborn or neonate,with other significant problems, not assigned to DRG 789 through 793 or 795
```

5. In `mdcs_12_21.txt`, for v38+ DRG 768 and 798, edit

```
NON-OPERATING ROOM PROCEDURES
10D07Z3* Extraction of Products of Conception, Low Forceps, Via Natural or Artificial Opening
```

to

```
NON-OPERATING ROOM PROCEDURES

  10D07Z3* Extraction of Products of Conception, Low Forceps, Via Natural or Artificial Opening
```

6. In `mdcs_12_21.txt`, for DRG 807,

```
NON-OPERATING ROOM PROCEDURES
10D07Z3*
```

to

```
NON-OPERATING ROOM PROCEDURES

  10D07Z3*
```

7. For v36, in appendix_D_E.txt,

Removed
10D17Z9 14 768
10D18Z9 14 796

As the DRG definition say other OR procedures except for these two above, but these are included as OR procedures in the appendix. Rather than changing the algorithm to deal with the discrepancy, we edit the underlying data to maintain consistency.

8. Any versions, in mdcs_08_11.txt,

There are group-level or conditions for 456&457&458, e.g., one of... "and" with one of...

Their categories are renamed as EXTENSIVE FUSION PART AB12..

## License

Apache 2.0

## Authors

| Contributor | Contribution |
|---|---|
| **Yubin Park, PhD** ([@yubin-park](https://github.com/yubin-park)) | Original library, v36–v40 data and grouper logic |
| **Shuo Yang** ([@syangdh](https://github.com/syangdh)) | v41 and v42 CMS data and initial modern-version routing |
| **Nikolaos Vergos** ([@nvergos](https://github.com/nvergos)) | v43 data, modern parser and grouper concordance fixes |
| **Svdmln** ([@Svdmln](https://github.com/Svdmln)) | Package-data and `importlib.resources` improvements |

## References

- https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/MS-DRG-Classifications-and-Software.html
- https://www.cms.gov/files/zip/icd-10-ms-drg-definitions-manual-files-v372.zip
- https://content.findacode.com/files/tutorials/DRG-Grouper-2019.pdf
