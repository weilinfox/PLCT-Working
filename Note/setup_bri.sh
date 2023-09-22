#!/bin/bash -x

bri="br0"
tap="tap"
ip="10.0.0.1/24"
broadcast="10.0.0.255"

if [ "$(brctl show | grep -w $bri)" != "" ]; then
    echo "Find bridge"
else
    echo "Add new bridge $bri"
    sudo brctl addbr br0
    sudo ip addr add $ip broadcast $broadcast dev $bri
    echo "Activate bridge $bri"
    sudo ip link set dev $bri up
fi

if [ "$(ip link | grep -w ${tap}0)" != "" ]; then
    echo "Find tap device"
else
    echo "Add new taps ${tap}0-${tap}49"
    for i in {0..49}; do sudo tunctl -t $tap$i -u $(whoami); done
    for i in {0..49}; do sudo ip link set dev $tap$i up; done
    for i in {0..49}; do sudo brctl addif $bri $tap$i; done
fi

echo "Quit script"
