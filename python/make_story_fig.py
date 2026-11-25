"""Motivating scenario figure: federated smart-city analytics (story fig)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle, Polygon
from matplotlib.lines import Line2D

FS = 8.5
FS_T = 10
LW = 0.75

RED = "#b03030"
BLUE = "#1f5fa8"
GREY = "#444444"
DOM = "#555555"


def rnode(ax, x, y, label, s=11.0, dead=False):
    ec = RED if dead else "black"
    fc = "#f3d5d5" if dead else "white"
    ax.add_patch(Rectangle((x - s / 2, y - s / 2), s, s, facecolor=fc,
                           edgecolor=ec, linewidth=LW, zorder=3))
    if dead:
        d = s * 0.34
        ax.plot([x - d, x + d], [y - d, y + d], color=RED, lw=LW,
                zorder=4)
        ax.plot([x - d, x + d], [y + d, y - d], color=RED, lw=LW,
                zorder=4)
    else:
        ax.text(x, y + 0.3, label, ha="center", va="center",
                fontsize=FS - 0.5, zorder=4)


def domain(ax, x, y, w, h, label):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h,
                 facecolor="none", edgecolor=DOM, linewidth=LW,
                 linestyle=(0, (4, 3)), zorder=1))
    ax.text(x, y + h / 2 + 1.8, label, ha="center", va="center",
            fontsize=FS - 1, color="#333333", zorder=5,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))


def elink(ax, p0, p1, color=GREY, ls="-", arrow=False, sh=6.0):
    ax.add_patch(FancyArrowPatch(p0, p1,
                 arrowstyle="-|>" if arrow else "-", mutation_scale=9,
                 color=color, lw=LW, linestyle=ls, zorder=2,
                 shrinkA=sh, shrinkB=sh))


def tnode(ax, x, y, label, r=5.0):
    ax.add_patch(Circle((x, y), r, facecolor="white", edgecolor="black",
                        linewidth=LW, zorder=3))
    ax.text(x, y - r - 2.4, label, ha="center", va="top",
            fontsize=FS - 0.5, zorder=4)


def partition(ax, x, y, w, h, label, edge=RED, lx=None, ly=None):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h,
                 facecolor="none", edgecolor=edge, linewidth=LW,
                 linestyle=(0, (4, 3)), zorder=1))
    ax.text(lx if lx is not None else x,
            ly if ly is not None else y + h / 2 + 1.8,
            label, ha="center", va="center",
            fontsize=FS - 1, color="#333333", zorder=5,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))


def camera(ax, x, y):
    ax.add_patch(Rectangle((x - 2.6, y - 1.6), 4.6, 3.2,
                 facecolor="white", edgecolor="black", linewidth=LW,
                 zorder=3))
    ax.add_patch(Polygon([[x + 1.8, y + 0.7], [x + 4.2, y + 2.0],
                          [x + 4.2, y - 2.0], [x + 1.8, y - 0.7]],
                         closed=True, facecolor="white",
                         edgecolor="black", linewidth=LW, zorder=3))
    ax.text(x, y - 4.2, "camera", ha="center", va="center",
            fontsize=FS - 1.5, color="#555555", zorder=4)


fig, ax = plt.subplots(figsize=(9.4, 4.4))
ax.set_xlim(0, 200)
ax.set_ylim(0, 104)
ax.axis("off")

ax.plot([2, 198], [56, 56], color="#dddddd", lw=0.9)
ax.text(3, 98, "federated\ninfrastructure", ha="left", va="top",
        fontsize=FS - 1, color="#666666", style="italic")
ax.text(3, 50, "analytics\nworkflow", ha="left", va="top",
        fontsize=FS - 1, color="#666666", style="italic")

# ---------------- three federated domains ----------------
domain(ax, 48, 73, 54, 26, "Traffic authority")
rnode(ax, 36, 77, "$f_1$")
rnode(ax, 60, 68, "$f_2$")
elink(ax, (36, 77), (60, 68))
camera(ax, 11, 83)
camera(ax, 11, 73)
elink(ax, (15.5, 82), (30.5, 78), arrow=True, sh=3)
elink(ax, (15.5, 74), (30.5, 76), arrow=True, sh=3)

domain(ax, 112, 73, 52, 26, "Transit agency")
rnode(ax, 102, 71, "$f_3$", dead=True)
rnode(ax, 122, 77, "$f_4$")
elink(ax, (102, 71), (122, 77))

domain(ax, 168, 73, 52, 26, "Public safety")
rnode(ax, 158, 71, "$f_5$")
rnode(ax, 178, 77, "$f_6$")
elink(ax, (158, 71), (178, 77))

elink(ax, (60, 68), (102, 71))
elink(ax, (122, 77), (158, 71))
ax.text(110, 96, "resource federation\n(shared capacity across domains)",
        ha="center", fontsize=FS - 1, color="#555555")
ax.text(102, 61.5, "member fails", color=RED, fontsize=FS - 1,
        ha="center", va="center",
        bbox=dict(facecolor="white", edgecolor="none", pad=1.0))

# ---------------- branching analytics DAG ----------------
# same topology as Fig. 2: ingest -> {detect, count} ->
# {track, localize} -> alert ; the top branch sits on failed f_3.
tnode(ax, 24, 32, "ingest")
tnode(ax, 60, 45, "detect")
tnode(ax, 60, 19, "count")
tnode(ax, 98, 45, "track")
tnode(ax, 98, 19, "localize")
tnode(ax, 140, 32, "alert")

elink(ax, (29, 33.7), (55, 43.3), arrow=True, sh=3)
elink(ax, (29, 30.3), (55, 20.7), arrow=True, sh=3)
elink(ax, (65, 45), (93, 45), arrow=True, sh=3)
elink(ax, (65, 19), (93, 19), arrow=True, sh=3)
elink(ax, (103, 43.5), (135, 33.5), arrow=True, sh=3)
elink(ax, (103, 20.5), (135, 30.5), arrow=True, sh=3)

# partitions pinned to resources (mirrors Fig. 2's partition layout);
# each box encloses the task circle and its name below
partition(ax, 24, 29, 15, 19, "$P_1 \\rightarrow f_1$", ly=40.5)
partition(ax, 79, 41.75, 55, 18.5, "$P_2 \\rightarrow f_3$ (failed)",
          edge=RED, ly=53)
partition(ax, 60, 15.5, 15, 19, "$P_3 \\rightarrow f_2$", ly=27.5)
partition(ax, 98, 15.5, 15, 19, "$P_4 \\rightarrow f_4$", ly=27.5)
partition(ax, 140, 29, 15, 19, "$P_5 \\rightarrow f_5$", ly=40.5)

fig.savefig("figures/fig0_story.png", dpi=220,
            bbox_inches="tight", facecolor="white")
fig.savefig("paper/figures/fig0_story.png", dpi=220,
            bbox_inches="tight", facecolor="white")
print("wrote fig0_story.png")
