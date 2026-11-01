#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schematische Darstellung der Kreatinin-Grenzbedingungen (AKI/AKIN).

- x = 0: aktuelle Messung mit Kreatinin m_k
- x = -2: Beginn des 48-h-Fensters
- x = -7: Beginn des 7-Tage-Fensters
- Jede Gerade verbindet den hypothetischen Minimalwert am linken Fensterrand
  mit dem aktuellen Kreatininwert bei x=0.

Die Bewertung im Originalcode verwendet das jeweilige Minimum IM Fenster,
nicht notwendig einen Messwert genau am Fensterrand.

Wichtig: is_stage3_abs ist die Kombination aus
    aktuelles Kreatinin >= 4.0 mg/dL UND Anstieg in 48 h >= 0.5 mg/dL.
Bei dem unten gewaehlten normalen m_k kann sie deshalb nicht ausloesen.

Stufe 2 (Ratio >= 2.0) wurde aus den ueblichen AKIN/KDIGO-Grenzen ergaenzt,
da sie im bereitgestellten Codeausschnitt nicht enthalten ist.
"""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Konfiguration -----------------------------------------------------------
NORMAL_MIN = 0.6  # mg/dL; rein schematischer Normalbereich
NORMAL_MAX = 1.2  # mg/dL
m_k = (NORMAL_MIN + NORMAL_MAX) / 2.0  # aktueller Messwert bei x=0

ANSTIEG_STUFE1_48H = 0.3  # mg/dL
ANSTIEG_STUFE3_48H = 0.5  # mg/dL
RATIO_STUFE1_7D = 1.5
RATIO_STUFE2_7D = 2.0  # Ergaenzung: im gezeigten Code nicht enthalten!
RATIO_STUFE3_7D = 3.0
ABSOLUT_STUFE3_AKTUELL = 4.0  # mg/dL, zusaetzlich zum 48-h-Anstieg

FARBEN = {
    1: "#167a76",  # Petrol: Stufe 1
    2: "#d99520",  # Bernstein: Stufe 2
    3: "#c1424c",  # Rot: Stufe 3
}


def main():
    fig, ax = plt.subplots(figsize=(13.2, 7.3))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    fig.subplots_adjust(left=0.085, right=0.695, bottom=0.21, top=0.88)

    # Die obere und untere Grenze des hier beispielhaften Normalbereichs.
    ax.axhspan(NORMAL_MIN, NORMAL_MAX, color="#c9d8d9", alpha=0.18, zorder=0)
    ax.axhline(m_k, color="#6d7d83", linewidth=1.0,
               linestyle=(0, (2, 4)), alpha=0.85, zorder=1)

    # Zeitfenster und aktuelle Messung markieren.
    for x, txt in [(-7, "7 Tage"), (-2, "48 Stunden")]:
        ax.axvline(x, color="#aebcc2", linestyle=(0, (3, 4)),
                   linewidth=1.15, zorder=1)
        ax.text(x + 0.07, 1.275, txt, fontsize=9, color="#607078",
                ha="left", va="top")
    ax.axvline(0, color="#34454f", linestyle=(0, (3, 4)),
               linewidth=1.4, alpha=0.7, zorder=1)

    # Nur die Grenzen werden gezeichnet, nicht frei erfundene Patientenwerte.
    # Format: (Stufe, Variablenname, Tag des Fensterrands, Grenzwert am Fensterrand,
    #          Linienstil, Text fuer die Legende, Beschriftung am Startpunkt,
    #          Transparenz)
    bedingungen = [
        (
            1, "is_stage1_diff", -2, m_k - ANSTIEG_STUFE1_48H, m_k - ANSTIEG_STUFE1_48H,
            ":", "Stufe 1: Anstieg >= 0,3 mg/dL in 48 h", "+0,3", 1.0,
        ),
        (
            1, "is_stage1_ratio", -7, m_k / RATIO_STUFE1_7D, m_k, 
            "--", "Stufe 1: Quotient >= 1,5 in 7 Tagen", "1,5 x", 1.0,
        ),
        (
            2, "is_stage2_ratio", -7, m_k / RATIO_STUFE2_7D, m_k,
            "--", "Stufe 2: Quotient >= 2,0 in 7 Tagen", "2,0 x", 1.0,
        ),
        (
            3, "is_stage3_ratio", -7, m_k / RATIO_STUFE3_7D, m_k,
            "--", "Stufe 3: Quotient >= 3,0 in 7 Tagen", "3,0 x", 1.0,
        ),
        (
            3, "is_stage3_abs", -2, 4.0 - ANSTIEG_STUFE3_48H, 4.0 - ANSTIEG_STUFE3_48H,
            ":", "Stufe 3: Anstieg >= 0,5 in 48 h UND Krea >= 4,0",
            "+0,5", 0.85,
        ),
    ]

    for stufe, code_name, x_start, y_start, m, stil, legend_text, punkt_text, alpha in bedingungen:
        farbe = FARBEN[stufe]
        ax.plot(
            [x_start, 0], [y_start, m],
            label=legend_text, color=farbe,
            linewidth=2.8, linestyle=stil, alpha=alpha,
            marker="o", markersize=9, markeredgewidth=1.25,
            markeredgecolor="white", markerfacecolor=farbe,
            zorder=5 + stufe,
        )
        ax.annotate(
            punkt_text, xy=(x_start, y_start), xytext=(9, -12),
            textcoords="offset points", fontsize=9.2,
            color=farbe, weight="bold", ha="left", va="bottom",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.72, pad=0.8),
            zorder=12,
        )

    # Gemeinsamer Endpunkt aller Grenzgeraden bei x=0.
    ax.scatter([0], [m_k], s=150, color="#273844", edgecolor="white",
               linewidth=1.7, zorder=20)

    ax.scatter([0], [4.0], s=150, color=FARBEN[3], edgecolor="white",
               linewidth=1.7, zorder=20)

    ax.set_xlim(-7.55, 0.42)
    ax.set_ylim(0, 4.1)
    ax.set_xticks([-7, -6, -5, -4, -3, -2, -1, 0])
    ax.set_xticklabels(["-7 d", "-6 d", "-5 d", "-4 d", "-3 d",
                        "-2 d", "-1 d", "0 (jetzt)"])
    ax.set_xlabel("Zeit relativ zur aktuellen Messung", fontsize=11, labelpad=10)
    ax.set_ylabel("Kreatinin (mg/dL)", fontsize=11, labelpad=9)
    ax.set_title("Kreatinin: Grenzen der AKIN-Alarmstufen",
                 fontsize=17, weight="bold", loc="left", pad=19)
    ax.grid(axis="y", color="#dfe5e8", linewidth=0.85, alpha=0.85, zorder=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#a9b7bc")
    ax.spines["bottom"].set_color("#a9b7bc")
    ax.tick_params(axis="both", colors="#40535d", labelsize=9.5)

    # Legende rechts ausserhalb der Grafik.
    legende = ax.legend(
        loc="upper left", bbox_to_anchor=(1.025, 1.015),
        title="Grenzbedingungen", frameon=False,
        fontsize=9.2, title_fontsize=11,
        labelspacing=1.17, handlelength=3.1,
        borderaxespad=0,
    )
    legende._legend_box.align = "left"

    # Wichtige Einschraenkung der Bedingung is_stage3_abs.
    ax.text(
        1.025, 0.49,
        "Um keine Alarme zu chronischen Patienten zu versenden,\n haben wir AKIN/KDIGO modifiziert\n und verlangen ZWEI Bedingungen:\n"
        "  Krea(0) >= 4,0 mg/dL UND Δ48 h >= 0,5.\n\n",
        transform=ax.transAxes, fontsize=9.2, color="#6c2730",
        va="top", ha="left", linespacing=1.5,
        bbox=dict(boxstyle="round,pad=0.8", facecolor="#fbf2f2",
                  edgecolor="#e7d5d7", linewidth=0.8),
    )

    fig.text(
        0.085, 0.095,
        "Die Linien sind nur schematisch: Der Code vergleicht den aktuellen Wert "
        "mit dem Minimum innerhalb von 48 h bzw. 7 Tagen.\n",
        ha="left", va="center", fontsize=9.2,
        color="#55636c", linespacing=1.55,
    )

    output = Path(__file__).resolve().with_suffix(".png")
    fig.savefig(output, dpi=210, bbox_inches="tight", facecolor="white")
    print(f"Grafik gespeichert unter: {output}")
    plt.show()


if __name__ == "__main__":
    main()
