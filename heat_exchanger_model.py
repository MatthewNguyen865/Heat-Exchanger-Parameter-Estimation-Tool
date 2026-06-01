def heat_exchanger_odes(t, y, mh, mc, Cph, Cpc, UA):
    Th, Tc = y
    Qdot = UA * (Th - Tc)

    #Hot-side temperature change
    dThdt = -Qdot / (mh * Cph)

    #Cold-side temperature change
    dTcdt = Qdot / (mc * Cpc)

    return [dThdt, dTcdt]