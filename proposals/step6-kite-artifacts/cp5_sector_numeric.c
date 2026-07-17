/*
 * CP5 sector-decomposed numerical evaluation of the scalar AAA-kite masters.
 *
 * Memo equations checked: (CP5.6), (CP5.10)--(CP5.12).
 * The program uses the common formal (d-4)=-2 epsilon-dimensional evanescent
 * subspace of D3,
 * resolves the two logarithmic parameter corners analytically, and applies a
 * randomized Halton rule only to bounded four-dimensional integrands.
 *
 * Build:
 *   cc -O3 -std=c11 cp5_sector_numeric.c -lm -o /tmp/cp5_sector_numeric
 * Run:
 *   /tmp/cp5_sector_numeric [points_per_replica] [replicas]
 */

#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define NM 6

static const double PI4 = 97.40909103400243723644033268870511124973;
static const double S1 = 1.0;
static const double S2 = 2.0;
static const double S12 = 0.3;

static double radical_inverse(uint64_t n, unsigned base) {
    double out = 0.0;
    double f = 1.0 / (double)base;
    while (n != 0) {
        out += (double)(n % base) * f;
        n /= base;
        f /= (double)base;
    }
    return out;
}

static uint64_t splitmix64(uint64_t *state) {
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    return z ^ (z >> 31);
}

static double uniform_shift(uint64_t *state) {
    return (double)(splitmix64(state) >> 11) * 0x1.0p-53;
}

static double frac(double x) {
    return x - floor(x);
}

static double positive_power(double x, double exponent) {
    if (x < 1.0e-300) x = 1.0e-300;
    return exp(exponent * log(x));
}

static void add_a_sector(double e, double w, double t, double u, double v,
                         int orientation, double out[NM]) {
    const double beta = orientation == 0 ? 1.0 : t;
    const double gamma = orientation == 0 ? t : 1.0;
    double r = w;
    double Ubar = beta + gamma + r * beta * gamma;
    double Fbar =
        S1 * u * ((1.0 - u) * (beta + gamma) + r * beta * gamma)
        + r * S2 * beta * v
          * (beta * (1.0 - v) * (1.0 + r * gamma) + gamma)
        + r * 2.0 * S12 * beta * gamma * u * v;

    /* Regular r^e pieces. */
    double bd = beta * positive_power(Ubar, -5.0 + 3.0 * e)
                      * positive_power(Fbar, 1.0 - 2.0 * e)
                      * positive_power(r, e);
    double C2 = gamma * gamma;
    double BC = (beta + gamma) * gamma;
    out[0] -= bd * e * C2;
    out[1] += bd * (e * (1.0 - e) * BC);
    out[2] -= bd * 0.5 * e * (1.0 - 2.0 * e) * C2;

    double bs = beta * positive_power(Ubar, -3.0 + 3.0 * e)
                      * positive_power(Fbar, -2.0 * e)
                      * positive_power(r, e);
    out[3] += bs * (-gamma);
    out[5] += bs * (beta + gamma);

    /* r^{-1+e} pieces: r = w^(1/e), so r^{-1+e} dr = dw/e. */
    r = exp(log(w > 1.0e-300 ? w : 1.0e-300) / e);
    Ubar = beta + gamma + r * beta * gamma;
    Fbar =
        S1 * u * ((1.0 - u) * (beta + gamma) + r * beta * gamma)
        + r * S2 * beta * v
          * (beta * (1.0 - v) * (1.0 + r * gamma) + gamma)
        + r * 2.0 * S12 * beta * gamma * u * v;
    bd = beta * positive_power(Ubar, -5.0 + 3.0 * e)
              * positive_power(Fbar, 1.0 - 2.0 * e) / e;
    double AB = (1.0 + r * gamma) * (beta + gamma);
    out[0] += bd * e * e * AB;
    out[2] -= bd * 0.5 * e * AB;

    bs = beta * positive_power(Ubar, -3.0 + 3.0 * e)
              * positive_power(Fbar, -2.0 * e) / e;
    out[4] += bs * (1.0 + r * gamma);
}

