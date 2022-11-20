#!/bin/sh
proof="$(/home/lean/lean-4.0.0-linux/bin/lean --run $1)"
if [ -z "${proof}" ];
then
	exit 0
else
	exit 1
fi