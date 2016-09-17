#!/bin/sh
rm -rf acmetool
mkdir acmetool
export GOPATH=`pwd`/acmetool
go get -v -d github.com/hlandau/acme/...
( cd $GOPATH/src/github.com/hlandau
  go get -v -d -u ./...
)
tar cf - --exclude .git acmetool | xz -9 >acmetool-`date '+%Y%m%d'`.tar.xz
