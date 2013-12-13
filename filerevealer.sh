#!/bin/bash

flag=$(defaults read com.apple.finder AppleShowAllFiles)
if [ $flag = "NO" ]; then
	defaults write com.apple.finder AppleShowAllFiles YES
        echo "visible"
elif [ $flag = "YES" ]; then
	defaults write com.apple.finder AppleShowAllFiles NO
        echo "hidden"
fi
killall Finder