static void add_b_sector(double e, double w, double t, double u, double v,
                         int orientation, double out[NM]) {
    const double alpha = orientation == 0 ? 1.0 : t;
    const double gamma = orientation == 0 ? t : 1.0;
    double r = w;
    double Ubar = alpha + gamma + r * alpha * gamma;
    double Fbar =
        S2 * v * ((1.0 - v) * (alpha + gamma) + r * alpha * gamma)
        + r * S1 * alpha * u
          * (alpha * (1.0 - u) * (1.0 + r * gamma) + gamma)
        + r * 2.0 * S12 * alpha * gamma * u * v;

    double bd = alpha * positive_power(Ubar, -5.0 + 3.0 * e)
                       * positive_power(Fbar, 1.0 - 2.0 * e)
                       * positive_power(r, e);
    double C2 = gamma * gamma;
    out[0] -= bd * e * C2;
    out[2] -= bd * 0.5 * e * (1.0 - 2.0 * e) * C2;

    double bs = alpha * positive_power(Ubar, -3.0 + 3.0 * e)
                       * positive_power(Fbar, -2.0 * e)
                       * positive_power(r, e);
    out[3] += bs * (-gamma);
    out[4] += bs * (alpha + gamma);

    r = exp(log(w > 1.0e-300 ? w : 1.0e-300) / e);
    Ubar = alpha + gamma + r * alpha * gamma;
    Fbar =
        S2 * v * ((1.0 - v) * (alpha + gamma) + r * alpha * gamma)
        + r * S1 * alpha * u
          * (alpha * (1.0 - u) * (1.0 + r * gamma) + gamma)
        + r * 2.0 * S12 * alpha * gamma * u * v;
    bd = alpha * positive_power(Ubar, -5.0 + 3.0 * e)
               * positive_power(Fbar, 1.0 - 2.0 * e) / e;
    double AB = (alpha + gamma) * (1.0 + r * gamma);
    double BC = gamma * (1.0 + r * gamma);
    out[0] += bd * e * e * AB;
    out[1] += bd * (e * (1.0 - e) * BC);
    out[2] -= bd * 0.5 * e * AB;

    bs = alpha * positive_power(Ubar, -3.0 + 3.0 * e)
               * positive_power(Fbar, -2.0 * e) / e;
    out[5] += bs * (1.0 + r * gamma);
}

static void add_c_sector(double e, double w, double t, double u, double v,
                         int orientation, double out[NM]) {
    const double alpha = orientation == 0 ? 1.0 : t;
    const double beta = orientation == 0 ? t : 1.0;
    const double r = w;
    const double Ubar = alpha + beta + r * alpha * beta;
    const double Fbar =
        S1 * alpha * u
          * (alpha * (1.0 - u) * (1.0 + r * beta) + beta)
        + S2 * beta * v
          * (beta * (1.0 - v) * (1.0 + r * alpha) + alpha)
        + 2.0 * S12 * alpha * beta * u * v;
    const double radial = positive_power(r, -e);

    double bd = alpha * beta * positive_power(Ubar, -5.0 + 3.0 * e)
                             * positive_power(Fbar, 1.0 - 2.0 * e)
                             * radial;
    double AB = (1.0 + r * alpha) * (1.0 + r * beta);
    double BC = 1.0 + r * beta;
    out[0] += bd * (e * e * AB - e);
    out[1] += bd * (e * (1.0 - e) * BC);
    out[2] -= bd * (0.5 * e * AB + 0.5 * e * (1.0 - 2.0 * e));

    double bs = alpha * beta * positive_power(Ubar, -3.0 + 3.0 * e)
                             * positive_power(Fbar, -2.0 * e)
                             * radial;
    out[3] -= bs;
    out[4] += bs * (1.0 + r * alpha);
    out[5] += bs * (1.0 + r * beta);
}

