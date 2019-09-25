#!/bin/sh

set -e

if [ ! -d venv ]
then
  python3 -m venv venv
  . venv/bin/activate
  pip install -r requirements.txt
else
  . venv/bin/activate 
fi

curl https://raw.githubusercontent.com/rook/rook/master/cluster/examples/kubernetes/ceph/common.yaml > common.yaml
# cp ~/go/src/github.com/rook/rook/cluster/examples/kubernetes/ceph/common.yaml common.yaml

python setup.py mkcodes
python setup.py develop
generate-model-classes common.yaml rook_ceph_client
python setup.py test
