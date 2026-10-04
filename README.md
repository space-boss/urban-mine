# Urban Mine Hamburg

This repository contains the computational workflow developed for the REAP Master’s thesis:

**Mapping the Urban Mine: A Typology-Based Geospatial Estimation of Demolition-Related Material Release Potentials in Hamburg**

The repository demonstrates the typology-assignment and material-stock estimation workflow used in the thesis. The analysis is implemented in Python using Jupyter notebooks, pandas and GeoPandas.

## Repository structure

The workflow is organised as a sequence of notebooks covering:

- preparation and exploration of the Hamburg building dataset
- interpretation of relevant ALKIS building attributes
- typology assignment and fallback logic
- confidence tiers and data-quality flags
- gross floor area estimation
- material-intensity assignment and material-stock calculation
- result analysis and spatial visualisation

The notebooks follow the methodological workflow described in the thesis.

## Data sources

The analysis uses:

- Hamburg ALKIS building data from the Landesbetrieb Geoinformation und Vermessung (LGV), accessed through HafenCity University Hamburg.
- Harmonised building material-intensity data compiled by Heeren and Fishman, including German residential building data from Gruhler et al. (2002) and Ortlepp et al. (2018).
- Hamburg-specific material-intensity values from the IÖR Information System Built Environment (ISBE), used as a separate plausibility benchmark.

Raw source datasets are obtained separately from their original providers. References and access links are provided below.

## Running the notebooks

Use Python 3 with JupyterLab (or another Jupyter-compatible editor). From the repository root, create an environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt jupyterlab
cd notebooks
python -m jupyterlab
```

On Windows, activate the environment with `.venv\Scripts\activate` instead. Select this environment as the notebook kernel. Run notebooks with `notebooks/` as the working directory; the early notebooks use relative paths.

The workflow expects these files in `data/raw/`, retaining their existing filenames:

- `hamburg_buildings_clean.gpkg` — prepared Hamburg building data with the ALKIS attributes used by the notebooks. The notebooks start from this GeoPackage; they do not convert the original ALKIS GML into it.
- `Heeren_Germany Only.csv` — German material-intensity reference table.
- `Attachment 1_Heeren_typology_assignment_working_template - Heeren_typology_assignment_working_template.csv` — typology-assignment rules.
- `IÖR_EFH_Hamburg.csv` and `IÖR_MFH_Hamburg.csv` — benchmark material quantities.
- `IÖR_EFH_Hamburg_building volume.csv` and `IÖR_MFH_Hamburg_building volume.csv` — reference building dimensions used to normalise the benchmark.

For address labels in notebook 07, also supply `ALKIS_Adressen_HH_2026-07-03.zip`, containing `Adressen.gml`. The address ZIP is optional for the material-stock calculations. `zentraler_adressservice.csv` is an optional diagnostic input and is not required for GML-based address matching.

Run each notebook from top to bottom in a fresh kernel, in this order:

1. `01_pilot_workflow.ipynb`
2. `02_construction_years.ipynb`
3. `03_residential_building_filter.ipynb`
4. `04_building_analysis.ipynb`
5. `05_typology_assignment_revised.ipynb`
6. `06_results_analysis.ipynb`
7. `07_result_sampling_dashboard.ipynb`
8. `08_result_scatter_plots.ipynb` (optional exploration)

Notebook 05 must finish before notebooks 06–08, which read its saved outputs. Generated datasets and summary tables are written to `data/processed/`; exported figures are written to `results/`. These directories are created as needed.

## Notes

This repository documents the analytical implementation of the thesis methodology. For the full methodological rationale, assumptions, uncertainty assessment and interpretation of results, please refer to the thesis text.

## References

Gruhler, K., Böhm, R., Deilmann, C., & Schiller, G. (2002). *Stofflich-energetische Gebäudesteckbriefe: Gebäudevergleiche und Hochrechnungen für Bebauungsstrukturen* (IÖR-Schriften, Vol. 38). Institut für ökologische Raumentwicklung. https://nbn-resolving.org/urn:nbn:de:0168-ssoar-396855

Heeren, N., & Fishman, T. (2019). A database seed for a community-driven material intensity research platform. *Scientific Data, 6*, Article 23. https://doi.org/10.1038/s41597-019-0021-x

Heeren, N., & Fishman, T. (2023). *Material intensity database* (Version 1.2) [Data set]. GitHub. https://github.com/nheeren/material_intensity_db

Landesbetrieb Geoinformation und Vermessung. (2025). *Amtliche Liegenschaftskatasterkarte (ALKIS), Hamburg* (October 2025, GML) [Data set]. Accessed through HafenCity University Hamburg. https://www.hcu-hamburg.de/it-und-medien/kartographie

Leibniz-Institut für ökologische Raumentwicklung. (n.d.-a). *Einfamilienhaus Hamburg* [Data set]. Information System Built Environment. https://ioer-isbe.de/ressourcen/bauwerksdaten/wohngebaeude/efh-hamburg

Leibniz-Institut für ökologische Raumentwicklung. (n.d.-b). *Mehrfamilienhaus Hamburg* [Data set]. Information System Built Environment. https://ioer-isbe.de/ressourcen/bauwerksdaten/wohngebaeude/mfh-hamburg

Ortlepp, R., Gruhler, K., & Schiller, G. (2018). Materials in Germany’s domestic building stock: Calculation model and uncertainties. *Building Research & Information, 46*(2), 164–178. https://doi.org/10.1080/09613218.2016.1264121
