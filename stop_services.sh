#!/bin/bash
if [ -f api.pid ]; then
    kill $(cat api.pid)
    rm api.pid
    echo "API parada"
fi

if [ -f chat.pid ]; then
    kill $(cat chat.pid)
    rm chat.pid
    echo "Chat parado"
fi
