#!/usr/bin/env bash

IFS=$'\n'
echo "<<<interface_addresses:sep(59)>>>"
for interface in `ls /sys/class/net/`; do
	HW_ADDR=`cat /sys/class/net/${interface}/address`
	IP4_ADDR=`ip address show dev ${interface} | fgrep 'inet ' | sed 's#.*inet \([^/]\+\)/[0-9]\+.*#\1#' | tr $'\n' ',' | sed 's/,$//'`
	IP6_ADDR=`ip address show dev ${interface} | fgrep 'inet6 ' | sed 's#.*inet6 \([^/]\+\)/[0-9]\+.*#\1#' | tr $'\n' ',' | sed 's/,$//'`

	echo "${interface};${HW_ADDR};${IP4_ADDR};${IP6_ADDR}"
done
