# Re-imagining Water Stress  
**An interactive, story-driven map of global freshwater availability (1961 – 2020)**  

A lightweight web app and notebook that transform the static BlueDot Observatory SDG map into an exploratory choropleth backed by open World Bank data. The redesign unites theory (Munzner’s *Visualization Analysis & Design*), research (Chen *et al.* colour-naming model, IEEE VIS 2021), and practice (Plotly Express + WebXR prototype).

---

## ✨ Features
| Capability | Detail |
|------------|--------|
| Animated choropleth | Plays through 1961-2020 with smooth frame-by-frame updates. |
| Hover tooltips | Exact value + one-line narrative call-out. |
| Instant search | Type a country, sub-region, or SDG keyword → map recentres. |
| “Spotlight” layer | Highlights top/bottom deciles (extreme scarcity / surplus). |
| Colour-blind-safe palette | Diverging scheme derived from perceptual colour naming. |
| Vision Pro/WebXR prototype | Depth-aware annotations, hand-ray interaction. |

---

## Quick start

```bash
# Clone + enter repo
git clone https://github.com/mskoudir/Infosci301_water-stress-viz.git
cd Infosci301_water-stress-viz

# Fresh environment (Conda example)
conda create -n waterstress python=3.10 -y
conda activate waterstress
pip install -r requirements.txt   # or: pip install pandas plotly numpy jupyter

# Notebook route
jupyter lab infosci301_water_stress_viz.ipynb

# One-shot HTML export
python infosci301_water_stress_viz.py
open water_stress_map.html        # (xdg-open on Linux, double-click on Windows)
