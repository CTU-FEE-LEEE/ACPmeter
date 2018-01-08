#!/bin/sh


ulimit -c unlimited

cd ~/repos/signal-piping-tools

if ! pidof sdr-widget > /dev/null; then
	{ ./sdr-widget -r 96000 | buffer & } | ./servestream -d -p 3701
fi

if ! pidof -x ACPmeter.py > /dev/null; then
	./ACPmeter.py > /dev/null &
fi

