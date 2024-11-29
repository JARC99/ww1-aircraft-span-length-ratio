"""Plot state of the art data."""

import matplotlib.pylab as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats as st

COLORS = ["darkblue", "darkred", "darkgreen", "darkorange",
          "darkcyan", "darkmagenta", "dimgray", "goldenrod"]
sns.set_theme(style="whitegrid", font="Palatino Linotype",
              context="paper", palette=COLORS)
GRAPHICS_PATH = "output/"
DPI = 300

data = pd.read_excel("data.xlsx", engine="openpyxl")

fig = plt.figure(dpi=DPI)
ax = fig.add_subplot(111)
sns.scatterplot(x="Span", y="Ratio", hue="Type",
                style="Type", s=75, data=data)
# ax.set_xlim(left=0)
# ax.set_ylim(bottom=0)
ax.set_xlabel("Span, m")
ax.set_ylabel("Length-to-Span Ratio")
ax.legend()
# fig.savefig(GRAPHICS_PATH + "/Wf_e+b_vs_R_max.pdf", format="pdf",
#             bbox_inches="tight")


# %%
data_array = data.to_numpy()

slope, intercept, r_val, p_val, stdderr = st.linregress(
    data_array[:, 1:3].astype("float64"))

span_array = np.arange(0, 50, 1)
length_array = slope*span_array + intercept

fig = plt.figure(dpi=DPI)
ax = fig.add_subplot(111)
sns.scatterplot(x="Span", y="Length", hue="Type",
                style="Type", s=75, data=data)
ax.plot(span_array, length_array)
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.set_xlabel("Span, m")
ax.set_ylabel("Length, m")
ax.legend()
# fig.savefig(GRAPHICS_PATH + "/Wf_e+b_vs_R_max.pdf", format="pdf",
#             bbox_inches="tight")
