# Advanced Physics Lab Toolkit - IFSC/USP

High-performance automation and statistical analysis toolkit designed for the Advanced Laboratory course at the Institute of Physics of São Carlos (IFSC/USP).

This project streamlines the scientific workflow by automating folder structures, performing rigorous non-linear least squares fitting (weighted), and generating publication-quality LaTeX reports. It eliminates manual formatting overhead, allowing a total focus on physics and data interpretation.

## 🚀 Features

* **Workflow Automation:** `new_exp.py` script instantly scaffolds new experiment directories with all necessary templates.
* **Robust Statistical Analysis:**
    * Non-linear curve fitting using `scipy.optimize.curve_fit` (Weighted Least Squares).
    * Automatic calculation of **Reduced Chi-Squared** ($\chi^2_{red}$) for goodness-of-fit validation.
    * Parameter uncertainty propagation via the Covariance Matrix.
* **Professional Visualization:** Generates dual-panel figures (Model Fit + Residuals) to detect systematic errors.
* **LaTeX Integration:** Pre-configured ABNT/IFSC templates ready for compilation.

## 📂 Repository Structure

```text
/
├── new_exp.py             # Automation script (Scaffolds new experiments)
├── templates/             # Core templates
│   ├── base_script.py     # Python analysis engine (Fit + Residuals + Chi2)
│   └── report_template.tex # LaTeX report boilerplate
│
├── exp01-example/         # (Generated folder structure)
│   ├── analysis.py        # Experiment-specific script
│   ├── data.csv           # Raw experimental data
│   ├── fit_plot.png       # Generated figure
│   └── report.tex         # Final report source
│
└── README.md
