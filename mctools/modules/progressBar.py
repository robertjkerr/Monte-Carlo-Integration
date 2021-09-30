"""
Basic Python progress bar

Robert Kerr

`_percent_str` converts percent to 3 digit number e.g. 45.0 -> 045%
`_plot` prints progress bar with percentage as argument
`pbar` prints progress bar as function of iterations and total iterations

"""

def _percent_str(percent):
    percent = str(int(percent))
    return (3-len(percent))*'0' + percent + '%'

def _plot(percent):
    total_bars = 15
    prog = percent/100
    number_of_bars = int(prog*total_bars)
    string = ' [' + number_of_bars*'#' + (total_bars - number_of_bars)*'-' + ']'
    print(end='\r' + _percent_str(percent) + string)

def pbar(iters,total_iters):
    percent = iters/total_iters
    _plot(percent*100)

