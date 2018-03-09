#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Acpmeter
# Generated: Wed Aug  2 09:16:23 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class ACPmeter(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Acpmeter")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 96000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=9600,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Power [Watts]",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="Units",
        	minval=-100,
        	maxval=1000,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label="Number Plot",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0.win)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(10, (firdes.low_pass(1, samp_rate, 100, 100, firdes.WIN_BLACKMAN_HARRIS)))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_rms_xx_0 = blocks.rms_ff(0.1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1, ))
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.blks2_tcp_source_0 = grc_blks2.tcp_source(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr="127.0.0.1",
        	port=3701,
        	server=False,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_tcp_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_rms_xx_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_abs_xx_0, 0))    
        self.connect((self.blocks_rms_xx_0, 0), (self.fir_filter_xxx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.wxgui_numbersink2_0, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.wxgui_scopesink2_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, 100, 100, firdes.WIN_BLACKMAN_HARRIS)))


def main(top_block_cls=ACPmeter, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
