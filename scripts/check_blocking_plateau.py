"""Plateau statistics for Langmuirian site blocking, p(R) = 1 - R/R_inf.

Events of size ell arrive at rate (m/ell)(1 - R/R_inf).  Writing N = R_inf/ell
for the number of sites, the rate per *empty* site is m/R_inf independently of
the others, so the filled count is exactly Binomial(N, 1-e^{-psi t}) with
psi = m/R_inf, and

    E[R](t)   = R_inf (1 - e^{-psi t})          <- the Kern-Seaton mean
    Var[R](t) = ell R_inf e^{-psi t}(1 - e^{-psi t})
    Var[R]_inf = 0 ,   max_t Var[R] = ell R_inf / 4  at  R = R_inf/2 .

Checked below against direct simulation of the site-filling times.
"""
import numpy as np

rng = np.random.default_rng(7)
m, ell, R_inf = 1.0, 0.25, 5.0
N, psi = int(R_inf / ell), m / R_inf
t = np.linspace(0, 6 / psi, 25)[1:]

p = 1 - np.exp(-psi * t)
mean_th, var_th = R_inf * p, ell * R_inf * p * (1 - p)

fill = rng.exponential(1 / psi, size=(200_000, N))
R = ell * (fill[:, None, :] <= t[None, :, None]).sum(axis=2)
mean_mc, var_mc = R.mean(axis=0), R.var(axis=0)

print("max |mean  theory - MC| = %.2e" % np.abs(mean_th - mean_mc).max())
print("max |var   theory - MC| = %.2e" % np.abs(var_th - var_mc).max())
print("peak variance: theory ell*R_inf/4 = %.4f, MC %.4f" % (ell * R_inf / 4, var_mc.max()))
print("variance at psi*t = 6 : theory %.3e, MC %.3e" % (var_th[-1], var_mc[-1]))

s2 = m * ell                                   # s^2 = m*ell at matched (m, ell)
eta = 0.5
print("\nplateau variance at matched R_inf and psi:")
print("  continuous linear removal   %.4f" % (s2 / (2 * psi)))
print("  sloughing (eta=%.1f)         %.4f" % (eta, s2 / ((2 - eta) * psi) + eta * R_inf**2 / (2 - eta)))
print("  Langmuirian blocking        %.4f" % 0.0)
