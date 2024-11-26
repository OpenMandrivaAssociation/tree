#!/bin/sh
curl -s 'https://oldmanprogrammer.net/source.php?dir=projects/tree' |grep '^<option selected' |sed -e 's,.*tree-,,;s,\.tgz.*,,'
