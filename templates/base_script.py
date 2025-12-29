import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. MODEL & DATA
def model_function(x, a, b):
    return a * x + b

# In the future, load this from a CSV
x_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_data = np.array([3.1, 3.9, 6.2, 8.1, 10.1])
y_error = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# 2. FITTING (Calculates the parameters)
popt, pcov = curve_fit(
    model_function,
    x_data, 
    y_data,
    sigma=y_error,
    absolute_sigma=True
)

a_opt, b_opt = popt
perr = np.sqrt(np.diag(pcov)) # Parameter errors

# 3. ANALYSIS (Residuals & Chi-Squared)
# Calculate theoretical Y for every data point
y_model_points = model_function(x_data, *popt)

# Residuals = Data - Theory
residuals = y_data - y_model_points

# Chi-Squared Calculation (Goodness of fit)
chisq = np.sum((residuals / y_error) ** 2)
dof = len(x_data) - len(popt) # Degrees of Freedom
chisq_red = chisq / dof

# 4. PRINT RESULTS
print(f"--- RESULTS ---")
print(f"Slope (a):     {a_opt:.4f} +/- {perr[0]:.4f}")
print(f"Intercept (b): {b_opt:.4f} +/- {perr[1]:.4f}")
print(f"Chi-Squared Reduced: {chisq_red:.3f} (Ideal is close to 1.0)")

# 5. PLOTTING (Top: Fit, Bottom: Residuals)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]}, figsize=(8, 6))

# -- Top Plot (The Fit) --
x_line = np.linspace(min(x_data), max(x_data), 100)
y_line = model_function(x_line, *popt)

ax1.errorbar(x_data, y_data, yerr=y_error, fmt='ko', label='Data', capsize=3)
ax1.plot(x_line, y_line, 'r-', label=f'Fit: y={a_opt:.2f}x + {b_opt:.2f}')
ax1.set_ylabel('Y Units')
ax1.legend()
ax1.set_title(f'Linear Fit (Chi2 Red: {chisq_red:.2f})')
ax1.grid(True, linestyle='--', alpha=0.5)

# -- Bottom Plot (The Residuals) --
ax2.errorbar(x_data, residuals, yerr=y_error, fmt='ko', capsize=3)
ax2.axhline(0, color='r', linestyle='--') # Zero line
ax2.set_xlabel('X Units')
ax2.set_ylabel('Residuals')
ax2.grid(True, linestyle='--', alpha=0.5)

# 6. SAVE & SHOW
plt.tight_layout()
plt.savefig('images/fit_plot.png', dpi=300) # Saves high-res image for LaTeX
print("\nGraph saved as 'fit_plot.png'")
plt.show()