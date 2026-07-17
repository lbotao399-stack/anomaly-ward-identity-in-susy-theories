"""Residual analysis round 2: add momentum-contracted-letter structures."""
exec(open("l1resid.py").read().split("R = rows_of")[0])  # reuse candidate build

# M-family: sum_{a,ad} eps^{ab} p(x)_{b ad} ... (D_a W^c) with dotted matchings
EPSL = {(0,1):Fr(1),(1,0):Fr(-1)}
Dw = {}
for a in range(2):
    Dw[(a,"wp")] = jet(wpj,[('D',a)],M_p)
    Dw[(a,"wm")] = jet(wmj,[('D',a)],M_p)
def eps_pair(cpA, cpB):
    # given dict ad->CP for two slots, return sum eps^{ad bd} A_ad B_bd
    e = {}
    for i in range(2):
        for j in range(2):
            s = EPSL.get((i,j))
            if s: e = cp_add(e, cp_scale(cp_mul(cpA[i], cpB[j]), (s, Fr(0))))
    return e
for x in MOMS:
    # xcontr[a][ad] = eps^{ab} p(x)_{b ad}
    xc = [[{},{}],[{},{}]]
    for a in range(2):
        for ad in range(2):
            e = {}
            for b in range(2):
                s = EPSL.get((a,b))
                if s: e = cp_add(e, cp_scale(MOMB[x][b][ad], (s, Fr(0))))
            xc[a][ad] = e
    for y in MOMS:
        for z in MOMS:
            for c in ("wp","wm"):
                # matching 1: (xdot,ydot)(zdot,Wt)
                S1 = gp_zero(); S2 = gp_zero(); S3 = gp_zero()
                for a in range(2):
                    L = Dw[(a,c)]
                    # m1
                    e1 = eps_pair([xc[a][0], xc[a][1]], [MOMB[y][0][0], MOMB[y][0][1]])
                    zW = gp_zero()
                    for cd in range(2):
                        for al in range(2):
                            s = EPSL.get((cd, al))
                            if s: zW = gp_add(zW, gp_scale_cp(wt[al], cp_scale(MOMB[z][0][cd], (s, Fr(0)))))
                    S1 = gp_add(S1, gp_scale_cp(gp_mul(zW, L), e1))
                    # m2: (xdot,zdot)(ydot,Wt)
                    e2 = eps_pair([xc[a][0], xc[a][1]], [MOMB[z][0][0], MOMB[z][0][1]])
                    yW = gp_zero()
                    for cd in range(2):
                        for al in range(2):
                            s = EPSL.get((cd, al))
                            if s: yW = gp_add(yW, gp_scale_cp(wt[al], cp_scale(MOMB[y][0][cd], (s, Fr(0)))))
                    S2 = gp_add(S2, gp_scale_cp(gp_mul(yW, L), e2))
                    # m3: (ydot,zdot)(xdot,Wt)
                    e3 = eps_pair([MOMB[y][0][0], MOMB[y][0][1]], [MOMB[z][0][0], MOMB[z][0][1]])
                    xW = gp_zero()
                    for ad in range(2):
                        for al in range(2):
                            s = EPSL.get((ad, al))
                            if s: xW = gp_add(xW, gp_scale_cp(wt[al], cp_scale(xc[a][ad], (s, Fr(0)))))
                    S3 = gp_add(S3, gp_scale_cp(gp_mul(xW, L), e3))
                cands[("M1",x,y,z,c)] = rows_of(S1)
                cands[("M2",x,y,z,c)] = rows_of(S2)
                cands[("M3",x,y,z,c)] = rows_of(S3)

R = rows_of(gp_apply_subst(agg_a.get(target, gp_zero()), subst))
keys = set(R)
for c in cands.values(): keys |= set(c)
eqkeys = []
for k in sorted(keys, key=str):
    monos = set(R.get(k, {}))
    for c in cands.values(): monos |= set(c.get(k, {}))
    for m in sorted(monos):
        eqkeys.append((k, m))
names = sorted(cands, key=str)
ncol = 2*len(names)
aug = []
meta = []
for (k, m) in eqkeys:
    row = []; row2 = []
    for n in names:
        cr, ci = cands[n].get(k, {}).get(m, (Fr(0), Fr(0)))
        row += [cr, -ci]; row2 += [ci, cr]
    bre, bim = R.get(k, {}).get(m, (Fr(0), Fr(0)))
    aug.append(row+[bre]); meta.append(((k,m),'re'))
    aug.append(row2+[bim]); meta.append(((k,m),'im'))
rr = 0
for c in range(ncol):
    pr = None
    for i in range(rr, len(aug)):
        if aug[i][c] != 0: pr = i; break
    if pr is None: continue
    aug[rr], aug[pr] = aug[pr], aug[rr]; meta[rr], meta[pr] = meta[pr], meta[rr]
    pv = aug[rr][c]
    aug[rr] = [t/pv for t in aug[rr]]
    for i in range(len(aug)):
        if i != rr and aug[i][c] != 0:
            f = aug[i][c]
            aug[i] = [t - f*u for t, u in zip(aug[i], aug[rr])]
    rr += 1
resid = [(meta[i], aug[i][ncol]) for i in range(rr, len(aug)) if aug[i][ncol] != 0]
print("candidates:", len(names), "rank:", rr, "residual eqs:", len(resid))
for ((k, m), p), val in resid[:20]:
    print("  ", k, m, p, val)
