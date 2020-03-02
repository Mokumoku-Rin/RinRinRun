#!/bin/sh

echo "----------------------------"
echo "client npm install"
echo "----------------------------"
npm --prefix ./client/src install ./client/src

echo "----------------------------"
echo "docker-compose build --no-cache"
echo "----------------------------"
docker-compose build --no-cache

echo "----------------------------"
echo "docker build finish. Please run"
echo "docker-compose up"
echo "----------------------------"
