# Code and reproducibility notebooks for "Classical heat exchanger fouling-resistance laws as first-moment identities of additive stochastic deposition"

Simone Casolo — [ORCID 0000-0003-2945-8931](https://orcid.org/0000-0003-2945-8931)

- **Paper:** [arXiv:2611.22808](https://arxiv.org/abs/2611.22808) [eess.SY]
- **Interactive explainer:** <https://simonecasolo.github.io/projects/0_fouling_theory/>

## What the paper shows

The classical fouling-resistance curves (linear growth, Kern–Seaton
saturation) are exact first-moment identities: they hold for *any*
microscopic deposition law and *any* of several removal mechanisms, so a
fitted curve identifies only a net deposition rate and, if the record
saturates, a relaxation time, never the
underlying mechanism. Modelling deposition as a Lévy subordinator shows
where the missing information actually lives — removal mechanisms separate
in the variance of the record, deposition mechanisms only in its higher
cumulants (skewness, kurtosis) — and that the latter are masked by ordinary
measurement noise for all practically achievable record lengths. This
repository reproduces every figure and every quantitative claim in the
paper and its Supplementary Material from first principles, with no
external data.

## Repository layout

```
notebooks/
├── 01_figures.ipynb                  main-text Figs. 1–5 and SM Figs. S1–S6
├── 02_first_passage_validation.ipynb Monte Carlo validation of the first-passage
│                                      formulas (SM Sec. S7); writes data/*.csv
└── 03_removal_checks.ipynb           numerical checks backing SM Sec. S4
scripts/
└── check_blocking_plateau.py         standalone check, Langmuirian site blocking
data/                                  small CSV results consumed by 01_figures.ipynb
figures/                               generated PDF/PNG figures (populated by running
                                        the notebooks above)
tutorials/                             optional, not required to reproduce the paper
manuscript/                            paper and Supplementary Material (PDF) and their LaTeX sources
```

## Figure → notebook → output file

| Figure | Notebook / cell | Output file |
|---|---|---|
| Fig. 1 (schematic) | `01_figures.ipynb`, "Fig. 1" | `fig_ks_ep_schematic.{pdf,png}` (not used in the manuscript, which uses a TikZ figure; kept for reference) |
| Fig. 2 | `01_figures.ipynb`, "Fig. 2" | `fig02_event_spectrum_6panel.{pdf,png}` |
| Fig. 3 | `01_figures.ipynb`, "Fig. 3" | `fig03_removal.{pdf,png}` |
| Fig. 4 | `01_figures.ipynb`, "Fig. 4" | `fig04_observability.{pdf,png}` |
| Fig. 5 | `01_figures.ipynb`, "Fig. 5 (and a companion layout)" — **part (A) only** | `fig05_rul_ridgeline.{pdf,png}` |
| Fig. S1 | `01_figures.ipynb`, "Figure S1" | `figS1_alpha_continuum.{pdf,png}` |
| Fig. S2 | `01_figures.ipynb`, "Figure S2" | `figS2_removal_moments.{pdf,png}` |
| Fig. S3 | `01_figures.ipynb`, "Figure S3" | `figS3_nonlinear_removal.{pdf,png}` |
| Fig. S4 | `01_figures.ipynb`, "Figure S4" | `figS4_mechanism_recovery.{pdf,png}` |
| Fig. S5 | `01_figures.ipynb`, "Figure S5" | `figS5_record_validation.{pdf,png}`; caches `data/figC_mc.npz` |
| Fig. S6 | `01_figures.ipynb`, "Figure S6" | `figS6_fpt_validation.{pdf,png}`; reads `data/fpt_validation_*.csv`, written by `02_first_passage_validation.ipynb` |

`data/fpt_validation_mean.csv`, `data/fpt_validation_shape.csv` and
`data/fpt_percentiles_nx223.csv` are committed so that `01_figures.ipynb`
can be run on its own; run `02_first_passage_validation.ipynb` first only if
you want to regenerate them from scratch.

## How to run

```bash
conda env create -f environment.yml
conda activate fouling-first-moment-laws
jupyter notebook notebooks/
```

Run notebooks from inside `notebooks/` (each asserts this on its first
cell). `01_figures.ipynb` can be run top to bottom on its own using the
committed CSVs in `data/`; `02_first_passage_validation.ipynb` and
`03_removal_checks.ipynb` are independent and do not depend on `01`.

Every figure-producing cell in `01_figures.ipynb` states its own random
seed and measured runtime in the markdown cell directly above it. Total
runtime for `01_figures.ipynb` top to bottom is a few minutes, dominated by
Fig. S2 (≈1 min) and Fig. S5 (≈45 s); `02` and `03` each run in well under a
minute.

## Citation

If you use this code, please cite the paper and this repository:

```bibtex
@misc{Casolo2026fouling,
  author        = {Casolo, Simone},
  title         = {Classical heat exchanger fouling-resistance laws as first-moment identities of additive stochastic deposition},
  year          = {2026},
  eprint        = {2611.22808},
  archivePrefix = {arXiv},
  primaryClass  = {eess.SY},
  url           = {https://arxiv.org/abs/2611.22808}
}
```

The repository's own citation entry is in [`CITATION.cff`](CITATION.cff).

## License

Code is licensed under the [MIT License](LICENSE). Figures and written
material (notebook prose, this README) are licensed under
[CC BY 4.0](LICENSE-figures).

## Data availability

No experimental or plant data are included in this repository. All
figures and numerical checks are produced from closed-form expressions and
Monte Carlo simulation with fixed, stated seeds.
