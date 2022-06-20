# import jtplot submodule from jupyterthemes
from jupyterthemes import jtplot
import matplotlib as mpl

# currently installed theme will be used to
# set plot style if no arguments provided
jtplot.style(theme='onedork', ticks=True, grid=True)
# jtplot.style(theme='grade3')  # 하얀 배경

mpl.rc('font', family='Malgun Gothic')  # 맑은고딕
mpl.rc('axes', unicode_minus=False)  # 유니코드 음수 기호 사용