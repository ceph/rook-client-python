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



python setup.py mkcodes
python setup.py develop

# curl https://raw.githubusercontent.com/rook/rook/master/cluster/examples/kubernetes/ceph/common.yaml > ceph_common.yaml
cp ~/go/src/github.com/rook/rook/cluster/examples/kubernetes/ceph/common.yaml ceph_common.yaml

python generate_model_classes.py ceph_common.yaml rook_client/ceph

# curl https://raw.githubusercontent.com/rook/rook/master/cluster/examples/kubernetes/cassandra/operator.yaml > cassandra_operator.yaml
cp ~/go/src/github.com/rook/rook/cluster/examples/kubernetes/cassandra/operator.yaml cassandra_operator.yaml

python generate_model_classes.py cassandra_operator.yaml rook_client/cassandra

# curl https://raw.githubusercontent.com/rook/rook/master/cluster/examples/kubernetes/edgefs/operator.yaml > edgefs_operator.yaml
cp ~/go/src/github.com/rook/rook/cluster/examples/kubernetes/edgefs/operator.yaml edgefs_operator.yaml

python generate_model_classes.py edgefs_operator.yaml rook_client/edgefs



python setup.py test
