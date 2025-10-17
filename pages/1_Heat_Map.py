import sys
import pandas as pd
import numpy as np
import streamlit as st
from tempfile import NamedTemporaryFile
import urllib

from mplsoccer import Pitch, VerticalPitch, PyPizza, FontManager
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.patches as patches
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch

st.set_page_config(page_title='Heat Map', layout='wide')
st.markdown('# Heat Map')