static void evaluate_replica(double e, uint64_t npoints, uint64_t replica,
                             double result[NM]) {
    uint64_t rng = UINT64_C(0x4350354b49544500) + replica
                 + (uint64_t)llround(1000000.0 * e);
    const double shift[4] = {
        uniform_shift(&rng), uniform_shift(&rng),
        uniform_shift(&rng), uniform_shift(&rng)
    };
    double sums[NM] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    const uint64_t skip = 4096;
    for (uint64_t j = 0; j < npoints; ++j) {
        const uint64_t n = skip + j;
        double w = frac(radical_inverse(n, 2) + shift[0]);
        double t = frac(radical_inverse(n, 3) + shift[1]);
        double u = frac(radical_inverse(n, 5) + shift[2]);
        double v = frac(radical_inverse(n, 7) + shift[3]);
        if (w == 0.0) w = 0x1.0p-53;
        if (t == 0.0) t = 0x1.0p-53;
        if (u == 0.0) u = 0x1.0p-53;
        if (v == 0.0) v = 0x1.0p-53;
        double sample[NM] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        for (int orientation = 0; orientation < 2; ++orientation) {
            add_a_sector(e, w, t, u, v, orientation, sample);
            add_b_sector(e, w, t, u, v, orientation, sample);
            add_c_sector(e, w, t, u, v, orientation, sample);
        }
        for (int m = 0; m < NM; ++m) sums[m] += sample[m];
    }

    const double d = 4.0 - 2.0 * e;
    const double pref_double = tgamma(-1.0 + 2.0 * e) / pow(4.0 * M_PI, d);
    const double pref_single = e * tgamma(2.0 * e) / pow(4.0 * M_PI, d);
    for (int m = 0; m < NM; ++m) {
        result[m] = sums[m] / (double)npoints
                  * (m < 3 ? pref_double : pref_single);
    }
}

static void mean_and_error(double values[][NM], int nrep, int master,
                           double *mean, double *error) {
    double s = 0.0;
    for (int r = 0; r < nrep; ++r) s += values[r][master];
    *mean = s / (double)nrep;
    double ss = 0.0;
    for (int r = 0; r < nrep; ++r) {
        double delta = values[r][master] - *mean;
        ss += delta * delta;
    }
    *error = nrep > 1 ? sqrt(ss / ((double)nrep * (double)(nrep - 1))) : 0.0;
}

int main(int argc, char **argv) {
    uint64_t npoints = argc > 1 ? strtoull(argv[1], NULL, 10) : UINT64_C(262144);
    int nrep = argc > 2 ? atoi(argv[2]) : 8;
    if (npoints == 0 || nrep < 2 || nrep > 32) {
        fprintf(stderr, "usage: %s [positive points] [replicas 2..32]\n", argv[0]);
        return 2;
    }
    const double eps_values[3] = {0.03, 0.02, 0.01};
    printf("# CP5.10 common-D3 sector decomposition\n");
    printf("# q1^2=1 q2^2=2 q1.q2=0.3 mu^2=1 points=%llu replicas=%d\n",
           (unsigned long long)npoints, nrep);
    printf("epsilon,master,value,replica_standard_error\n");
    for (int ie = 0; ie < 3; ++ie) {
        double replicas[32][NM];
        for (int r = 0; r < nrep; ++r)
            evaluate_replica(eps_values[ie], npoints, (uint64_t)r, replicas[r]);
        for (int m = 0; m < NM; ++m) {
            double mean, error;
            mean_and_error(replicas, nrep, m, &mean, &error);
            printf("%.2f,N%d,%.17g,%.6g\n", eps_values[ie], m + 1, mean, error);
        }
    }
    printf("# K3.7 targets at the same point: q1-branch=%.17g q2-branch=%.17g\n",
           -1.0 / (3072.0 * PI4), -2.0 / (3072.0 * PI4));
    return 0;
}
