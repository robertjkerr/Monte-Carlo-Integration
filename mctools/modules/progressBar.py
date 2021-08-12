"""
Basic Python progress bar

Robert Kerr

`_percentStr` converts percent to 3 digit number e.g. 45.0 -> 045%
`_plot` prints progress bar with percentage as argument
`pbar` prints progress bar as function of iterations and total iterations

"""

def _percentStr(percent):
    percent = str(int(percent))
    return (3-len(percent))*'0' + percent + '%'

def _plot(percent):
    totalBars = 15
    prog = percent/100
    number_of_bars = int(prog*totalBars)
    string = ' [' + number_of_bars*'#' + (totalBars - number_of_bars)*'-' + ']'
    print(end='\r' + _percentStr(percent) + string)

def pbar(iters,totalIters):
    percent = iters/totalIters
    _plot(percent*100)

